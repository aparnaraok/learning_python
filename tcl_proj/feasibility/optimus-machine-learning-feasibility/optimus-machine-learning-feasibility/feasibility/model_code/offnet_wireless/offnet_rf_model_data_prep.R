options(digits = 10)
options(sqldf.driver = "SQLite")
# Suppress warnings
options( warn = -1 )

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Setting input parameters ####
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
path_py <- "C:/Users/MRajakum/Documents/SP/9.Optimus/feasibility/offnet_wireless"
setwd(path_py)
source("offnet_rf_model_data_prep_aux.R")
# set error parameter
err <- FALSE

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# R Libraries to be loaded
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
tryCatch(
  {
    
    packages <- c("dplyr","plyr","geosphere","lubridate","data.table",
                  "sqldf","randomForest","RecordLinkage","jsonlite","RMySQL","reshape2", "gdata",
                  "Metrics", "caTools", "stringi", "RMySQL", "jsonlite")
    if (length(setdiff(packages, rownames(installed.packages()))) > 0) {
      install.packages(setdiff(packages, rownames(installed.packages())))
    }
    rm(packages)
    
    library(dplyr)
    library(geosphere)
    library(gdata)
    library(randomForest)
    library(Metrics)
    library(caTools)
    library(stringi)
    library(RMySQL)
    library(jsonlite)
    
  },
  error=function(e){
    err <<- TRUE
    df_error$error_flag <- 1
    df_error$error_code <- "E11"
    df_error$error_msg <- "R Package Error: R Package not found"
    df_error <<- cbind(
      # input_json_data,df_error[,!(colnames(df_error) %in% colnames(input_json_data))]
      df_error)
  } 
)
if(err==TRUE){
  return(df_error)
}

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Database Connection ####
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Establishing connection
tryCatch(
  {
    mydb_abstract_db = dbConnect(MySQL(), 
                                 user='optimus_user', 
                                 password='Tata123', 
                                 dbname='optimus_abstract_uat2', 
                                 host='INP44XDDB2552')
  },
  error=function(e){
    err <<- TRUE
    df_error$error_flag <- 1
    df_error$error_code <- "E3"
    df_error$error_msg <- "DB Error: Error in connecting to DB"
    df_error <<- cbind(input_json_data,df_error[,!(colnames(df_error) %in% colnames(input_json_data))])
  }
)
if(err==TRUE){
  return(df_error)
}

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Fetching tables from DB
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
tryCatch(
  {
    #1. Provider name
    service_provider = dbSendQuery(mydb_abstract_db, "select * from provider_name_cleanup")
    service_provider = fetch(service_provider, n=-1)
    
    #1 a) Sify Base Station Data
    sify_data = dbSendQuery(mydb_abstract_db, "select * from sify_bs_data")
    sify_data = fetch(sify_data, n=-1)
    
    #1 b) Tikona Data
    tikona_data = dbSendQuery(mydb_abstract_db, "select * from tikona_bs_data")
    tikona_data = fetch(tikona_data, n=-1)
    
    #2. Prospect data
    prospect_data = dbSendQuery(mydb_abstract_db, "select * from Prospect_Rolled_Up_Offnet_RF_Refreshed_SP_01")
    prospect_data = fetch(prospect_data, n=-1)
    prospect_data = dplyr::rename(prospect_data,
                                  BW_mbps = Cleaned_BW)
    
    #3. Customer data
    offnet_cust_data = dbSendQuery(mydb_abstract_db, 
                                   "select * from Prospect_Customer_Rolled_Up_data_Offnet_RF_Refreshed")
    offnet_cust_data = fetch(offnet_cust_data, n=-1)
    
    
    #4 Mast height data
    mast_ht_data_all = dbSendQuery(mydb_abstract_db, "select * from Onnet_RF_prospect_coords_2")
    mast_ht_data_all = fetch(mast_ht_data_all, n=-1)
    
    #5 ARC BW
    arc_bw_cost = dbSendQuery(mydb_abstract_db, "select bw_mbps,vendor,arc,otc from cq_offnet_vendor_rc")
    arc_bw_cost = fetch(arc_bw_cost, n=-1)
    
    # take only required vendors
    arc_bw_cost_sify <- subset(arc_bw_cost,arc_bw_cost$vendor=="sify")
    arc_bw_cost_tikona <- subset(arc_bw_cost,arc_bw_cost$vendor=="tikona")
    
    #Remove unwanted df
    rm(arc_bw_cost)
  },
  error=function(e){
    err <<- TRUE
    df_error$error_flag <- 1
    df_error$error_code <- "E6"
    df_error$error_msg <- "DB Error: Error in querying the DB Tables"
    df_error <<- cbind(input_json_data,df_error[,!(colnames(df_error) %in% colnames(input_json_data))])
  }
)
if(err==TRUE){
  return(df_error)
}

#######################################################################
# Data pre-processing
#######################################################################

#1. Historical Prospects Data
prospect_data <- select(prospect_data,
                        Feasibility_Response_Feasibility_Response_Auto_No,
                        CustomerLongitude1,
                        CustomerLatitude1,
                        Feasibility_Response_Created_Date,
                        BW_mbps,
                        Product_Name,
                        Provider_Name,
                        L1_or_L2,
                        Onnet_Offnet,
                        Wireline_or_RF,
                        resp_state,
                        Request_no,
                        Response_related_to_2,
                        Final_Provider_Name,
                        final_key_level,
                        Local_Loop_Capacity,
                        Local_Loop_Interface,
                        Mast_Height,
                        Sales_Selected_Response,
                        Last_Mile_Contract_Term,
                        Status,
                        Sales_Selected_Response
) %>%
  dplyr::rename(
    Feasibility.Response..Feasibility.Response.Auto.No. = Feasibility_Response_Feasibility_Response_Auto_No,
    Feasibility.Response..Created.Date = Feasibility_Response_Created_Date
  )

prospect_data$BW_mbps <- as.numeric(prospect_data$BW_mbps)
prospect_data$Feasibility.Response..Created.Date <- as.Date(prospect_data$Feasibility.Response..Created.Date,
                                                            format = "%Y-%m-%d")
prospect_data$Feasibility_flag <- ifelse(prospect_data$Status == "Feasible", 1 ,0)
print("Total Feasible/NFs in Historic Proect Data ***")
table(prospect_data$Status)

# Imputing with median to avoid error in min/ max (na.rm = T in max min returns a warning if all values are null)
prospect_data$BW_mbps[is.na(prospect_data$BW_mbps)] <- median(prospect_data$BW_mbps, na.rm = T)
# prospect_data <- dplyr::rename(prospect_data, #**** Uncomment later
#                                CustomerLongitude1 = prospect_long,
#                                CustomerLatitude1 = prospect_lat)

#3. Historic Customer Data
cust_cols <- c("","Commissioning.Date","BW.In.MB","accuracy_num","Longitude","Latitude")
offnet_cust_data <- select(offnet_cust_data,
                           TCL_SERVICE_ID,
                           Commissioning_Date,
                           BW_In_MB,
                           accuracy_num,
                           Longitude,
                           Latitude) %>%
  dplyr::rename(BW.In.MB = BW_In_MB,
                TCL.SERVICE.ID = TCL_SERVICE_ID,
                Commissioning.Date = Commissioning_Date
                )


#***** Added here
offnet_cust_data$Date.Of.Acceptance <- as.Date(offnet_cust_data$Commissioning.Date, format="%Y-%m-%d")
offnet_cust_data$Latitude <- as.numeric(offnet_cust_data$Latitude)
offnet_cust_data$Longitude <- as.numeric(offnet_cust_data$Longitude)

#4. LM Pricebook
# LM_pricebook <- dplyr::rename(LM_pricebook,
#                               BW_mbps = Cleaned_Bandwidth)
# 
# LM_pricebook <- LM_pricebook[which(LM_pricebook$Interface == "FE"),]

#5. Mast Height 
prospect_coords <- mast_ht_data_all[c("prospect_date",
                                      "prospect_lat",
                                      "prospect_lon")]

prospect_coords_new <- mast_ht_data_all[c("prospect_date",
                                          "prospect_lat",
                                          "prospect_lon",
                                          "prospect_mast_ht")]
prospect_coords_new$prospect_mast_ht <- as.numeric(prospect_coords_new$prospect_mast_ht)

##############################################################
#
# Prepare Features
#
##############################################################
#1. Prospect count near by
prospect_data$result <- apply(prospect_data, 1, function(x) prospect_distance_calc(
  x["CustomerLatitude1"],
  x["CustomerLongitude1"],
  x["Feasibility.Response..Created.Date"],
  prospect_data))

prospect_data$prospect_0_5km_cust_Count<- as.numeric(unlist(lapply(prospect_data$result, "[[",1)))
prospect_data$prospect_0_5km_Avg_DistanceKilometers<- as.numeric(unlist(lapply(prospect_data$result, "[[",2)))
prospect_data$prospect_0_5km_Min_DistanceKilometers<- as.numeric(unlist(lapply(prospect_data$result, "[[",3)))
prospect_data$prospect_0_5km_Avg_BW_Mbps<- as.numeric(unlist(lapply(prospect_data$result, "[[",4)))
prospect_data$prospect_0_5km_Min_BW_Mbps<- as.numeric(unlist(lapply(prospect_data$result, "[[",5)))
prospect_data$prospect_0_5km_Max_BW_Mbps<- as.numeric(unlist(lapply(prospect_data$result, "[[",6)))
prospect_data$prospect_0_5km_feasibility_pct<- as.numeric(unlist(lapply(prospect_data$result, "[[",7)))
prospect_data$prospect_0_5km_Sum_Feasibility_flag<- as.numeric(unlist(lapply(prospect_data$result, "[[",8)))

prospect_data$prospect_2km_cust_Count<- as.numeric(unlist(lapply(prospect_data$result, "[[",9)))
prospect_data$prospect_2km_Avg_DistanceKilometers<- as.numeric(unlist(lapply(prospect_data$result, "[[",10)))
prospect_data$prospect_2km_Min_DistanceKilometers<- as.numeric(unlist(lapply(prospect_data$result, "[[",11)))
prospect_data$prospect_2km_Avg_BW_Mbps<- as.numeric(unlist(lapply(prospect_data$result, "[[",12)))
prospect_data$prospect_2km_Min_BW_Mbps<- as.numeric(unlist(lapply(prospect_data$result, "[[",13)))
prospect_data$prospect_2km_Max_BW_Mbps<- as.numeric(unlist(lapply(prospect_data$result, "[[",14)))
prospect_data$prospect_2km_Sum_Feasibility_flag<- as.numeric(unlist(lapply(prospect_data$result, "[[",15)))
prospect_data$prospect_2km_feasibility_pct<- as.numeric(unlist(lapply(prospect_data$result, "[[",16)))

prospect_data$result <- NULL

saveRDS(prospect_data,"1_Prospect_Features_Prepared.RDS")

# #2. BTS Features
prospect_data$result <- apply(prospect_data, 1, 
                                          function(x) vendor_distance_calc(
                                            x["CustomerLatitude1"],
                                            x["CustomerLongitude1"],
                                            sify_data))

prospect_data$sify_min_dist_km  = as.numeric(unlist(lapply(prospect_data$result, "[[", 1)))
prospect_data$sify_3km_radius   = as.numeric(unlist(lapply(prospect_data$result, "[[", 2)))
prospect_data$sify_avg_dist_3km = as.numeric(unlist(lapply(prospect_data$result, "[[", 3)))

prospect_data$result <- NULL

saveRDS(prospect_data,"2A_Prospect_Sify_Features_Prepared.RDS")

# #2. BTS Features
prospect_data$result <- apply(prospect_data, 1, 
                              function(x) vendor_distance_calc(
                                x["CustomerLatitude1"],
                                x["CustomerLongitude1"],
                                tikona_data))

prospect_data$tikona_min_dist_km  = as.numeric(unlist(lapply(prospect_data$result, "[[", 1)))
prospect_data$tikona_3km_radius   = as.numeric(unlist(lapply(prospect_data$result, "[[", 2)))
prospect_data$tikona_avg_dist_3km = as.numeric(unlist(lapply(prospect_data$result, "[[", 3)))

prospect_data$result <- NULL

saveRDS(prospect_data,"2B_Prospect_Tikona_Features_Prepared.RDS")

#3. Offnet Customer Data
offnet_cust_data <- offnet_cust_data[order(offnet_cust_data$TCL.SERVICE.ID,
                                           offnet_cust_data$Commissioning.Date),]
offnet_cust_data <- offnet_cust_data[!duplicated(offnet_cust_data$TCL.SERVICE.ID),]
prospect_data$row_idx <- c(1:nrow(prospect_data))
prospect_data$result <- apply(prospect_data, 1, function(x) offnet_RF_customer_distance_calc(
  x["row_idx"],
  x["CustomerLatitude1"],
  x["CustomerLongitude1"],
  x["Feasibility.Response..Created.Date"],
  offnet_cust_data))

prospect_data$offnet_0_5km_cust_Count = as.numeric(unlist(lapply(prospect_data$result, "[[", 1)))
prospect_data$offnet_0_5km_Avg_DistanceKilometers = as.numeric(unlist(lapply(prospect_data$result, "[[", 2)))
prospect_data$offnet_0_5km_Min_DistanceKilometers = as.numeric(unlist(lapply(prospect_data$result, "[[", 3)))
prospect_data$offnet_0_5km_Avg_BW_Mbps = as.numeric(unlist(lapply(prospect_data$result, "[[", 4)))
prospect_data$offnet_0_5km_Min_BW_Mbps = as.numeric(unlist(lapply(prospect_data$result, "[[", 5)))
prospect_data$offnet_0_5km_Max_BW_Mbps = as.numeric(unlist(lapply(prospect_data$result, "[[", 6)))
prospect_data$offnet_0_5km_Min_accuracy_num = as.numeric(unlist(lapply(prospect_data$result, "[[", 7)))

prospect_data$offnet_2km_cust_Count = as.numeric(unlist(lapply(prospect_data$result, "[[", 8)))
prospect_data$offnet_2km_Avg_DistanceKilometers = as.numeric(unlist(lapply(prospect_data$result, "[[", 9)))
prospect_data$offnet_2km_Min_DistanceKilometers = as.numeric(unlist(lapply(prospect_data$result, "[[", 10)))
prospect_data$offnet_2km_Avg_BW_Mbps = as.numeric(unlist(lapply(prospect_data$result, "[[", 11)))
prospect_data$offnet_2km_Min_BW_Mbps = as.numeric(unlist(lapply(prospect_data$result, "[[", 12)))
prospect_data$offnet_2km_Max_BW_Mbps = as.numeric(unlist(lapply(prospect_data$result, "[[", 13)))
prospect_data$offnet_2km_Min_accuracy_num = as.numeric(unlist(lapply(prospect_data$result, "[[", 14)))

prospect_data$offnet_5km_cust_Count = as.numeric(unlist(lapply(prospect_data$result, "[[", 15)))
prospect_data$offnet_5km_Avg_DistanceKilometers = as.numeric(unlist(lapply(prospect_data$result, "[[", 16)))
prospect_data$offnet_5km_Min_DistanceKilometers = as.numeric(unlist(lapply(prospect_data$result, "[[", 17)))
prospect_data$offnet_5km_Avg_BW_Mbps = as.numeric(unlist(lapply(prospect_data$result, "[[", 18)))
prospect_data$offnet_5km_Min_BW_Mbps = as.numeric(unlist(lapply(prospect_data$result, "[[", 19)))
prospect_data$offnet_5km_Max_BW_Mbps = as.numeric(unlist(lapply(prospect_data$result, "[[", 20)))
prospect_data$offnet_5km_Min_accuracy_num = as.numeric(unlist(lapply(prospect_data$result, "[[", 21)))

prospect_data$result <- NULL

saveRDS(prospect_data,"3_Prospect_Customer_Features_Prepared.RDS")
# 
# ##############################################################
# #
# # Clean Features
# #
# ##############################################################
# prospect_data <- final_cleaning_func(prospect_data)
#####################################################################################
# Final data cleaning for modelling
#####################################################################################

# Converting null distances to 99999
cols_to_impute_99999 <- c("offnet_0_5km_Avg_DistanceKilometers",                
                          "offnet_0_5km_Min_DistanceKilometers",
                          "offnet_2km_Avg_DistanceKilometers",                 
                          "offnet_2km_Min_DistanceKilometers",
                          "offnet_5km_Avg_DistanceKilometers",                  
                          "offnet_5km_Min_DistanceKilometers",
                          "prospect_0_5km_Avg_DistanceKilometers",              
                          "prospect_0_5km_Min_DistanceKilometers",
                          "prospect_2km_Avg_DistanceKilometers",                
                          "prospect_2km_Min_DistanceKilometers",
                          "sify_avg_dist_3km",
                          "tikona_avg_dist_3km",
                          "sify_min_dist_km",
                          "tikona_min_dist_km"
)
final_offnet_RF_data <- prospect_data
final_offnet_RF_data[cols_to_impute_99999][is.na(final_offnet_RF_data[cols_to_impute_99999])] <- 99999
rm(cols_to_impute_99999)

# Imputing with 0
cols_to_impute_o <- c("offnet_0_5km_cust_Count" ,
                      "offnet_0_5km_Avg_BW_Mbps" ,
                      "offnet_0_5km_Min_BW_Mbps" ,
                      "offnet_0_5km_Max_BW_Mbps" ,
                      "offnet_0_5km_Min_accuracy_num" ,
                      "offnet_2km_cust_Count" ,
                      "offnet_2km_Avg_BW_Mbps" ,
                      "offnet_2km_Min_BW_Mbps" ,
                      "offnet_2km_Max_BW_Mbps" ,
                      "offnet_2km_Min_accuracy_num" ,
                      "offnet_5km_cust_Count" ,
                      "offnet_5km_Avg_BW_Mbps" ,
                      "offnet_5km_Min_BW_Mbps" ,
                      "offnet_5km_Max_BW_Mbps" ,
                      "offnet_5km_Min_accuracy_num" ,
                      "prospect_0_5km_cust_Count" ,
                      "prospect_0_5km_Avg_BW_Mbps" ,
                      "prospect_0_5km_Min_BW_Mbps" ,
                      "prospect_0_5km_Max_BW_Mbps" ,
                      "prospect_0_5km_feasibility_pct" ,
                      "prospect_0_5km_Sum_Feasibility_flag" ,
                      "prospect_2km_cust_Count" ,
                      "prospect_2km_Avg_BW_Mbps" ,
                      "prospect_2km_Min_BW_Mbps" ,
                      "prospect_2km_Max_BW_Mbps" ,
                      "prospect_2km_Sum_Feasibility_flag" ,
                      "prospect_2km_feasibility_pct",
                      "sify_3km_radius",
                      "tikona_3km_radius"
)

final_offnet_RF_data[cols_to_impute_o][is.na(final_offnet_RF_data[cols_to_impute_o])] <- 0 
rm(cols_to_impute_o)

# Creating final provider variables
# Total number of provider towers
final_offnet_RF_data$provider_tot_towers <- final_offnet_RF_data$sify_3km_radius + final_offnet_RF_data$tikona_3km_radius

# Closest provider distance
final_offnet_RF_data <- transform(final_offnet_RF_data,
                                  provider_min_dist = pmin(sify_min_dist_km,
                                                           tikona_min_dist_km
                                  ))

df <-final_offnet_RF_data[,c("sify_min_dist_km",
                             "tikona_min_dist_km")]

# Closest provider name
final_offnet_RF_data$closest_provider <- colnames(df)[apply(df , 1, which.min)]
rm(df)

final_offnet_RF_data <- final_offnet_RF_data[, -which(names(final_offnet_RF_data) %in% 
                                                        c("sify_min_dist_km",
                                                          "tikona_min_dist_km",
                                                          "sify_avg_dist_3km",
                                                          "tikona_avg_dist_3km",
                                                          "sify_3km_radius",
                                                          "tikona_3km_radius",
                                                          "Provider_Name",
                                                          "Feasibility.Response..Feasibility.Response.Auto.No.",
                                                          "Final_Provider_Name"
                                                        ))]

# # Grouping categorical variables
# final_offnet_RF_data$Customer.Segment[is.na(final_offnet_RF_data$Customer.Segment)] <- "Others"
# final_offnet_RF_data$Customer.Segment <- case(final_offnet_RF_data$Customer.Segment,
#                                               'Enterprise ? Silver' = 'Enterprise ? Silver',
#                                               'Enterprise - Gold' = 'Enterprise - Gold',
#                                               'Enterprise - Strategic' = 'Enterprise - Strategic',
#                                               'Enterprise-Direct' = 'Enterprise-Direct',
#                                               'Carriers' = 'Carriers',
#                                               'Enterprise-Partners Account' = 'Enterprise-Partners Account',
#                                               'Enterprise ? Growth Accounts' = 'Enterprise ? Growth Accounts',
#                                               'Enterprise ? Government/PSU' = 'Enterprise ? Government/PSU',
#                                               'SMB' = 'SMB',
#                                               'Enterprise - System Integrators' = 'Enterprise - System Integrators',
#                                               default = "Others"
# )

final_offnet_RF_data$Local_Loop_Interface[is.na(final_offnet_RF_data$Local_Loop_Interface)] <- "Others"
final_offnet_RF_data$Local_Loop_Interface <- case(final_offnet_RF_data$Local_Loop_Interface,
                                                  "100-Base-TX" = "100-Base-TX",
                                                  "FE" = "FE",
                                                  "Ethernet" = "Ethernet",
                                                  default = "Others"
)

final_offnet_RF_data$Product_Name[is.na(final_offnet_RF_data$Product_Name)] <- "Other"
final_offnet_RF_data$Product_Name <- case(final_offnet_RF_data$Product_Name,
                                          "Global VPN" = "Global VPN",
                                          "Internet Access Service" = "Internet Access Service",
                                          "Priority Ethernet - Point to Point" = "Priority Ethernet - Point to Point",
                                          "Priority Ethernet - Point to MultiPoint" = "Priority Ethernet - Point to MultiPoint",
                                          "National Dedicated Ethernet" = "National Dedicated Ethernet",
                                          "NPL" = "NPL",
                                          default = "Other"
)

# final_offnet_RF_data$Sales.Org[is.na(final_offnet_RF_data$Sales.Org)] <- "Others"
# final_offnet_RF_data$Sales.Org <- case(final_offnet_RF_data$Sales.Org,
#                                        "Enterprise" = "Enterprise" ,
#                                        "Service Provider" = "Service Provider",
#                                        "CSO" = "CSO",
#                                        "IT" = "IT",
#                                        default = "Others"
# )

final_offnet_RF_data$Last_Mile_Contract_Term[final_offnet_RF_data$Last_Mile_Contract_Term==""] <- "Others"
final_offnet_RF_data$Last_Mile_Contract_Term[as.character(final_offnet_RF_data$Last_Mile_Contract_Term) == "3 Years"] <- "2 Years"
final_offnet_RF_data$Last_Mile_Contract_Term <- case(final_offnet_RF_data$Last_Mile_Contract_Term,
                                                     "1 Year" = "1 Year",
                                                     "2-3 Years" = "2 Years",
                                                     default = "Others"
)
# Removing cols based on correlation
final_offnet_RF_data <- select(final_offnet_RF_data,
                               -offnet_0_5km_Avg_DistanceKilometers,
                               -offnet_2km_Avg_DistanceKilometers,
                               -offnet_5km_Avg_DistanceKilometers
)


saveRDS(final_offnet_RF_data, "OFFNET_RF_MODEL_DATA.rds")
write.csv(final_offnet_RF_data, "OFFNET_RF_MODEL_DATA.csv", row.names = F)


final_offnet_RF_data$class_wt_3 <- ifelse(final_offnet_RF_data$Status == "Feasible", 1, 3)
final_offnet_RF_data$class_wt_2 <- ifelse(final_offnet_RF_data$Status == "Feasible", 1, 2)

write.csv(final_offnet_RF_data, file = "OFFNET_RF_MODEL_DATA_SB.csv", row.names = F)

saveRDS(final_offnet_RF_data,"4_Offnet_RF_Data_to_Model.RDS")

#lapply(dbListConnections(MySQL()), dbDisconnect)
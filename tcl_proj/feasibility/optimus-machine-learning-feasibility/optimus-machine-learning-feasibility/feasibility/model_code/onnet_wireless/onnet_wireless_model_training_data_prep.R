options(digits = 10)
options(sqldf.driver = "SQLite")
# Suppress warnings
options( warn = -1 )

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Setting input parameters ####
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
path_py <- "C:/Users/MRajakum/Documents/SP/9.Optimus/feasibility/onnet_wireless"
setwd(path_py)
source("onnet_wireless_aux_functions.R")
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
    #1. BTS data
    bts_data_file = dbSendQuery(mydb_abstract_db, "select * from bts_data")
    
    # fetching data from mysql server
    bts_data_file = fetch(bts_data_file, n=-1) 
    
    #2. Prospect data
    prospect_data = dbSendQuery(mydb_abstract_db, "select * from Prospect_Rolled_Up_Onnet_RF_Refreshed_SP")
    prospect_data = fetch(prospect_data, n=-1)
    prospect_data = dplyr::rename(prospect_data,
                                  BW_mbps = Cleaned_BW)
    
    #3. Customer data
    onnet_cust_data = dbSendQuery(mydb_abstract_db, "select * from Prospect_Customer_Rolled_Up_data_Onnet_RF_Refreshed")
    onnet_cust_data = fetch(onnet_cust_data, n=-1)
    
    # #4. LM pricebook
    # LM_pricebook = dbSendQuery(mydb_abstract_db, "select * from Onnet_RF_LM_Cleaned")
    # LM_pricebook = fetch(LM_pricebook, n=-1)
    # 
    # #5. Mast height data
    # prospect_coords_2 = dbSendQuery(mydb_abstract_db, "select * from Onnet_RF_prospect_coords_2")
    # prospect_coords_2 = fetch(prospect_coords_2, n=-1)
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
# Fetching tables from DB
#######################################################################

#1. BTS Data
# Converting type
bts_data_file <- select(bts_data_file,
                        -seq_no,
                        -etl_batch_id,
                        -etl_load_dt,
                        -created_dt,
                        -updated_dt,
                        -src_system)
bts_data_file$longitude <- as.numeric(bts_data_file$longitude)
bts_data_file$latitude <- as.numeric(bts_data_file$latitude)
bts_data_file$pmp_flag <- as.numeric(bts_data_file$pmp_flag)
bts_data_file$pmp_angle <- as.numeric(bts_data_file$pmp_angle)

bts_data_file <- dplyr::rename(bts_data_file,
                               Site_ID = site_id,
                               Longitude = longitude,
                               Latitude = latitude,
                               AZIMUTH = azimuth,
                               INFRA_PROVIDER = intra_provider,
                               SITE_TYPE = site_type)

#2. Historical Prospects Data
prospect_data <- select(prospect_data,
                        Feasibility_Response_Feasibility_Response_Auto_No,
                        CustomerLongitude1,
                        CustomerLatitude1,
                        Feasibility_Response_Created_Date,
                        BW_mbps,
                        Product_Name,
                        Provider_Name,
                        L1_or_L2,
                        final_key_level,
                        Local_Loop_Capacity,
                        Local_Loop_Interface,
                        Mast_Height,
                        Sales_Selected_Response,
                        Last_Mile_Contract_Term,
                        Status,
                        Sales_Selected_Response
) %>%
  dplyr::rename(Feasibility.Response..Feasibility.Response.Auto.No. = Feasibility_Response_Feasibility_Response_Auto_No,
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
onnet_cust_data <- select(onnet_cust_data,
                          Longitude,
                          Latitude,
                          Date_Of_Acceptance,
                          Cleaned_customer_Bandwidth) %>%
  dplyr::rename(BW = Cleaned_customer_Bandwidth,
                Date.Of.Acceptance = Date_Of_Acceptance)


#***** Added here
onnet_cust_data$Date.Of.Acceptance <- as.Date(onnet_cust_data$Date.Of.Acceptance, format="%Y-%m-%d")
onnet_cust_data$Latitude <- as.numeric(onnet_cust_data$Latitude)
onnet_cust_data$Longitude <- as.numeric(onnet_cust_data$Longitude)
# 
# #4. LM Pricebook
# LM_pricebook <- dplyr::rename(LM_pricebook,
#                               BW_mbps = Cleaned_Bandwidth)
# 
# LM_pricebook <- LM_pricebook[which(LM_pricebook$Interface == "FE"),]
# 
# #5. Mast Height 
# prospect_coords_2$prospect_mast_ht <- as.numeric(prospect_coords_2$prospect_mast_ht)
# prospect_coords_2$row_names <- NULL

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

#2. BTS Features
prospect_data$result <- apply(prospect_data, 1, function(x) bts_distance_calc(
  x["CustomerLatitude1"],
  x["CustomerLongitude1"],
  bts_data_file,
  angle_between))
prospect_data$bts_num_BTS  <-    unlist(lapply(prospect_data$result, "[[", 1))
prospect_data$bts_min_dist_km <- as.numeric(unlist(lapply(prospect_data$result, "[[", 2)))
prospect_data$solution_type <-   unlist(lapply(prospect_data$result, "[[", 3))
prospect_data$PMP_bts_3km_radius <-  as.numeric(unlist(lapply(prospect_data$result, "[[", 4)))
prospect_data$P2P_bts_3km_radius <-  as.numeric(unlist(lapply(prospect_data$result, "[[", 5)))
prospect_data$bts_Closest_infra_provider <-  unlist(lapply(prospect_data$result, "[[", 6))
prospect_data$bts_Closest_Site_type <-  unlist(lapply(prospect_data$result, "[[", 7))
prospect_data$bts_IP_PMP <-  unlist(lapply(prospect_data$result, "[[", 8))
prospect_data$result <- NULL

saveRDS(prospect_data,"2_Prospect_BTS_Features_Prepared.RDS")

#3. Onnet Customer Data
prospect_data$result <- apply(prospect_data, 1, function(x) customer_distance_calc(
  x["CustomerLatitude1"],
  x["CustomerLongitude1"],
  x["Feasibility.Response..Created.Date"],
  onnet_cust_data))

prospect_data$onnet_0_5km_cust_Count = as.numeric(unlist(lapply(prospect_data$result, "[[", 1)))
prospect_data$onnet_0_5km_Avg_DistanceKilometers = as.numeric(unlist(lapply(prospect_data$result, "[[", 2)))
prospect_data$onnet_0_5km_Min_DistanceKilometers = as.numeric(unlist(lapply(prospect_data$result, "[[", 3)))
prospect_data$onnet_0_5km_Avg_BW_Mbps = as.numeric(unlist(lapply(prospect_data$result, "[[", 4)))
prospect_data$onnet_0_5km_Min_BW_Mbps = as.numeric(unlist(lapply(prospect_data$result, "[[", 5)))
prospect_data$onnet_0_5km_Max_BW_Mbps = as.numeric(unlist(lapply(prospect_data$result, "[[", 6)))
prospect_data$onnet_2km_cust_Count = as.numeric(unlist(lapply(prospect_data$result, "[[", 7)))
prospect_data$onnet_2km_Avg_DistanceKilometers = as.numeric(unlist(lapply(prospect_data$result, "[[", 8)))
prospect_data$onnet_2km_Min_DistanceKilometers = as.numeric(unlist(lapply(prospect_data$result, "[[", 9)))
prospect_data$onnet_2km_Avg_BW_Mbps = as.numeric(unlist(lapply(prospect_data$result, "[[", 10)))
prospect_data$onnet_2km_Min_BW_Mbps = as.numeric(unlist(lapply(prospect_data$result, "[[", 11)))
prospect_data$onnet_2km_Max_BW_Mbps = as.numeric(unlist(lapply(prospect_data$result, "[[", 12)))
prospect_data$onnet_5km_cust_Count = as.numeric(unlist(lapply(prospect_data$result, "[[", 13)))
prospect_data$onnet_5km_Avg_DistanceKilometers = as.numeric(unlist(lapply(prospect_data$result, "[[", 14)))
prospect_data$onnet_5km_Min_DistanceKilometers = as.numeric(unlist(lapply(prospect_data$result, "[[", 15)))
prospect_data$onnet_5km_Avg_BW_Mbps = as.numeric(unlist(lapply(prospect_data$result, "[[", 16)))
prospect_data$onnet_5km_Min_BW_Mbps = as.numeric(unlist(lapply(prospect_data$result, "[[", 17)))
prospect_data$onnet_5km_Max_BW_Mbps = as.numeric(unlist(lapply(prospect_data$result, "[[", 18)))
prospect_data$result <- NULL
saveRDS(prospect_data,"3_Prospect_Customer_Features_Prepared.RDS")

##############################################################
#
# Clean Features
#
##############################################################
prospect_data <- final_cleaning_func(prospect_data)
saveRDS(prospect_data,"4_Prospect_Customer_Features_Prepared.RDS")

lapply(dbListConnections(MySQL()), dbDisconnect)
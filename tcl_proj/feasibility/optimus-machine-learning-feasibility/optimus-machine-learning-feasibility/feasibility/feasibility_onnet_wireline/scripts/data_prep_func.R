# Cleaning BW in live inventory data
bw_clean_up <- function(bw){
  bw_mapping <- data.frame("id" = 1:7,
                           "bw_id" = c("e1","e3","ds3","stm1","stm4","stm16","stm64"),
                           "bw_in_mbps" = c(2, 34, 45, 155, 622, 2560, 10240))
  bw_value_mbps = NA
  
  bw <- str_to_lower(bw)
  bw <- gsub("[-,() ]","" , bw,ignore.case = TRUE)
  
  if(is.na(bw) || bw==""){
    return(bw_value_mbps)
  }
  else{
    alpha_loc <- str_locate(bw,"[a-z]+")
    num_loc <- str_locate_all(bw, "[0-9]+")[[1]]
    #print(alpha_loc)
    if(is.na(alpha_loc[1]))
    {
      bw_value_mbps <- as.numeric(str_sub(bw,num_loc[1],num_loc[2]))
      return(bw_value_mbps)
    }
    #String start from alphabet
    if(alpha_loc[1]==1){
      loc <- str_locate(bw,c("e1","e3","ds3","stm1","stm4","stm16","stm64"))
      idx <- which(!is.na(loc[,1]))
      if(length(idx)){
        bw_value_mbps <- bw_mapping[tail(idx, n=1),"bw_in_mbps"]
      }
    }
    else{
      bw_value <- as.numeric(str_sub(bw,num_loc[1,"start"],num_loc[1,"end"]))
      bw_unit <- str_sub(bw,alpha_loc[1],alpha_loc[2])
      loc <- str_locate(bw_unit,c("mbps","mb","m"))
      idx <- which(!is.na(loc[,1]))
      if(length(idx)){
        bw_value_mbps <- bw_value
      }
      else{
        loc <- str_locate(bw_unit,c("kbps","kb","k"))
        idx <- which(!is.na(loc[,1]))
        if(length(idx)){
          bw_value_mbps <- bw_value/1000
        }
        else{
          loc <- str_locate(bw_unit,c("gbps","g","gig","gb"))
          idx <- which(!is.na(loc[,1]))
          if(length(idx)){
            bw_value_mbps <- bw_value * 1024
          }
        }
      }
    }
    return(bw_value_mbps)
  }
}

init_envt <- function(){
  
  ##########################################################################################
  ##########################################################################################
  # R Packages - Check if needed packages are installed - if not, install them
  ##########################################################################################
  ##########################################################################################
  options(digits = 10)
  options(sqldf.driver = "SQLite")
  # Suppress warnings
  options( warn = -1 )
  packages <- c("dplyr","plyr","geosphere","lubridate","data.table",
                "sqldf","randomForest","RecordLinkage","jsonlite","RMySQL","reshape2")
  if (length(setdiff(packages, rownames(installed.packages()))) > 0) {
    install.packages(setdiff(packages, rownames(installed.packages())))
  }
  
  ##########################################################################################
  ##########################################################################################
  # R Libraries to be called
  ##########################################################################################
  ##########################################################################################
  time_start <- proc.time()
  library(dplyr)
  library(plyr)
  library(geosphere)
  library(lubridate)
  library(data.table)
  library(sqldf)
  library(randomForest)
  library(RecordLinkage)
  library(RMySQL)
  library(reshape2)
  
  
}

level_mapping<- function(t_data, input_data)
{

  for(attr in colnames(t_data))
  {
    if (is.factor(t_data[[attr]]))
    {
      input_data[[attr]]  =  factor(input_data[[attr]], levels = levels(t_data[[attr]] ) )

    }
  }

  vec <- c("POP_Network_Location_Type","POP_Construction_Status","POP_Building_Type",
           "POP_Category","POP_TCL_Access",  "FATG_Network_Location_Type","FATG_Building_Type",
           "FATG_Category","FATG_TCL_Access" ,"FATG_PROW" ,"FATG_Ring_type" , "Product.Name")
  #
  # # after levelling whichever are NAs - convert them
  input_data[vec][is.na(input_data[vec])] <- "xxx"

  
  # input_data=input_data %>% mutate_if(is.character, as.factor)

  # ##########################################################################################
  # # Level mapping with Training data
  # ##########################################################################################
  # # t_data <- training_set  #onnent_wireline_under
  # t_data$Identifier <- "Train"
  # # t_data$site_id <- "Site_VAL"
  # t_extra_cols <- setdiff(colnames(input_data), colnames(t_data))
  # i_extra_cols <- setdiff(colnames(t_data), colnames(input_data))
  # t_data[,t_extra_cols] <- NA
  # input_data[,i_extra_cols] <- NA
  # input_data <- rbind(input_data,t_data)
  # input_data <- input_data[which(is.na(input_data$Identifier)),]

  
  return (input_data)
  
}

clean_input <- function(input_data){
  
  col_list = c("Latitude_final", "Longitude_final", "BW_mbps", "Feasibility_Response_Created_Date", "Product.Name", "resp_city")
  if (sum(col_list %in% names(input_data)) < length(col_list)) stop("Missing Column")
  
  #Data type formatting for input data
  input_data$Latitude_final <- as.numeric(input_data$Latitude_final)
  input_data$Longitude_final <- as.numeric(input_data$Longitude_final)
  input_data$BW_mbps <- as.numeric(input_data$BW_mbps)
  # input_data$BW_mbps_act <- as.numeric(input_data$BW_mbps)
  input_data$Feasibility_Response_Created_Date <- as.Date(input_data$Feasibility_Response_Created_Date,
                                                          format = "%Y-%m-%d", origin="1900-01-01")
  
  input_data$Product.Name <- ifelse(is.na(input_data$Product.Name),"others",as.character(input_data$Product.Name))
  
  # Creating Product Flag for input data
  input_data$product.name.flag <-
    ifelse(tolower(input_data$Product.Name) == "national dedicated ethernet","NDE",
           ifelse(tolower(input_data$Product.Name) == "npl","NPL",
                  ifelse(tolower(input_data$Product.Name) == "global vpn","GVPN",
                         ifelse(tolower(input_data$Product.Name) == "internet access service","ILL",
                                ifelse(tolower(input_data$Product.Name) == "global dedicated ethernet","GDE",
                                       ifelse(tolower(input_data$Product.Name) == "ipl","IPL",
                                              ifelse(tolower(input_data$Product.Name) == "priority ethernet - point to point","Ethernet",
                                                     ifelse(tolower(input_data$Product.Name) == "video connect","VC","others"))))))))
  
  
  
  return (input_data)
}

load_training_data <- function(mydb_abstract_db, PROSPECT_TBL){
  

  query = "select Prospect_ID, resp_state, Feasibility_Response_Created_Date, Latitude_final, Longitude_final, Status_2, Cleaned_BW, Product_Name, resp_city, Local_Loop_Interface as LLE, Prospect_Name as prospect_name, CAST(Latitude_final as CHAR(50)) as lat_str, CAST(Longitude_final as CHAR(50)) as lon_str   from"
  query = paste(query, PROSPECT_TBL, sep = " ")
  input_data = dbSendQuery(mydb_abstract_db, query)
  # fetching data from mysql server
  input_data = fetch(input_data, n=-1)
  
  input_data = dplyr::rename(input_data, Product.Name = Product_Name, BW_mbps = Cleaned_BW)
  
  input_data = input_data[!is.na(input_data$resp_city),]
  
  input_data = clean_input(input_data)
  
  
  return(input_data)
  
}

load_pop_data <- function(mydb_abstract_db){
  
  
  pop_data_file = dbSendQuery(mydb_abstract_db, "select seq_no,name,network_location_type,construction_status,building_type,network_location_id,longitude,latitude,site_address,category,services_offered_gde,services_offered_gvpn,services_offered_ias,services_offered_ipl,services_offered_vpls,services_offered_video_connect,services_offered_nde,services_offered_npl,services_offered_priority_ethernet,tcl_access from pop_data")
  
  # fetching data from mysql server
  pop_data_file = fetch(pop_data_file, n=-1)
  # Column Mapping
  pop_cols <- c('POP_ID','pop_name','POP_Network_Location_Type','POP_Construction_Status','POP_Building_Type','pop_network_loc_id','pop_long','pop_lat','pop_address','POP_Category','Services.Offered.GDE','Services.Offered.GVPN','Services.Offered.IAS','Services.Offered.IPL','Services.Offered.VPLS','Services.Offered.Video.Connect','Services.Offered.NDE','Services.Offered.NPL','Services.Offered.Priority.Ethernet','POP_TCL_Access')
  
  colnames(pop_data_file) <- pop_cols
  

  pop_data_file$pop_lat <- as.numeric(pop_data_file$pop_lat)
  pop_data_file$pop_long <- as.numeric(pop_data_file$pop_long)
  
  return (pop_data_file)
}

load_fatg_data <- function(mydb_abstract_db){
  
  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  # FATG Data - Import
  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  fatg_data_file = dbSendQuery(mydb_abstract_db, "select seq_no,network_location_type,building_type,fatg_long,fatg_lat,site_address,category,tcl_access,fatg_state,prow,ring_type from fatg_data")
  
  # fetching data from mysql server
  fatg_data_file = fetch(fatg_data_file, n=-1)
  # Column Mapping
  fatg_cols <- c('FATG_ID','FATG_Network_Location_Type','FATG_Building_Type','fatg_long','fatg_lat','FATG_Site_Address','FATG_Category','FATG_TCL_Access','fatg_state','FATG_PROW','FATG_Ring_type')
  
  colnames(fatg_data_file) <- fatg_cols
  fatg_data_file$fatg_lat <- as.numeric(fatg_data_file$fatg_lat)
  fatg_data_file$fatg_long <- as.numeric(fatg_data_file$fatg_long)
  # Manually adding FATG Ring Type as it is not present in the GIS source system directly
  fatg_data_file$FATG_Ring_type <- "SDH"
  
  return (fatg_data_file)
}

load_hh_data <- function(mydb_abstract_db){
  hh_data_file = dbSendQuery(mydb_abstract_db, "select seq_no,num_hh,hh_state,hh_lat,hh_long from hh_data")
  
  # fetching data from mysql server
  hh_data_file = fetch(hh_data_file, n=-1)
  # Column Mapping
  hh_cols <- c('HH_ID','hh_name','HH_STATE','hh_lat','hh_long')
  
  colnames(hh_data_file) <- hh_cols
  hh_data_file$hh_lat <- as.numeric(hh_data_file$hh_lat)
  hh_data_file$hh_long <- as.numeric(hh_data_file$hh_long)
  
  return (hh_data_file)
}

load_cust_data <- function(mydb_abstract_db, CUST_TBL){
  query = "select Circuit_ID, cust_name, Longitude, Latitude, Cleaned_customer_Bandwidth, Date_Of_Acceptance, (LENGTH(SUBSTR(Longitude ,INSTR(Longitude,'.'))) - 1) as long_sigdig , (LENGTH(SUBSTR(Latitude ,INSTR(Latitude,'.'))) - 1) as lat_sigdig 
 from"
  query = paste(query, CUST_TBL, sep = " ")
  
  cust_data_file = dbSendQuery(mydb_abstract_db, query)
  # fetching data from mysql server
  cust_data_file = fetch(cust_data_file, n=-1)
  # Column Mapping
  cust_cols <- c('SERVICEID','CUST_NAME','Longitude','Latitude','F12','PROVISIONING_START_DATE', "long_sigdig", "lat_sigdig")
  
  colnames(cust_data_file) <- cust_cols
  
  cust_data_file$Latitude <- as.numeric(cust_data_file$Latitude)
  cust_data_file$Longitude <- as.numeric(cust_data_file$Longitude)
  
  return (cust_data_file)
}

load_prospect_data <- function(mydb_abstract_db, PROSPECT_TBL){
  
  query = "select Prospect_ID, resp_state, Feasibility_Response_Created_Date, Latitude_final, Longitude_final, Status, Cleaned_BW from"
  query = paste(query, PROSPECT_TBL, sep = " ")
  pros_data = dbSendQuery(mydb_abstract_db, query)
  # fetching data from mysql server
  pros_data = fetch(pros_data, n=-1)
  
  pros_cols <- c("Prospect_ID_2","prospect_state","prospect_date","prospect_lat","prospect_lon",
                 "prospect_status","prospect_bw")
  
  colnames(pros_data) <- pros_cols
  
  pros_data$prospect_lat <- as.numeric(pros_data$prospect_lat)
  pros_data$prospect_lon <- as.numeric(pros_data$prospect_lon)
  
  # prospect_coords <- pros_data
  
  return (pros_data)
}

load_man_city_data <- function(mydb_abstract_db){
  
  man_city = dbSendQuery(mydb_abstract_db, "select seq_no,city_id,city_name,cost_permeter,state_name,refrfstateid,center_x,center_y,if(isonnetcity, 1, 0) as isonnetcity from eeplus_city_master_data")
  
  # fetching data from mysql server
  man_city = fetch(man_city, n=-1)
  # Column Mapping
  man_city_cols <- c('seq_no','City_id','CITY_NAME','cost_permeter','State_Name','refRFstateid','CENTER_X','CENTER_Y','IsOnnetCity')
  
  colnames(man_city) <- man_city_cols
  
  return (man_city)
  
}

load_row_city_data <- function(mydb_abstract_db){
  
  row_city = dbSendQuery(mydb_abstract_db, "select city_name, manual_flag from row_capex_cities_manual where manual_flag = 1")
  
  # fetching data from mysql server
  row_city = fetch(row_city, n=-1)

  
  return (row_city)
  
}


add_pop_features <- function(pop_data_file, input_data, save_matrix){

    col_list = c("Prospect_ID", "Latitude_final", "Longitude_final", "product.name.flag")
    if (sum(col_list %in% names(input_data)) < length(col_list)) stop("Missing Column")
    
    col_list = c("pop_long", "pop_lat", "Services.Offered.IAS", "Services.Offered.NPL", "Services.Offered.GVPN", 
                 "Services.Offered.GDE", "Services.Offered.NDE", "Services.Offered.IPL", "Services.Offered.Video.Connect", "Services.Offered.Priority.Ethernet")
    
    if (sum(col_list %in% names(pop_data_file)) < length(col_list)) stop("Missing Column")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Pop related Features
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    pop_features_matrix <- bind_rows(lapply(as.list(input_data$Prospect_ID), fn_pop_distance_calc))
    
    if (save_matrix != ""){saveRDS(pop_features_matrix, save_matrix)}
    
    
    # Merge features to input data
    input_data <- merge(x= input_data,
                        y=pop_features_matrix,
                        by.x="Prospect_ID",
                        by.y="Prospect_ID",
                        all.x=T)
    
    
    # Add more features about the nearest POP ID
    input_data <- merge(x= input_data,
                        y=pop_data_file,
                        by.x="POP_ID_service",
                        by.y="POP_ID",
                        all.x=T)
    

    
    # input_data = input_data[!is.na(input_data$Prospect_ID),]
    
    input_data$pop_lat <- ifelse(is.na(input_data$pop_lat), 0, input_data$pop_lat)
    input_data$pop_long <- ifelse(is.na(input_data$pop_long), 0, input_data$pop_long)
    
    
    # Change column names
    colnames(input_data)[which(names(input_data) == "DistanceBetween")] <- "POP_DIST_KM"
    colnames(input_data)[which(names(input_data) == "DistanceBetween_service")] <- "POP_DIST_KM_SERVICE"
    
    # Add 1 more feature
    input_data$POP_DIST_KM_NOT_NULL <- ifelse(input_data$POP_DIST_KM > 0,1,0)
    
    # Remove later
    rm(pop_features_matrix)
  
  return (input_data)
  
}


add_fatg_features <- function(fatg_data_file, input_data, save_matrix){
  col_list = c("Prospect_ID", "Latitude_final", "Longitude_final")
  if (sum(col_list %in% names(input_data)) < length(col_list)) stop("Missing Column")
  
  col_list = c("fatg_long", "fatg_lat")
  if (sum(col_list %in% names(fatg_data_file)) < length(col_list)) stop("Missing Column")
  
  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  # FATG related Features
  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  fatg_features_matrix <- bind_rows(lapply(as.list(input_data$Prospect_ID), fn_fatg_distance_calc))
  
  if (save_matrix != ""){saveRDS(fatg_features_matrix, save_matrix)}
  
  # Merge features to input data
  input_data <- merge(x= input_data,
                      y=fatg_features_matrix,
                      by.x="Prospect_ID",
                      by.y="Prospect_ID",
                      all.x=T)
  
  # Add more features about the nearest POP ID
  input_data <- merge(x= input_data,
                      y=fatg_data_file,
                      by.x="FATG_ID",
                      by.y="FATG_ID",
                      all.x=T)

  # Change column names
  colnames(input_data)[which(names(input_data) == "DistanceBetween")] <- "FATG_DIST_KM"
  
  # Remove later
  rm(fatg_features_matrix)
  
  return (input_data)
  
}

add_hh_features <- function(hh_data_file, input_data, save_matrix){

  col_list = c("Prospect_ID", "Latitude_final", "Longitude_final")
  if (sum(col_list %in% names(input_data)) < length(col_list)) stop("Missing Column")
  
  col_list = c("hh_long", "hh_lat")
  if (sum(col_list %in% names(hh_data_file)) < length(col_list)) stop("Missing Column")
  
  hh_features_matrix <- bind_rows(lapply(as.list(input_data$Prospect_ID), fn_hh_distance_calc_features))
  if (save_matrix != ""){saveRDS(hh_features_matrix, save_matrix)}

  # Merge features to input data
  input_data <- merge(x= input_data,
                      y=hh_features_matrix,
                      by.x="Prospect_ID",
                      by.y="Prospect_ID",
                      all.x=T)

  # Add more features about the nearest POP ID
  input_data <- merge(x= input_data,
                      y=hh_data_file,
                      by.x="HH_ID",
                      by.y="HH_ID",
                      all.x=T)

  # # Change column names
  colnames(input_data)[which(names(input_data) == "DistanceBetween")] <- "HH_DIST_KM"
  
  rm(hh_features_matrix)
  
  return (input_data)
  
  
}

add_cust_features <- function(cust_coords, input_data, save_matrix){
  col_list = c("Prospect_ID", "Latitude_final", "Longitude_final", "Feasibility_Response_Created_Date")
  if (sum(col_list %in% names(input_data)) < length(col_list)) stop("Missing Column")
  
  col_list = c("cust_long", "cust_lat", "cust_date")
  if (sum(col_list %in% names(cust_coords)) < length(col_list)) stop("Missing Column")
  
  cust_features_matrix <- rbind(lapply(as.list(input_data$Prospect_ID), fn_cust_distance_calc_onnet_wl))
  cust_features_matrix <- do.call(rbind,cust_features_matrix)
  colnames(cust_features_matrix) <- c("Prospect_ID",
                                      "X0.5km_cust_count",
                                      "X0.5km_min_dist",
                                      "X0.5km_avg_dist",
                                      "X0.5km_min_bw",
                                      "X0.5km_avg_bw",
                                      "X0.5km_max_bw",
                                      "X2km_cust_count",
                                      "X2km_min_dist",
                                      "X2km_avg_dist",
                                      "X2km_min_bw",
                                      "X2km_avg_bw",
                                      "X2km_max_bw",
                                      "X5km_cust_count",
                                      "X5km_min_dist",
                                      "X5km_avg_dist",
                                      "X5km_min_bw",
                                      "X5km_avg_bw",
                                      "X5km_max_bw")
  
  
  #Missing value treatment
  cust_features_matrix[cust_features_matrix=='Inf'] <- 9999999
  cust_features_matrix[cust_features_matrix=='-Inf'] <- 9999999
  cust_features_matrix[cust_features_matrix=='NaN'] <- 9999999
  cust_features_matrix[is.na(cust_features_matrix)] <- 9999999
  
  chk <- sapply(cust_features_matrix,is.infinite)
  cust_features_matrix[chk] <- 9999999
  
  chk <- sapply(cust_features_matrix,is.nan)
  cust_features_matrix[chk] <- 9999999
  
  chk <- sapply(cust_features_matrix,is.na)
  cust_features_matrix[chk] <- 9999999
  
  if (save_matrix != ""){saveRDS(cust_features_matrix, save_matrix)}
  
  
  # Merge features to input data
  input_data <- merge(x= input_data,
                      y=cust_features_matrix,
                      by.x="Prospect_ID",
                      by.y="Prospect_ID",
                      all.x=T)
  
  rm(cust_features_matrix)
  return (input_data)
  
}


add_prospect_features <- function(prospect_coords, input_data, save_matrix, cc){
  col_list = c("Prospect_ID", "Latitude_final", "Longitude_final", "Feasibility_Response_Created_Date")
  if (sum(col_list %in% names(input_data)) < length(col_list)) stop("Missing Column")
  
  col_list = c("prospect_lon", "prospect_lat", "prospect_date")
  if (sum(col_list %in% names(prospect_coords)) < length(col_list)) stop("Missing Column")
  
  pros_features_matrix <- rbind(lapply(as.list(input_data$Prospect_ID), fn_prospect_distance_calc_onnet_wl))

  
    
  pros_features_matrix <- do.call(rbind,pros_features_matrix)
  colnames(pros_features_matrix) <- c("Prospect_ID",
                                      "X0.5km_prospect_count",
                                      "X0.5km_prospect_min_dist",
                                      "X0.5km_prospect_avg_dist",
                                      "X0.5km_prospect_min_bw",
                                      "X0.5km_prospect_avg_bw",
                                      "X0.5km_prospect_max_bw",
                                      "X0.5km_prospect_num_feasible",
                                      "X0.5km_prospect_perc_feasible",
                                      "X2km_prospect_count",
                                      "X2km_prospect_min_dist",
                                      "X2km_prospect_avg_dist",
                                      "X2km_prospect_min_bw",
                                      "X2km_prospect_avg_bw",
                                      "X2km_prospect_max_bw",
                                      "X2km_prospect_num_feasible",
                                      "X2km_prospect_perc_feasible",
                                      "X5km_prospect_count",
                                      "X5km_prospect_min_dist",
                                      "X5km_prospect_avg_dist",
                                      "X5km_prospect_min_bw",
                                      "X5km_prospect_avg_bw",
                                      "X5km_prospect_max_bw",
                                      "X5km_prospect_num_feasible",
                                      "X5km_prospect_perc_feasible")
  
  pros_features_matrix[pros_features_matrix=='Inf'] <- 9999999
  pros_features_matrix[pros_features_matrix=='-Inf'] <- 9999999
  pros_features_matrix[pros_features_matrix=='NaN'] <- 9999999
  pros_features_matrix[is.na(pros_features_matrix)] <- 9999999
  
  chk <- sapply(pros_features_matrix,is.infinite)
  pros_features_matrix[chk] <- 9999999
  
  chk <- sapply(pros_features_matrix,is.nan)
  pros_features_matrix[chk] <- 9999999
  
  chk <- sapply(pros_features_matrix,is.na)
  pros_features_matrix[chk] <- 9999999
  
  pros_features_matrix[ ,c("X0.5km_prospect_num_feasible",
                           "X2km_prospect_num_feasible",
                           "X5km_prospect_num_feasible",
                           "X0.5km_prospect_perc_feasible",
                           "X2km_prospect_perc_feasible",
                           "X5km_prospect_perc_feasible")][pros_features_matrix[ ,c("X0.5km_prospect_num_feasible",
                                                                                    "X2km_prospect_num_feasible",
                                                                                    "X5km_prospect_num_feasible",
                                                                                    "X0.5km_prospect_perc_feasible",
                                                                                    "X2km_prospect_perc_feasible",
                                                                                    "X5km_prospect_perc_feasible")]==9999999 ] <- 0
  
  
  if (save_matrix != ""){saveRDS(pros_features_matrix, save_matrix)}
  # Merge features to input data
  input_data <- merge(x= input_data,
                      y=pros_features_matrix,
                      by.x="Prospect_ID",
                      by.y="Prospect_ID",
                      all.x=T)
  
  rm(pros_features_matrix)
  return (input_data)
}

add_man_city_features <- function(man_city, input_data){

  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  # MAN CITY data - Roll up
  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  man_city$CITY_NAME = tolower(man_city$CITY_NAME)
  man_city <- man_city[!duplicated(man_city$CITY_NAME),]
  
  input_data$resp_city = tolower(input_data$resp_city)
  
  input_data <- merge(x=input_data,y=man_city[,c("CITY_NAME","IsOnnetCity")],by.x="resp_city",by.y="CITY_NAME", all.x = T)
  
  # Clean MAN CIty feature
  # input_data$OnnetCity_tag <- ifelse(is.na(input_data$IsOnnetCity)==T,1,0)
  input_data$OnnetCity_tag <- input_data$IsOnnetCity
  input_data$OnnetCity_tag[is.na(input_data$OnnetCity_tag)] <- 0
  
  return (input_data)
}

convert_to_num <- function(input_data){
  
  
  # Convert to numeric
  
  features_factor <- c("X0.5km_cust_count",
                       "X0.5km_min_dist",
                       "X0.5km_avg_dist",
                       "X0.5km_min_bw",
                       "X0.5km_avg_bw",
                       "X0.5km_max_bw",
                       "X2km_cust_count",
                       "X2km_min_dist",
                       "X2km_avg_dist",
                       "X2km_min_bw",
                       "X2km_avg_bw",
                       "X2km_max_bw",
                       "X5km_cust_count",
                       "X5km_min_dist",
                       "X5km_avg_dist",
                       "X5km_min_bw",
                       "X5km_avg_bw",
                       "X5km_max_bw",
                       
                       "X0.5km_prospect_count",
                       "X0.5km_prospect_min_dist",
                       "X0.5km_prospect_avg_dist",
                       "X0.5km_prospect_min_bw",
                       "X0.5km_prospect_avg_bw",
                       "X0.5km_prospect_max_bw",
                       "X0.5km_prospect_num_feasible",
                       "X0.5km_prospect_perc_feasible",
                       "X2km_prospect_count",
                       "X2km_prospect_min_dist",
                       "X2km_prospect_avg_dist",
                       "X2km_prospect_min_bw",
                       "X2km_prospect_avg_bw",
                       "X2km_prospect_max_bw",
                       "X2km_prospect_num_feasible",
                       "X2km_prospect_perc_feasible",
                       "X5km_prospect_count",
                       "X5km_prospect_min_dist",
                       "X5km_prospect_avg_dist",
                       "X5km_prospect_min_bw",
                       "X5km_prospect_avg_bw",
                       "X5km_prospect_max_bw",
                       "X5km_prospect_num_feasible",
                       "X5km_prospect_perc_feasible",
                       "BW_mbps")
  
  input_data[,features_factor] = apply(input_data[features_factor], 2, function(x) as.numeric(as.character(x)));
  return (input_data)
  
}

convert_to_char <- function(input_data){
  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  # Cleaning all features
  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  # input_data$BW_mbps <- as.numeric(input_data$BW_mbps)
  input_data$POP_Network_Location_Type <- as.character(input_data$POP_Network_Location_Type)
  input_data$POP_Construction_Status <- as.character(input_data$POP_Construction_Status)
  input_data$POP_Building_Type <- as.character(input_data$POP_Building_Type)
  input_data$POP_Category <- as.character(input_data$POP_Category)
  input_data$POP_TCL_Access <- as.character(input_data$POP_TCL_Access)
  input_data$FATG_Network_Location_Type <- as.character(input_data$FATG_Network_Location_Type)
  input_data$FATG_Building_Type <- as.character(input_data$FATG_Building_Type)
  input_data$FATG_Category <- as.character(input_data$FATG_Category)
  input_data$FATG_TCL_Access <- as.character(input_data$FATG_TCL_Access) 
  input_data$FATG_PROW <- as.character(input_data$FATG_PROW )
  input_data$FATG_Ring_type <- as.character(input_data$FATG_Ring_type) 
  
  vec <- c("POP_Network_Location_Type","POP_Construction_Status","POP_Building_Type","POP_Category","POP_TCL_Access",
           "FATG_Network_Location_Type","FATG_Building_Type","FATG_Category","FATG_TCL_Access" ,"FATG_PROW" ,"FATG_Ring_type" )
  
  input_data[vec][is.na(input_data[vec])] <- "xxx"
  #input_data$Customer_Segment <- ifelse(input_data$Customer_Segment=="","XXX",as.character(input_data$Customer_Segment))
  
  return (input_data)
}

create_log <- function(logfile, msg ,log ){
  if (log)
  {
    sink(logfile, append = TRUE)
    print(paste(Sys.time(), msg, sep=":"))
    sink()
  }
}
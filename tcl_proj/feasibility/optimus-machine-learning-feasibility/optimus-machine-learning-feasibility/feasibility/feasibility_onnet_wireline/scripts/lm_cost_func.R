calc_match <- function(prospect_name, cust_name)
{
  RecordLinkage = 0
  #Connected Building: condition cust_name != NA added
  if(!is.na(prospect_name) & prospect_name != "" & !is.na(cust_name))
  {
    RecordLinkage <- RecordLinkage::levenshteinSim(tolower(prospect_name), tolower(cust_name))

  }

  return (RecordLinkage)
}


convert_bw_to_lle <- function(local_loop_interface, BW_mbps)
{

  # local_loop_interface <- ifelse(toupper(local_loop_interface)=="GE","GE","FE)
  local_loop_interface <- toupper(local_loop_interface)
  
  #In case BW < 50 and it is GE,  we convert to FE
  local_loop_interface <- ifelse((BW_mbps<CUTOFF_FE
                                             & local_loop_interface == "GE"),"FE",
                                            as.character(local_loop_interface))

  local_loop_interface <- ifelse((BW_mbps>CUTOFF_GE
                                  & local_loop_interface == "FE"),"GE",
                                 as.character(local_loop_interface))

  return (local_loop_interface)
}


round_bw <- function(BW_mbps, local_loop_interface)
{
  #Rounding bandwidth to nearest 2 
  BW_mbps_2 <- as.numeric(as.character(BW_mbps))
  
  BW_mbps_2 <- ifelse(BW_mbps < 2,2,
                     ifelse(((BW_mbps%%2==1) & (BW_mbps <= 100) & (local_loop_interface == "FE")),(BW_mbps+1),
                            ifelse(((BW_mbps >100) & (BW_mbps%%50 >0) & (local_loop_interface == "FE")),plyr::round_any(BW_mbps,50), 
                                   ifelse(((BW_mbps >=50) & (BW_mbps%%50 >0) & (local_loop_interface == "GE")),plyr::round_any(BW_mbps,50),
                                          BW_mbps))))
  
  return (BW_mbps_2)
}

get_adj_pop_dist <- function(POP_DIST_SERVICE_MTR, adj_fac)
{

  # Converting metres to Kms and adjust by 1.25 as per the business rule
  POP_DIST_KM_SERVICE <- (POP_DIST_SERVICE_MTR/1000)*(adj_fac)
  # input_data$POP_DIST_KM <- input_data$POP_DIST_KM/1000
  
  #Rounding distance to nearest 5 and putting upper limit of 501 and lower limit of 5 kms to it
  POP_DIST_KM_SERVICE_MOD <- plyr::round_any(POP_DIST_KM_SERVICE, 5, ceiling)
  POP_DIST_KM_SERVICE_MOD <- ifelse(POP_DIST_KM_SERVICE_MOD > 501,501,ifelse(POP_DIST_KM_SERVICE_MOD==0,5,POP_DIST_KM_SERVICE_MOD))
  
  return (POP_DIST_KM_SERVICE_MOD)
  
}

load_arc_rate_card <- function(mydb_abstract_db)
{
  # sending query to mysql db
  bw_all_stack = dbSendQuery(mydb_abstract_db, "select seq_no,sno,Distance,Bandwidth,local_loop_type,price from cq_tblcapexarc_onnet")
  
  # fetching data from mysql server
  bw_all_stack = fetch(bw_all_stack, n=-1)
  # Column Mapping
  bw_all_stack_cols <- c('seq_no','sno','Distance','BW_mbps','type','value')
  
  colnames(bw_all_stack) <- bw_all_stack_cols
  
  return (bw_all_stack)
  
}


  #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  # Function to check for connected customers and connected buildings for LM costs
  #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
fn_connected_bldgs <- function(ID){
  
  col_list = c("Prospect_ID", "Feasibility_Response_Created_Date")
  if (sum(col_list %in% names(input_data)) < length(col_list)) stop("Missing Column")
  
  col_list = c("cust_long", "cust_lat", "cust_date")
  if (sum(col_list %in% names(cust_coords)) < length(col_list)) stop("Missing Column")

  
  TMP <- subset(input_data,input_data$Prospect_ID == ID)
  P_long <- TMP$Longitude_final
  P_lat <- TMP$Latitude_final
  # reducing search space
  cust_coords_sub <- cust_coords[which(between(cust_coords$cust_long, P_long - 0.01, P_long + 0.01) &
                                         between(cust_coords$cust_lat, P_lat - 0.01, P_lat + 0.01) & (cust_coords$cust_date < TMP$Feasibility_Response_Created_Date | is.na(cust_coords$cust_date))),]
  
  #Creating an empty vector
  name_vec <-   c("V1","CUST_ID","SERVICE_ID","cust_date","cust_lat",
                  "cust_long", "cust_bw","cust_name", "cust_lat_dig", "cust_long_dig",colnames(input_data))
  E <- data.frame(matrix(NA, nrow = 1, ncol = length(name_vec)))
  names(E) = name_vec
  

  if(nrow(cust_coords_sub) ==0)
  {return(E)
  } else {
    TMP1 <- distHaversine(TMP[,c("Longitude_final","Latitude_final")],cust_coords_sub[,c("cust_long","cust_lat")])
    TMP1_c <- which(TMP1 <= CONNECT_BUILD_DIST)
    if(length(TMP1_c)==0)
    {return(E)
    }else{
      TMP2 <-as.data.frame(cbind(TMP1[TMP1_c],cust_coords_sub[TMP1_c,],as.data.frame(TMP[rep(1:nrow(TMP),each=length(TMP1_c)),])))
      #print(ID)
      return(TMP2)
      gc()}}
}

get_connected_entity <- function(input_data, cust_coords){
  
  connected_custs <- rbind(lapply(as.list(as.character(input_data$Prospect_ID)), fn_connected_bldgs))
  connected_custs <- do.call(rbind,connected_custs)

  connected_custs$cust_name <- tolower(connected_custs$cust_name)
  connected_custs$prospect_name <- tolower(connected_custs$prospect_name)
  # connected_custs_match <- subset(connected_custs,!is.na(connected_custs$cust_name))
  ##Connected Building: Above condition for Cust Names as NA reloved as 15K cust data does not contain cust name
  connected_custs_match = subset(connected_custs,!is.na(connected_custs$CUST_ID))
  
  # if no customer is connected then do error handling and add 0 for corresponding features
  if(nrow(connected_custs_match)!=0){
    # See if the prospect is one of our own customer or not
    RecordLinkage_all <- plyr::empty(df)
    
    # for(i in 1 : nrow(connected_custs_match)){
    #   if (connected_custs_match[i,c("prospect_name")]==""){RecordLinkage <- 0} else {
    #     RecordLinkage <- RecordLinkage::levenshteinSim(connected_custs_match[i,c("prospect_name")],connected_custs_match[i,c("cust_name")])
    #   }
    #   
    #   RecordLinkage_all <- rbind(RecordLinkage_all,RecordLinkage)
    #   #print(i)
    # }
    RecordLinkage_all <- mapply(calc_match, connected_custs_match$prospect_name, connected_custs_match$cust_name)
    
    RecordLinkage_all_2 <- as.data.frame(RecordLinkage_all)
    # RecordLinkage_all_2 <- RecordLinkage_all_2[2:nrow(RecordLinkage_all_2),]
    connected_custs_match <- cbind(connected_custs_match,RecordLinkage_all_2)
    

  }
  
  return (connected_custs_match)
}

get_connected_entity_overload <- function(input_data, cust_coords, dist_list){
  
  connected_custs <- rbind(lapply(as.list(as.character(input_data$Prospect_ID)), fn_connected_bldgs))
  connected_custs <- do.call(rbind,connected_custs)
  
  connected_custs$cust_name <- tolower(connected_custs$cust_name)
  connected_custs$prospect_name <- tolower(connected_custs$prospect_name)
  connected_custs_match <- subset(connected_custs,!is.na(connected_custs$cust_name))
  
  # if no customer is connected then do error handling and add 0 for corresponding features
  if(nrow(connected_custs_match)!=0){
    # See if the prospect is one of our own customer or not
    RecordLinkage_all <- plyr::empty(df)
    
    # for(i in 1 : nrow(connected_custs_match)){
    #   if (connected_custs_match[i,c("prospect_name")]==""){RecordLinkage <- 0} else {
    #     RecordLinkage <- RecordLinkage::levenshteinSim(connected_custs_match[i,c("prospect_name")],connected_custs_match[i,c("cust_name")])
    #   }
    #   
    #   RecordLinkage_all <- rbind(RecordLinkage_all,RecordLinkage)
    #   #print(i)
    # }
    RecordLinkage_all <- mapply(calc_match, connected_custs_match$prospect_name, connected_custs_match$cust_name)
    
    RecordLinkage_all_2 <- as.data.frame(RecordLinkage_all)
    # RecordLinkage_all_2 <- RecordLinkage_all_2[2:nrow(RecordLinkage_all_2),]
    connected_custs_match <- cbind(connected_custs_match,RecordLinkage_all_2)
    
    connected_custs_match$similar_cust_name <- ifelse(connected_custs_match$RecordLinkage_all >= 0.7,1,0)
    
    # connected_custs_match$connected_building <- 1
    
    # tmp = head(connected_custs_match[,c("V1", "similar_cust_name")], 20)
    
    ## Create multiple columns for connected building
    df = cbind((sapply(dist_list,function (x) ifelse(connected_custs_match$V1 <= x, 1, 0) )))
    df = as.data.frame(df)
    names(df) <- sapply(dist_list, function(x) paste0("connected_building_", x))
    connected_custs_match = cbind(connected_custs_match, df)
    
    ## Create multiple columns for connected building
    df = cbind((sapply(dist_list,function (x) ifelse(connected_custs_match[paste0("connected_building_", x)] & connected_custs_match$similar_cust_name, 1, 0) )))
    df = as.data.frame(df)
    names(df) <- sapply(dist_list, function(x) paste0("connected_cust_", x))
    connected_custs_match = cbind(connected_custs_match, df)
    
    # connected_custs_match$connected_building_50 <- ifelse(connected_custs_match$V1 < 50, 1, 0)
    # connected_custs_match$connected_building_100 <- ifelse(connected_custs_match$V1 <= 100, 1, 0)
    
    # connected_custs_match$connected_cust_50 <- ifelse(connected_custs_match$connected_building_50 & connected_custs_match$similar_cust_name, 1, 0)
    # connected_custs_match$connected_cust_100 <- ifelse(connected_custs_match$connected_building_100 & connected_custs_match$similar_cust_name, 1, 0)
    # 
    # 
    # 
  }
  
  return (connected_custs_match)
}


decimalplaces <- function(x) {
  if (abs(x - round(x)) > .Machine$double.eps^0.5) {
    nchar(strsplit(sub('0+$', '', as.character(x)), ".", fixed = TRUE)[[1]][[2]])
  } else {
    return(0)
  }
}


connected_building_rule <- function(lat, long)
{
  ##Both lat, long of the customer should have at least 4 or more significant digits to qualify for connected building
  lat_dig = sapply(as.numeric(lat), decimalplaces)
  long_dig = sapply(as.numeric(long), decimalplaces)
  
  conn_build = ifelse(lat_dig >= 4 & long_dig >= 4, 1, 0)
  
  ##For scoring google api will send prospect lat/ long with 6 digits precision.
  return (conn_build)
}

#"Customer_Segment", ,"FATG_Ring_type"
# FEATURE_SET = c("Product.Name","BW_mbps","POP_DIST_KM",
#                 "POP_DIST_KM_SERVICE","POP_Network_Location_Type","POP_Construction_Status",
#                 "POP_Building_Type","POP_Category","POP_TCL_Access","FATG_DIST_KM",
#                 "FATG_Network_Location_Type","FATG_Building_Type","FATG_Category", "FATG_Ring_type",
#                 "FATG_TCL_Access","FATG_PROW","HH_DIST_KM",
#                 "X0.5km_cust_count","X0.5km_min_dist","X0.5km_avg_dist","X0.5km_min_bw",
#                 "X0.5km_max_bw","X0.5km_avg_bw","X2km_cust_count","X2km_min_dist",
#                 "X2km_avg_dist","X2km_min_bw","X2km_max_bw","X2km_avg_bw",
#                 "X5km_cust_count","X5km_min_dist","X5km_avg_dist","X5km_min_bw",
#                 "X5km_max_bw","X5km_avg_bw","X0.5km_prospect_count","X0.5km_prospect_min_dist",
#                 "X0.5km_prospect_avg_dist","X0.5km_prospect_min_bw","X0.5km_prospect_avg_bw",
#                 "X0.5km_prospect_max_bw","X0.5km_prospect_num_feasible","X0.5km_prospect_perc_feasible",
#                 "X2km_prospect_count","X2km_prospect_min_dist","X2km_prospect_avg_dist",
#                 "X2km_prospect_min_bw","X2km_prospect_avg_bw","X2km_prospect_max_bw",
#                 "X2km_prospect_num_feasible","X2km_prospect_perc_feasible","X5km_prospect_count",
#                 "X5km_prospect_min_dist","X5km_prospect_avg_dist","X5km_prospect_min_bw",
#                 "X5km_prospect_avg_bw","X5km_prospect_max_bw","X5km_prospect_num_feasible",
#                 "X5km_prospect_perc_feasible","OnnetCity_tag")




  ##########################################################################################
  ##########################################################################################
  # FUNTIONS - User defined functions - Add them to source file later
  ##########################################################################################
  ##########################################################################################
  
  #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  # Function to calculate features for Pop locations and service
  #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  fn_pop_distance_calc <- function(ID){


    TMP <- subset(input_data,input_data$Prospect_ID == ID)
    P_long <- TMP$Longitude_final
    P_lat <- TMP$Latitude_final
    # reducing search space
    pop_sub <- pop_data_file[which(between(pop_data_file$pop_long, P_long - 1, P_long + 1) &
                                     between(pop_data_file$pop_lat, P_lat - 1, P_lat + 1)),]
    #pop_sub <- subset(pop_data_file,pop_data_file$POP_state == TMP$resp_state)
    
    pop_sub$product_match <- ifelse(TMP$product.name.flag == "ILL" & pop_sub$Services.Offered.IAS == "Yes",1,
                                    ifelse(TMP$product.name.flag == "NPL" & pop_sub$Services.Offered.NPL == "Yes",1,
                                           ifelse(TMP$product.name.flag == "GVPN" & pop_sub$Services.Offered.GVPN == "Yes",1,
                                                  ifelse(TMP$product.name.flag == "GDE" & pop_sub$Services.Offered.GDE == "Yes",1,
                                                         ifelse(TMP$product.name.flag == "NDE" & pop_sub$Services.Offered.NDE == "Yes",1,
                                                                ifelse(TMP$product.name.flag == "IPL" & pop_sub$Services.Offered.IPL == "Yes",1,
                                                                       ifelse(TMP$product.name.flag == "VC" & pop_sub$Services.Offered.Video.Connect == "Yes",1,
                                                                              ifelse(TMP$product.name.flag == "Ethernet" & pop_sub$Services.Offered.Priority.Ethernet == "Yes",1,0
                                                                              ))))))))
    
    pop_service <- subset(pop_sub,pop_sub$product_match==1)
    
    if(nrow(pop_sub) ==0)
    {E = data.frame(Prospect_ID=ID,POP_ID=0,DistanceBetween=9999999,POP_ID_service=0,DistanceBetween_service=9999999)
    return(E)
    } else { 
      if(nrow(pop_service) == 0)
      {TMP1 <- (cbind(distHaversine(TMP[,c("Longitude_final","Latitude_final")],pop_sub[,c("pop_long", "pop_lat")]),pop_sub$product_match,pop_sub$POP_ID))
      TMP2 <- data.frame(Prospect_ID=TMP$Prospect_ID,POP_ID=as.numeric(as.character(pop_sub[which.min(TMP1[,1]),1])),DistanceBetween=min(TMP1[,1]))
      TMP3 = data.frame(POP_ID_service = 0,DistanceBetween_service=0)
      TMP4 <- cbind(TMP2,TMP3) 
      #print(ID)
      return(TMP4)
      } else {
        
        TMP1 <- (cbind(distHaversine(TMP[,c("Longitude_final","Latitude_final")],pop_sub[,c("pop_long", "pop_lat")]),pop_sub$product_match,pop_sub$POP_ID))
        TMP1_c <- (cbind(distHaversine(TMP[,c("Longitude_final","Latitude_final")],pop_service[,c("pop_long", "pop_lat")]),pop_service$product_match,pop_service$POP_ID))
        TMP2 <- data.frame(Prospect_ID=TMP$Prospect_ID,POP_ID=as.numeric(as.character(pop_sub[which.min(TMP1[,1]),1])),DistanceBetween=min(TMP1[,1]))
        TMP3 <- data.frame(POP_ID_service=as.numeric(as.character(pop_service[which.min(TMP1_c[,1]),1])),DistanceBetween_service=min(TMP1_c[,1]))
        TMP4 <- cbind(TMP2,TMP3) }                                                                                                                                                      
      #print(ID)
      return(TMP4)}
    gc()
  }
  
  #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  # Function to calculate features for FATG locations and service
  #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  fn_fatg_distance_calc <- function(ID){
    

    TMP <- subset(input_data,input_data$Prospect_ID == ID)
    P_long <- TMP$Longitude_final
    P_lat <- TMP$Latitude_final
    # reducing search space
    fatg_sub <- fatg_data_file[which(between(fatg_data_file$fatg_long, P_long - 1, P_long + 1) &
                                       between(fatg_data_file$fatg_lat, P_lat - 1, P_lat + 1)),]
    #fatg_sub <- subset(fatg_data_file,fatg_data_file$fatg_state == TMP$resp_state)
    if(nrow(fatg_sub) ==0)
    {E = data.frame(Prospect_ID=ID,FATG_ID=0,DistanceBetween=0)
    return(E)
    } else {
      TMP1 <- distHaversine(TMP[,c("Longitude_final","Latitude_final")],fatg_sub[,c("fatg_long","fatg_lat")])
      TMP2 <- data.frame(Prospect_ID=ID,FATG_ID=as.numeric(as.character(fatg_sub[which.min(TMP1),1])),DistanceBetween=min(TMP1))
      #print(ID)
      return(TMP2)
      gc()}
  }
  
  #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  # Function to calculate features for HH locations and service
  #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  fn_hh_distance_calc_features <- function(ID){
    

    TMP <- subset(input_data,input_data$Prospect_ID == ID)
    P_long <- TMP$Longitude_final
    P_lat <- TMP$Latitude_final
    # reducing search space
    hh_coords_sub <- hh_data_file[which(between(hh_data_file$hh_long, P_long - 1, P_long + 1) &
                                          between(hh_data_file$hh_lat, P_lat - 1, P_lat + 1)),]
    #hh_coords_sub <- subset(hh_coords,hh_coords$hh_state == TMP$resp_state)
    if(nrow(hh_coords_sub) ==0)
    {E = data.frame(Prospect_ID=ID,HH_ID=0,DistanceBetween=99999999)
    return(E)
    } else {
      TMP1 <- distHaversine(TMP[,c("Longitude_final","Latitude_final")],hh_coords_sub[,c("hh_long","hh_lat")])
      TMP2 <- data.frame(Prospect_ID=ID,HH_ID=as.numeric(as.character(hh_coords_sub[which.min(TMP1),1])),DistanceBetween=min(TMP1))
      #print(ID)
      return(TMP2)
      gc()}
  }
  
  #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  # Function to calculate features for Customers locations and service
  #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  fn_cust_distance_calc_onnet_wl <- function(ID){

    TMP <- subset(input_data,input_data$Prospect_ID == ID)
    P_long <- TMP$Longitude_final
    P_lat <- TMP$Latitude_final
    # reducing search space
    cust_coords_sub <- cust_coords[which(between(cust_coords$cust_long, P_long - 0.1, P_long + 0.1) &
                                           between(cust_coords$cust_lat, P_lat - 0.1, P_lat + 0.1) & (cust_coords$cust_date < TMP$Feasibility_Response_Created_Date | is.na(cust_coords$cust_date))),]
    
    if(nrow(cust_coords_sub) ==0)
    {E = c(ID,0,9999999,9999999,9999999,9999999,9999999,0,9999999,9999999,9999999,9999999,9999999,0,9999999,9999999,9999999,9999999,9999999)
    return(E)
    } else {
      TMP1 <- distHaversine(TMP[,c("Longitude_final","Latitude_final")],cust_coords_sub[,c("cust_long","cust_lat")])
      dist_condn <- c(500,2000,5000)
      summ <- sapply(dist_condn, function(x){
        TMP1_c <- which(TMP1 <= x)
        data.frame(
          cust_count = length(TMP1_c),  
          min_dist = min(TMP1[TMP1_c],na.rm = T),
          avg_dist = mean(TMP1[TMP1_c],na.rm = T),
          min_bw = min(as.vector(cust_coords_sub$cust_bw[TMP1_c]),na.rm = T),
          avg_bw = mean(as.vector(cust_coords_sub$cust_bw[TMP1_c]),na.rm = T),
          max_bw = max(as.vector(cust_coords_sub$cust_bw[TMP1_c]),na.rm = T))})
      TMP2 <- c(ID,as.vector(unlist(summ)))
      #print(ID)
      return(TMP2)
      gc()}
  }
  
  #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  # Function to calculate features for Prospects locations and service
  #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

  fn_prospect_distance_calc_onnet_wl <- function(ID){

    TMP <- subset(input_data,input_data$Prospect_ID == ID)
    P_long <- TMP$Longitude_final
    P_lat <- TMP$Latitude_final
    # reducing search space
    prospect_dup_coords_sub <- prospect_coords[which(between(prospect_coords$prospect_lon, P_long - 0.1, P_long + 0.1) &
                                                       between(prospect_coords$prospect_lat, P_lat - 0.1, P_lat + 0.1) & (prospect_coords$prospect_date < TMP$Feasibility_Response_Created_Date)),]
    
    
    if(nrow(prospect_dup_coords_sub) ==0)
    {E = c(ID,0,9999999,9999999,9999999,9999999,9999999,9999999,9999999,0,9999999,9999999,9999999,9999999,9999999,9999999,9999999,0,9999999,9999999,9999999,9999999,9999999,9999999,9999999)
    return(E)
    } else {
      TMP1 <- distHaversine(TMP[,c("Longitude_final","Latitude_final")],prospect_dup_coords_sub[,c("prospect_lon","prospect_lat")])
      dist_condn <- c(500,2000,5000)
      summ <- sapply(dist_condn, function(x){
        TMP1_c <- which(TMP1 <= x)
        data.frame(
          cust_count = length(TMP1_c),
          min_dist = min(TMP1[TMP1_c],na.rm = T),
          avg_dist = mean(TMP1[TMP1_c],na.rm = T),
          min_bw = min(as.vector(as.numeric(as.character(prospect_dup_coords_sub$prospect_bw[TMP1_c]))),na.rm = T),
          avg_bw = mean(as.vector(as.numeric(as.character(prospect_dup_coords_sub$prospect_bw[TMP1_c]))),na.rm = T),
          max_bw = max(as.vector(as.numeric(as.character(prospect_dup_coords_sub$prospect_bw[TMP1_c]))),na.rm = T),
          num_feasible =  length(which(as.vector(prospect_dup_coords_sub$prospect_status[TMP1_c])=="Feasible")),
          perc_feasible = length(which(as.vector(prospect_dup_coords_sub$prospect_status[TMP1_c])=="Feasible"))/length(TMP1_c))})
      TMP2 <- c(ID,as.vector(unlist(summ)))
      #print(ID)
      return(TMP2)
      gc()}
  }

load_nwk_hh_data <- function(mydb_abstract_db)
{
  
  #hh_data_network <- read.csv(hh_data_network_name)
  # sending query to mysql db
  hh_data_network = dbSendQuery(mydb_abstract_db, "select seq_no,chamber_name,latitude,longitude,rings from chamber_ring")
  
  # fetching data from mysql server
  hh_data_network = fetch(hh_data_network, n=-1)
  # Column Mapping
  hh_data_network_cols <- c('seq_no','chamber_name','latitude','longitude','access_rings_hh')
  
  colnames(hh_data_network) <- hh_data_network_cols
  
  hh_data_network$latitude <- as.numeric(hh_data_network$latitude)
  hh_data_network$longitude <- as.numeric(hh_data_network$longitude)
  
  return (hh_data_network)
}


load_nwk_mux_serviceid_mapping <- function(mydb_abstract_db)
{
  
  dropporttoservice = dbSendQuery(mydb_abstract_db, "select seq_no,serviceoriorid,nodename, nodealias2, portname from dropporttoservice")
  
  # fetching data from mysql server
  dropporttoservice = fetch(dropporttoservice, n=-1)
  # Column Mapping
  dropporttoservice_cols <- c('seq_no','SERVICEORIORID','mux', 'mux_port', 'mux_ip')
  
  colnames(dropporttoservice) <- dropporttoservice_cols
  
  return (dropporttoservice)
}


load_nwk_access_ring_data <- function(mydb_abstract_db)
  {
  #TopologyTerminationReport <- read.csv(TopologyTerminationReport_name,stringsAsFactors = F)
  
  # Access Ring
  # sending query to mysql db
  TopologyTerminationReport_access = dbSendQuery(mydb_abstract_db, "select seq_no,topologyname,bandwidth,nodename,coverage from topology_termination_access_ring_report")
  
  # fetching data from mysql server
  TopologyTerminationReport_access = fetch(TopologyTerminationReport_access, n=-1)
  top_term_access_cols <- c('seq_no','selected_access_ring','selected_access_ring_Bandwidth','NODENAME','selected_access_ring_Coverage')
  
  colnames(TopologyTerminationReport_access) <- top_term_access_cols
  
  return (TopologyTerminationReport_access)
}


load_nwk_core_ring_data <- function(mydb_abstract_db)
{# Core Ring
  # sending query to mysql db
  
  TopologyTerminationReport_core = dbSendQuery(mydb_abstract_db, "select seq_no,topologyname,nodename from topology_termination_core_ring_report")
  
  # fetching data from mysql server
  TopologyTerminationReport_core = fetch(TopologyTerminationReport_core, n=-1)
  top_term_core_cols <- c('seq_no','core_ring','NODENAME')
  
  colnames(TopologyTerminationReport_core) <- top_term_core_cols
  
  return (TopologyTerminationReport_core)
  
}

load_nwk_hub_ring_data <- function(mydb_abstract_db)
{
  # HUB Ring
  # sending query to mysql db
  
  TopologyTerminationReport_hub = dbSendQuery(mydb_abstract_db, "select seq_no,topologyname,nodename from topology_termination_hub_ring_report")
  
  # fetching data from mysql server
  TopologyTerminationReport_hub = fetch(TopologyTerminationReport_hub, n=-1)
  top_term_hub_cols <- c('seq_no','hub_ring','hub_node')
  
  colnames(TopologyTerminationReport_hub) <- top_term_hub_cols
  
  return (TopologyTerminationReport_hub)
}


load_nwk_ring_Util_data <- function(mydb_abstract_db)
{
  #Ring_Utilisation_Report <- read.csv(Ring_Utilisation_Report_name,na.strings = c("NA", "", "<NA>"))
  # sending query to mysql db
  Ring_Utilisation_Report = dbSendQuery(mydb_abstract_db, "select seq_no,ring_name,topology_type,total_capacity,free_vc4_ts,freevc3,free_vc12_ts,utlpercentage,ring_type, util_available from ring_utilization_report")
  
  # fetching data from mysql server
  Ring_Utilisation_Report = fetch(Ring_Utilisation_Report, n=-1)
  ring_util_cols <- c('seq_no','RING.NAME','Topology.Type','TOTAL.CAPACITY','Free.VC4.TS','FREEVC3','Free.VC12.TS','UTLPERCENTAGE','RING.TYPE', 'available_BW')
  
  colnames(Ring_Utilisation_Report) <- ring_util_cols
  
  return(Ring_Utilisation_Report)
}


load_nwk_corering_pop_mapping <- function(mydb_abstract_db)
{
    # sending query to mysql db
    nodemaster = dbSendQuery(mydb_abstract_db, "select NODENAME, BUILDING_CODE from node_master")
    
    # fetching data from mysql server
    nodemaster = fetch(nodemaster, n=-1)
    
    return (nodemaster)
}


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Function to find out nearest HH name from Chamber Ring file for Network check
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# This function find the nearest hand hold (if available in 0.5Km radius)
fn_HH_distance_calc <- function(P_lat, P_long, hh_data_network_n){
  
  P_long <- as.numeric(P_long)
  P_lat  <- as.numeric(P_lat)
  # reducing search space
  hh_data_network_n <- hh_data_network_n[which(between(hh_data_network_n$longitude, P_long - 0.1, P_long + 0.1) &
                                                 between(hh_data_network_n$latitude, P_lat - 0.1, P_lat + 0.1)
  ),] 
  if (nrow(hh_data_network_n) == 0) {
    #print("99999 error")
    return (list(
      "selected_HH" = NA
    ))
  }
  else {
    tryCatch( {
      hh_data_network_n$prospect_distance_km <- distHaversine(
        c(P_long, P_lat),
        hh_data_network_n[, c("longitude","latitude")])
      hh_data_network_n$prospect_distance_km <- hh_data_network_n$prospect_distance_km/ 1000
      
      hh_data_network_n <- hh_data_network_n[which(hh_data_network_n$prospect_distance_km <= 0.5),]
      if (nrow(hh_data_network_n) > 0) {
        selected_HH <- hh_data_network_n$chamber_name[which.min(hh_data_network_n$prospect_distance_km)]
      } else {
        selected_HH <- NA
      }
      return (list(
        "selected_HH" = selected_HH
      ))
    }, 
    error = function(error_message) {
      #print("Error Encountered")
      return(list(
        "selected_HH" = NA
      ))
    })
  }
}

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Function to check Access Ring Capacity for Network check
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
fn_access_cap_util <-function(access_ring, req_bw, Ring_Utilisation_Report_n){
  Ring_Utilisation_Report_n <- Ring_Utilisation_Report_n[which(Ring_Utilisation_Report_n$RING.NAME == access_ring),]
  if(nrow(Ring_Utilisation_Report_n) > 0) {
    # Ring_Utilisation_Report_n$req_bw <- req_bw
    Ring_Utilisation_Report_n$f_nf <- ifelse(as.numeric(Ring_Utilisation_Report_n$available_BW) > as.numeric(req_bw), 1, 0)
    access_f_nf <- sum(Ring_Utilisation_Report_n$f_nf, na.rm = T)
  }else{
    access_f_nf <- 0
  }
  return(list("access_f_nf" = access_f_nf))
}

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Function to check Network Feasibility through MUX in Connected Customer
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
fn_Network_Feasibility_CC_Check <- function(df){
  
  if (! "connected_cust_tag" %in% names(df)) {stop("Missing Columns")}

  if(nrow(df[df$connected_cust_tag>0, ]) > 0)
    {
    # Step 1 : Finding mux of the connected customer (ServiceID --> MUX)
    # Find MUX associated with Service ID of connected customer
    connected_custs_mux <- merge(x = connected_cc,
                                 y = dropporttoservice,
                                 by.x = "SERVICE_ID",
                                 by.y = "SERVICEORIORID",
                                 all.x = T)
    #rm(dropporttoservice)
    
    # Find all unique MUXs of all connected customers
    df_unique_mux <- connected_custs_mux[, c("Prospect_ID","BW_mbps","mux","pop_network_loc_id", "mux_ip", "mux_port")]
    df_unique_mux <- df_unique_mux[df_unique_mux$mux %in% unique(na.omit(connected_custs_mux$mux)),]
    
    #df_unique_mux <- data.frame(mux = unique(na.omit(connected_custs_mux$mux)))
    
    # Check if any MUX are found or not
    if(nrow(df_unique_mux)>0){
      
      # Step 2 : Finding Access ring based on MUX (MUX --> Access ring)
      df_unique_mux <- merge(x = df_unique_mux,
                             y = TopologyTerminationReport_access,
                             by.x = "mux",
                             by.y = "NODENAME",
                             all.x = T)
      #rm(TopologyTerminationReport_access)
      
      # Step 3 : Finding Access ring capacity and utilization
      df_unique_mux$access_f_nf <- apply(df_unique_mux,1,
                                         function(x) fn_access_cap_util(x["selected_access_ring"],
                                                                        x["BW_mbps"],
                                                                        Ring_Utilisation_Report))
      
      df_unique_mux$access_f_nf <- unlist(lapply(df_unique_mux$access_f_nf, "[[",1))
      
      # Step 4 : Finding hub node for each Access ring (Access Ring --> Hub Node)
      df_unique_mux <- merge(x = df_unique_mux,
                             y = TopologyTerminationReport_hub,
                             by.x = "selected_access_ring",
                             by.y = "hub_ring",
                             all.x = T)
      
      
      # Step 5 : Finding core ring for each hub node (Hub Node --> Core Ring)
      df_unique_mux <- merge(x = df_unique_mux,
                             y = TopologyTerminationReport_core,
                             by.x = "hub_node",
                             by.y = "NODENAME",
                             all.x = T)
      
      # Step 6 : Checking core ring capacity
      df_unique_mux$core_f_nf <- apply(df_unique_mux,1,
                                       function(x) fn_access_cap_util(x["core_ring"],
                                                                      x["BW_mbps"],
                                                                      Ring_Utilisation_Report))
      
      df_unique_mux$core_f_nf <- unlist(lapply(df_unique_mux$core_f_nf, "[[",1))
      #rm(Ring_Utilisation_Report)
      
      # Remove rows with any NA
      df_unique_mux <- na.omit(df_unique_mux)
      
      # Identify the core ring which is ending at the required POP
      df_unique_mux <- merge(x = df_unique_mux,
                             y = na.omit(nodemaster),
                             by.x = "hub_node",
                             by.y = "NODENAME")
      
      #Check whether the selected pop and the pop where core ring is ending at
      df_unique_mux$core_to_pop <- ifelse(df_unique_mux$pop_network_loc_id==df_unique_mux$BUILDING_CODE,
                                          1,0)
      
      #df_unique_mux <- df_unique_mux[df_unique_mux$core_to_pop==1,]
      
      if(nrow(df_unique_mux[df_unique_mux$core_to_pop==1,])>0){
        df_unique_mux_F <- df_unique_mux[df_unique_mux$core_to_pop==1,]
        #all name attributes stored separately
        df_names <- df_unique_mux_F
        df_names <- df_names[,c("Prospect_ID","mux","selected_access_ring", "mux_ip", "mux_port")]
        # df_names <- df_names %>%
        #   group_by(Prospect_ID) %>%
        #   mutate(hub_node = paste0(unique(hub_node), collapse = ","))
        #
        # df_names <- df_names %>%
        #   group_by(Prospect_ID) %>%
        #   mutate(core_ring = paste0(unique(core_ring), collapse = ","))

        df_names <- df_names %>% 
          group_by(Prospect_ID) %>% 
          mutate(selected_access_ring = paste0(unique(selected_access_ring), collapse = ","))
        
        df_names <- df_names %>% 
          group_by(Prospect_ID) %>% 
          mutate(mux = paste0(unique(mux), collapse = ","))

        ##O2C
        # df_names <- df_names %>%
        #   group_by(Prospect_ID) %>%
        #   mutate(mux_name = paste0(unique(mux_name), collapse = ","))
        
        df_names <- df_names %>% 
          group_by(Prospect_ID) %>% 
          mutate(mux_port = paste0(unique(mux_port), collapse = ","))
        
        df_names <- df_names %>% 
          group_by(Prospect_ID) %>% 
          mutate(mux_ip = paste0(unique(mux_ip), collapse = ","))

        df_names = dplyr::rename(df_names, mux_access_ring = selected_access_ring)
        
        df_names <- df_names[!duplicated(df_names),]
        
        # N/W F_NF Reason - Show ring names
        # CC_0_5_access_rings_NF <- toString(unique(df_unique_mux_F[df_unique_mux_F$access_capacity_flag_hh==0,]$selected_access_ring))
        # CC_0_5_access_rings_F <- toString(unique(df_hh[df_hh$access_capacity_flag_hh==1,]$access_rings_hh))
        
        # F/ NF flag for each prospect ID
        df_unique_mux_F <- df_unique_mux_F %>% group_by(Prospect_ID) %>%
          dplyr::summarise(tot_access_f_nf = sum(access_f_nf, na.rm = T),
                           tot_core_f_nf = sum(core_f_nf, na.rm = T))
        
        df_unique_mux_F$Network_F_NF_CC_Flag <- ifelse((df_unique_mux_F$tot_access_f_nf > 0 &
                                                          df_unique_mux_F$tot_core_f_nf > 0), 
                                                       1, 0)
        
        df_unique_mux_F$Network_F_NF_CC <- ifelse((df_unique_mux_F$tot_access_f_nf > 0 &
                                                     df_unique_mux_F$tot_core_f_nf > 0), 
                                                  "Network Feasible on CC", "Network Not Feasible on CC")
        
        df_unique_mux_F$access_check_CC <- ifelse(df_unique_mux_F$tot_access_f_nf > 0, 
                                                  "Network Feasible on Access Ring of CC",
                                                  "Network Not Feasible on Access Ring of CC")
        
        df_unique_mux_F$core_check_CC <- ifelse(df_unique_mux_F$tot_core_f_nf > 0,
                                                "Network Feasible on Core Ring of CC", 
                                                "Network Not Feasible on Core Ring of CC")
        # Merge with main input file
        df <- merge(x = df,
                    y = df_unique_mux_F[,c("Prospect_ID",
                                           "Network_F_NF_CC_Flag","Network_F_NF_CC",
                                           "access_check_CC","core_check_CC")],
                    by = "Prospect_ID",
                    all.x = T)
        
        # merge to get mux name info
        df <- merge(x = df,
                    y = df_names,
                    by = "Prospect_ID",
                    all.x = T)
        #O2C
        df$Network_F_NF_CC[is.na(df$Network_F_NF_CC_Flag)] <- "No CC/ mux/ core"
        df$access_check_CC[is.na(df$Network_F_NF_CC_Flag)] <- "NA"
        df$core_check_CC[is.na(df$Network_F_NF_CC_Flag)] <- "NA"
        df$mux[is.na(df$Network_F_NF_CC_Flag)] <- "NA"
        df$mux_ip[is.na(df$Network_F_NF_CC_Flag)] <- "NA"
        df$mux_port[is.na(df$Network_F_NF_CC_Flag)] <- "NA"
        df$mux_access_ring[is.na(df$Network_F_NF_CC_Flag)] <- "NA"
        df$Network_F_NF_CC_Flag[is.na(df$Network_F_NF_CC_Flag)] <- 0
      }
      else{
        df$access_check_CC <- "NA"
        df$core_check_CC <- "NA"
        df$mux <- "NA"
        df$mux_ip <- "NA"
        df$mux_port <- "NA"
        df$mux_access_ring <- "NA"
        
        df$Network_F_NF_CC_Flag <- 0
        df$Network_F_NF_CC <- "No Core ends on POP"
      }
    }
    else{
      df$access_check_CC <- "NA"
      df$core_check_CC <- "NA"
      df$mux <- "NA"
      df$mux_ip <- "NA"
      df$mux_port <- "NA"
      df$mux_access_ring <- "NA"
      
      df$Network_F_NF_CC_Flag <- 0
      df$Network_F_NF_CC <- "No Mux found"
    }
  }
  else{
    # If no CC found then Network Not Feasible on CC, move to next step to check HH in 0.5km
    df$access_check_CC <- "NA"
    df$core_check_CC <- "NA"
    df$mux <- "NA"
    df$mux_ip <- "NA"
    df$mux_port <- "NA"
    df$mux_access_ring <- "NA"

    df$Network_F_NF_CC_Flag <- 0
    df$Network_F_NF_CC <- "No CC Found"
    # df$Network_F_NF_CC[is.na(df$Network_F_NF_CC_Flag)] <- "No mux or no core ends on pop"
    # df$Network_F_NF_CC_Flag[is.na(df$Network_F_NF_CC_Flag)] <- 0
  }

    # # If no CC found then Network Not Feasible on CC, move to next step to check HH in 0.5km
    # df$access_check_CC[(df$connected_cust_tag < 1) | is.na(df$Network_F_NF_CC_Flag)] <- "NA"
    # df$core_check_CC[(df$connected_cust_tag < 1) | is.na(df$Network_F_NF_CC_Flag)] <- "NA"
    # df$mux[(df$connected_cust_tag < 1) | is.na(df$Network_F_NF_CC_Flag)] <- "NA"
    # df$mux_ip[(df$connected_cust_tag < 1) | is.na(df$Network_F_NF_CC_Flag)] <- "NA"
    # df$mux_port[(df$connected_cust_tag < 1) | is.na(df$Network_F_NF_CC_Flag)] <- "NA"
    # df$mux_access_ring[(df$connected_cust_tag < 1) | is.na(df$Network_F_NF_CC_Flag)] <- "NA"
    # 
    # df$Network_F_NF_CC_Flag[df$connected_cust_tag < 1] <- 0
    # df$Network_F_NF_CC[df$connected_cust_tag < 1] <- "No CC Found"
    # df$Network_F_NF_CC[is.na(df$Network_F_NF_CC_Flag)] <- "No mux or no core ends on pop"
    # df$Network_F_NF_CC_Flag[is.na(df$Network_F_NF_CC_Flag)] <- 0

  return(df)
}

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Function to check HH Access Ring and Core Ring capacity for Network Check
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
fn_Network_Feasibility_HH_Check <- function(df){
  # Check Handhole within 0.5kms for Not Feasible cases
  # Identify the nearest HH name in 0.5km from Chamber Ring file
  HH_0_5km_list <- apply(df, 1, function(x) fn_HH_distance_calc(x["Latitude_final"],
                                                                x["Longitude_final"],
                                                                hh_data_network))
  
  df$HH_0_5km <- unlist(lapply(HH_0_5km_list, "[[",1))
  df$hh_flag <- ifelse(!is.na(df$HH_0_5km), 1, 0)
  if(nrow(df[df$hh_flag>0, ]) > 0)
  {
    # Create small DF with Prospect ID and HH
    df_hh <- data.frame(Prospect_ID = df$Prospect_ID, hh = df$HH_0_5km, BW_mbps = df$BW_mbps_2,pop_network_loc_id = df$pop_network_loc_id)
    # Step 1: Obtain access ring associated with hand hold ( HH --> Access Ring)
    df_hh <- merge(x = df_hh,
                   y = chamber_ring,
                   by.x = "hh",
                   by.y = "chamber_name",
                   all.x = T)
    #rm(chamber_ring)
    
    # Step 2 : Access ring ----> Hub node
    df_hh <- merge(x = df_hh,
                   y = TopologyTerminationReport_hub,
                   by.x = "access_rings_hh",
                   by.y = "hub_ring",
                   all.x = T)
    #rm(TopologyTerminationReport_hub)
    
    # Step 3 : Hub node ---> Core ring
    df_hh <- merge(x = df_hh,
                   y = TopologyTerminationReport_core,
                   by.x = "hub_node",
                   by.y = "NODENAME",
                   all.x = T)
    #rm(TopologyTerminationReport_core)
    
    # Step 4 : Checking access and core ring capacity
    # Obtaining utilizations results for access ring 
    df_hh$result <- apply(df_hh, 1, function(x) fn_access_cap_util(
      x["access_rings_hh"],
      x["BW_mbps"],
      Ring_Utilisation_Report))
    
    df_hh$access_capacity_flag_hh <- unlist(lapply(df_hh$result, "[[", 1))
    df_hh$result <- NULL
    
    # Obtaining utilizations results for Core ring 
    df_hh$result_c <- apply(df_hh, 1, function(x) fn_access_cap_util(
      x["core_ring"],
      x["BW_mbps"],
      Ring_Utilisation_Report))
    #rm(Ring_Utilisation_Report)
    
    df_hh$core_capacity_flag_hh <- unlist(lapply(df_hh$result_c, "[[", 1))
    df_hh$result_c <- NULL
    
    # Filter for Core rings which are ending at selected pop
    df_hh <- merge(x = df_hh,
                   y = na.omit(nodemaster),
                   by.x = "hub_node",
                   by.y = "NODENAME",
                   all.x = T)
    
    # df_hh <- df_hh[(df_hh$access_capacity_flag_hh==1 & df_hh$core_capacity_flag_hh==1),]
    
    #Check whether the selected pop and the pop where core ring is ending at
    df_hh$core_to_pop <- ifelse(df_hh$pop_network_loc_id==df_hh$BUILDING_CODE,
                                1,0)
    
    if(nrow(df_hh[df_hh$core_to_pop==1,])>0){
      #all name attributes stored separately
      df_hh <- df_hh[df_hh$core_to_pop==1,]
      df_names <- df_hh[,c("Prospect_ID","access_rings_hh")]

      # df_names <- df_names %>%
      #   group_by(Prospect_ID) %>%
      #   mutate(hub_node_hh = paste0(unique(hub_node), collapse = ","))
      #
      # df_names <- df_names %>%
      #   group_by(Prospect_ID) %>%
      #   mutate(core_ring_hh = paste0(unique(core_ring), collapse = ","))

      df_names <- df_names %>%
        group_by(Prospect_ID) %>%
        mutate(access_rings_hh = paste0(unique(access_rings_hh), collapse = ","))


      df_names <- df_names[!duplicated(df_names[,c("Prospect_ID","access_rings_hh")]),]
      df_names <- df_names[,c("Prospect_ID","access_rings_hh")]

      # F/ NF flag for each prospect ID
      #all_core_rings_HH_0_5 = toString(unique(access_rings_hh))

      df_hh <- df_hh %>% group_by(Prospect_ID) %>%
        dplyr::summarise(tot_access_f_nf = sum(access_capacity_flag_hh, na.rm = T),
                         tot_core_f_nf = sum(core_capacity_flag_hh, na.rm = T))

      df_hh$Network_F_NF_HH_Flag <- ifelse((df_hh$tot_access_f_nf > 0 &
                                              df_hh$tot_core_f_nf > 0),1,0)

      df_hh$Network_F_NF_HH <- ifelse((df_hh$tot_access_f_nf > 0 &
                                         df_hh$tot_core_f_nf > 0),
                                      "Network Feasible on HH",
                                      "Network Not Feasible on HH")

      df_hh$access_check_hh <- ifelse(df_hh$tot_access_f_nf > 0,
                                      "Network Feasible on Access Ring of HH",
                                      "Network Not Feasible on Access Ring of HH")

      df_hh$core_check_hh <- ifelse(df_hh$tot_core_f_nf > 0,
                                    "Network Feasible on Core Ring of HH",
                                    "Network Not Feasible on Core Ring of HH")

      # Merge with main input file
      df <- merge(x = df,
                  y = df_hh[,c("Prospect_ID","Network_F_NF_HH_Flag","Network_F_NF_HH",
                               "access_check_hh","core_check_hh")],
                  by = "Prospect_ID",
                  all.x = T)
      df <- merge(x = df,
                  y = df_names,
                  by = "Prospect_ID",
                  all.x = T)

      #O2C
      df$Network_F_NF_HH[is.na(df$Network_F_NF_HH_Flag)] <- "No HH/core ring found"
      df$access_check_hh[is.na(df$Network_F_NF_HH_Flag)] <- "No HH/core ring found"
      df$core_check_hh[is.na(df$Network_F_NF_HH_Flag)] <- "No HH/core ring found"
      df$access_rings_hh[is.na(df$Network_F_NF_HH_Flag)] <- "No HH/core ring found"
      df$Network_F_NF_HH_Flag[is.na(df$Network_F_NF_HH_Flag)] <- 0

    }else{
      df$Network_F_NF_HH <- "No HH/core ring found"
      df$access_check_hh <- "No HH/core ring found"      #O2C
      df$core_check_hh <- "No HH/core ring found"
      df$access_rings_hh <- "No HH/core ring found"
      df$Network_F_NF_HH_Flag <- 0
    }

  }else{
   df$Network_F_NF_HH <- "No HH/core ring found"
   df$access_check_hh <- "No HH/core ring found"      #O2C
   df$core_check_hh <- "No HH/core ring found"
   df$access_rings_hh <- "No HH/core ring found"
   df$Network_F_NF_HH_Flag <- 0
 }



    ##Commceted for o2C - dont show these sttributes if there is no connectivity with selected POP
    # df_names <- df_hh[,c("Prospect_ID","access_rings_hh","hub_node","core_ring")]

    # if(nrow(df_names)>0){
    #
    #   df_names <- df_names %>%
    #     group_by(Prospect_ID) %>%
    #     mutate(hub_node_hh = paste0(unique(hub_node), collapse = ","))
    #
    #   df_names <- df_names %>%
    #     group_by(Prospect_ID) %>%
    #     mutate(core_ring_hh = paste0(unique(core_ring), collapse = ","))
    #
    #   df_names <- df_names %>%
    #     group_by(Prospect_ID) %>%
    #     mutate(access_rings_hh = paste0(unique(access_rings_hh), collapse = ","))
    #
    #   df_names <- df_names[!duplicated(df_names[,c("Prospect_ID","access_rings_hh","hub_node_hh","core_ring_hh")]),]
    #   df_names <- df_names[,c("Prospect_ID","access_rings_hh","hub_node_hh","core_ring_hh")]
    #
    # }
    # # Merge with main file
    # df <- merge(x = df,
    #             y = df_names,
    #             by = "Prospect_ID",
    #             all.x = T)

  # }
  return(df)
}


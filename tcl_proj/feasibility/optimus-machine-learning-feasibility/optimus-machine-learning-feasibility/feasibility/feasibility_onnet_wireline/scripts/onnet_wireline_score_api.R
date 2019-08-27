score <-    function(input_data, path_py){
  setwd(path_py)
  input_json_data <- input_data


  # set error parameter
  err <- FALSE


  source("scripts/config.R")
  source("scripts/feature_generation_func.R")
  source("scripts/data_prep_func.R")
  source("scripts/lm_cost_func.R")
  source("scripts/network_func.R")

  ##########################################################################################
  # Define Error Output JSON to be thrown in case of any error encountered
  ##########################################################################################
  # Define Error response dataframe
  df_error <- data.frame('site_id' = 'NA','POP_DIST_KM_SERVICE_MOD' = 'NA','Product.Name' = 'NA','POP_DIST_KM' = 'NA','POP_DIST_KM_SERVICE' = 'NA','pop_name' = 'NA','POP_Network_Location_Type' = 'NA','POP_Construction_Status' = 'NA','POP_Building_Type' = 'NA','pop_network_loc_id' = 'NA','pop_long' = 'NA','pop_lat' = 'NA','pop_address' = 'NA','POP_Category' = 'NA','POP_TCL_Access' = 'NA','FATG_DIST_KM' = 'NA','FATG_Network_Location_Type' = 'NA','FATG_Building_Type' = 'NA','FATG_Category' = 'NA','FATG_TCL_Access' = 'NA','FATG_PROW' = 'NA','FATG_Ring_type' = 'NA','HH_DIST_KM' = 'NA','hh_name' = 'NA','X0.5km_cust_count' = 'NA','X0.5km_min_dist' = 'NA','X0.5km_avg_dist' = 'NA','X0.5km_min_bw' = 'NA','X0.5km_avg_bw' = 'NA','X0.5km_max_bw' = 'NA','X2km_cust_count' = 'NA','X2km_min_dist' = 'NA','X2km_avg_dist' = 'NA','X2km_min_bw' = 'NA','X2km_avg_bw' = 'NA','X2km_max_bw' = 'NA','X5km_cust_count' = 'NA','X5km_min_dist' = 'NA','X5km_avg_dist' = 'NA','X5km_min_bw' = 'NA','X5km_avg_bw' = 'NA','X5km_max_bw' = 'NA','X0.5km_prospect_count' = 'NA','X0.5km_prospect_min_dist' = 'NA','X0.5km_prospect_avg_dist' = 'NA','X0.5km_prospect_min_bw' = 'NA','X0.5km_prospect_avg_bw' = 'NA','X0.5km_prospect_max_bw' = 'NA','X0.5km_prospect_num_feasible' = 'NA','X0.5km_prospect_perc_feasible' = 'NA','X2km_prospect_count' = 'NA','X2km_prospect_min_dist' = 'NA','X2km_prospect_avg_dist' = 'NA','X2km_prospect_min_bw' = 'NA','X2km_prospect_avg_bw' = 'NA','X2km_prospect_max_bw' = 'NA','X2km_prospect_num_feasible' = 'NA','X2km_prospect_perc_feasible' = 'NA','X5km_prospect_count' = 'NA','X5km_prospect_min_dist' = 'NA','X5km_prospect_avg_dist' = 'NA','X5km_prospect_min_bw' = 'NA','X5km_prospect_avg_bw' = 'NA','X5km_prospect_max_bw' = 'NA','X5km_prospect_num_feasible' = 'NA','X5km_prospect_perc_feasible' = 'NA','OnnetCity_tag' = 'NA','Probabililty_Access_Feasibility' = 'NA','Predicted_Access_Feasibility' = 'NA','lm_arc_bw_onwl' = 'NA','connected_cust_tag' = 'NA','connected_building_tag' = 'NA','Service_ID' = 'NA','num_connected_cust' = 'NA','num_connected_building' = 'NA','lm_nrc_mux_onwl' = 'NA','lm_nrc_inbldg_onwl' = 'NA','lm_nrc_nerental_onwl' = 'NA','lm_nrc_bw_onwl' = 'NA','cost_permeter' = 'NA','min_hh_fatg' = 'NA','lm_nrc_ospcapex_onwl' = 'NA','total_cost' = 'NA','city_tier' = 'NA','scenario_1' = 'NA','scenario_2' = 'NA','net_pre_feasible_flag' = 'NA','Network_F_NF_CC_Flag' = 'NA','Network_F_NF_CC' = 'NA','access_check_CC' = 'NA','core_check_CC' = 'NA','mux' = 'NA','HH_0_5km' = 'NA','hh_flag' = 'NA','Network_F_NF_HH_Flag' = 'NA','Network_F_NF_HH' = 'NA','access_check_hh' = 'NA','core_check_hh' = 'NA','HH_0_5_access_rings_F' = 'NA','HH_0_5_access_rings_NF' = 'NA','access_rings_hh' = 'NA','hub_node' = 'NA','core_ring' = 'NA','Network_Feasibility_Check' = 'NA','Orch_LM_Type' = 'NA','Orch_Connection' = 'NA','Orch_Category' = 'NA','Orch_BW' = 'NA','latitude_final' = 'NA','longitude_final' = 'NA','prospect_name' = 'NA','bw_mbps' = 'NA','burstable_bw' = 'NA','resp_city' = 'NA','customer_segment' = 'NA','sales_org' = 'NA','product_name' = 'NA','feasibility_response_created_date' = 'NA','local_loop_interface' = 'NA','last_mile_contract_term' = 'NA','account_id_with_18_digit' = 'NA','opportunity_term' = 'NA','quotetype_quote' = 'NA','connection_type' = 'NA','sum_no_of_sites_uni_len' = 'NA','cpe_variant' = 'NA','cpe_management_type' = 'NA','cpe_supply_type' = 'NA','topology' = 'NA','additional_ip_flag' = 'NA','ip_address_arrangement' = 'NA','ipv4_address_pool_size' = 'NA','ipv6_address_pool_size' = 'NA','lm_arc_bw_prov_ofrf' = 'NA','lm_nrc_bw_prov_ofrf' = 'NA','lm_nrc_mast_ofrf' = 'NA','lm_arc_bw_onrf' = 'NA','lm_nrc_bw_onrf' = 'NA','lm_nrc_mast_onrf' = 'NA','error_code' = 'NA','error_flag' = 'NA','error_msg' = 'NA','time_taken' = 'NA', 'Predicted_Feasibility_Comment' = 'NA')


  tryCatch(
  {
    init_envt()
    library(jsonlite)
    create_log(logfile, "Load package completed", log_flag)
  },
  error=function(e){
    create_log(logfile, e, log_flag)
    err <<- TRUE
    df_error$error_flag <- 1
    df_error$error_code <- "E11"
    df_error$error_msg <- "R Package Error: R Package not found"
    df_error <<- cbind(input_json_data,df_error[,!(colnames(df_error) %in% colnames(input_json_data))])
    })
  if(err==TRUE){
    return(df_error)
  }
  

  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  # Database Connection
  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  #establishing connection
  tryCatch(
  {
    mydb_abstract_db = dbConnect(MySQL(),
    user = username,
    password=pwd,
    dbname=database,
    host=hostname)

    create_log(logfile, "DB Connection completed", log_flag)
  }, 
  error=function(e){
      create_log(logfile, e, log_flag)
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
  # POP Data - Import
  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  
  tryCatch(
  {
    pop_data_file <<- load_pop_data(mydb_abstract_db)
    create_log(logfile, "Pop Data Loaded", log_flag)

    fatg_data_file <<- load_fatg_data(mydb_abstract_db)
    create_log(logfile, "Fatg Data Loaded", log_flag)

    hh_data_file <<- load_hh_data(mydb_abstract_db)
    create_log(logfile, "HH Data Loaded", log_flag)

    cust_data_file <<- load_cust_data(mydb_abstract_db, CUST_TBL)
    create_log(logfile, "Customer Data Loaded", log_flag)

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Customer data - Roll up for Model scoring
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    cust_coords <<- data.table(CUST_ID = 1:nrow(cust_data_file),
                               cust_date = as.Date(cust_data_file$PROVISIONING_START_DATE),
                               cust_lat=as.vector(as.numeric(cust_data_file$Latitude)),
                               cust_long=as.vector(as.numeric(cust_data_file$Longitude)),
                               cust_bw = as.vector(as.numeric(cust_data_file$F12)))
    create_log(logfile, "Customer Data Rolled Up", log_flag)
    rm(cust_data_file)

    ##Connected Building: Load real time customer data for Business rules
    cust_data_file_br <<- load_cust_data(mydb_abstract_db, CUST_TBL_LIVE)
    create_log(logfile, "Real Time Customer Data for business rules Loaded", log_flag)

  
    prospect_coords <<- load_prospect_data(mydb_abstract_db, PROSPECT_TBL)
    create_log(logfile, "Prospect Data Loaded", log_flag)

    man_city <<- load_man_city_data(mydb_abstract_db)
    create_log(logfile, "Mancity Data Loaded", log_flag)
    
    row_city <<- load_row_city_data(mydb_abstract_db)
    create_log(logfile, "Row city Data Loaded", log_flag)
    
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # ARC BW Rate Cards for LM Costs
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    bw_all_stack <- load_arc_rate_card(mydb_abstract_db)

    ## Get Network Data
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # HH Chamber Ring - Network Check
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    hh_data_network <<- load_nwk_hh_data(mydb_abstract_db)

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Chamber Ring data - HandHole Access Rings - Network Check
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    chamber_ring <<- hh_data_network

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # MUX Info - Service IDs - Network Check
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    dropporttoservice <<- load_nwk_mux_serviceid_mapping(mydb_abstract_db)

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Access Ring - Network Check
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    TopologyTerminationReport_access <<- load_nwk_access_ring_data(mydb_abstract_db)

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Core Ring - Network Check
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    TopologyTerminationReport_core <<- load_nwk_core_ring_data(mydb_abstract_db)


    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Hub Ring - Network Check
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    TopologyTerminationReport_hub <<- load_nwk_hub_ring_data(mydb_abstract_db)

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Access Ring Utilization for capacity check- Network Check
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    Ring_Utilisation_Report <<- load_nwk_ring_Util_data(mydb_abstract_db)

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Core Ring to POP - Network Check
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    nodemaster <<- load_nwk_corering_pop_mapping(mydb_abstract_db)

    create_log(logfile, "Data for Network Loaded", log_flag)


  },
  error=function(e){
    create_log(logfile, e, log_flag)
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

  # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  # # Read Model Object
  # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  # Read Original Training data for setting same factor level
  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  tryCatch(
  {

    modelobj = readRDS(MODEL_OBJ)
    rf_model_val = modelobj$model
    cut_off = modelobj$cutoff
    xtrain = modelobj$train_row
    
    create_log(logfile, "Model Object Loaded", log_flag)
  },
  error=function(e){
    create_log(logfile, e, log_flag)
    err <<- TRUE
    df_error$error_flag <- 1
    df_error$error_code <- "E4"
    df_error$error_msg <- "Load Error: Error in loading the Model Object or training object"
    df_error <<- cbind(input_json_data,df_error[,!(colnames(df_error) %in% colnames(input_json_data))])
  }
  )
  if(err==TRUE){
    return(df_error)
  }

  tryCatch(
  {

    # align column names according to the old training format
    oldnames = c("site_id","latitude_final", "longitude_final", "bw_mbps", "burstable_bw",
                  "customer_segment", "sales_org", "product_name", "feasibility_response_created_date")
    newnames = c("site_id","Latitude_final", "Longitude_final", "BW_mbps", "Burstable_BW", "Customer_Segment",
                 "Sales.Org", "Product.Name", "Feasibility_Response_Created_Date")
    input_data = input_data %>% rename_at(vars(oldnames), ~ newnames)

    #Data type formatting for input data
    input_data$Prospect_ID <- input_data$site_id
    input_data$site_id <- NULL
    input_data = clean_input(input_data)

    input_data$Burstable_BW  <- as.numeric(input_data$Burstable_BW)
    input_data$BW_mbps_act <- as.numeric(input_data$BW_mbps)

    #Selecting BW - if Burstable is higher then select Burstable BW for Access, LM and Network Feasibility
    input_data$Burstable_BW <- ifelse((is.na(input_data$Burstable_BW)|(input_data$Burstable_BW==0)),0,input_data$Burstable_BW)

    input_data$BW_mbps <- ifelse(input_data$Burstable_BW>input_data$BW_mbps, input_data$Burstable_BW, input_data$BW_mbps)


    input_data <<- input_data
    create_log(logfile, "Input Data Cleanup completed", log_flag)

    if(any(is.na(input_data))){
      throw("Input Error")
  }
  },
  error=function(e){
      create_log(logfile, e, log_flag)
      err <<- TRUE
      df_error$error_flag <- 1
      df_error$error_code <- "E1"
      df_error$error_msg <- "Input Error: Unexpected input received"
      df_error <<- cbind(input_json_data,df_error[,!(colnames(df_error) %in% colnames(input_json_data))])
    }
  )
  if(err==TRUE){
    return(df_error)
  }
  

  ##########################################################################################
  ##########################################################################################
  # Feature Building
  ##########################################################################################
  
  ##########################################################################################
  
  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  # POP related Features
  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  
  tryCatch({
    input_data = add_pop_features(pop_data_file, input_data, save_matrix = "")
    create_log(logfile, "Pop features generated", log_flag)
    rm(pop_data_file)
    gc()
  },
  error=function(e){
    create_log(logfile, e, log_flag)
    err <<- TRUE
    df_error$error_flag <- 1
    df_error$error_code <- "E7"
    df_error$error_msg <- "Model Error: Error in Feature Creation"
    df_error <<- cbind(input_json_data,df_error[,!(colnames(df_error) %in% colnames(input_json_data))])
  }
  )
  if(err==TRUE){
    return(df_error)
  }

  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  # FATG related Features
  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

  tryCatch({
    input_data = add_fatg_features(fatg_data_file, input_data, save_matrix = "")
    create_log(logfile, "FATG features generated", log_flag)
    rm(fatg_data_file)
    gc()
  },
  error=function(e){
    create_log(logfile, e, log_flag)
    err <<- TRUE
    df_error$error_flag <- 1
    df_error$error_code <- "E7"
    df_error$error_msg <- "Model Error: Error in Feature Creation"
    df_error <<- cbind(input_json_data,df_error[,!(colnames(df_error) %in% colnames(input_json_data))])
  }
  )
  if(err==TRUE){
    return(df_error)
  }

  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  # HH related Features
  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  
  tryCatch(
  {
    input_data = add_hh_features(hh_data_file, input_data, save_matrix = "")
    create_log(logfile, "HH features generated", log_flag)
    rm(hh_data_file)
    gc()
  },
  error=function(e){
    create_log(logfile, e, log_flag)
    err <<- TRUE
    df_error$error_flag <- 1
    df_error$error_code <- "E7"
    df_error$error_msg <- "Model Error: Error in Feature Creation"
    df_error <<- cbind(input_json_data,df_error[,!(colnames(df_error) %in% colnames(input_json_data))])
  }
  )
  if(err==TRUE){
    return(df_error)
  }

  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  # Customer related Features
  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  tryCatch(
  {
    input_data = add_cust_features(cust_coords, input_data, save_matrix = "")
    create_log(logfile, "Cust features generated", log_flag)
    rm(cust_coords)
  },
  error=function(e){
    create_log(logfile, e, log_flag)
    err <<- TRUE
    df_error$error_flag <- 1
    df_error$error_code <- "E7"
    df_error$error_msg <- "Model Error: Error in Feature Creation"
    df_error <<- cbind(input_json_data,df_error[,!(colnames(df_error) %in% colnames(input_json_data))])
  }
  )
  if(err==TRUE){
    return(df_error)
  }

  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  # Prospect related Features
  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  tryCatch({
    input_data = add_prospect_features(prospect_coords, input_data, save_matrix = "", 1)
    create_log(logfile, "Prospect features generated", log_flag)
    rm(prospect_coords)
    gc()
  },
  error=function(e){
    create_log(logfile, e, log_flag)
    err <<- TRUE
    df_error$error_flag <- 1
    df_error$error_code <- "E7"
    df_error$error_msg <- "Model Error: Error in Feature Creation"
    df_error <<- cbind(input_json_data,df_error[,!(colnames(df_error) %in% colnames(input_json_data))])
  }
  )
  if(err==TRUE){
    return(df_error)
  }

  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  # MAN CITY related Features
  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  
  tryCatch({
    input_data <- add_man_city_features(man_city, input_data)
    create_log(logfile, "Man City features generated", log_flag)
  },
  error=function(e){
    create_log(logfile, e, log_flag)
    err <<- TRUE
    df_error$error_flag <- 1
    df_error$error_code <- "E7"
    df_error$error_msg <- "Model Error: Error in Feature Creation"
    df_error <<- cbind(input_json_data,df_error[,!(colnames(df_error) %in% colnames(input_json_data))])
    }
  )
  if(err==TRUE){
    return(df_error)
  }

  # ######## FEATURE GENERATION ENDS
  #   # ##########################################################################################
  # # FEATURE CONVERSION NAD CLEANING
  # ##########################################################################################
  # 
  tryCatch(
  {
  #Retaining only relevant columns
  # Removing "Status_2" as it is dependent variable
  sel_cols <- c("Prospect_ID",
  "prospect_name",
  "Customer_Segment",
  "Product.Name",
  "BW_mbps",
  "Burstable_BW",
  "BW_mbps_act",
  "local_loop_interface",
  "resp_city",
  "Feasibility_Response_Created_Date",
  "Latitude_final",
  "Longitude_final",
  "pop_name",
  "pop_network_loc_id",
  "pop_address",
  "pop_long",
  "pop_lat",
  "POP_DIST_KM",
  "POP_DIST_KM_SERVICE",
  "POP_Network_Location_Type",
  "POP_Construction_Status",
  "POP_Building_Type",
  "POP_Category",
  "POP_TCL_Access",
  "FATG_DIST_KM",
  "FATG_Network_Location_Type",
  "FATG_Building_Type",
  "FATG_Category",
  "FATG_TCL_Access",
  "FATG_PROW",
  "FATG_Ring_type",
  "hh_name",
  "HH_DIST_KM",
  "X0.5km_cust_count",
  "X0.5km_min_dist",
  "X0.5km_avg_dist",
  "X0.5km_min_bw",
  "X0.5km_max_bw",
  "X0.5km_avg_bw",
  "X2km_cust_count",
  "X2km_min_dist",
  "X2km_avg_dist",
  "X2km_min_bw",
  "X2km_max_bw",
  "X2km_avg_bw",
  "X5km_cust_count",
  "X5km_min_dist",
  "X5km_avg_dist",
  "X5km_min_bw",
  "X5km_max_bw",
  "X5km_avg_bw",
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
  "OnnetCity_tag")
  
  input_data <- input_data[,sel_cols]
  input_data = convert_to_num(input_data)
  input_data = convert_to_char(input_data)

  # input_data=input_data %>% mutate_if(is.character, as.factor)

  if(any(is.na(input_data[,FEATURE_SET]))){
    throw("Input Error")
  }
  },
  error=function(e){
    create_log(logfile, e, log_flag)
    err <<- TRUE
    df_error$error_flag <- 1
    df_error$error_code <- "E7"
    df_error$error_msg <- "Feature Error: Error in Feature cleaning"
    df_error <<- cbind(input_json_data,df_error[,!(colnames(df_error) %in% colnames(input_json_data))])
  }
  )
  if(err==TRUE){
    return(df_error)
  }
  
  tryCatch(
  {
  # input_data <- level_mapping(xtrain, input_data)
    pred_data <- level_mapping(xtrain[,FEATURE_SET], input_data[, FEATURE_SET])
    create_log(logfile, "level mapping complete", log_flag)

    #Scoring
    # # ##########################################################################################
    # # ##########################################################################################
    # # # Scoring the input data
    # # ##########################################################################################
    # # ##########################################################################################
    # #
    # # # Score the inputs
    Prediction_Probability=predict(rf_model_val,type = "prob",pred_data)
    # # # #Applying to validation dataset
    input_data$Probabililty_Access_Feasibility = as.vector(Prediction_Probability[,2])

    ceiling_dec <- function(x, level=2) round(x + 5*10^(-level-1), level)
    input_data$Probabililty_Access_Feasibility <- sapply(input_data$Probabililty_Access_Feasibility, ceiling_dec)
    input_data$Probabililty_Access_Feasibility <- as.numeric(as.character(input_data$Probabililty_Access_Feasibility))

    input_data$Predicted_Access_Feasibility <- ifelse(input_data$Probabililty_Access_Feasibility < cut_off, "Not Feasible", "Feasible")

    create_log(logfile, "Scoring Complete", log_flag)
  },
  error=function(e){
    create_log(logfile, e, log_flag)
    err <<- TRUE
    df_error$error_flag <- 1
    df_error$error_code <- "E7"
    df_error$error_msg <- "Model Error: Error in Prediction"
    df_error <<- cbind(input_json_data,df_error[,!(colnames(df_error) %in% colnames(input_json_data))])
  }
  )
  if(err==TRUE){
    return(df_error)
  }
  
  # 
  # ##########################################################################################
  # ##########################################################################################
  # # Last Mile Cost Calculation
  # ##########################################################################################
  # ##########################################################################################

  
  # local loop interface

  input_data$local_loop_interface <- ifelse((grepl("fast", tolower(input_data$local_loop_interface)) & (grepl("ethernet", tolower(input_data$local_loop_interface)))), "FE",input_data$local_loop_interface)
  input_data$local_loop_interface <- ifelse((grepl("gigabit", tolower(input_data$local_loop_interface)) & (grepl("ethernet", tolower(input_data$local_loop_interface)))), "GE",input_data$local_loop_interface)
  
  ## Added for MACD
  input_data$valid_lle <- toupper(input_data$local_loop_interface) %in% c("FE", "GE")
    

  tryCatch(
  {
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Getting nearest distance from service pop
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    ## Clean Local Loop interface for LM cost
    input_data$local_loop_interface <- convert_bw_to_lle(input_data$local_loop_interface, input_data$BW_mbps)

    #Rounding bandwidth to nearest 2
    input_data$BW_mbps_2 <- round_bw(input_data$BW_mbps, input_data$local_loop_interface)

    # Converting metres to Kms and adjust
    input_data$POP_DIST_KM <- input_data$POP_DIST_KM/1000
    input_data$POP_DIST_KM_SERVICE_MOD <- get_adj_pop_dist(input_data$POP_DIST_KM_SERVICE, adj_fac)

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # ARC BW Rate Cards for LM Costs
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # bw_all_stack <- load_arc_rate_card(mydb_abstract_db)

    #Merging rate card with input file to get corresponding rates to the distance
    input_data <- merge(x=input_data,
                        y=bw_all_stack,
                        by.x = c("BW_mbps_2","POP_DIST_KM_SERVICE_MOD","local_loop_interface"),
                        by.y=c("BW_mbps","Distance","type"),
                        all.x=T)

    #Assigning BW-ARC cost
    colnames(input_data)[colnames(input_data) == 'value'] <- 'bw_arc_cost'
    
    ## Added for MACD: Non FE/ GE interface: Set lm ARC to 0 for invalid interface
    input_data$bw_arc_cost[!input_data$valid_lle] <- 0
    

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # MUX Cost, In-Building Capex cost, ne rental cost calculations
    # Checking whether prospect is amongst connected customers and connected buildings
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    #Connected Building: Use the real tiem custo data for business rules
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Customer data - Roll up for Business rules
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    cust_coords <<- data.table(CUST_ID = 1:nrow(cust_data_file_br),
                                  SERVICE_ID = as.vector(cust_data_file_br$SERVICEID),
                                  cust_date = as.Date(cust_data_file_br$PROVISIONING_START_DATE),
                                  cust_lat=as.vector(as.numeric(cust_data_file_br$Latitude)),
                                  cust_long=as.vector(as.numeric(cust_data_file_br$Longitude)),
                                  cust_bw = as.vector(as.numeric(cust_data_file_br$F12)),
                                  cust_name = as.vector(cust_data_file_br$CUST_NAME),
                                  cust_lat_dig = as.vector(as.numeric(cust_data_file_br$lat_sigdig)),
                                  cust_long_dig = as.vector(as.numeric(cust_data_file_br$long_sigdig)))
    create_log(logfile, "Customer Data Rolled Up for business rules", log_flag)
    rm(cust_data_file_br)
    #Creating an empty vector
    # name_vec <-   c("V1","CUST_ID","SERVICE_ID","cust_date","cust_lat", "cust_long",
    #                 "cust_bw","cust_name", "cust_lat_dig", "cust_long_dig", colnames(input_data))
    # E <- data.frame(matrix(NA, nrow = 1, ncol = length(name_vec)))
    # names(E) = name_vec

    input_data <<- input_data
    connected_custs_match <- get_connected_entity(input_data, cust_coords)

    if (nrow(connected_custs_match)==0)
    {
      input_data$Service_ID <- 0
      input_data$connected_cust_tag <- 0
      input_data$connected_building_tag <- 0
      input_data$num_connected_cust <- 0
      input_data$num_connected_building <- 0
    }else
    {
      # Cutoff for similar text match taken at 0.7
      # connected_custs_match$connected_cust <- ifelse(connected_custs_match$RecordLinkage_all_2 >= 0.7,1,0)
      connected_custs_match$similar_cust_name <- ifelse(connected_custs_match$RecordLinkage_all >= CUST_NAME_MATCH_CUTOFF,1,0)

      # connected_custs_match$connected_building <- 1
      # connected_custs_match$connected_building <- connected_building_rule(connected_custs_match$cust_lat, connected_custs_match$cust_long)
      connected_custs_match$connected_building <- ifelse(connected_custs_match$cust_lat_dig >= GEO_CODE_SIG_DIG & connected_custs_match$cust_long_dig >= GEO_CODE_SIG_DIG, 1, 0)

      # connected_custs_match$connected_building <- ifelse(connected_custs_match$V1 < CONNECT_BUILD_DIST, 1, 0)
      # connected_custs_match$connected_building_50 <- ifelse(connected_custs_match$V1 < 50, 1, 0)


      connected_custs_match$connected_cust <- ifelse(connected_custs_match$connected_building & connected_custs_match$similar_cust_name, 1, 0)


      # take subset of actual connected custs for network check
      connected_cc <<- connected_custs_match[connected_custs_match$connected_cust==1,]

      connected_custs_match_agg <- sqldf("select
                                          connected_custs_match.Prospect_ID,
                                          connected_custs_match.Service_ID,
                                          sum(connected_custs_match.connected_cust) as num_connected_cust,
                                          sum(connected_custs_match.connected_building) as num_connected_building
                                          from connected_custs_match
                                          group by 1")


      input_data <- merge(x=input_data,
                          y= connected_custs_match_agg,
                          by.x="Prospect_ID",by.y="Prospect_ID",all.x=T)



      # clean the 2 fields
      # input_data$num_connected_cust <- ifelse(is.na(input_data$num_connected_cust),0,input_data$num_connected_cust)
      # input_data$num_connected_building <- ifelse(is.na(input_data$num_connected_building),0,input_data$num_connected_building)

      input_data$num_connected_cust[is.na(input_data$num_connected_cust)] <- 0
      input_data$num_connected_building[is.na(input_data$num_connected_building)] <- 0


      # create tags for 2 fields on which checks will be done
      input_data$connected_cust_tag <- ifelse(input_data$num_connected_cust >= 1,1,0)
      input_data$connected_building_tag <- ifelse(input_data$num_connected_building >= 1,1,0)

      # input_data$connected_cust_tag_50 <- ifelse(input_data$num_connected_cust_50 >= 1,1,0)
      # input_data$connected_cust_tag_100 <- ifelse(input_data$num_connected_cust_100 >= 1,1,0)
      #
      # input_data$connected_building_tag_50 <- ifelse(input_data$num_connected_building_50 >= 1,1,0)
      # input_data$connected_building_tag_100 <- ifelse(input_data$num_connected_building_100 >= 1,1,0)
    }



      #Assigining MUX cost
      input_data$mux_cost <- ifelse(input_data$connected_cust_tag==1,0,
                                    ifelse(input_data$BW_mbps_2<=350,58810,
                                           ifelse(input_data$BW_mbps_2<=1000, 80611,
                                                  ifelse(input_data$BW_mbps_2<=2000, 623173,
                                                         ifelse(input_data$BW_mbps_2<=5000, 835108, 917744)))))

    #Assigning In Building Capex Costs
    input_data$in_building_capex_cost <- ifelse(input_data$connected_cust_tag==1,0,IN_BUILD_CAPEX)

    #Assigning NE Rental cost
    input_data$ne_rental_cost <- 0

    #Assigning BW OTC charges
    input_data$bw_otc_cost <- 0

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # OSP Capex Cost Calculation
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    #Retaining only relevant variables
    osp_cost <- man_city[,c("CITY_NAME","cost_permeter")]
    osp_cost$CITY_NAME = tolower(osp_cost$CITY_NAME)
    osp_cost <- osp_cost[(!duplicated(osp_cost$CITY_NAME)),]
    input_data$resp_city <- tolower(input_data$resp_city)

    #Merging with eeplus master to get cost per meter
    input_data <- merge(x=input_data,
                        y=osp_cost,
                        by.x = "resp_city",
                        by.y="CITY_NAME",
                        all.x=T)
    # In case the requested city is not present then OSP cost is zero
    if(any(is.na(input_data$cost_permeter))){
      input_data$cost_permeter[is.na(input_data$cost_permeter)]<-0
    }


    #Assigning OSP capex cost
    ##input_data$min_hh_fatg <- pmin(input_data$HH_DIST_KM,input_data$FATG_DIST_KM)
    input_data$min_hh_fatg <- input_data$HH_DIST_KM
    # take 25% extra as it's aerial distance
    input_data$min_hh_fatg <- round(input_data$min_hh_fatg * 1.25)
    input_data$HH_DIST_KM <- round(input_data$HH_DIST_KM * 1.25)
    input_data$osp_capex_cost <- (input_data$cost_permeter)*(input_data$min_hh_fatg)

    # No OSP Capex if connected cust or connected bldg
    input_data$osp_capex_cost <- ifelse((input_data$connected_cust_tag==1)|(input_data$connected_building_tag==1),0,input_data$osp_capex_cost)
    # input_data$osp_capex_cost_50 <- ifelse((input_data$connected_cust_tag_50 ==1)|(input_data$connected_building_tag_50 ==1),0,input_data$osp_capex_cost)

    # RG ADDED: If connected building or connect customer set OSP_dist to 0
    input_data$min_hh_fatg <- ifelse((input_data$connected_cust_tag==1)|(input_data$connected_building_tag==1),0,input_data$min_hh_fatg)

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Total Cost Calculation
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    input_data$total_cost <- (input_data$bw_arc_cost+
                                input_data$mux_cost +
                                input_data$in_building_capex_cost +
                                input_data$ne_rental_cost +
                                input_data$bw_otc_cost +
                                input_data$osp_capex_cost)

    create_log(logfile, "LM Cost completed", log_flag)
  }, 
  error=function(e){
    err <<- TRUE
    create_log(logfile, e, log_flag)
    df_error$error_flag <- 1
    df_error$error_code <- "E9"
    df_error$error_msg <- "Model Error: Error in LM Cost Calculation"
    df_error <<- cbind(input_json_data,df_error[,!(colnames(df_error) %in% colnames(input_json_data))])
  }
  )
  if(err==TRUE){
    return(df_error)
  }


  ##########################################################################################
  ##########################################################################################
  # Network Feasibility Checks
  ##########################################################################################
  ##########################################################################################

  tryCatch(
  {
      # Add city tier
      input_data$resp_city <- toupper(input_data$resp_city)
      input_data$city_tier <- ifelse(input_data$resp_city %in% TIER1_CITY_LIST, TIER1_LABEL, NON_TIER1_LABEL)

      # Pre-Feasible scenarios

      input_data$scenario_1 <- ifelse((input_data$city_tier == TIER1_LABEL &
                                         input_data$BW_mbps <= TIER1_PRE_FEASIBLE_BW), 1, 0)
      input_data$scenario_2 <- ifelse((input_data$city_tier == NON_TIER1_LABEL &
                                         input_data$BW_mbps <= NON_TIER1_PRE_FEASIBLE_BW), 1, 0)

      # Pre-Feasible flag
      input_data$net_pre_feasible_flag <- ifelse((input_data$scenario_1+input_data$scenario_2)> 0, 1, 0)

      ##O2C
      input_data <- fn_Network_Feasibility_CC_Check(input_data)
      input_data <- fn_Network_Feasibility_HH_Check(input_data)

      input_data$selected_access_ring = ifelse(input_data$Network_F_NF_CC_Flag > 0, input_data$mux_access_ring,
                                                                                          ifelse(input_data$Network_F_NF_HH_Flag> 0, input_data$access_rings_hh, "NA"))


    #   # Separate cases which are pre-feasible and not pre-feasible
    #   input_data_pre_f <- input_data[input_data$net_pre_feasible_flag==1, ]
    #   input_data_pre_nf <- input_data[input_data$net_pre_feasible_flag==0, ]
    #
    #
    #   # Check only if there is at least one request which is not Pre-Feasible
    #   if(nrow(input_data_pre_nf)>0){
    #     #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     # Check Network Feasibility through MUX in Connected Customer for Not Feasible cases
    #     #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     input_data_pre_nf <- fn_Network_Feasibility_CC_Check(input_data_pre_nf)
    #
    #     #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     # Check Network Feasibility through Handhole within 0.5kms for Not Feasible cases
    #     #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     input_data_pre_nf <- fn_Network_Feasibility_HH_Check(input_data_pre_nf)
    #
    #     #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     # Combine Pre Feasibile and Not Pre Feasible cases
    #     #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     # Add extra columns in input_data_pre_f which are there in Pre NF
    #     pre_nf_col_diff <- setdiff(colnames(input_data_pre_nf),colnames(input_data_pre_f))
    #     extra_cols_df <- data.frame(matrix(ncol = length(pre_nf_col_diff), nrow = 0))
    #     colnames(extra_cols_df) <- pre_nf_col_diff
    #
    #     # Add blank values on these extra columns
    #     if(nrow(input_data_pre_f)>0){
    #       input_data_pre_f[pre_nf_col_diff] <- "NA"
    #     }else{
    #       input_data_pre_f <- cbind(input_data_pre_f,extra_cols_df)
    #     }
    #     # Comine requests which are pre-feasible and not pre-feasible
    #     input_data <- rbind(input_data_pre_f,input_data_pre_nf)
    #
    #   input_data$selected_access_ring = ifelse(input_data$Network_F_NF_CC_Flag > 0, input_data$mux_access_ring,
    #                                            ifelse(input_data$Network_F_NF_HH_Flag> 0, input_data$access_rings_hh, "NA"))
    #
    #   }else{
    #     col_extra <- c("Network_F_NF_CC_Flag",
    #                  "Network_F_NF_CC",
    #                  "access_check_CC",
    #                  "core_check_CC",
    #                  "HH_0_5km",
    #                  "hh_flag",
    #                  "Network_F_NF_HH_Flag",
    #                  "Network_F_NF_HH",
    #                  "access_check_hh",
    #                  "core_check_hh",
    #                  "HH_0_5_access_rings_F",
    #                  "HH_0_5_access_rings_NF",
    #                  #added for O2C
    #                  "selected_access_ring",
    #                  "mux",
    #                  "mux_ip",
    #                  "mux_port")
    #
    #   input_data_pre_f[col_extra] <- "NA"
    #   input_data <- input_data_pre_f
    # }


      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Check final Network Feasibility
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      input_data$net_pre_feasible_flag <- ifelse(is.na(input_data$net_pre_feasible_flag),0,input_data$net_pre_feasible_flag)
      input_data$Network_F_NF_CC_Flag <- ifelse(is.na(input_data$Network_F_NF_CC_Flag),0,input_data$Network_F_NF_CC_Flag)
      input_data$Network_F_NF_HH_Flag <- ifelse(is.na(input_data$Network_F_NF_HH_Flag),0,input_data$Network_F_NF_HH_Flag)

      input_data$Network_Feasibility_Check <- ifelse(((input_data$net_pre_feasible_flag == 1) |
                                                        (input_data$Network_F_NF_CC_Flag == 1) |
                                                        (input_data$Network_F_NF_HH_Flag == 1)),
                                                     "Feasible",
                                                     "Not Feasible")
      create_log(logfile, "Network Complete", log_flag)
  },
    error=function(e){
      err <<- TRUE
      create_log(logfile, e, log_flag)
      df_error$error_flag <- 1
      df_error$error_code <- "E10"
      df_error$error_msg <- "Model Error: Error in checking Network Feasibility"
      df_error <<- cbind(input_json_data,df_error[,!(colnames(df_error) %in% colnames(input_json_data))])
    }
  )
  if(err==TRUE){
    return(df_error)
  }

  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  # Adding Orchestration columns
  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

  input_data$Orch_LM_Type <- "Onnet"
  input_data$Orch_Connection <- "Wireline"
  input_data$Orch_Category <- ifelse(input_data$connected_cust_tag==1, "Connected Customer",
                                     ifelse(input_data$connected_building_tag==1, "Connected Building",
                                            ifelse(input_data$min_hh_fatg<=175, "Capex less than 175m",
                                                   "Capex greater than 175m")))


  input_data$Orch_BW <- input_data$BW_mbps
  #Partner
  input_data$solution_type = "MAN"

  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  # adjustment for "Capex greater than 175m" Orch_Category
  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  input_data$Predicted_Access_Feasibility <- ifelse((input_data$Orch_Category=="Capex greater than 175m")&(input_data$Predicted_Access_Feasibility=="Feasible"), "Feasible with Capex", input_data$Predicted_Access_Feasibility)

  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  # adjustment for Connected Customer or Connected Building
  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  input_data$Predicted_Access_Feasibility <- ifelse((input_data$connected_cust_tag==1)|(input_data$connected_building_tag==1), "Feasible", input_data$Predicted_Access_Feasibility)

  ## Added for MACD: Non FE/ GE interface: Set lm ARC to 0 for invalid interface
  input_data$Predicted_Feasibility_Comment <- ifelse(input_data$Predicted_Access_Feasibility == "Not Feasible", "Access_Not_Feasible", "Access_Feasible")
  #If any of condition 1, 2 or 3 is true then set Predicted_Access_Feasibility to Not feasible and update reason
  
  #Conditon 1: BW > 1000 Mbps
  input_data$high_bw <- input_data$Orch_BW>MANUAL_FEASIBILITY_BW
  
  # Condition 2: resp_city exists in list of manual row city list
  input_data$row_manual = (toupper(input_data$resp_city) %in% toupper(row_city$city_name)) & !(input_data$connected_cust_tag==1) & !(input_data$connected_building_tag==1)
  
  #Condition 3: Invalid ll interface
  
  #Partner   FP-17
  #Condition 4: Chargeable Distance beyond 50km
  CD_CAP_KMS = 50
  input_data$high_cd =input_data$POP_DIST_KM_SERVICE_MOD >  CD_CAP_KMS

  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  # adjustment for BW > 1000 Mbps for manual feasibility & manual row & invalid LL Interface
  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  input_data$Predicted_Access_Feasibility <- ifelse(input_data$high_cd | input_data$high_bw | input_data$row_manual | !input_data$valid_lle, "Not Feasible", input_data$Predicted_Access_Feasibility)
  
  input_data$Predicted_Feasibility_Comment <- ifelse(input_data$high_bw , paste(input_data$Predicted_Feasibility_Comment, "BW > 1 GIG", sep=", "), input_data$Predicted_Feasibility_Comment) 
  input_data$Predicted_Feasibility_Comment <- ifelse(input_data$row_manual , paste(input_data$Predicted_Feasibility_Comment, "ROW_ISSUE", sep=", "), input_data$Predicted_Feasibility_Comment) 
  input_data$Predicted_Feasibility_Comment <- ifelse(!input_data$valid_lle , paste(input_data$Predicted_Feasibility_Comment, "Invalid_LL_Interface", sep=", "), input_data$Predicted_Feasibility_Comment) 
  
  #Partner FP-17
  input_data$Predicted_Feasibility_Comment <- ifelse(input_data$high_cd , paste(input_data$Predicted_Feasibility_Comment, "CD > 50 Km", sep=", "), input_data$Predicted_Feasibility_Comment)



  ##########################################################################################
  ##########################################################################################
  # Final Output
  ##########################################################################################
  ##########################################################################################
  # exclude the input json column as they are merged in later step
  input_data <- input_data[, !(tolower(colnames(input_data)) %in% tolower(colnames(input_json_data)))]

  # Merge with original input json to get original inputs which will be passed to pricing
  input_data <- merge(input_data, input_json_data, by.x = "Prospect_ID", by.y = "site_id", all.x = T)

  #Change Prospect ID to Site ID for orchestration
  colnames(input_data)[colnames(input_data) == 'Prospect_ID'] <- 'site_id'


  # # replace all NAs
  # if(any(is.na(input_data))){
  #   input_data[is.na(input_data)] <- "NA"
  # }
  input_data[is.na(input_data)] <- "NA"

  ##########################################################################################
  # Add Last Mile columns
  ##########################################################################################

  # Onnet Wireline LM cols
  colnames(input_data)[colnames(input_data) == 'bw_arc_cost'] <- 'lm_arc_bw_onwl'
  colnames(input_data)[colnames(input_data) == 'bw_otc_cost'] <- 'lm_nrc_bw_onwl'
  colnames(input_data)[colnames(input_data) == 'mux_cost'] <- 'lm_nrc_mux_onwl'
  colnames(input_data)[colnames(input_data) == 'in_building_capex_cost'] <- 'lm_nrc_inbldg_onwl'
  colnames(input_data)[colnames(input_data) == 'osp_capex_cost'] <- 'lm_nrc_ospcapex_onwl'
  colnames(input_data)[colnames(input_data) == 'ne_rental_cost'] <- 'lm_nrc_nerental_onwl'

  input_data$lm_arc_bw_onwl <- as.numeric(input_data$lm_arc_bw_onwl)
  input_data$lm_nrc_bw_onwl <- as.numeric(input_data$lm_nrc_bw_onwl)
  input_data$lm_nrc_mux_onwl <- as.numeric(input_data$lm_nrc_mux_onwl)
  input_data$lm_nrc_inbldg_onwl <- as.numeric(input_data$lm_nrc_inbldg_onwl)
  input_data$lm_nrc_ospcapex_onwl <- as.numeric(input_data$lm_nrc_ospcapex_onwl)
  input_data$lm_nrc_nerental_onwl <- as.numeric(input_data$lm_nrc_nerental_onwl)


  # Offnet RF LM cols
  input_data$lm_arc_bw_prov_ofrf <- 0
  input_data$lm_nrc_bw_prov_ofrf <- 0
  input_data$lm_nrc_mast_ofrf <- 0

  # Onnet RF LM cols
  input_data$lm_arc_bw_onrf <- 0
  input_data$lm_nrc_bw_onrf <- 0
  input_data$lm_nrc_mast_onrf <- 0

  # for removing nan for ARC BW in case of higher bws in NPL
  input_data$lm_arc_bw_onwl <- ifelse(is.na(input_data$lm_arc_bw_onwl), 0 , input_data$lm_arc_bw_onwl)

  # Add blank error attributes in case everything runs smoothly
  input_data$error_code <- "NA"
  input_data$error_flag <- 0
  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  # Set the error message if  BW > 1000 Mbps
  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  input_data$error_msg <- "No error"
  input_data$error_msg <- ifelse((input_data$Orch_BW > MANUAL_FEASIBILITY_BW), "BW values is greater than 1 Gig", input_data$error_msg)



  # Remove cols which are not required or are duplicates in the output
  input_data$bw_mbps <- as.numeric(input_data$BW_mbps_act)

  rem_cols <- c("BW_mbps",
    "BW_mbps_2",
    "BW_mbps_act",
    "Burstable_BW",
    "Feasibility_Response_Created_Date",
    "Latitude_final",
    "Longitude_final",
    "seq_no",
    "sno",
    "Status.v2",
    "Identifier",
    "valid_lle",
    "row_manual",
    "high_bw",
    "high_cd"
  )

  input_data <- input_data[,!(names(input_data) %in% rem_cols)]

  # Disconnect DB connections once processing done
  lapply(dbListConnections(MySQL()), dbDisconnect)

  return(input_data)
}

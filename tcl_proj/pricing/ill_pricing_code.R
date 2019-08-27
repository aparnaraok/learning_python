run_ILL_pricing <- function(bm_data, path_py){
  ##########################################################################################
  ##########################################################################################
  # ILL_Price_Generation: Generates price components for ILL overall, port & CPE pricing
  #
  ##########################################################################################
  ##########################################################################################
  #
  # Version: History
  #
  #V1: Create Date: 02-07-2018
  #V2: Modified Date: 18-07-2018
  #V3: Modified Date: 20-07-2018
  # Applied changed in calculation of CPE components as per discussion with Reema Dahariya
  # Calculation changes are applicable for HW, Support & Installation SP
  #V4: Modified Date: 23-07-2018
  #   Last Mile ARC discount of flat 60% is applied for passive port for MAN 
  #   Last Mile ARC discount of port predicted discount + adjsutment factor is applied for active MAN ports
  #   Last Mile ARC i+PE sale calulations
  #V5: Fixed order change on input request as resulut of merges & binds
  # 
  #V6: Updated CPE pricing construct based on management type
  
  #2.1: Changes aplied for handling legal entity based nuances for rate-card customers
  
  #2.2: Separating Mast height charges for LM
  ##########################################################################################
  # set error parameter
  err <<- FALSE
  
  version <- 4.2
  ##########################################################################################
  # Define Error Output JSON to be thrown in case of any error encountered
  ##########################################################################################
  # Define Error response dataframe
  df_error <- data.frame('site_id' = 'NA','latitude_final' = 'NA','longitude_final' = 'NA','prospect_name' = 'NA','bw_mbps' = 'NA','burstable_bw' = 'NA','resp_city' = 'NA','customer_segment' = 'NA','sales_org' = 'NA','product_name' = 'NA','feasibility_response_created_date' = 'NA','local_loop_interface' = 'NA','last_mile_contract_term' = 'NA','account_id_with_18_digit' = 'NA','opportunity_term' = 'NA','quotetype_quote' = 'NA','connection_type' = 'NA','sum_no_of_sites_uni_len' = 'NA','cpe_variant' = 'NA','cpe_management_type' = 'NA','cpe_supply_type' = 'NA','topology' = 'NA','sum_onnet_flag' = 'NA','sum_offnet_flag' = 'NA','f_lm_arc_bw_onwl' = 'NA','f_lm_nrc_bw_onwl' = 'NA','f_lm_nrc_mux_onwl' = 'NA','f_lm_nrc_inbldg_onwl' = 'NA','f_lm_nrc_ospcapex_onwl' = 'NA','f_lm_nrc_nerental_onwl' = 'NA','f_lm_arc_bw_prov_ofrf' = 'NA','f_lm_nrc_bw_prov_ofrf' = 'NA','f_lm_nrc_mast_ofrf' = 'NA','f_lm_arc_bw_onrf' = 'NA','f_lm_nrc_bw_onrf' = 'NA','f_lm_nrc_mast_onrf' = 'NA','Orch_Connection' = 'NA','Orch_LM_Type' = 'NA','additional_ip_flag' = 'NA','ip_address_arrangement' = 'NA','ipv4_address_pool_size' = 'NA','ipv6_address_pool_size' = 'NA','overall_CPE_node' = 'NA','overall_node' = 'NA','Sum_Offnet_Flag' = 'NA','Sum_Onnet_Flag' = 'NA','Last_Mile_Cost_ARC' = 'NA','Last_Mile_Cost_NRC' = 'NA','additional_IP_ARC' = 'NA','additional_IP_MRC' = 'NA','port_lm_arc' = 'NA','hist_flag' = 'NA','opportunity_day' = 'NA','opportunity_month' = 'NA','Sum_New_ARC_Converted' = 'NA','Sum_IAS_FLAG' = 'NA','Sum_GVPN_Flag' = 'NA','Sum_NPL_Flag' = 'NA','Sum_Other_Flag' = 'NA','Inv_ILL_bw' = 'NA','Inv_GVPN_bw' = 'NA','Inv_NPL_bw' = 'NA','Inv_Other_bw' = 'NA','Inv_Tot_BW' = 'NA','Sum_New_ARC_Converted_ILL' = 'NA','Sum_New_ARC_Converted_GVPN' = 'NA','Sum_New_ARC_Converted_NPL' = 'NA','Sum_New_ARC_Converted_Other' = 'NA','ILL_ARC_per_BW' = 'NA','GVPN_ARC_per_BW' = 'NA','NPL_ARC_per_BW' = 'NA','Other_ARC_per_BW' = 'NA','TOT_ARC_per_BW' = 'NA','Sum_CAT_1_2_MACD_FLAG' = 'NA','Sum_CAT_1_2_New_Opportunity_FLAG' = 'NA','Sum_CAT_3_MACD_FLAG' = 'NA','Sum_CAT_3_New_Opportunity_FLAG' = 'NA','Sum_CAT_4_MACD_FLAG' = 'NA','Sum_CAT_4_New_Opportunity_FLAG' = 'NA','Sum_Cat_1_2_opp' = 'NA','Sum_New_Opportunity' = 'NA','Sum_MACD_Opportunity' = 'NA','sum_cat1_2_Opportunity' = 'NA','sum_cat_3_Opportunity' = 'NA','sum_cat_4_Opportunity' = 'NA','Sum_tot_oppy_historic_opp' = 'NA','Sum_tot_oppy_historic_prod' = 'NA','createdDate_quote' = 'NA','OpportunityID_Prod_Identifier' = 'NA','Industry_Cust' = 'NA','Segment_Cust' = 'NA','Account.RTM_Cust' = 'NA','ILL_ARC' = 'NA','ILL_NRC' = 'NA','calc_arc_list_inr' = 'NA','list_price_mb' = 'NA','list_price_mb_dummy' = 'NA','log_Inv_Tot_BW' = 'NA','log_Inv_Tot_BW_dummy' = 'NA','overall_BW_mbps_upd' = 'NA','num_products_opp_new.x' = 'NA',
                         'sum_product_flavours.x' = 'NA','tot_oppy_current_prod.x' = 'NA','overall_PortType' = 'NA','Identifier' = 'NA','port_pred_discount' = 'NA','predicted_ILL_Port_ARC' = 'NA','predicted_ILL_Port_NRC' = 'NA','predicted_net_price' = 'NA','Bucket_Adjustment_Type' = 'Manual Trigger- Run-time Error','Adjustment_Factor' = 'NA','ILL_Port_Adjusted_net_Price' = 'NA','ILL_Port_ARC_Adjusted' = 'NA','ILL_Port_NRC_Adjusted' = 'NA','burst_per_MB_price' = 'NA','ILL_Port_MRC_Adjusted' = 'NA','Last_Mile_Cost_MRC' = 'NA','CPE_pred' = 'NA','CPE_Installation_INR' = 'NA','CPE_Support_INR' = 'NA','CPE_Management_INR' = 'NA','Recovery_INR' = 'NA','CPE_Hardware_LP_USD' = 'NA','OEM_Discount' = 'NA','CPE_HW_MP' = 'NA','CPE_Installation_MP' = 'NA','CPE_Support_MP' = 'NA','ILL_CPE_ARC' = 'NA','ILL_CPE_NRC' = 'NA','ILL_CPE_MRC' = 'NA','Adjusted_CPE_Discount' = 'NA','Discounted_CPE_ARC' = 'NA','Discounted_CPE_NRC' = 'NA','Discounted_CPE_MRC' = 'NA','Total_CPE_Cost' = 'NA','Total_CPE_Price' = 'NA','time_taken' = 'NA','error_code' = 'NA','error_flag' = 'NA','error_msg' = 'NA','p_lm_arc_bw_onwl' = 'NA','p_lm_nrc_bw_onwl' = 'NA','p_lm_nrc_mux_onwl' = 'NA','p_lm_nrc_inbldg_onwl' = 'NA','p_lm_nrc_ospcapex_onwl' = 'NA','p_lm_nrc_nerental_onwl' = 'NA','p_lm_arc_bw_prov_ofrf' = 'NA','p_lm_nrc_bw_prov_ofrf' = 'NA','p_lm_nrc_mast_ofrf' = 'NA','p_lm_arc_bw_onrf' = 'NA','p_lm_nrc_bw_onrf' = 'NA','p_lm_nrc_mast_onrf' = 'NA','total_contract_value' = 'NA',
                         'version' = version, 'total_commission' = 'NA', 'sp_lm_arc_bw_onwl' = 'NA','sp_lm_nrc_bw_onwl' = 'NA','sp_lm_nrc_mux_onwl' = 'NA','sp_lm_nrc_inbldg_onwl' = 'NA','sp_lm_nrc_ospcapex_onwl' = 'NA','sp_lm_nrc_nerental_onwl' = 'NA','sp_lm_arc_bw_prov_ofrf' = 'NA','sp_lm_nrc_bw_prov_ofrf' = 'NA','sp_lm_nrc_mast_ofrf' = 'NA','sp_lm_arc_bw_onrf' = 'NA','sp_lm_nrc_bw_onrf' = 'NA','lm_nrc_mast_ofrf' = 'NA','lm_nrc_mast_onrf' = 'NA','sp_lm_nrc_mast_onrf' = 'NA',
                         'sp_CPE_Outright_NRC' = 'NA',
                         'sp_CPE_Rental_ARC' = 'NA',
                         'sp_CPE_Install_NRC' = 'NA',
                         'sp_CPE_Management_ARC' = 'NA',
                         'sp_port_arc' = 'NA',
                         'sp_port_nrc' = 'NA',
                         'sp_burst_per_MB_price_ARC' = 'NA',
                         'sp_additional_IP_ARC' = 'NA',
                         'effective_port_discount' = 'NA',
                         'tot_commission_pct' = 'NA',
                         stringsAsFactors = FALSE)
  tryCatch(
    {
      ##########################################################################################
      # I. SET ENVIRONMENT
      #
      # R Packages - Check if needed packages are installed - if not, install them
      
      ##########################################################################################
      ##########################################################################################
      options(digits = 10)
      options(sqldf.driver = "SQLite")
      # Suppress warnings
      options( warn = -1 )
      packages <- c("dplyr","plyr","readxl","geosphere","lubridate","data.table",
                    "sqldf","randomForest","RecordLinkage","jsonlite","RMySQL","reshape2", "gdata", "Metrics", "caTools", "openxlsx", "stringi", "jsonlite")
      
      if (length(setdiff(packages, rownames(installed.packages()))) > 0) {
        print(package)
        install.packages(setdiff(packages, rownames(installed.packages())))
      }
      rm(packages)
      
      time_start <- proc.time()
      ##########################################################################################
      # II. LOAD LIBRARIES
      ##########################################################################################
      library(dplyr, quietly = TRUE)
      library(geosphere, quietly = TRUE)
      library(gdata, quietly = TRUE)
      library(readxl, quietly = TRUE)
      library(caTools, quietly = TRUE)
      library(sqldf, quietly = TRUE)
      library(randomForest, quietly = TRUE)
      library(lubridate, quietly = TRUE)
      library(RMySQL, quietly = TRUE)
      library(jsonlite, quietly = TRUE)
      library(stringi, quietly = TRUE)
    },
    error=function(e){
      err <<- TRUE
      df_error$error_flag <- 1
      df_error$error_code <- "E11"
      df_error$error_msg <- "R Package Error: R Package not found"
      df_error <<- cbind(input_json_data,df_error[,!(colnames(df_error) %in% colnames(input_json_data))])
    }
  )
  if(err==TRUE){
    return(df_error)
  }
  
  ##########################################################################################
  # III. SET INPUT PARAMETERS	
  # 1. Set path
  # 2. Define Filenames
  # 3. Input JSON #***
  ##########################################################################################
  #1. Set path
  setwd(path_py)
  
  #2. Define Filenames
  ILL_CPE_Discount_Rates <- "ILL_CPE_Node_Prediction.rda"
  adjustment_data_name <- "ILL_Error_Adjustment.rda"
  ILL_model_object_name <- "ILL_RF_Model_oct_16_may_18.rda"
  Train_data_sample_name <- "train_data_sample_june2018.rda"
  
  #3. Input JSON
  JSON_filename <- "test.json"
  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  # Read Input JSON File
  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  input_json_data <- bm_data
  
  # Preserve order of data
  bm_data$order_no <- 1:nrow(bm_data)
  # Map the input JSON cols from Feasibility engine according to input json of Pricing
  bm_data <- dplyr::mutate(bm_data,
                           a_site_id = site_id,
                           a_latitude_final = latitude_final,
                           a_longitude_final = longitude_final,
                           a_prospect_name = prospect_name,
                           a_bw_mbps = bw_mbps,
                           a_burstable_bw = burstable_bw,
                           a_resp_city = resp_city,
                           a_customer_segment = customer_segment,
                           a_sales_org = sales_org,
                           a_product_name = product_name,
                           a_feasibility_response_created_date = feasibility_response_created_date,
                           a_local_loop_interface = local_loop_interface,
                           a_last_mile_contract_term = last_mile_contract_term,
                           a_account_id_with_18_digit = account_id_with_18_digit,
                           a_opportunity_term = opportunity_term,
                           a_quotetype_quote = quotetype_quote,
                           a_connection_type = connection_type,
                           a_sum_no_of_sites_uni_len = sum_no_of_sites_uni_len,
                           a_cpe_variant = cpe_variant,
                           a_cpe_management_type = cpe_management_type,
                           a_cpe_supply_type = cpe_supply_type,
                           a_topology = topology,
                           a_ipv4_address_pool_size = ipv4_address_pool_size,
                           a_ipv6_address_pool_size = ipv6_address_pool_size,
                           a_ip_address_arrangement = ip_address_arrangement,
                           a_additional_ip_flag = additional_ip_flag)
  
  bm_data <- dplyr::mutate(bm_data,
                           Account_id_with_18_Digit = account_id_with_18_digit,
                           Last_Modified_Date = feasibility_response_created_date,
                           opportunityTerm = opportunity_term,
                           quoteType_quote = quotetype_quote,
                           BW_mbps_upd = bw_mbps,
                           CPE_Variant = cpe_variant,
                           CPE_management_type = cpe_management_type,
                           CPE_supply_type = cpe_supply_type,
                           Burstable_BW = burstable_bw)
  
  # Add Onnet Offnet flags from orchestration attributes generated from Feasibility engine
  bm_data$Sum_Offnet_Flag <- ifelse(bm_data$Orch_LM_Type=="Offnet",1,0)
  bm_data$Sum_Onnet_Flag <- ifelse(bm_data$Orch_LM_Type=="Onnet",1,0)
  bm_data$Sum_Offnet_Flag <- sum(as.numeric(bm_data$Sum_Offnet_Flag))
  bm_data$Sum_Onnet_Flag <- sum(as.numeric(bm_data$Sum_Onnet_Flag))
  bm_data$sum_no_of_sites_uni_len <- length(bm_data$sum_no_of_sites_uni_len)
  bm_data$connection_type <- ifelse(bm_data$connection_type == "Compressed Internet",
                                    ifelse(bm_data$Compressed_Internet_Ratio == "1:2",
                                           "Compressed_1_2",
                                           "Compressed_1_4"),
                                    bm_data$connection_type)
  
  # Add Last Mile cost attributes from LM attributes from Feasibility engine - only for respective scenario it will be populated, otherwise it will be zero, hence add all
  bm_data$lm_nrc_mux_onwl <- ifelse((bm_data$Orch_LM_Type=='Onnet')&(bm_data$Orch_Connection=='Wireline'),0,bm_data$lm_nrc_mux_onwl)
  bm_data$lm_nrc_inbldg_onwl <- ifelse((bm_data$Orch_LM_Type=='Onnet')&(bm_data$Orch_Connection=='Wireline'),0,bm_data$lm_nrc_inbldg_onwl)
  
  bm_data$Last_Mile_Cost_ARC <- as.numeric(bm_data$lm_arc_bw_onwl) +
    as.numeric(bm_data$lm_arc_bw_prov_ofrf) +
    as.numeric(bm_data$lm_arc_bw_onrf)
  
  # All LM NRC components are added except OSP Capex & MAST HEIGHT CHARGES
  bm_data$lm_nrc_bw_onrf <- 0 #As per BR: combined NRC (LM+Port) is applicable
  bm_data$Last_Mile_Cost_NRC <- as.numeric(bm_data$lm_nrc_bw_onwl) +
    as.numeric(bm_data$lm_nrc_mux_onwl) +
    as.numeric(bm_data$lm_nrc_inbldg_onwl) +
    #as.numeric(bm_data$lm_nrc_ospcapex_onwl) +
    as.numeric(bm_data$lm_nrc_nerental_onwl) +
    as.numeric(bm_data$lm_nrc_bw_prov_ofrf) +
    #as.numeric(bm_data$lm_nrc_mast_ofrf) +
    as.numeric(bm_data$lm_nrc_bw_onrf) #+ REMOVE MAST CHARGES FROM LM COST
  #as.numeric(bm_data$lm_nrc_mast_onrf)
  
  #4. Set Flags & constant variables
  RATE_CARD_AVAILABLE <- FALSE
  CPE_PRICE_AVAILABLE <- FALSE
  LM_COST_AVAILABLE <- FALSE
  DEBUG_MODE <- FALSE
  ETL_CONNECTION <- TRUE
  
  ETL_col_names <- c("seq_no", "etl_batch_id", "etl_load_dt", "created_dt", "updated_dt", "src_system")
  
  #++++++++++++++++++++++++++++++++++++++++++++++++++++
  #     Port CONSTANT VARIABLES
  #+++++++++++++++++++++++++++++++++++++++++++++++++++++
  PORT_NRC_CHARGE <- 5000
  
  PORT_NRC_CHARGE_1_TO_100MB <- 5000
  PORT_NRC_CHARGE_101_TO_300MB <- 10000
  PORT_NRC_CHARGE_300_TO_1000MB <- 15000
  PORT_NRC_CHARGE_GT_THAN_1000MB <- 20000
  
  LM_PORT_NRC_CHARGE_ONRF <- 15000
  
  LM_ARC_DISCOUNT_ONNET_RF <- 0.25
  
  MAST_HEIGHT_PER_METER_COST <- 4700
  #++++++++++++++++++++++++++++++++++++++++++++++++++++
  #     CPE CONSTANT VARIABLES
  #+++++++++++++++++++++++++++++++++++++++++++++++++++++
  USD_2_INR_CONVERSION <- 74
  
  CPE_HW_MARKUP <- 0.35 #40%
  CPE_VENDOR_DISCOUNT <- 0.03 #3%
  CPE_HW_DISCOUNT_CEILING <- 1 #100%
  CPE_HW_DDP <- 0.061
  
  CPE_SUPPORT_MARKUP <- 0.35
  CPE_SUPPORT_DISCOUNT_CEILING <- 1
  
  CPE_INSTALL_MARKUP <- CPE_HW_MARKUP
  CPE_DEFAULT_MARKUP <- 0.15
  CPE_INSTALL_DISCOUNT <- 0.25
  CPE_INSTALL_DISCOUNT_CEILING <- 1
  
  CPE_MANAGEMENT_MARKUP <- 0
  CPE_MANAGEMENT_DISCOUNT_CEILING <- 0.5
  
  COC <- 0.12
  CPE_OVERALL_DISCOUNT_CEILING <- 0.25
  
  DOA <- 0.95
  
  #5. Database Connection
  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  # Database Connection
  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  # Establishing connection
  if(ETL_CONNECTION){
    tryCatch(
      {
        mydb_abstract_db = dbConnect(MySQL(),
                                     user='optimus_user', 
                                     password='Tata123', 
                                     dbname='optimus_abstract_uat2', 
                                     host='INP44XDDB2552')
      }
      , error=function(e) 
      {
        err <<- TRUE
        df_error$error_flag <- 1
        df_error$error_code <- "E3"
        df_error$error_msg <- "DB Error: Error in connecting to DB"
        df_error <<- cbind(input_json_data,df_error[,!(colnames(df_error) %in% colnames(input_json_data))])
      })
  }
  if(err==TRUE){
    return(df_error)
  }
  ### v.READ DATA FROM ETL #################################
  # 1.FETCH DATA FROM ETL
  # 2.READ LOCAL DEPENDENCY DATA
  ##########################################################################################
  # Fetching data from ETL
  if(ETL_CONNECTION){
    tryCatch(
      {
        #dynamic      
        q = stri_paste( "SELECT * FROM opportunity_with_products_data WHERE OpportunityID_Prod_Identifier =
                        '",input_json_data$account_id_with_18_digit ,"'",collapse="")
        oppy_with_products = dbSendQuery(mydb_abstract_db, q)
        oppy_with_products = fetch(oppy_with_products, n=-1)
        
        #dynamic      
        # live_inv_data = dbSendQuery(mydb_abstract_db,"select * from live_inventory_data")
        q = stri_paste( "SELECT * FROM live_inventory_data WHERE Account_Account_id_with_18_Digit =
                        '",input_json_data$account_id_with_18_digit ,"'",collapse="")
        live_inv_data = dbSendQuery(mydb_abstract_db, q)
        live_inv_data = fetch(live_inv_data, n=-1)
        
        #dynamic     
        # cust_master_data = dbSendQuery(mydb_abstract_db, "select * from customer_data")
        q = stri_paste( "SELECT * FROM customer_data WHERE Account_id_with_18_Digit = 
                        '",input_json_data$account_id_with_18_digit ,"'",collapse="")
        cust_master_data = dbSendQuery(mydb_abstract_db, q)
        cust_master_data = fetch(cust_master_data, n=-1)
        
        #dynamic    
        # rate_card = dbSendQuery(mydb_abstract_db,"select * from 20181024_ILL_rate_card")
        q = stri_paste( "SELECT * FROM 20181024_ILL_rate_card WHERE Account_id_with_18_Digit =
                        '",input_json_data$account_id_with_18_digit ,"'",collapse="")
        
        rate_card = dbSendQuery(mydb_abstract_db, q)
        rate_card = fetch(rate_card, n=-1)
        # 
        # price_book = dbSendQuery(mydb_abstract_db,
        #                          "select * from ILL_Price_book")
        price_book = dbSendQuery(mydb_abstract_db,
                                 "select * from ILL_Price_book")
        price_book = fetch(price_book, n=-1)
        
        CPE_data = dbSendQuery(mydb_abstract_db,
                               "select * from CPE_Price_book")
        CPE_data = fetch(CPE_data, n=-1)
        
        historical_bm_data = dbSendQuery(mydb_abstract_db,
                                         "select * from Historic_Customer_Type_Upd_ILL")
        historical_bm_data = fetch(historical_bm_data, n=-1)
        
        le_to_rcid = dbSendQuery(mydb_abstract_db,
                                 "select * from ILL_AccountID_CUID_RCID")
        le_to_rcid = fetch(le_to_rcid, n=-1)
        
        if(tolower(bm_data$quotetype_partner[1]) == 'sell through' | tolower(bm_data$quotetype_partner[1]) == 'sell with'){
          #sell with
          partner_commission_profile = dbSendQuery(mydb_abstract_db,
                                                   "select Partner_Level, Profile, Commission  from Partner_CommissionProfile_Mapping")
          partner_commission_profile = fetch(partner_commission_profile, n=-1)
          
          if(tolower(bm_data$quotetype_partner[1]) != 'sell with'){
            partner_discount = dbSendQuery(mydb_abstract_db,
                                           'select Profile, Product_Type, Dis_Port_ARC, Dis_Port_NRC, Dis_Port_Backup_ARC, Dis_Port_Backup_NRC, Dis_MAN_NRC, Dis_MAN_ARC, Dis_UBR_PMP_NRC, Dis_UBR_PMP_ARC, Dis_P2P_ARC, Dis_P2P_NRC, Dis_CPE_Install_NRC, Dis_CPE_Outright_NRC, Dis_CPE_Rental_ARC, Dis_Management_ARC, Dis_Additional_IP_ARC, Region
                                           from Partner_SellThrough_Discount')
            partner_discount = fetch(partner_discount, n=-1)
            
            partner_inc_discount = dbSendQuery(mydb_abstract_db,
                                               'select * from Partner_SellThrough_Incremental_Discount')
            partner_inc_discount = fetch(partner_inc_discount, n=-1)
            
            partner_max_discount = dbSendQuery(mydb_abstract_db,
                                               'select * from Partner_SellThrough_Max_Discount')
            partner_max_discount = fetch(partner_max_discount, n=-1)
          }else{
            partner_commision = dbSendQuery(mydb_abstract_db,
                                            'select * from Partner_SellWith_Commission')
            partner_commision = fetch(partner_commision, n=-1)
          }
        }
      }
      , error=function(e)
      {
        err <<- TRUE
        df_error$error_flag <- 1
        df_error$error_code <- "E6"
        df_error$error_msg <- "DB Error: Error in querying the DB Tables"
        df_error <<- cbind(input_json_data,df_error[,!(colnames(df_error) %in% colnames(input_json_data))])
      })
  }else{
    load(paste0("oppy_with_products.rda"))
    load(paste0("live_inv_data.rda"))
    load(paste0("cust_master_data.rda"))
    load("historical_bm_data.rda")
    load("CPE_data.rda")
    load("price_book.rda")
    load("rate_card.rda")
  }
  if(err==TRUE){
    return(df_error)
  }
  time1 <- Sys.time()
  
  #2. Read Dependencies
  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  # 1. Import - CPE Node Predictions
  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  tryCatch(
    {
      load(ILL_CPE_Discount_Rates)
    }
    , error = function(e){
      err <<- TRUE
      df_error$error_flag <- 1
      df_error$error_code <- "E12"
      df_error$error_msg <- "Load Error: Error in loading CPE Discount"
      df_error <<- cbind(input_json_data,df_error[,!(colnames(df_error) %in% colnames(input_json_data))])
    })
  
  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  # 2. Import - Port Price adjustment factor
  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  tryCatch(
    {
      load(adjustment_data_name)
    }
    , error = function(e){
      err <<- TRUE
      df_error$error_flag <- 1
      df_error$error_code <- "E13"
      df_error$error_msg <- "Load Error: Error in loading CPE Discount"
      df_error <<- cbind(input_json_data,df_error[,!(colnames(df_error) %in% colnames(input_json_data))])
    })
  
  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  # 3. Import - Prediction Model Object & Sample Data
  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  tryCatch(
    {
      load(ILL_model_object_name)
      
    }
    , error = function(e){
      err <<- TRUE
      df_error$error_flag <- 1
      df_error$error_code <- "E4"
      df_error$error_msg <- "Load Error: Error in loading the Model Object"
      df_error <<- cbind(input_json_data,df_error[,!(colnames(df_error) %in% colnames(input_json_data))])
    })
  
  tryCatch(
    {
      load(Train_data_sample_name)
      
    }
    , error = function(e){
      err <<- TRUE
      df_error$error_flag <- 1
      df_error$error_code <- "E5"
      df_error$error_msg <- "Load Error: Error in loading the Training Object"
      df_error <<- cbind(input_json_data,df_error[,!(colnames(df_error) %in% colnames(input_json_data))])
    }
  )
  
  if(err==TRUE){
    return(df_error)
  }
  
  ##########################################################################################
  # IV. PREDICT PORT PRICE	
  # 1. Check rate-card availabilty & pick all prince point available
  # 2. Run pricing engine for pricing port
  ########################################################################################
  cols_required <- which(!names(price_book) %in% ETL_col_names)
  price_book <- price_book[,cols_required]
  
  cols_required <- which(!names(cust_master_data) %in% ETL_col_names)
  cust_master_data <- cust_master_data[,cols_required]
  
  PMT <- function (rate, nper, pv)
  {
    stopifnot(rate > 0, rate < 1, nper >= 1, pv > 0)
    return(round(-pv * rate/(1 - 1/(1 + rate)^nper), 2))
  }
  
  #*********************************************************************
  # Function to obtain historic records
  #*********************************************************************
  
  last_bm_price_func <- function(accid,
                                 bw,
                                 create_date,
                                 connection_type,
                                 bm_overall_data_n) {
    
    # create_date must be in yyyy-mm-dd format
    accid = as.character(accid)
    bw = as.numeric(bw)
    create_date = as.Date(create_date)
    # Initialization:
    port_lm_arc = 0
    hist_flag = 0
    
    # Calculate average historc price
    avg_price_bw = mean(bm_overall_data_n$Historic_Port_LM_ARC[which(bm_overall_data_n$BW_mbps_upd==bw & 
                                                                       bm_overall_data_n$connection_type == connection_type &
                                                                       bm_overall_data_n$Account_id_with_18_Digit == accid)])
    # Filtering for the required case
    bm_overall_data_n = bm_overall_data_n[which(bm_overall_data_n$Account_id_with_18_Digit == accid &
                                                  bm_overall_data_n$BW_mbps_upd == bw &
                                                  bm_overall_data_n$connection_type == connection_type &
                                                  bm_overall_data_n$createdDate_quote < create_date),]
    
    if (nrow(bm_overall_data_n) > 0) {
      bm_overall_data_n <- dplyr::arrange(bm_overall_data_n,
                                          desc(createdDate_quote))
      
      port_lm_arc = bm_overall_data_n$Historic_Port_LM_ARC[1]
      if(port_lm_arc < 0.9*avg_price_bw){
        port_lm_arc = 0.9*avg_price_bw
      }
      
      hist_flag = 1
      
    } else {
      port_lm_arc = 0
      hist_flag = 0
    }
    
    return( c("port_lm_arc" = port_lm_arc,
              "hist_flag" = hist_flag
    ))
    
  }
  
  # Converting to required data-type
  bm_data$createdDate_quote <- as.Date(bm_data$Last_Modified_Date)
  bm_data$BW_mbps_upd <- as.numeric(bm_data$BW_mbps_upd)
  bm_data$Burstable_BW <- as.numeric(bm_data$Burstable_BW)
  bm_data$opportunityTerm <- as.numeric(bm_data$opportunityTerm)
  bm_data$adjusted_opportunityTerm <- ifelse(bm_data$opportunityTerm==18, 24, bm_data$opportunityTerm)
  #bm_data$Bucket_Adjustment_Type <- "No Change"
  bm_data$CPE_Pricing_Req <- 1
  bm_data$additional_IP_ARC <- ifelse(tolower(bm_data$additional_ip_flag)=="yes",
                                      ifelse(tolower(bm_data$ip_address_arrangement)=="ipv4",
                                             ifelse(bm_data$ipv4_address_pool_size==0,
                                                    as.numeric(bm_data$no_of_additional_ip)*4500,
                                                    2^(32-as.numeric(bm_data$ipv4_address_pool_size)) * 4500),
                                             0),
                                      0)
  bm_data$additional_IP_MRC <- bm_data$additional_IP_ARC/12
  
  tryCatch(
    {
      historcal_prices_matrix <- apply(bm_data, 1, function(x) last_bm_price_func(
        x["Account_id_with_18_Digit"],
        x["BW_mbps_upd"],
        x["Last_Modified_Date"],
        x["connection_type"],
        historical_bm_data))
      
      # Check if Historical Pricing Available
      bm_data$port_lm_arc <- ifelse( bm_data$Orch_Connection=="Wireline" & bm_data$Orch_LM_Type=="Onnet",
                                     as.numeric(historcal_prices_matrix[1,]),0)
      bm_data$hist_flag <- ifelse( bm_data$Orch_Connection=="Wireline" & bm_data$Orch_LM_Type=="Onnet",
                                   as.numeric(historcal_prices_matrix[2,]),0)
    },
    error=function(e){
      err <<- TRUE
      df_error$error_flag <- 1
      df_error$error_code <- "E15"
      df_error$error_msg <- "Model Error: Error in calculating Historical price"
      df_error <<- cbind(input_json_data,df_error[,!(colnames(df_error) %in% colnames(input_json_data))])
    }
  )
  if(err==TRUE){
    return(df_error)
  }
  
  #bm_data$createdDate_quote <- "2017-01-01"
  
  # Check rate-card eligibility using account ID & Onnet LM
  if(nrow(rate_card)){
    bm_data_rate_card <- bm_data[(bm_data$Account_id_with_18_Digit %in% rate_card$Account_id_with_18_Digit
                                  & bm_data$Orch_LM_Type=="Onnet"),]
    bm_data_non_rate_card <- bm_data[!(bm_data$Account_id_with_18_Digit %in% rate_card$Account_id_with_18_Digit 
                                       & bm_data$Orch_LM_Type=="Onnet"),]
  }else{
    bm_data_non_rate_card <- bm_data
    bm_data_rate_card <- bm_data[0,]
  }
  
  if(nrow(bm_data_rate_card)){
    
    # Check rate-card eligibility using account ID & Legal-Entity
    le_to_rcid <- select(le_to_rcid,
                         "Account_id_with_18_Digit",
                         "cu_le_id",
                         "RC_ID")
    le_to_rcid <- le_to_rcid[which(le_to_rcid$cu_le_id!=""),]
    bm_data = merge(bm_data,
                    le_to_rcid,
                    by = c("Account_id_with_18_Digit","cu_le_id"),
                    all.x = T)
    bm_data$RC_ID <- ifelse(is.na(bm_data$RC_ID),
                            "RC1",
                            bm_data$RC_ID)
    #Validity_Period <- rate_card$validity[which(rate_card$Account_id_with_18_Digit==bm_data$Account_id_with_18_Digit[1])][1]
    Validity_Period <- as.Date("2099-03-31")
    rate_card_connection_type <- rate_card$IASFlavourVal[which(rate_card$Account_id_with_18_Digit==bm_data$Account_id_with_18_Digit[1])]
    
    if(nrow(rate_card) >0 ){  
      bm_data_rate_card <- dplyr::filter(bm_data,
                                         (Account_id_with_18_Digit %in% rate_card$Account_id_with_18_Digit) & 
                                           #(tolower(bm_data$backup_port_requested)=="no") &
                                           RC_ID != "NoRC" &
                                           (as.Date(bm_data$createdDate_quote) <= as.Date(Validity_Period))&
                                           (bm_data$connection_type %in% rate_card_connection_type[1]))
    }
    bm_data_non_rate_card <- dplyr::filter(bm_data,
                                           RC_ID == "NoRC"|
                                             #(tolower(bm_data$backup_port_requested) == "yes")|
                                             (Account_id_with_18_Digit %in% rate_card$Account_id_with_18_Digit) &
                                             (as.Date(bm_data$createdDate_quote) > as.Date(Validity_Period)) |
                                             !(bm_data$connection_type %in% rate_card_connection_type[1]))
  }
  #++++++++++++++++++++++++++++++++++++++++++++++++
  #
  # Check Rate Card Availability
  #
  #++++++++++++++++++++++++++++++++++++++++++++++++
  tryCatch(
    {
      if(nrow(bm_data_rate_card)){
        col_to_rem = c('PortSpeedMaxVal','PortTypeVal','Location','LastMileType','validity','orderType')
        cols_required <- which(!names(rate_card) %in% c(ETL_col_names,col_to_rem))
        rate_card <- rate_card[,cols_required]
        #bm_data <- bm_data_rate_card
        #1. Pick all prince point available in rate-card
        #rate_card = rate_card[rate_card$Account_id_with_18_Digit == bm_data_rate_card$Account_id_with_18_Digit[1],]# Assuming only one account ID        names()
        rate_card <- rate_card[which(rate_card$Account_id_with_18_Digit==bm_data$Account_id_with_18_Digit
                                     & rate_card$RC_ID==bm_data_rate_card$RC_ID),]
        bm_data_rate_card <- merge(bm_data_rate_card,
                                   rate_card,
                                   by.x = c("Account_id_with_18_Digit","BW_mbps_upd"),
                                   by.y = c("Account_id_with_18_Digit","PortSpeedMinVal"),
                                   all.x = TRUE)
        # bm_data_rate_card <- bm_data_rate_card[which(bm_data_rate_card$PortSpeedMinVal == bm_data_rate_card$BW_mbps_upd),]
        bm_data_rate_card$ILL_Port_ARC <- as.numeric(bm_data_rate_card$portChargesARC)
        bm_data_rate_card$ILL_Port_NRC <- as.numeric(bm_data_rate_card$portChargesOTC)
        # bm_data_rate_card$Last_Mile_Cost_ARC <- 0
        
        
        bm_data_rate_card$predicted_net_price <- 0
        bm_data_rate_card$predicted_ILL_Port_ARC <- 0
        bm_data_rate_card$predicted_ILL_Port_NRC <- 0
        # bm_data_rate_card$additional_IP_ARC <- ifelse(bm_data_rate_card$additional_IP_ARC==0,
        #                                               bm_data_rate_card$additional_IP_ARC,
        #                                               ifelse(tolower(bm_data_rate_card$AdditionalIPNegotiated) == "yes",
        #                                                      2^(32-as.numeric(bm_data$ipv4_address_pool_size)) * bm_data_rate_card$ChargePerAdditionalIP,
        #                                                      bm_data_rate_card$additional_IP_ARC))
        # bm_data_rate_card$additional_IP_MRC <- bm_data_rate_card$additional_IP_ARC/12
        # bm_data_rate_card$lm_nrc_mast_onrf <- as.numeric(bm_data_rate_card$lm_nrc_mast_onrf)
        # bm_data_rate_card$lm_nrc_mast_onrf <- ifelse(bm_data_rate_card$lm_nrc_mast_onrf>0,
        #                                              ifelse((bm_data_rate_card$lm_nrc_mast_onrf/MAST_HEIGHT_PER_METER_COST)>as.numeric(bm_data_rate_card$MastHeightIncludedInARC),
        #                                                     bm_data_rate_card$lm_nrc_mast_onrf,
        #                                                     0),
        #                                              0)
        # bm_data_rate_card$ILL_LM_ARC <- bm_data_rate_card$Last_Mile_Cost_ARC
        # bm_data_rate_card$ILL_LM_NRC <- bm_data_rate_card$Last_Mile_Cost_NRC
        
        intermediate_BW_request <- bm_data_rate_card[which(is.na(bm_data_rate_card$ILL_Port_ARC)),]
        pricebook_BW_request <- bm_data_rate_card[which(!is.na(bm_data_rate_card$ILL_Port_ARC)),]
        
        ## only rate card     
        price_interpolation <- function(BW_requested)
        {
          p1 <- rate_card[tail(which(rate_card$PortSpeedMinVal<as.numeric(BW_requested)),1),]
          p2 <- rate_card[head(which(rate_card$PortSpeedMinVal>as.numeric(BW_requested)),1),]
          if(nrow(p1) & nrow(p2)){
            ILL_ARC_per_mb <- (p2$portChargesARC - p1$portChargesARC)/(p2$PortSpeedMinVal - p1$PortSpeedMinVal)
            portChargesARC <- p1$portChargesARC + ILL_ARC_per_mb*(as.numeric(BW_requested) - p1$PortSpeedMinVal)
            portChargesNRC <- p1$portChargesOTC
            AdditionalIPNegotiated <- p1$AdditionalIPNegotiated
            ChargePerAdditionalIP <- p1$ChargePerAdditionalIP
            MastHeightIncludedInARC <- p1$MastHeightIncludedInARC
            lastMileIncluded <- p1$lastMileIncluded
            cpeIncluded <- p1$cpeIncluded
            CPE_Provided_by <- p1$CPE_Provided_by
            CPE_OTC <- p1$CPE_OTC
            CPE_ARC <- p1$CPE_ARC
            CPE_Management <- p1$CPE_Management
            CPE_Basic_Chassis <- p1$CPE_Basic_Chassis
            CPE_support_Type <- p1$CPE_support_Type
            opptyTerm <- p1$opptyTerm
          }else{
            portChargesARC <- ifelse(nrow(p1),
                                     p1$portChargesARC/p1$PortSpeedMinVal*as.numeric(BW_requested),
                                     p2$portChargesARC/p2$PortSpeedMinVal*as.numeric(BW_requested))
            portChargesNRC <- ifelse(nrow(p1),
                                     p1$portChargesOTC/p1$PortSpeedMinVal*as.numeric(BW_requested),
                                     p2$portChargesOTC/p2$PortSpeedMinVal*as.numeric(BW_requested))
            AdditionalIPNegotiated <- ifelse(nrow(p1),
                                             p1$AdditionalIPNegotiated,
                                             p2$AdditionalIPNegotiated)
            ChargePerAdditionalIP <- ifelse(nrow(p1),
                                            p1$ChargePerAdditionalIP,
                                            p2$ChargePerAdditionalIP)
            MastHeightIncludedInARC <- ifelse(nrow(p1),
                                              p1$MastHeightIncludedInARC,
                                              p2$MastHeightIncludedInARC)
            lastMileIncluded <- ifelse(nrow(p1),
                                       p1$lastMileIncluded,
                                       p2$lastMileIncluded)
            cpeIncluded <- ifelse(nrow(p1),p1$cpeIncluded, p2$cpeIncluded)
            CPE_Provided_by <- ifelse(nrow(p1),p1$CPE_Provided_by, p2$CPE_Provided_by)
            CPE_OTC <- ifelse(nrow(p1),p1$CPE_OTC, p2$CPE_OTC)
            CPE_ARC <- ifelse(nrow(p1),p1$CPE_ARC, p2$CPE_ARC)
            CPE_Management <- ifelse(nrow(p1),p1$CPE_Management, p2$CPE_Management)
            CPE_Basic_Chassis <- ifelse(nrow(p1),p1$CPE_Basic_Chassis, p2$CPE_Basic_Chassis)
            CPE_support_Type <- ifelse(nrow(p1),p1$CPE_support_Type, p2$CPE_support_Type)
            opptyTerm <- ifelse(nrow(p1),p1$opptyTerm,p2$opptyTerm)
          }
          result = data.frame(portChargesARC, portChargesNRC, AdditionalIPNegotiated, ChargePerAdditionalIP, MastHeightIncludedInARC, lastMileIncluded, cpeIncluded, CPE_Provided_by,
                              CPE_OTC, CPE_ARC, CPE_Management, CPE_Basic_Chassis, CPE_support_Type, opptyTerm) 
          return(result)
          
        }
        
        
        if(nrow(intermediate_BW_request)){
          bm_data_non_rate_card <- rbind(bm_data_non_rate_card,
                                         intermediate_BW_request[intermediate_BW_request$BW_mbps_upd < min(rate_card$PortSpeedMinVal) | 
                                                                   intermediate_BW_request$BW_mbps_upd > max(rate_card$PortSpeedMinVal),which(colnames(intermediate_BW_request) %in% colnames(bm_data_non_rate_card))])
          intermediate_BW_request <- intermediate_BW_request[intermediate_BW_request$BW_mbps_upd >= min(rate_card$PortSpeedMinVal) & intermediate_BW_request$BW_mbps_upd <= max(rate_card$PortSpeedMinVal),]
          if(nrow(intermediate_BW_request)){
            intermediate_BW_request$result <- apply(intermediate_BW_request,
                                                    1,
                                                    function(x) price_interpolation(x["BW_mbps_upd"])) #rate card interpolation is called here
            intermediate_BW_request$ILL_Port_ARC <- unlist(lapply(intermediate_BW_request$result, "[[", 1))
            intermediate_BW_request$ILL_Port_NRC <- unlist(lapply(intermediate_BW_request$result, "[[", 2))
            intermediate_BW_request$AdditionalIPNegotiated <- unlist(lapply(intermediate_BW_request$result, "[[", 3))
            intermediate_BW_request$ChargePerAdditionalIP <- unlist(lapply(intermediate_BW_request$result, "[[", 4))
            intermediate_BW_request$MastHeightIncludedInARC <- unlist(lapply(intermediate_BW_request$result, "[[", 5))
            intermediate_BW_request$lastMileIncluded <- unlist(lapply(intermediate_BW_request$result, "[[", 6))
            intermediate_BW_request$cpeIncluded <- unlist(lapply(intermediate_BW_request$result, "[[", 7))
            intermediate_BW_request$CPE_Provided_by <- unlist(lapply(intermediate_BW_request$result, "[[", 8))
            intermediate_BW_request$CPE_OTC <- unlist(lapply(intermediate_BW_request$result, "[[", 9))
            intermediate_BW_request$CPE_ARC <- unlist(lapply(intermediate_BW_request$result, "[[", 10))
            intermediate_BW_request$CPE_Management <- unlist(lapply(intermediate_BW_request$result, "[[", 11))
            intermediate_BW_request$CPE_Basic_Chassis <- unlist(lapply(intermediate_BW_request$result, "[[", 12))
            intermediate_BW_request$CPE_support_Type <- unlist(lapply(intermediate_BW_request$result, "[[", 13))
            intermediate_BW_request$opptyTerm <- unlist(lapply(intermediate_BW_request$result, "[[", 14))
            intermediate_BW_request$result <- NULL
            
          }
          bm_data_rate_card <- rbind(pricebook_BW_request, intermediate_BW_request)
          bm_data_rate_card$ILL_LM_ARC <- NULL
          bm_data_rate_card$ILL_LM_NRC <-NULL
          bm_data_rate_card$portChargesARC <- NULL
          bm_data_rate_card$portChargesOTC <- NULL 
        }
        bm_data_rate_card$additional_IP_ARC <- ifelse(bm_data_rate_card$additional_IP_ARC==0,
                                                      bm_data_rate_card$additional_IP_ARC,
                                                      ifelse(tolower(bm_data_rate_card$AdditionalIPNegotiated) == "yes",
                                                             2^(32-as.numeric(bm_data$ipv4_address_pool_size)) * bm_data_rate_card$ChargePerAdditionalIP,
                                                             bm_data_rate_card$additional_IP_ARC))
        bm_data_rate_card$additional_IP_MRC <- bm_data_rate_card$additional_IP_ARC/12
        
        bm_data_rate_card$lm_nrc_mast_onrf <- as.numeric(bm_data_rate_card$lm_nrc_mast_onrf)
        bm_data_rate_card$lm_nrc_mast_onrf <- ifelse(bm_data_rate_card$lm_nrc_mast_onrf>0,
                                                     ifelse((bm_data_rate_card$lm_nrc_mast_onrf/MAST_HEIGHT_PER_METER_COST)>as.numeric(bm_data_rate_card$MastHeightIncludedInARC),
                                                            bm_data_rate_card$lm_nrc_mast_onrf,
                                                            0),
                                                     0)
        
        bm_data_rate_card$Last_Mile_Cost_NRC <- ifelse(is.na(bm_data_rate_card$lastMileIncluded),
                                                       bm_data_rate_card$Last_Mile_Cost_NRC,
                                                       ifelse(tolower(bm_data_rate_card$lastMileIncluded) == "yes",
                                                              0,
                                                              bm_data_rate_card$Last_Mile_Cost_NRC))
        #In case LM is included, LM ARC & LM NRC will be 0
        bm_data_rate_card$Last_Mile_Cost_ARC <- ifelse(is.na(bm_data_rate_card$lastMileIncluded),
                                                       bm_data_rate_card$Last_Mile_Cost_ARC,
                                                       ifelse(tolower(bm_data_rate_card$lastMileIncluded) == "yes",
                                                              0,
                                                              bm_data_rate_card$Last_Mile_Cost_ARC))
        
        #Check CPE pricing requirement
        CPE_RC_Validity <- tolower(bm_data_rate_card$CPE_Basic_Chassis) == tolower(bm_data_rate_card$CPE_Variant) &
          tolower(bm_data_rate_card$CPE_management_type) == tolower(bm_data_rate_card$CPE_support_Type) & 
          tolower(bm_data_rate_card$CPE_supply_type) == "rental"
        
        CPE_RC_Validity[is.na(CPE_RC_Validity)] <- 0
        bm_data_rate_card$CPE_Pricing_Req <- !CPE_RC_Validity
        
        bm_data_rate_card$CPE_Management <- ifelse(!bm_data_rate_card$CPE_Pricing_Req,
                                                   ifelse(is.na(bm_data_rate_card$CPE_Management),
                                                          0,
                                                          as.numeric(bm_data_rate_card$CPE_Management)),
                                                   0)
        bm_data_rate_card$Discounted_CPE_ARC <- bm_data_rate_card$CPE_ARC + bm_data_rate_card$CPE_Management
        bm_data_rate_card$Discounted_CPE_NRC <- bm_data_rate_card$CPE_OTC
        bm_data_rate_card$sp_CPE_Management_ARC <- bm_data_rate_card$CPE_Management
        bm_data_rate_card$sp_CPE_Install_NRC <- bm_data_rate_card$CPE_OTC
        bm_data_rate_card$sp_CPE_Rental_ARC <- bm_data_rate_card$CPE_ARC
        bm_data_rate_card$sp_CPE_Outright_NRC <- 0
        #Merge Customer info with request
        bm_data_rate_card<- merge(x = bm_data_rate_card,
                                  y = cust_master_data,
                                  by = "Account_id_with_18_Digit",
                                  all.x = T)
        bm_data_rate_card <- dplyr:: rename(bm_data_rate_card,
                                            Account.RTM_Cust = Account_RTM,
                                            Industry_Cust = Industry,
                                            Segment_Cust = Segment)
        bm_data_rate_card$overall_BW_mbps_upd <- bm_data_rate_card$BW_mbps_upd
        
        bm_data_rate_card$ILL_Port_Adjusted_net_Price <- bm_data_rate_card$ILL_Port_ARC + bm_data_rate_card$ILL_Port_NRC
        bm_data_rate_card$ILL_Port_ARC_Adjusted <- bm_data_rate_card$ILL_Port_ARC
        #Marking-up for lower contract term
        # Additional mutli-year discounting 2 year=5% 3 year=10%
        bm_data_rate_card$ILL_Port_ARC_Adjusted <- ifelse(bm_data_rate_card$adjusted_opportunityTerm >= rate_card$opptyTerm[1],
                                                          bm_data_rate_card$ILL_Port_ARC_Adjusted,
                                                          ifelse((rate_card$opptyTerm[1]-bm_data_rate_card$adjusted_opportunityTerm)==12,
                                                                 bm_data_rate_card$ILL_Port_ARC_Adjusted*1.05,
                                                                 bm_data_rate_card$ILL_Port_ARC_Adjusted*1.10))
        
        bm_data_rate_card$ILL_Port_MRC_Adjusted <- bm_data_rate_card$ILL_Port_ARC/12
        bm_data_rate_card$ILL_Port_NRC_Adjusted <- bm_data_rate_card$ILL_Port_NRC
        
        
        bm_data_rate_card$burst_per_MB_price <- ifelse(bm_data_rate_card$Burstable_BW>0,
                                                       bm_data_rate_card$ILL_Port_ARC_Adjusted/bm_data_rate_card$overall_BW_mbps_upd*1.2,0)
        bm_data_rate_card$ILL_Port_ARC <- NULL
        bm_data_rate_card$ILL_Port_NRC <- NULL
      }
    },
    error=function(e){
      err <<- TRUE
      df_error$error_flag <- 1
      df_error$error_code <- "E16"
      df_error$error_msg <- "Model Error: Error in RateCard Price calculation		"
      df_error <<- cbind(input_json_data,df_error[,!(colnames(df_error) %in% colnames(input_json_data))])
    }
  )
  if(err==TRUE){
    return(df_error)
  }
  
  
  if(nrow(bm_data_non_rate_card)){
    # 2. Run pricing engine for pricing Port
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # User Defined Function
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
    
    #  interpolation function here
    
    
    price_interpolation <- function(BW_requested, price_book_select)
    {
      # View(price_book_select)
      BW_requested = as.numeric( BW_requested)
      p1 <- price_book_select[tail(which(price_book_select$Speed<as.numeric(BW_requested)),1),]
      p2 <- price_book_select[head(which(price_book_select$Speed>as.numeric(BW_requested)),1),]
      if(nrow(p1) & nrow(p2)){
        ILL_ARC_per_mb <- (p2$ILL_ARC - p1$ILL_ARC)/(p2$Speed - p1$Speed)
        p1$ILL_ARC <- p1$ILL_ARC + ILL_ARC_per_mb*(as.numeric(BW_requested) - p1$Speed)
        p1$ILL_NRC <- p1$ILL_NRC
        p1$Speed <- NULL
      }
      # new code here
      if(BW_requested> max(price_book_select$Speed)){
        max_BW = max(price_book_select$Speed)
        max_ARC = max(price_book_select$ILL_ARC)
        ILL_ARC_per_mb =(max_ARC/max_BW) 
        p1$ILL_ARC = ILL_ARC_per_mb* BW_requested
        p1$ILL_NRC <- NA#p1$ILL_NRC
        p1$Speed <- BW_requested
      }
      
      else{
        p1$ILL_ARC <- 0
        p1$ILL_NRC <- 0
        p1$Speed <- NULL
      }
      return(p1)
    }
    
    
    
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Pricebook Lookup
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    bm_data_prm <- bm_data_non_rate_card[bm_data_non_rate_card$connection_type=="Premium",]
    bm_data_std <- bm_data_non_rate_card[bm_data_non_rate_card$connection_type=="Standard",]
    bm_data_shared <- bm_data_non_rate_card[bm_data_non_rate_card$connection_type=="Shared",]
    bm_data_comp_1_2 <- bm_data_non_rate_card[bm_data_non_rate_card$connection_type=="Compressed_1_2",]
    bm_data_comp_1_4 <- bm_data_non_rate_card[bm_data_non_rate_card$connection_type=="Compressed_1_4",]
    
    
    # connection type = standard
    if(nrow(bm_data_std)) {
      pricebook_active_std <- dplyr::select(price_book,
                                            'Speed',
                                            as.character(bm_data_std$connection_type),
                                            'NRC')
      names(pricebook_active_std) <- c('Speed','ILL_ARC','ILL_NRC') #*** To be removed after pricebooks are available in ETL
      pricebook_active_std <- pricebook_active_std[!is.na(pricebook_active_std$ILL_ARC),]
      pricebook_active_std <- pricebook_active_std[order(pricebook_active_std$Speed),]
      bm_data_std <- merge(x = bm_data_std,
                           y = pricebook_active_std,
                           by.x = "BW_mbps_upd",
                           by.y = "Speed",
                           all.x = T)
      
      # print(bm_data_std$ILL_ARC)
      intermediate_BW_request <- bm_data_std[which(is.na(bm_data_std$ILL_ARC)),]
      pricebook_BW_request <- bm_data_std[which(!is.na(bm_data_std$ILL_ARC)),]
      
      ## if BW is not in the pricebook
      if(nrow(intermediate_BW_request)){
        # print('here')
        intermediate_BW_request$result <- apply(intermediate_BW_request,
                                                1,
                                                function(x) price_interpolation(x["BW_mbps_upd"], pricebook_active_std))
        
        intermediate_BW_request$ILL_ARC <- unlist(lapply(intermediate_BW_request$result, "[[", 2))
        intermediate_BW_request$ILL_NRC <- unlist(lapply(intermediate_BW_request$result, "[[", 3))
        intermediate_BW_request$result <- NULL
        
        bm_data_std <- rbind(pricebook_BW_request, intermediate_BW_request)
        #bm_data_non_rate_card$ILL_NRC <- 0
      }  
    }
    
    
    # connection type = premium 
    if(nrow(bm_data_prm)) {
      pricebook_active_prm <- dplyr::select(price_book,
                                            'Speed',
                                            as.character(bm_data_prm$connection_type),
                                            'NRC')
      names(pricebook_active_prm) <- c('Speed','ILL_ARC','ILL_NRC') #*** To be removed after pricebooks are available in ETL
      pricebook_active_prm <- pricebook_active_prm[!is.na(pricebook_active_prm$ILL_ARC),]
      pricebook_active_prm <- pricebook_active_prm[order(pricebook_active_prm$Speed),]
      bm_data_prm <- merge(x = bm_data_prm,
                           y = pricebook_active_prm,
                           by.x = "BW_mbps_upd",
                           by.y = "Speed",
                           all.x = T)
      
      intermediate_BW_request <- bm_data_prm[which(is.na(bm_data_prm$ILL_ARC)),]
      pricebook_BW_request <- bm_data_prm[which(!is.na(bm_data_prm$ILL_ARC)),]
      
      
      ## if BW not in pricebook  
      if(nrow(intermediate_BW_request)){
        intermediate_BW_request$result <- apply(intermediate_BW_request,
                                                1,
                                                function(x) price_interpolation(x["BW_mbps_upd"], pricebook_active_prm))
        intermediate_BW_request$ILL_ARC <- unlist(lapply(intermediate_BW_request$result, "[[", 2))
        intermediate_BW_request$ILL_NRC <- unlist(lapply(intermediate_BW_request$result, "[[", 3))
        intermediate_BW_request$result <- NULL
        
        bm_data_prm <- rbind(pricebook_BW_request, intermediate_BW_request)
        #bm_data_non_rate_card$ILL_NRC <- 0
      }  
    }
    
    
    # connection type = compression_1_2
    if(nrow(bm_data_comp_1_2)) {
      pricebook_active_comp_1_2 <- dplyr::select(price_book,
                                                 'Speed',
                                                 as.character(bm_data_comp_1_2$connection_type),
                                                 'NRC')
      names(pricebook_active_comp_1_2) <- c('Speed','ILL_ARC','ILL_NRC') #*** To be removed after pricebooks are available in ETL
      pricebook_active_comp_1_2 <- pricebook_active_comp_1_2[!is.na(pricebook_active_comp_1_2$ILL_ARC),]
      pricebook_active_comp_1_2 <- pricebook_active_comp_1_2[order(pricebook_active_comp_1_2$Speed),]
      bm_data_comp_1_2 <- merge(x = bm_data_comp_1_2,
                                y = pricebook_active_comp_1_2,
                                by.x = "BW_mbps_upd",
                                by.y = "Speed",
                                all.x = T)
      
      intermediate_BW_request <- bm_data_comp_1_2[which(is.na(bm_data_comp_1_2$ILL_ARC)),]
      pricebook_BW_request <- bm_data_comp_1_2[which(!is.na(bm_data_comp_1_2$ILL_ARC)),]
      
      
      ## if BW not in pricebook
      
      if(nrow(intermediate_BW_request)){
        intermediate_BW_request$result <- apply(intermediate_BW_request,
                                                1,
                                                function(x) price_interpolation(x["BW_mbps_upd"],
                                                                                pricebook_active_comp_1_2))
        intermediate_BW_request$ILL_ARC <- unlist(lapply(intermediate_BW_request$result, "[[", 2))
        intermediate_BW_request$ILL_NRC <- unlist(lapply(intermediate_BW_request$result, "[[", 3))
        intermediate_BW_request$result <- NULL
        
        bm_data_comp_1_2 <- rbind(pricebook_BW_request, intermediate_BW_request)
        #bm_data_non_rate_card$ILL_NRC <- 0
      }  
    }
    
    
    # connection type = compression_1_4
    if(nrow(bm_data_comp_1_4)) {
      pricebook_active_comp_1_4 <- dplyr::select(price_book,
                                                 'Speed',
                                                 as.character(bm_data_comp_1_4$connection_type),
                                                 'NRC')
      names(pricebook_active_comp_1_4) <- c('Speed','ILL_ARC','ILL_NRC') #*** To be removed after pricebooks are available in ETL
      pricebook_active_comp_1_4 <- pricebook_active_comp_1_4[!is.na(pricebook_active_comp_1_4$ILL_ARC),]
      pricebook_active_comp_1_4 <- pricebook_active_comp_1_4[order(pricebook_active_comp_1_4$Speed),]
      bm_data_comp_1_4 <- merge(x = bm_data_comp_1_4,
                                y = pricebook_active_comp_1_4,
                                by.x = "BW_mbps_upd",
                                by.y = "Speed",
                                all.x = T)
      
      intermediate_BW_request <- bm_data_comp_1_4[which(is.na(bm_data_comp_1_4$ILL_ARC)),]
      pricebook_BW_request <- bm_data_comp_1_4[which(!is.na(bm_data_comp_1_4$ILL_ARC)),]
      
      
      ##  if BW not in pricebook
      if(nrow(intermediate_BW_request)){
        intermediate_BW_request$result <- apply(intermediate_BW_request,
                                                1,
                                                function(x) price_interpolation(x["BW_mbps_upd"],
                                                                                pricebook_active_comp_1_4))
        intermediate_BW_request$ILL_ARC <- unlist(lapply(intermediate_BW_request$result, "[[", 2))
        intermediate_BW_request$ILL_NRC <- unlist(lapply(intermediate_BW_request$result, "[[", 3))
        intermediate_BW_request$result <- NULL
        
        bm_data_comp_1_4 <- rbind(pricebook_BW_request, intermediate_BW_request)
        #bm_data_non_rate_card$ILL_NRC <- 0
      }  
    }
    
    
    bm_data_non_rate_card <- rbind(bm_data_std, bm_data_prm, bm_data_comp_1_2, bm_data_comp_1_4)
    
    # active , passive, historical check here    
    #Seprate into active & passive topology request & hisorical
    bm_data_historical_price <- dplyr::filter(bm_data_non_rate_card, hist_flag ==1)
    bm_data_active <- dplyr::filter(bm_data_non_rate_card, topology != "secondary_passive" & hist_flag ==0)
    bm_data_passive <- dplyr::filter(bm_data_non_rate_card, topology == "secondary_passive" & hist_flag == 0)
    
    if(nrow(bm_data_historical_price)){
      bm_data_historical_price$ILL_Port_ARC_Adjusted <- bm_data_historical_price$port_lm_arc
      
      bm_data_historical_price$ILL_Port_NRC_Adjusted <- ifelse(bm_data_historical_price$BW_mbps_upd<=100,
                                                               PORT_NRC_CHARGE_1_TO_100MB,
                                                               ifelse(bm_data_historical_price$BW_mbps_upd<=300,
                                                                      PORT_NRC_CHARGE_101_TO_300MB,
                                                                      ifelse(bm_data_historical_price$BW_mbps_upd<=1000,
                                                                             PORT_NRC_CHARGE_300_TO_1000MB,
                                                                             PORT_NRC_CHARGE_GT_THAN_1000MB)
                                                               )
      )
      
      bm_data_historical_price$Last_Mile_Cost_ARC <- 0
      
      bm_data_historical_price$port_pred_discount <- 1-bm_data_historical_price$port_lm_arc/(bm_data_historical_price$ILL_ARC + as.numeric(bm_data_historical_price$lm_arc_bw_onwl))
      
      #bm_data_historical_price$Last_Mile_Cost_NRC <- bm_data_historical_price$Last_Mile_Cost_NRC
      
      bm_data_historical_price<- merge(x = bm_data_historical_price,
                                       y = cust_master_data,
                                       by = "Account_id_with_18_Digit",
                                       all.x = T)
      bm_data_historical_price <- dplyr:: rename(bm_data_historical_price,
                                                 Account.RTM_Cust = Account_RTM,
                                                 Industry_Cust = Industry,
                                                 Segment_Cust = Segment)
      bm_data_historical_price$overall_BW_mbps_upd <- bm_data_historical_price$BW_mbps_upd
      bm_data_historical_price$burst_per_MB_price <- ifelse(bm_data_historical_price$Burstable_BW>0,
                                                            bm_data_historical_price$ILL_Port_ARC_Adjusted/bm_data_historical_price$overall_BW_mbps_upd*1.2,
                                                            0)
      
    }
    
    if(nrow(bm_data_active)){ #*** Shall be removed as customer will have min. of one active request
      tryCatch(
        {
          #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
          #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
          # BM data - pre-processing & cleaning
          #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
          #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
          
          # Creating ID
          bm_data_active$OpportunityID_Prod_Identifier <- paste(bm_data_active$Account_id_with_18_Digit, "1", sep = "|")
          
          # Adding date and month
          bm_data_active$opportunity_day <-  1 #Keeping it as one. As price fluctuation are only at month level
          bm_data_active$opportunity_month <- as.numeric(format(bm_data_active$createdDate_quote, "%m"))
          
          #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
          # Processing Live Inventory Data
          #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
          # Extracting required fiels
          cols_required <- which(!names(live_inv_data) %in% ETL_col_names)
          live_inv_data <- live_inv_data[,cols_required]
          
          # Merging Live Inventory Data with active configuration requests
          live_inv_data <- dplyr::rename(live_inv_data,
                                         Account_id_with_18_Digit = Account_Account_id_with_18_Digit)
          bm_data_active <- merge(x = bm_data_active,
                                  y = live_inv_data,
                                  by = "Account_id_with_18_Digit",
                                  all.x = T)
          if(!DEBUG_MODE){
            rm(live_inv_data)
          }else{
            print("The dimension below must have one row (post Live Inv data merge)")
            print(dim(bm_data_active))
          }
          
          #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
          # Processing Opportunity with Products Data
          #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
          # Extracting required fiels
          cols_required <- which(!names(oppy_with_products) %in% ETL_col_names)
          oppy_with_products <- oppy_with_products[,cols_required]
          
          # Merging Opportunity with Products Data with active configuration requests
          oppy_with_products <- dplyr::rename(oppy_with_products,
                                              Account_id_with_18_Digit = OpportunityID_Prod_Identifier)
          bm_data_active<- merge(x = bm_data_active,
                                 y = oppy_with_products,
                                 by = "Account_id_with_18_Digit",
                                 all.x = T)
          if(!DEBUG_MODE){
            rm(oppy_with_products)
          }else{
            print("The dimension below must have one row (post opportunity with products data merge)")
            print(dim(bm_data_active))
          }
          
          #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
          # Processing Customer Master Data
          #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
          # Extracting required fiels
          # cols_required <- which(!names(cust_master_data) %in% ETL_col_names)
          # cust_master_data <- cust_master_data[,cols_required]
          bm_data_active<- merge(x = bm_data_active,
                                 y = cust_master_data,
                                 by = "Account_id_with_18_Digit",
                                 all.x = T)
          if(!DEBUG_MODE){
            rm(cust_master_data)
          }else{
            print("The dimension below must have one row (post customer master data merge)")
            print(dim(bm_data_active))
          }
          
          #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
          # Missing value treatment
          #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
          bm_data_numeric <- bm_data_active[sapply(bm_data_active, function(x) is.numeric(x))]
          bm_data_numeric[is.na(bm_data_numeric)] <- 0
          
          bm_data_non_numeric <- bm_data_active[sapply(bm_data_active, function(x) !is.numeric(x))]
          bm_data_active <- cbind(bm_data_numeric,bm_data_non_numeric)
          #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
          # Additional Features Creation
          #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
          modified_date <- as.Date(bm_data_active$Last_Modified_Date)
          # Changing date to the first day of the month, to ensure pricing change reflects with
          #the changing month: Shalini
          
          day(modified_date) <- 1
          
          bm_data_active$datediff <-  difftime(modified_date,
                                               as.Date("2016-10-01") , units = c("days"))
          
          bm_data_active$calc_arc_list_inr <- bm_data_active$ILL_ARC
          bm_data_active$list_price_mb <- bm_data_active$calc_arc_list_inr/ bm_data_active$BW_mbps_upd
          bm_data_active$list_price_mb_dummy <- ifelse(bm_data_active$list_price_mb >=237672.18 & bm_data_active$list_price_mb <= 271253.65,1,0)
          bm_data_active$log_Inv_Tot_BW <- log(bm_data_active$Inv_Tot_BW)
          bm_data_active$log_Inv_Tot_BW_dummy <- ifelse(bm_data_active$log_Inv_Tot_BW >=5.12 & bm_data_active$log_Inv_Tot_BW <= 5.14,1,0)
          bm_data_active$log_Inv_Tot_BW <- ifelse(is.infinite(bm_data_active$log_Inv_Tot_BW)==T,0,bm_data_active$log_Inv_Tot_BW)
          
          
          #Renaming some variables
          bm_data_active$overall_BW_mbps_upd = bm_data_active$BW_mbps_upd
          # Add part for add & removing some features: Shalini
          bm_data_active$num_products_opp_new.x <- 0 #Training data has all 0 zero. Model retraining this feature shouldnt be considered- Shalini
          bm_data_active$sum_product_flavours.x <- bm_data_active$sum_no_of_sites_uni_len # To be confirmed
          bm_data_active$tot_oppy_current_prod.x <- 1 # Assumtion take is request will be for single product
          bm_data_active$overall_PortType <- "Fixed" # Discount to be predicted for fixed BW only
        },
        error=function(e){
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
      
      tryCatch(
        {
          #######################################################################
          # Predict Discount Percent
          #######################################################################
          
          train_data_sample$Discount_Overall <- NULL
          train_data_sample$Identifier <- "TRAIN"
          
          bm_data_active$Identifier <- "VALIDATION"
          bm_data_active <- dplyr:: rename(bm_data_active,
                                           Account.RTM_Cust = Account_RTM,
                                           Industry_Cust = Industry,
                                           Segment_Cust = Segment
          )
          
          bm_data_active_scoring <- bm_data_active[, which(names(bm_data_active) %in% names(train_data_sample))]
          #-----------------------------------------------------------
          # Handling new levels
          levels_Industry_Cust <- levels(train_data_sample$Industry_Cust)
          levels_Segment_Cust <- levels(train_data_sample$Segment_Cust)
          levels_Account_RTM <- levels(train_data_sample$Account.RTM_Cust)
          
          match_level_found <- agrep(bm_data_active_scoring$Industry_Cust,
                                     levels_Industry_Cust, max = 0.2)[1]
          bm_data_active_scoring$Industry_Cust<- ifelse(!is.na(match_level_found),
                                                        levels_Industry_Cust[match_level_found],
                                                        "OTHERS")
          match_level_found <- agrep(bm_data_active_scoring$Segment_Cust,
                                     levels_Segment_Cust, max = 0.2)[1]
          bm_data_active_scoring$Segment_Cust <- ifelse(!is.na(match_level_found),
                                                        levels_Segment_Cust[match_level_found],
                                                        "Others")
          match_level_found <- agrep(bm_data_active_scoring$Account.RTM_Cust,
                                     levels_Account_RTM, max = 0.2)[1]
          bm_data_active_scoring$Account.RTM_Cust <- ifelse(!is.na(match_level_found),
                                                            levels_Account_RTM[match_level_found],
                                                            "Direct")
          #-----------------------------------------------------------
          
          bm_data_active_scoring <- rbind(train_data_sample,
                                          bm_data_active_scoring)
          bm_data_active_scoring <- bm_data_active_scoring[which(bm_data_active_scoring$Identifier == "VALIDATION"),]
          bm_data_active_scoring$opportunityTerm <- 12 # Running model for 1 year opp. term
          # Additional discounts will be applied later
          
          bm_data_active$port_pred_discount = predict(rf_model, newdata = bm_data_active_scoring)
          
          # Calculating net price and net price error
          bm_data_active$predicted_ILL_Port_ARC <- bm_data_active$ILL_ARC*(1-bm_data_active$port_pred_discount)
          bm_data_active$predicted_ILL_Port_NRC <- bm_data_active$ILL_NRC*(1-bm_data_active$port_pred_discount)
          bm_data_active$predicted_net_price <- bm_data_active$predicted_ILL_Port_ARC + bm_data_active$predicted_ILL_Port_NRC
        },
        error=function(e){
          err <<- TRUE
          df_error$error_flag <- 1
          df_error$error_code <- "E8"
          df_error$error_msg <- "Error while scoring due to New Levels introduced in the input"
          df_error <<- cbind(input_json_data,df_error[,!(colnames(df_error) %in% colnames(input_json_data))])
        }
      )
      if(err==TRUE){
        return(df_error)
      }
      
      tryCatch(
        {
          #######################################################################
          # Price Adjustment: Error Profiling
          #######################################################################
          
          bm_data_active$Segment_Cust <- as.character(bm_data_active$Segment_Cust)
          bm_data_active$Segment_Cust <- ifelse(bm_data_active$Segment_Cust %in% c("Enterprise",
                                                                                   "MES",
                                                                                   "Service Provider"),
                                                bm_data_active$Segment_Cust,"Others")
          bm_data_active <- bm_data_active %>%
            mutate(
              #Node 1 pred >=0.59 & pred <0.83  Inv_Tot_BW >=0 & Inv_Tot_BW  < 15
              node_1 = ifelse(port_pred_discount <0.83 & Inv_Tot_BW >=0 & Inv_Tot_BW  < 15, 1, 0),
              
              # Node 2     pred >=0.59 & pred <0.83             Inv_Tot_BW>=15  & Inv_Tot_BW< 540.58
              node_2 = ifelse(port_pred_discount <0.83 & Inv_Tot_BW>=15 & Inv_Tot_BW< 540.58, 1, 0),
              
              # Node 3     port_pred_discount >=0.59 & port_pred_discount <0.83 Inv_Tot_BW>=540.58  & Inv_Tot_BW<=43001.43
              node_3 =    ifelse(port_pred_discount <0.83 & Inv_Tot_BW>=540.58 , 1, 0),
              
              # Node 4     port_pred_discount >=0.83 & port_pred_discount <0.86  overall_BW_mbps_upd >=2  & overall_BW_mbps_upd <5
              node_4 = ifelse(port_pred_discount >=0.83 & port_pred_discount <0.86 & overall_BW_mbps_upd <5,1,0),
              
              # Node 5     port_pred_discount >=0.83 & port_pred_discount <0.86               
              node_5 = ifelse(port_pred_discount >=0.83 & port_pred_discount <0.86,1,0),
              
              # Node 6     port_pred_discount >=0.86 & port_pred_discount <0.88 Inv_Tot_BW >= 0 &Inv_Tot_BW <0.26
              node_6 = ifelse(port_pred_discount >=0.86 & port_pred_discount <0.88 & Inv_Tot_BW >= 0 & Inv_Tot_BW <0.26,1,0),
              
              # Node 7     port_pred_discount >=0.86 & port_pred_discount <0.88               Inv_Tot_BW >= 1 &Inv_Tot_BW <43001.42
              node_7 = ifelse(port_pred_discount >=0.86 & port_pred_discount <0.88 ,1,0),
              
              # Node 8     port_pred_discount >=0.88 & port_pred_discount <0.90               Sum_New_ARC_Converted >=0 & Sum_New_ARC_Converted<11532.31
              node_8 = ifelse(port_pred_discount >=0.88 & port_pred_discount <0.90 &
                                Sum_New_ARC_Converted >=0 & Sum_New_ARC_Converted<11532.31,1,0),
              
              # Node 9     port_pred_discount >=0.86 & port_pred_discount <0.90               Sum_New_ARC_Converted >=11532.31 & Sum_New_ARC_Converted<=187407180.80
              node_9 = ifelse(port_pred_discount >=0.86 & port_pred_discount <0.90 &
                                Sum_New_ARC_Converted >=11532.31 ,1,0),
              
              #Node 12 port_pred_discount >=0.90 & port_pred_discount <0.93  Sum_IAS_FLAG >=0 & Sum_IAS_FLAG <7                Inv_Tot_BW>=0 & Inv_Tot_BW<1
              node_12 = ifelse(port_pred_discount >=0.90 & port_pred_discount <0.93 &
                                 Sum_IAS_FLAG >=0 & Sum_IAS_FLAG <7 &  Inv_Tot_BW>=0 & Inv_Tot_BW<1,1,0),
              
              #Node 13    port_pred_discount >=0.90 & port_pred_discount <0.93               Sum_IAS_FLAG >=0 & Sum_IAS_FLAG <7           Inv_Tot_BW>=1 & Inv_Tot_BW<235.02
              node_13 = ifelse(port_pred_discount >=0.90 & port_pred_discount <0.93 & 
                                 Sum_IAS_FLAG >=0 & Sum_IAS_FLAG <7 & Inv_Tot_BW>=1 & Inv_Tot_BW<235.02,1,0),
              
              #Node 14    port_pred_discount >=0.90 & port_pred_discount <0.93               Sum_IAS_FLAG >=0 & Sum_IAS_FLAG <7           Inv_Tot_BW>=235.02 & Inv_Tot_BW<=43001.42
              node_14 = ifelse(port_pred_discount >=0.90 & port_pred_discount <0.93 &
                                 Sum_IAS_FLAG >=0 & Sum_IAS_FLAG <7 &  Inv_Tot_BW>=235.02,1,0),
              
              #Node 15    port_pred_discount >=0.90 & port_pred_discount <0.93               Sum_IAS_FLAG >=7 & Sum_IAS_FLAG <=82
              node_15 = ifelse(port_pred_discount >=0.90 & port_pred_discount <0.93 & 
                                 Sum_IAS_FLAG >=7,1,0),
              
              #Node 16    port_pred_discount >=0.93 & port_pred_discount <=0.97             Segment_Cust == Enterprise, MES & Others
              node_16 = ifelse(port_pred_discount >=0.93 & port_pred_discount <=0.97 &
                                 sum(Segment_Cust == c("Enterprise", "MES", "Others")),1,0),
              
              #Node 17    port_pred_discount >=0.93 & port_pred_discount <=0.97             Segment_Cust == Service
              node_17     = ifelse(port_pred_discount >=0.93 & port_pred_discount <=0.97
                                   & Segment_Cust == "Service",1,0))
          
          bm_data_active <- bm_data_active %>%
            mutate(overall_node = ifelse(node_1 == 1  , "node_1",
                                         ifelse(node_2 == 1  , 'node_2',
                                                ifelse(node_3 == 1  , 'node_3',
                                                       ifelse(node_4 == 1  , 'node_4',
                                                              ifelse(node_5 == 1  , 'node_5',
                                                                     ifelse(node_6 == 1  , 'node_6',
                                                                            ifelse(node_7 == 1  , 'node_7',
                                                                                   ifelse(node_8 == 1  , 'node_8',
                                                                                          ifelse(node_9 == 1  , 'node_9',
                                                                                                 ifelse(node_12 == 1  , 'node_12',
                                                                                                        ifelse(node_13 == 1  , 'node_13',
                                                                                                               ifelse(node_14 == 1  , 'node_14',
                                                                                                                      ifelse(node_15 == 1  , 'node_15',
                                                                                                                             ifelse(node_16 == 1  , 'node_16',
                                                                                                                                    ifelse(node_17 == 1  , 'node_17',
                                                                                                                                           "Others"))))))))))))))))
          
          adjustment_data$Adjustment_Factor <- as.numeric(adjustment_data$Adjustment_Factor)
          adjustment_data$Bucket_Adjustment_Type <- ifelse(adjustment_data$Bucket_Adjustment_Type == "Manual Trigger",
                                                           "Manual Trigger - Error Profiling",adjustment_data$Bucket_Adjustment_Type)
          bm_data_active <- merge(x = bm_data_active,
                                  y = adjustment_data,
                                  by.x = "overall_node",
                                  by.y = "Node_Name",
                                  all.x = T)
          
          bm_data_active$ILL_Port_Adjusted_net_Price <- ifelse(bm_data_active$Bucket_Adjustment_Type=="Change",
                                                               bm_data_active$predicted_net_price +
                                                                 (bm_data_active$predicted_net_price * bm_data_active$Adjustment_Factor),
                                                               bm_data_active$predicted_net_price)
          bm_data_active$ILL_Port_ARC_Adjusted <- ifelse(bm_data_active$Bucket_Adjustment_Type=="Change",
                                                         bm_data_active$predicted_ILL_Port_ARC*(1+bm_data_active$Adjustment_Factor),
                                                         bm_data_active$predicted_ILL_Port_ARC)
          
          bm_data_active$effective_port_discount <- ifelse(bm_data_active$Bucket_Adjustment_Type=="Change",
                                                           1-(1-bm_data_active$port_pred_discount)*(1+bm_data_active$Adjustment_Factor),
                                                           bm_data_active$port_pred_discount)
          bm_data_active$effective_port_discount <- ifelse(bm_data_active$adjusted_opportunityTerm==12,
                                                           bm_data_active$effective_port_discount,
                                                           ifelse(bm_data_active$adjusted_opportunityTerm==36,
                                                                  1-(1-bm_data_active$effective_port_discount)*0.90,
                                                                  1-(1-bm_data_active$effective_port_discount)*0.95)
          )
          
          bm_data_active$ILL_Port_NRC_Adjusted <- ifelse(bm_data_active$Orch_LM_Type == "Onnet",
                                                         ifelse(bm_data_active$BW_mbps_upd<=100,
                                                                PORT_NRC_CHARGE_1_TO_100MB,
                                                                ifelse(bm_data_active$BW_mbps_upd<=300,
                                                                       PORT_NRC_CHARGE_101_TO_300MB,
                                                                       ifelse(bm_data_active$BW_mbps_upd<=1000,
                                                                              PORT_NRC_CHARGE_300_TO_1000MB,
                                                                              PORT_NRC_CHARGE_GT_THAN_1000MB))),
                                                         PORT_NRC_CHARGE)
          
          bm_data_active$Last_Mile_Cost_ARC <- ifelse(
            bm_data_active$Orch_Connection=="Wireline" & bm_data_active$Orch_LM_Type=="Onnet",
            ifelse(bm_data_active$Bucket_Adjustment_Type=="Change",
                   bm_data_active$Last_Mile_Cost_ARC*(1-bm_data_active$port_pred_discount)*(1+bm_data_active$Adjustment_Factor),
                   bm_data_active$Last_Mile_Cost_ARC*(1-bm_data_active$port_pred_discount)),
            bm_data_active$Last_Mile_Cost_ARC)
          
          bm_data_active$Last_Mile_Cost_ARC <- ifelse(
            bm_data_active$Orch_Connection=="Wireless" & bm_data_active$Orch_LM_Type=="Onnet",
            bm_data_active$Last_Mile_Cost_ARC*(1-LM_ARC_DISCOUNT_ONNET_RF), #25% Discount on Onnet RF
            bm_data_active$Last_Mile_Cost_ARC)
          
          # Removing columns not required
          bm_data_active <- dplyr::select(bm_data_active,
                                          -node_1,
                                          -node_2,
                                          -node_3,
                                          -node_4,
                                          -node_5,
                                          -node_6,
                                          -node_7,
                                          -node_8,
                                          -node_9,
                                          -node_12,
                                          -node_13,
                                          -node_14,
                                          -node_15,
                                          -node_16,
                                          -node_17)
        },
        error=function(e){
          err <<- TRUE
          df_error$error_flag <- 1
          df_error$error_code <- "E17"
          df_error$error_msg <- "Model Error: Error in Adjustments Calculations"
          df_error <<- cbind(input_json_data,df_error[,!(colnames(df_error) %in% colnames(input_json_data))])
        }
      )
      if(err==TRUE){
        return(df_error)
      }
      bm_data_active$burst_per_MB_price <- ifelse(bm_data_active$Burstable_BW>0,bm_data_active$ILL_Port_ARC_Adjusted/bm_data_active$overall_BW_mbps_upd*1.2,0)
    }
    
    if(nrow(bm_data_passive)){
      tryCatch(
        {
          
          
          pricebook_passive <- dplyr::select(price_book,
                                             'Speed',
                                             'Backup',
                                             'NRC')
          names(pricebook_passive) <- c('Speed','ILL_ARC','ILL_NRC') #*** To be removed after pricebooks are available in ETL
          pricebook_passive <- pricebook_passive[-which(is.na(pricebook_passive$ILL_ARC)),]
          pricebook_passive <- pricebook_passive[order(pricebook_passive$Speed),]
          
          names(pricebook_passive) <- c('Speed','ILL_ARC','ILL_NRC')
          bm_data_passive <- merge(x = bm_data_passive,
                                   y = pricebook_passive,
                                   by.x = "BW_mbps_upd",
                                   by.y = "Speed",
                                   all.x = T)
          intermediate_BW_request <- bm_data_passive[which(is.na(bm_data_passive$ILL_ARC)),]
          pricebook_BW_request <- bm_data_passive[which(!is.na(bm_data_passive$ILL_ARC)),]
          if(nrow(intermediate_BW_request)){
            intermediate_BW_request$result<- apply(intermediate_BW_request,
                                                   1,
                                                   function(x) price_interpolation(x["BW_mbps_upd"], pricebook_passive))
            intermediate_BW_request$ILL_ARC <-unlist(lapply(intermediate_BW_request$result, "[[", 1))
            intermediate_BW_request$ILL_NRC <- 10000#unlist(lapply(intermediate_BW_request$result, "[[", 2))
            intermediate_BW_request$result <- NULL
          }
          bm_data_passive <- rbind(pricebook_BW_request, intermediate_BW_request)
          bm_data_passive$calc_arc_list_inr <- bm_data_passive$ILL_ARC
          bm_data_passive$port_pred_discount <- 0.2
          bm_data_passive$ILL_Port_Adjusted_net_Price <- (1-bm_data_passive$port_pred_discount) * bm_data_passive$calc_arc_list_inr # 20% flat discountment_Factor)
          bm_data_passive$ILL_Port_ARC_Adjusted <- bm_data_passive$ILL_ARC*bm_data_passive$port_pred_discount
          bm_data_passive$ILL_Port_NRC_Adjusted <- ifelse(bm_data_passive$Orch_LM_Type == "Onnet",
                                                          ifelse(bm_data_passive$BW_mbps_upd<=100,
                                                                 PORT_NRC_CHARGE_1_TO_100MB,
                                                                 ifelse(bm_data_passive$BW_mbps_upd<=300,
                                                                        PORT_NRC_CHARGE_101_TO_300MB,
                                                                        ifelse(bm_data_passive$BW_mbps_upd<=1000,
                                                                               PORT_NRC_CHARGE_300_TO_1000MB,
                                                                               PORT_NRC_CHARGE_GT_THAN_1000MB))),
                                                          PORT_NRC_CHARGE)
          
          bm_data_passive$Last_Mile_Cost_ARC <- ifelse(
            bm_data_passive$Orch_Connection=="Wireline" & bm_data_passive$Orch_LM_Type=="Onnet",
            bm_data_passive$Last_Mile_Cost_ARC*0.4,# 60% disount for backup
            bm_data_passive$Last_Mile_Cost_ARC)
          
          bm_data_passive$overall_BW_mbps_upd = bm_data_passive$BW_mbps_upd
          bm_data_passive$burst_per_MB_price <- ifelse(bm_data_passive$Burstable_BW>0,
                                                       bm_data_passive$ILL_Port_ARC_Adjusted/bm_data_passive$overall_BW_mbps_upd*1.2,
                                                       0)
          
          bm_data_passive<- merge(x = bm_data_passive,
                                  y = cust_master_data,
                                  by = "Account_id_with_18_Digit",
                                  all.x = T)
          bm_data_passive <- dplyr:: rename(bm_data_passive,
                                            Account.RTM_Cust = Account_RTM,
                                            Industry_Cust = Industry,
                                            Segment_Cust = Segment)
        },
        error=function(e){
          err <<- TRUE
          df_error$error_flag <- 1
          df_error$error_code <- "E18"
          df_error$error_msg <- "Model Error: Error is calculation price for passive port"
          df_error <<- cbind(input_json_data,df_error[,!(colnames(df_error) %in% colnames(input_json_data))])
        }
      )
      if(err==TRUE){
        return(df_error)
      }
    }
    
    ######################### 
    bm_data_non_rate_card <- plyr::rbind.fill(bm_data_active, bm_data_passive, bm_data_historical_price)
    
    # Additional mutli-year discounting 2 year=5% 3 year=10%
    bm_data_non_rate_card$ILL_Port_ARC_Adjusted <- ifelse(bm_data_non_rate_card$adjusted_opportunityTerm==12,
                                                          bm_data_non_rate_card$ILL_Port_ARC_Adjusted,
                                                          ifelse(bm_data_non_rate_card$adjusted_opportunityTerm==24,
                                                                 bm_data_non_rate_card$ILL_Port_ARC_Adjusted*0.95,
                                                                 bm_data_non_rate_card$ILL_Port_ARC_Adjusted*0.90)
    )
    bm_data_non_rate_card$ILL_Port_MRC_Adjusted <- bm_data_non_rate_card$ILL_Port_ARC_Adjusted/12
    
    bm_data_non_rate_card$Last_Mile_Cost_ARC <- ifelse(bm_data_non_rate_card$adjusted_opportunityTerm==12,
                                                       bm_data_non_rate_card$Last_Mile_Cost_ARC,
                                                       ifelse(bm_data_non_rate_card$adjusted_opportunityTerm==24,
                                                              bm_data_non_rate_card$Last_Mile_Cost_ARC*0.95,
                                                              bm_data_non_rate_card$Last_Mile_Cost_ARC*0.90))
    
    # Apply Port Discount % to LM ARC for Onnet Wireline
    # bm_data$v <- ifelse(
    #   bm_data$Orch_Connection=="Wireline" & bm_data$Orch_LM_Type=="Onnet",
    #   bm_data$Last_Mile_Cost_ARC*(1-bm_data$port_pred_discount),
    #   bm_data$Last_Mile_Cost_ARC)
    
    bm_data_non_rate_card[is.na(bm_data_non_rate_card)] <- "NA"
  }
  if(nrow(bm_data_rate_card)){
    bm_data_rate_card$ratecard_flag <- TRUE
  }
  if(nrow(bm_data_non_rate_card)){
    bm_data_non_rate_card$ratecard_flag <- FALSE
  }
  
  
  
  #LM Cost components
  bm_data_non_rate_card$sp_lm_arc_bw_onwl <- ifelse(bm_data_non_rate_card$Orch_Connection=="Wireline" & bm_data_non_rate_card$Orch_LM_Type=="Onnet",
                                                    bm_data_non_rate_card$Last_Mile_Cost_ARC,
                                                    as.numeric(bm_data_non_rate_card$lm_arc_bw_onwl))
  bm_data_non_rate_card$sp_lm_arc_bw_onrf <- ifelse(bm_data_non_rate_card$Orch_Connection=="Wireless" & bm_data_non_rate_card$Orch_LM_Type=="Onnet",
                                                    bm_data_non_rate_card$Last_Mile_Cost_ARC,
                                                    as.numeric(bm_data_non_rate_card$lm_arc_bw_onrf))
  bm_data_non_rate_card$sp_lm_arc_bw_prov_ofrf <- ifelse(bm_data_non_rate_card$Orch_Connection=="Wireless" & bm_data_non_rate_card$Orch_LM_Type=="Offnet",
                                                         bm_data_non_rate_card$Last_Mile_Cost_ARC,
                                                         as.numeric(bm_data_non_rate_card$lm_arc_bw_prov_ofrf))
  bm_data_non_rate_card <- dplyr::mutate(bm_data_non_rate_card,
                                         sp_lm_nrc_mux_onwl = lm_nrc_mux_onwl,
                                         sp_lm_nrc_inbldg_onwl = lm_nrc_inbldg_onwl,
                                         sp_lm_nrc_nerental_onwl = as.numeric(lm_nrc_nerental_onwl),
                                         
                                         # Mast
                                         sp_lm_nrc_mast_onrf = as.numeric(lm_nrc_mast_onrf),
                                         sp_lm_nrc_mast_ofrf = as.numeric(lm_nrc_mast_ofrf),
                                         
                                         #OSP CAPEX
                                         #sp_lm_nrc_ospcapex_onwl = lm_nrc_ospcapex_onwl,
                                         
                                         # BW NRC
                                         sp_lm_nrc_bw_onwl = as.numeric(lm_nrc_bw_onwl),
                                         sp_lm_nrc_bw_prov_ofrf = as.numeric(lm_nrc_bw_prov_ofrf),
                                         sp_lm_nrc_bw_onrf =  as.numeric(lm_nrc_bw_onrf))
  
  
  bm_data <- plyr::rbind.fill(bm_data_rate_card, bm_data_non_rate_card)
  
  bm_data$burst_per_MB_price <- bm_data$burst_per_MB_price/12
  
  # Compute Last_Mile_Cost_NRC
  TCV <- (bm_data$Last_Mile_Cost_ARC +  bm_data$ILL_Port_ARC_Adjusted)*(bm_data$opportunityTerm/12) + bm_data$Last_Mile_Cost_NRC + bm_data$ILL_Port_NRC_Adjusted
  bm_data$sp_lm_nrc_ospcapex_onwl <- ifelse(as.numeric(bm_data$lm_nrc_ospcapex_onwl)<=(TCV/3),
                                            0,
                                            as.numeric(bm_data$lm_nrc_ospcapex_onwl)-(TCV/3))
  #Check if bucket adjustment_type exists
  bm_data$Bucket_Adjustment_Type <- ifelse("Bucket_Adjustment_Type" %in% names(bm_data),
                                           bm_data$Bucket_Adjustment_Type,
                                           "No Change") 
  # bm_data$Bucket_Adjustment_Type <- ifelse(bm_data$lm_nrc_ospcapex_onwl>0,
  #                                        "Manual Trigger - OSP Capex",
  #                                        bm_data$Bucket_Adjustment_Type)
  bm_data$Bucket_Adjustment_Type <- ifelse(tolower(bm_data$backup_port_requested) == "yes",
                                           "Manual Trigger- Backup Port Requested for the Site",
                                           bm_data$Bucket_Adjustment_Type)
  
  bm_data$Last_Mile_Cost_NRC <- bm_data$Last_Mile_Cost_NRC + bm_data$sp_lm_nrc_ospcapex_onwl
  
  ##########################################################################################
  # IV. PREDICT CPE PRICE	
  # 1. Set path
  # 2. Define Filenames
  ##########################################################################################
  bm_data_cpe_pricing <- bm_data[bm_data$CPE_Pricing_Req==1,]
  bm_data <- bm_data[bm_data$CPE_Pricing_Req==0,]
  tryCatch(
    {
      if(nrow(bm_data_cpe_pricing)){
        cols_required <- which(!names(CPE_data) %in% ETL_col_names)
        CPE_data <- CPE_data[,cols_required]
        names(CPE_data) <- c("CPE_Variant","CPE_Installation_INR","CPE_Support_INR","CPE_Management_INR","Recovery_INR","CPE_Hardware_LP_USD","OEM_Discount")
        #if(!CPE_PRICE_AVAILABLE){
        
        bm_data_cpe_pricing$Industry_Cust <- ifelse(bm_data_cpe_pricing$Industry_Cust %in% c("Financial",
                                                                                             "Media & Entertainment",
                                                                                             "IT Enabled Services (ITeS)",
                                                                                             "Information Technology",
                                                                                             "Services"),bm_data_cpe_pricing$Industry_Cust,"OTHERS")
        ######## 1. Predict CPE Discount ###############
        bm_data_cpe_pricing <- bm_data_cpe_pricing %>%
          mutate(
            node_1 = ifelse(overall_BW_mbps_upd < 5 & #Replaced BW_mbps_upd with overall_BW_mbps_upd
                              opportunityTerm < 36 &
                              Industry_Cust %in% c("Financial",
                                                   "Media & Entertainment"), 1, 0),
            node_2 = ifelse(overall_BW_mbps_upd < 5 &
                              opportunityTerm < 36 &
                              Industry_Cust %in% c("IT Enabled Services (ITeS)",
                                                   "Information Technology"), 1, 0),
            
            node_3 = ifelse(overall_BW_mbps_upd < 5 &
                              opportunityTerm < 36 &
                              Industry_Cust %in% c("Manufacturing",
                                                   "OTHERS",
                                                   "Services"), 1, 0),
            
            node_4 = ifelse(overall_BW_mbps_upd < 5 &
                              opportunityTerm >= 36 , 1, 0),
            
            node_5 = ifelse(overall_BW_mbps_upd >= 5 &
                              opportunityTerm < 24 , 1, 0),
            
            node_6 = ifelse(overall_BW_mbps_upd >= 5 &
                              opportunityTerm >= 24 , 1, 0)
          )
        
        
        bm_data_cpe_pricing <- bm_data_cpe_pricing %>%
          mutate(overall_CPE_node = ifelse(node_1 == 1  , "Node_1",
                                           ifelse(node_2 == 1  , 'Node_2',
                                                  ifelse(node_3 == 1  , 'Node_3',
                                                         ifelse(node_4 == 1  , 'Node_4',
                                                                ifelse(node_5 == 1  , 'Node_5',
                                                                       ifelse(node_6 == 1  , 'Node_6',
                                                                              "Others")))))))
        
        bm_data_cpe_pricing <- merge(x = bm_data_cpe_pricing,
                                     y = ILL_CPE_node_prediction,
                                     by = "overall_CPE_node",
                                     all.x = T)
        
        bm_data_cpe_pricing <- dplyr::select(bm_data_cpe_pricing,
                                             -node_1,
                                             -node_2,
                                             -node_3,
                                             -node_4,
                                             -node_5,
                                             -node_6)
        
        ########## b. Calculate LP & Net price #############
        
        bm_data_cpe_pricing <- merge(bm_data_cpe_pricing,
                                     CPE_data,
                                     by = "CPE_Variant",
                                     all.x = T)
        bm_data_cpe_pricing$CPE_HW_MP <- (((bm_data_cpe_pricing$CPE_Hardware_LP_USD*(1-bm_data_cpe_pricing$OEM_Discount/100))/(1-CPE_VENDOR_DISCOUNT))*(1+CPE_HW_DDP)*USD_2_INR_CONVERSION)/(1-CPE_HW_MARKUP)
        bm_data_cpe_pricing$CPE_Installation_MP <- as.numeric(bm_data_cpe_pricing$CPE_Installation_INR)/(1-CPE_SUPPORT_MARKUP)
        bm_data_cpe_pricing$CPE_Support_MP <- (as.numeric(bm_data_cpe_pricing$CPE_Support_INR)*(as.numeric(bm_data_cpe_pricing$opportunityTerm))/12)/(1-CPE_SUPPORT_MARKUP)
        
        calculate_CPE <- function(bm_data_tmp){
          result = data.frame("CPE_ARC"=0, "CPE_NRC"=0, "CPE_MRC"=0, "CPE_Rental_MRC"=0, "CPE_Management_ARC"=0, "Install_NRC"=0, 'CPE_Outright_NRC'=0)
          if(bm_data_tmp["CPE_Variant"]!="None"){
            if(bm_data_tmp["CPE_management_type"]=="full_managed" || bm_data_tmp["CPE_management_type"]=="physical_managed"){
              if(tolower(bm_data_tmp["CPE_supply_type"]) == "rental"){
                bm_data_tmp["pricipal_value"] <- as.numeric(bm_data_tmp["CPE_HW_MP"]) + as.numeric(bm_data_tmp["CPE_Support_MP"]) + as.numeric(bm_data_tmp["Recovery_INR"])
                term = ifelse(as.numeric(bm_data_tmp["opportunityTerm"])>=36, as.numeric(bm_data_tmp["opportunityTerm"]), 36)
                result$CPE_MRC <- 0-PMT(COC/12, term, as.numeric(bm_data_tmp["pricipal_value"]))
                result$CPE_MRC <- ifelse(as.numeric(bm_data_tmp["opportunityTerm"])<36,
                                         result$CPE_MRC*1.3,
                                         result$CPE_MRC)
                result$CPE_ARC <- as.numeric(bm_data_tmp["CPE_Management_INR"])
                result$CPE_NRC <- round(as.numeric(bm_data_tmp["CPE_Installation_MP"]),2)
                result$CPE_Rental_MRC <- result$CPE_MRC
                result$CPE_Management_ARC <- result$CPE_ARC
                result$Install_NRC <- result$CPE_NRC
                result$CPE_Outright_NRC <- 0
              }else if (tolower(bm_data_tmp["CPE_supply_type"]) == "sale"){
                result$CPE_MRC <- 0
                result$CPE_ARC <- as.numeric(bm_data_tmp["CPE_Management_INR"])
                result$CPE_NRC <- as.numeric(bm_data_tmp["CPE_HW_MP"]) + as.numeric(bm_data_tmp["CPE_Support_MP"]) + round(as.numeric(bm_data_tmp["CPE_Installation_MP"]),2)
                result$CPE_Rental_MRC <- 0
                result$CPE_Management_ARC <- result$CPE_ARC
                result$Install_NRC <- round(as.numeric(bm_data_tmp["CPE_Installation_MP"]),2)
                result$CPE_Outright_NRC <- as.numeric(bm_data_tmp["CPE_HW_MP"]) + as.numeric(bm_data_tmp["CPE_Support_MP"])
              }else{
                result$CPE_MRC <- 0
                result$CPE_ARC <- as.numeric(bm_data_tmp["CPE_Management_INR"])
                result$CPE_NRC <- as.numeric(bm_data_tmp["CPE_Support_MP"]) + round(as.numeric(bm_data_tmp["CPE_Installation_MP"]),2)
                result$CPE_Rental_MRC <- 0
                result$CPE_Management_ARC <- result$CPE_ARC
                result$Install_NRC <- round(as.numeric(bm_data_tmp["CPE_Installation_MP"]),2)
                result$CPE_Outright_NRC <- as.numeric(bm_data_tmp["CPE_Support_MP"])
              }
            }else if(bm_data_tmp["CPE_management_type"]=="proactive_services" || bm_data_tmp["CPE_management_type"]=="configuration_management"){
              if(tolower(bm_data_tmp["CPE_supply_type"]) == "sale"){
                result$CPE_MRC <- 0
                result$CPE_ARC <- as.numeric(bm_data_tmp["CPE_Management_INR"])
                result$CPE_NRC <- as.numeric(bm_data_tmp["CPE_HW_MP"]) + round(as.numeric(bm_data_tmp["CPE_Installation_MP"]),2) + as.numeric(bm_data_tmp["CPE_Support_MP"])
                result$CPE_Rental_MRC <- 0
                result$CPE_Management_ARC <- result$CPE_ARC
                result$Install_NRC <- round(as.numeric(bm_data_tmp["CPE_Installation_MP"]),2)
                result$CPE_Outright_NRC <- as.numeric(bm_data_tmp["CPE_HW_MP"]) + as.numeric(bm_data_tmp["CPE_Support_MP"])
              }
              else if(tolower(bm_data_tmp["CPE_supply_type"]) == "customer_owned"){ 
                result$CPE_ARC <- as.numeric(bm_data_tmp["CPE_Management_INR"])
                result$CPE_NRC <- round(as.numeric(bm_data_tmp["CPE_Installation_MP"]),2)
                result$CPE_MRC <- 0
                result$CPE_Rental_MRC <- 0
                result$CPE_Management_ARC <- result$CPE_ARC
                result$Install_NRC <- round(as.numeric(bm_data_tmp["CPE_Installation_MP"]),2)
                result$CPE_Outright_NRC <- 0
              }
              else{ #Rental
                result$CPE_MRC <- 0
                result$CPE_ARC <- 0
                result$CPE_NRC <- 0
                result$CPE_Rental_MRC <- 0
                result$CPE_Management_ARC <- 0
                result$Install_NRC <- 0
                result$CPE_Outright_NRC <- 0
              }
              
            }else{ #Unmanaged
              if (tolower(bm_data_tmp["CPE_supply_type"]) == "sale"){ # Unmanaged + OUTRIGHT SALE
                result$CPE_ARC <- 0
                result$CPE_NRC <- as.numeric(bm_data_tmp["CPE_HW_MP"]) + round(as.numeric(bm_data_tmp["CPE_Installation_MP"]),2) + as.numeric(bm_data_tmp["CPE_Support_MP"])
                result$CPE_MRC <- 0
                result$CPE_Rental_MRC <- 0
                result$CPE_Management_ARC <- result$CPE_ARC
                result$Install_NRC <- round(as.numeric(bm_data_tmp["CPE_Installation_MP"]),2)
                result$CPE_Outright_NRC <- as.numeric(bm_data_tmp["CPE_HW_MP"]) + as.numeric(bm_data_tmp["CPE_Support_MP"])
              }
              else if(tolower(bm_data_tmp["CPE_supply_type"]) == "rental"){ # Unmanaged + RENTAL [Invalid Option]
                result$CPE_ARC <- 0
                result$CPE_NRC <- 0
                result$CPE_MRC <- 0
                result$CPE_Rental_MRC <- 0
                result$CPE_Management_ARC <- 0
                result$Install_NRC <- 0
                result$CPE_Outright_NRC <- 0
              }
              else{ # Unmanaged + CUSTOMER CPE
                result$CPE_ARC <- 0
                result$CPE_NRC <- round(as.numeric(bm_data_tmp["CPE_Installation_MP"]),2)
                result$CPE_MRC <- 0
                result$CPE_Rental_MRC <- 0
                result$CPE_Management_ARC <- 0
                result$Install_NRC <- round(as.numeric(bm_data_tmp["CPE_Installation_MP"]),2)
                result$CPE_Outright_NRC <- 0
              }
            }
          }
          else{ # No BOM SELECTED
            result$CPE_ARC <- 0
            result$CPE_NRC <- 0
            result$CPE_MRC <- 0
            result$CPE_Rental_MRC <- 0
            result$CPE_Management_ARC <- 0
            result$Install_NRC <- 0
            result$CPE_Outright_NRC <- 0
          }
          return(result)
        }
        result <- apply(bm_data_cpe_pricing, 1, function(x) calculate_CPE(x))
        bm_data_cpe_pricing$ILL_CPE_ARC <- unlist(lapply(result, "[[", 1))
        bm_data_cpe_pricing$ILL_CPE_NRC <- unlist(lapply(result, "[[", 2))
        bm_data_cpe_pricing$ILL_CPE_MRC <- unlist(lapply(result, "[[", 3))
        bm_data_cpe_pricing$CPE_Rental_MRC <- unlist(lapply(result, "[[", 4))
        bm_data_cpe_pricing$CPE_Management_ARC <- unlist(lapply(result, "[[", 5))
        bm_data_cpe_pricing$Install_NRC <- unlist(lapply(result, "[[", 6))
        bm_data_cpe_pricing$CPE_Outright_NRC <- unlist(lapply(result, "[[", 7))
        
        bm_data_cpe_pricing$Adjusted_CPE_Discount <- ifelse(bm_data_cpe_pricing$CPE_pred>CPE_OVERALL_DISCOUNT_CEILING
                                                            ,CPE_OVERALL_DISCOUNT_CEILING
                                                            ,bm_data_cpe_pricing$CPE_pred)
        
        bm_data_cpe_pricing$Discounted_CPE_ARC <- bm_data_cpe_pricing$ILL_CPE_ARC*(1-bm_data_cpe_pricing$Adjusted_CPE_Discount)
        bm_data_cpe_pricing$Discounted_CPE_NRC <- bm_data_cpe_pricing$ILL_CPE_NRC*(1-bm_data_cpe_pricing$Adjusted_CPE_Discount)
        bm_data_cpe_pricing$Discounted_CPE_MRC <- bm_data_cpe_pricing$ILL_CPE_MRC*(1-bm_data_cpe_pricing$Adjusted_CPE_Discount)
        
        bm_data_cpe_pricing$Discounted_CPE_MRC <- bm_data_cpe_pricing$Discounted_CPE_MRC + (bm_data_cpe_pricing$Discounted_CPE_ARC/12)
        bm_data_cpe_pricing$Discounted_CPE_ARC <- bm_data_cpe_pricing$Discounted_CPE_MRC*12
        
        bm_data_cpe_pricing$sp_CPE_Rental_ARC <- bm_data_cpe_pricing$CPE_Rental_MRC*12*(1-bm_data_cpe_pricing$Adjusted_CPE_Discount)
        bm_data_cpe_pricing$sp_CPE_Management_ARC <- bm_data_cpe_pricing$CPE_Management_ARC*(1-bm_data_cpe_pricing$Adjusted_CPE_Discount)
        bm_data_cpe_pricing$sp_CPE_Install_NRC <- bm_data_cpe_pricing$Install_NRC*(1-bm_data_cpe_pricing$Adjusted_CPE_Discount)
        bm_data_cpe_pricing$sp_CPE_Outright_NRC <- bm_data_cpe_pricing$CPE_Outright_NRC*(1-bm_data_cpe_pricing$Adjusted_CPE_Discount)
        
        bm_data_cpe_pricing$Total_CPE_Cost <- bm_data_cpe_pricing$ILL_CPE_ARC + bm_data_cpe_pricing$ILL_CPE_NRC + bm_data_cpe_pricing$ILL_CPE_MRC * 12
        bm_data_cpe_pricing$Total_CPE_Price <- bm_data_cpe_pricing$Discounted_CPE_ARC + bm_data_cpe_pricing$Discounted_CPE_NRC + bm_data_cpe_pricing$Discounted_CPE_MRC * 12
      }
      bm_data <- plyr::rbind.fill(bm_data_cpe_pricing, bm_data)
    },
    error=function(e){
      err <<- TRUE
      df_error$error_flag <- 1
      df_error$error_code <- "E14"
      df_error$error_msg <- "Model Error: Error in CPE Discounting Model"
      df_error <<- cbind(input_json_data,df_error[,!(colnames(df_error) %in% colnames(input_json_data))])
    }
  )
  if(err==TRUE){
    return(df_error)
  }
  #########################################################################################
  # Rounding off decimal digits
  #########################################################################################
  bm_data$Last_Mile_Cost_MRC <- bm_data$Last_Mile_Cost_ARC/12
  bm_data$ILL_Port_MRC_Adjusted <- bm_data$ILL_Port_ARC_Adjusted/12
  bm_data$Discounted_CPE_MRC <- bm_data$Discounted_CPE_ARC/12
  
  cols_to_round <- c('ILL_Port_ARC_Adjusted','ILL_Port_MRC_Adjusted','ILL_Port_NRC_Adjusted',
                     'Last_Mile_Cost_ARC','Last_Mile_Cost_MRC','Last_Mile_Cost_NRC',
                     'Discounted_CPE_ARC','Discounted_CPE_MRC','Discounted_CPE_NRC',
                     'additional_IP_ARC','additional_IP_MRC','burst_per_MB_price')
  bm_data[,which(names(bm_data) %in% cols_to_round)] <- apply(bm_data[,which(names(bm_data) %in% cols_to_round)], 2, function(x) round(x,2))
  
  # Calculating total contract value
  bm_data$total_mrc <- bm_data$ILL_Port_MRC_Adjusted + bm_data$Last_Mile_Cost_MRC + bm_data$Discounted_CPE_MRC + bm_data$additional_IP_MRC
  bm_data$total_arc = bm_data$total_mrc*12
  bm_data$total_nrc <- (bm_data$ILL_Port_NRC_Adjusted + bm_data$Last_Mile_Cost_NRC + bm_data$Discounted_CPE_NRC + as.numeric(bm_data$lm_nrc_mast_onrf) + as.numeric(bm_data$lm_nrc_mast_ofrf))
  bm_data$total_contract_value <- bm_data$total_mrc*bm_data$opportunityTerm + bm_data$total_nrc
  
  sell_with_commission <- function(commission, id, port_sp, port_lp, deal_reg, multi_year, doa, tcv, opportunityTerm)
  {
    
    output_frame <- data.frame("prospect_id"=id,'port_sp'= port_sp, 'port_lp' = port_lp, 'tcv'=tcv, 
                               'commission' = commission, 'multi_year' = multi_year, 'deal_reg' = deal_reg,
                               'doa' = doa, 'opportunityTerm' = opportunityTerm,stringsAsFactors = F)
    colnames(output_frame) <- c("prospect_id",'port_sp', 'port_lp', 'tcv', 'commission', 'multi_year', 'deal_reg',
                                'doa','opportunityTerm')
    output_frame$tcv <- as.numeric(output_frame$tcv)
    output_frame$multi_year <- ifelse(as.numeric(output_frame$opportunityTerm) > 12, as.numeric(output_frame$multi_year), 0)
    
    output_frame$tot_commision = output_frame$tcv*as.numeric(output_frame$commission) + 
      output_frame$tcv * as.numeric(output_frame$deal_reg) + 
      output_frame$tcv * as.numeric(output_frame$multi_year)
    
    output_frame$effect_commision_pct = as.numeric(output_frame$commission) + as.numeric(output_frame$deal_reg) + as.numeric(output_frame$multi_year)
    
    output_frame$effect_port_disc = 1 - ((as.numeric(output_frame$port_sp) - output_frame$tot_commision)/ as.numeric(output_frame$port_lp))
    
    output_frame$manual = ifelse(output_frame$effect_port_disc > output_frame$doa, TRUE, FALSE)
    
    return (output_frame[,c('prospect_id', 'tot_commision', 'manual','effect_commision_pct')])
    
  }
  
  
  #Check if Quote is for partner pricing
  if(tolower(bm_data$quotetype_partner[1]) == 'sell with'){
    bm_data$partner_profile <- stri_replace_all_fixed(bm_data$partner_profile," ","_")
    # Get Partner COmmission Level
    bm_data <- merge(bm_data,
                     partner_commission_profile,
                     by.x = 'partner_profile',
                     by.y = 'Profile',
                     all.x = T)
    bm_data <- dplyr::rename(bm_data,
                             Commission_Level = Commission)
    
    #Get Partner Commission %
    bm_data <- merge(bm_data,
                     partner_commision,
                     by.x = c('Commission_Level','product_name'),
                     by.y = c('Profile','Product_Type'),
                     all.x = T)
    
    #function(commission, id, port_sp, port_lp, deal_reg, multi_year, doa, arc)
    bm_data$doa <- DOA #Fixing to 0
    bm_data$ILL_SP_ARC <- ifelse(bm_data$hist_flag, 
                                 bm_data$ILL_Port_ARC_Adjusted-(1-bm_data$port_pred_discount)*as.numeric(bm_data$lm_arc_bw_onwl),
                                 bm_data$ILL_Port_ARC_Adjusted)
    
    bm_data$result <- apply(bm_data, 1, function(x) sell_with_commission(x["Commission"],
                                                                         x['site_id'],
                                                                         x['ILL_SP_ARC'],
                                                                         x['ILL_ARC'],
                                                                         x['DR'],
                                                                         x['Multiyear'],
                                                                         x['doa'],
                                                                         x['total_arc'],
                                                                         x['opportunityTerm']))
    bm_data$total_commission <- unlist(lapply(bm_data$result, "[[", 2))
    bm_data$Bucket_Adjustment_Type <- ifelse(bm_data$ratecard_flag,
                                             bm_data$Bucket_Adjustment_Type,
                                             ifelse(unlist(lapply(bm_data$result, "[[", 3)),
                                                    "Manual Trigger: After comission C3 DOA breach",
                                                    bm_data$Bucket_Adjustment_Type))
    bm_data$tot_commission_pct <- unlist(lapply(bm_data$result, "[[", 4))
    bm_data$result <- NULL
    
  }else{
    bm_data$total_commission <- 0
  }
  
  bm_data <- mutate(bm_data,
                    sp_port_arc = ILL_Port_ARC_Adjusted,
                    sp_port_nrc = ILL_Port_NRC_Adjusted,
                    sp_burst_per_MB_price_ARC = burst_per_MB_price,
                    sp_additional_IP_ARC = additional_IP_ARC)
  
  #Added code for BW > 10G
  bm_data$Bucket_Adjustment_Type <- ifelse('Bucket_Adjustment_Type' %in% colnames(bm_data),
                                           ifelse(as.numeric(bm_data$bw_mbps)>10000,
                                                  "Manual Trigger: BW > 10Gbps",
                                                  bm_data$Bucket_Adjustment_Type),
                                           ifelse(as.numeric(bm_data$bw_mbps)>10000,
                                                  "Manual Trigger: BW > 10Gbps",
                                                  "No change"))
  
  bm_data$version <- version
  bm_data <- dplyr::arrange(bm_data,order_no)
  bm_data$order_no <- NULL
  
  time_end <- proc.time() - time_start
  time_end <- time_end[['elapsed']]
  bm_data$time_taken <- time_end
  
  bm_data$error_code <- "NA"
  bm_data$error_flag <- 0
  bm_data$error_msg <- "No Error"
  
  if(ncol(bm_data) < ncol(df_error)){
    bm_data = cbind(bm_data, df_error[,!(colnames(df_error) %in% colnames(bm_data))])
  }
  
  ##########################################################################################
  # Align datatypes with orchestration
  ##########################################################################################
  str_cols <- c('createdDate_quote','Account.RTM_Cust','Account_id_with_18_Digit','BW_mbps_upd','Bucket_Adjustment_Type','CPE_HW_MP','CPE_Hardware_LP_USD','CPE_Installation_INR','CPE_Installation_MP','CPE_Management_INR','CPE_Support_INR','CPE_Support_MP','CPE_Variant','CPE_management_type','CPE_supply_type','Identifier','Industry_Cust','Last_Modified_Date','OEM_Discount','OpportunityID_Prod_Identifier','Orch_Connection','Orch_LM_Type','Recovery_INR','Segment_Cust','a_account_id_with_18_digit','a_additional_ip','a_burstable_bw','a_bw_mbps','a_connection_type','a_cpe_management_type','a_cpe_supply_type','a_cpe_variant','a_customer_segment','a_feasibility_response_created_date','a_last_mile_contract_term','a_latitude_final','a_local_loop_interface','a_longitude_final','a_opportunity_term','a_pool_size','a_product_name','a_prospect_name','a_quotetype_quote','a_resp_city','a_sales_org','a_site_id','a_sum_no_of_sites_uni_len','a_topology','connection_type','customer_segment','last_mile_contract_term','latitude_final','lm_arc_bw_onrf','lm_arc_bw_onwl','lm_arc_bw_prov_ofrf','lm_nrc_bw_onrf','lm_nrc_bw_onwl','lm_nrc_bw_prov_ofrf','lm_nrc_inbldg_onwl','lm_nrc_mast_ofrf','lm_nrc_mast_onrf','lm_nrc_mux_onwl','lm_nrc_nerental_onwl','lm_nrc_ospcapex_onwl','local_loop_interface','longitude_final','overall_CPE_node','overall_PortType','overall_node','product_name','prospect_name','quoteType_quote','resp_city','sales_org','site_id','sum_offnet_flag','sum_onnet_flag','topology')
  
  numeric_cols <- c('Adjusted_CPE_Discount','Adjustment_Factor','Burstable_BW','CPE_pred','Discounted_CPE_ARC','Discounted_CPE_MRC','Discounted_CPE_NRC','GVPN_ARC_per_BW','ILL_ARC','ILL_ARC_per_BW','ILL_CPE_ARC','ILL_CPE_MRC','ILL_CPE_NRC','ILL_NRC','ILL_Port_ARC_Adjusted','ILL_Port_Adjusted_net_Price','ILL_Port_NRC_Adjusted','Inv_GVPN_bw','Inv_ILL_bw','Inv_NPL_bw','Inv_Other_bw','Inv_Tot_BW','Last_Mile_Cost_ARC','Last_Mile_Cost_NRC','NPL_ARC_per_BW','Other_ARC_per_BW','Sum_CAT_1_2_MACD_FLAG','Sum_CAT_1_2_New_Opportunity_FLAG','Sum_CAT_3_MACD_FLAG','Sum_CAT_3_New_Opportunity_FLAG','Sum_CAT_4_MACD_FLAG','Sum_CAT_4_New_Opportunity_FLAG','Sum_Cat_1_2_opp','Sum_GVPN_Flag','Sum_IAS_FLAG','Sum_MACD_Opportunity','Sum_NPL_Flag','Sum_New_ARC_Converted','Sum_New_ARC_Converted_GVPN','Sum_New_ARC_Converted_ILL','Sum_New_ARC_Converted_NPL','Sum_New_ARC_Converted_Other','Sum_New_Opportunity','Sum_Other_Flag','Sum_tot_oppy_historic_opp','Sum_tot_oppy_historic_prod','TOT_ARC_per_BW','Total_CPE_Cost','Total_CPE_Price','additional_IP','burst_per_MB_price','calc_arc_list_inr','list_price_mb','list_price_mb_dummy','log_Inv_Tot_BW','log_Inv_Tot_BW_dummy','node_1','node_2','node_3','node_4','node_5','node_6','num_products_opp_new.x','opportunityTerm','opportunity_day','opportunity_month','overall_BW_mbps_upd','pool_size','port_pred_discount','predicted_ILL_Port_ARC','predicted_ILL_Port_NRC','predicted_net_price','sum_cat1_2_Opportunity','sum_cat_3_Opportunity','sum_cat_4_Opportunity','sum_no_of_sites_uni_len','sum_product_flavours.x','time_taken','tot_oppy_current_prod.x','additional_IP_ARC','additional_IP_MRC','ILL_Port_MRC_Adjusted','Last_Mile_Cost_MRC','total_contract_value',
                    'total_commission')
  
  bm_data[,which(names(bm_data) %in% numeric_cols)] = apply(bm_data[,which(names(bm_data) %in% numeric_cols)], 2, function(x) as.numeric(as.character(x)))
  
  bm_data[,which(names(bm_data) %in% str_cols)] = apply(bm_data[,which(names(bm_data) %in% str_cols)], 2, function(x) as.character(x))
  
  bm_data$datediff = NULL
  ##########################################################################################
  # Save adjusted Last Mile components as separate pricing LM 
  ##########################################################################################
  # create LM cost components for pricing output
  bm_data <- dplyr::mutate(bm_data,
                           p_lm_arc_bw_onwl = lm_arc_bw_onwl,
                           p_lm_nrc_bw_onwl = lm_nrc_bw_onwl,
                           p_lm_nrc_mux_onwl = lm_nrc_mux_onwl,
                           p_lm_nrc_inbldg_onwl = lm_nrc_inbldg_onwl,
                           p_lm_nrc_ospcapex_onwl = lm_nrc_ospcapex_onwl,
                           p_lm_nrc_nerental_onwl = lm_nrc_nerental_onwl,
                           p_lm_arc_bw_prov_ofrf = lm_arc_bw_prov_ofrf,
                           p_lm_nrc_bw_prov_ofrf = lm_nrc_bw_prov_ofrf,
                           p_lm_nrc_mast_ofrf = lm_nrc_mast_ofrf,
                           p_lm_arc_bw_onrf = lm_arc_bw_onrf,
                           p_lm_nrc_bw_onrf = lm_nrc_bw_onrf,
                           p_lm_nrc_mast_onrf = lm_nrc_mast_onrf)
  
  ##########################################################################################
  # Output Column Clean up
  ##########################################################################################
  bm_data <- bm_data[,!(colnames(bm_data) %in% colnames(input_json_data))]
  
  bm_data <- dplyr::rename(bm_data,
                           site_id = a_site_id,
                           latitude_final = a_latitude_final,
                           longitude_final = a_longitude_final,
                           prospect_name = a_prospect_name,
                           bw_mbps = a_bw_mbps,
                           burstable_bw = a_burstable_bw,
                           resp_city = a_resp_city,
                           customer_segment = a_customer_segment,
                           sales_org = a_sales_org,
                           product_name = a_product_name,
                           feasibility_response_created_date = a_feasibility_response_created_date,
                           local_loop_interface = a_local_loop_interface,
                           last_mile_contract_term = a_last_mile_contract_term,
                           account_id_with_18_digit = a_account_id_with_18_digit,
                           opportunity_term = a_opportunity_term,
                           quotetype_quote = a_quotetype_quote,
                           connection_type = a_connection_type,
                           sum_no_of_sites_uni_len = a_sum_no_of_sites_uni_len,
                           cpe_variant = a_cpe_variant,
                           cpe_management_type = a_cpe_management_type,
                           cpe_supply_type = a_cpe_supply_type,
                           topology = a_topology,
                           ipv4_address_pool_size = a_ipv4_address_pool_size,
                           ipv6_address_pool_size = a_ipv6_address_pool_size,
                           ip_address_arrangement = a_ip_address_arrangement,
                           additional_ip_flag = a_additional_ip_flag)
  
  # save original LM cost attributes as feasibility LM
  input_json_data <- dplyr::rename(input_json_data,
                                   f_lm_arc_bw_onwl = lm_arc_bw_onwl,
                                   f_lm_nrc_bw_onwl = lm_nrc_bw_onwl,
                                   f_lm_nrc_mux_onwl = lm_nrc_mux_onwl,
                                   f_lm_nrc_inbldg_onwl = lm_nrc_inbldg_onwl,
                                   f_lm_nrc_ospcapex_onwl = lm_nrc_ospcapex_onwl,
                                   f_lm_nrc_nerental_onwl = lm_nrc_nerental_onwl,
                                   f_lm_arc_bw_prov_ofrf = lm_arc_bw_prov_ofrf,
                                   f_lm_nrc_bw_prov_ofrf = lm_nrc_bw_prov_ofrf,
                                   f_lm_nrc_mast_ofrf = lm_nrc_mast_ofrf,
                                   f_lm_arc_bw_onrf = lm_arc_bw_onrf,
                                   f_lm_nrc_bw_onrf = lm_nrc_bw_onrf,
                                   f_lm_nrc_mast_onrf = lm_nrc_mast_onrf)
  
  # maintain original input json along with other attributes
  tmp_merge <- bm_data[,!(colnames(bm_data) %in% colnames(input_json_data))]
  tmp_merge$site_id <- bm_data$site_id
  
  bm_data = merge(x = input_json_data,
                  y = tmp_merge,
                  by = "site_id",
                  all.x = TRUE)
  rm(tmp_merge)
  
  ##########################################################################################
  # Clean-up
  ##########################################################################################
  # Round off numeric values to 2 decimal digits
  bm_data <- bm_data %>% mutate_if(is.numeric, funs(round(., 2)))
  num_cols <- sapply(bm_data, is.numeric)
  char_cols <- sapply(bm_data, is.character)
  fact_cols <- sapply(bm_data, is.factor)
  
  if(any(is.na(bm_data[num_cols]))){
    bm_data[num_cols][is.na(bm_data[num_cols])]<-0
  }
  
  if(any(is.na(bm_data[char_cols]))){
    bm_data[char_cols][is.na(bm_data[char_cols])]<-"NA"
  }
  
  if(any(is.na(bm_data[fact_cols]))){
    bm_data[fact_cols][is.na(bm_data[fact_cols])]<-"NA"
  }
  
  if(any(is.na(bm_data))){
    bm_data[is.na(bm_data)] <- "NA"
  }
  lapply(dbListConnections(MySQL()), dbDisconnect)
  
  return(bm_data)
}

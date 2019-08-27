
# coding: utf-8

# In[1]:


import os 
import numpy as np 
import pandas as pd
import requests,json
import io
import rpy2.robjects as robjects
from flask import Flask, abort, jsonify, request
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri
pandas2ri.activate()


# In[2]:


path_py = os.path.dirname(os.path.abspath(__file__))


# In[ ]:


# utils = importr('utils')
# utils.install_packages('dplyr')
# utils.install_packages('plyr')
# utils.install_packages('readxl')
# utils.install_packages('geosphere')
# utils.install_packages('gdata')
# utils.install_packages('lubridate')
# utils.install_packages('data.table')
# utils.install_packages('sqldf')
# utils.install_packages('RecordLinkage')
# utils.install_packages('stringr')
# utils.install_packages('randomForest')
# utils.install_packages('reshape2')
# utils.install_packages('RMySQL')
# utils.install_packages('jsonlite')


# In[ ]:


app = Flask(__name__)

@app.route('/api', methods = ['POST'])

def make_predict_onnet_wireline():
    #get the json file as an input
    data = request.get_json(force=True)
    input_data = pd.io.json.json_normalize(data,'input_data')
    # here write your rcode 
    rstr ='''
    function(input_data,path_py){
      ##########################################################################################
      ##########################################################################################
      # Code Header
      ##########################################################################################
      ##########################################################################################
      #Objective - Access Feasibility, LM Cost & Network Feasibility check for Onnet Wireline Scenario
      #Create Date - 19/06/2018
      #Modified Date - 19/07/2018
      #Version - v2.0

      ##########################################################################################
      # SET WORKING DIRECTORY
      ##########################################################################################
      #setwd("E:/gv_personal_folder/prod_codes/gaurav_ETL/Onnet_Wireline")
      setwd(path_py)

      ##########################################################################################
      # SET PARAMETERS
      ##########################################################################################
      # set error parameter
      err <- FALSE

      # save input json
      input_json_data <- input_data

      ##########################################################################################
      # Define Error Output JSON to be thrown in case of any error encountered
      ##########################################################################################
      # Define Error response dataframe
      df_error <- data.frame('site_id' = 'NA','POP_DIST_KM_SERVICE_MOD' = 'NA','Product.Name' = 'NA','POP_DIST_KM' = 'NA','POP_DIST_KM_SERVICE' = 'NA','pop_name' = 'NA','POP_Network_Location_Type' = 'NA','POP_Construction_Status' = 'NA','POP_Building_Type' = 'NA','pop_network_loc_id' = 'NA','pop_long' = 'NA','pop_lat' = 'NA','pop_address' = 'NA','POP_Category' = 'NA','POP_TCL_Access' = 'NA','FATG_DIST_KM' = 'NA','FATG_Network_Location_Type' = 'NA','FATG_Building_Type' = 'NA','FATG_Category' = 'NA','FATG_TCL_Access' = 'NA','FATG_PROW' = 'NA','FATG_Ring_type' = 'NA','HH_DIST_KM' = 'NA','hh_name' = 'NA','X0.5km_cust_count' = 'NA','X0.5km_min_dist' = 'NA','X0.5km_avg_dist' = 'NA','X0.5km_min_bw' = 'NA','X0.5km_avg_bw' = 'NA','X0.5km_max_bw' = 'NA','X2km_cust_count' = 'NA','X2km_min_dist' = 'NA','X2km_avg_dist' = 'NA','X2km_min_bw' = 'NA','X2km_avg_bw' = 'NA','X2km_max_bw' = 'NA','X5km_cust_count' = 'NA','X5km_min_dist' = 'NA','X5km_avg_dist' = 'NA','X5km_min_bw' = 'NA','X5km_avg_bw' = 'NA','X5km_max_bw' = 'NA','X0.5km_prospect_count' = 'NA','X0.5km_prospect_min_dist' = 'NA','X0.5km_prospect_avg_dist' = 'NA','X0.5km_prospect_min_bw' = 'NA','X0.5km_prospect_avg_bw' = 'NA','X0.5km_prospect_max_bw' = 'NA','X0.5km_prospect_num_feasible' = 'NA','X0.5km_prospect_perc_feasible' = 'NA','X2km_prospect_count' = 'NA','X2km_prospect_min_dist' = 'NA','X2km_prospect_avg_dist' = 'NA','X2km_prospect_min_bw' = 'NA','X2km_prospect_avg_bw' = 'NA','X2km_prospect_max_bw' = 'NA','X2km_prospect_num_feasible' = 'NA','X2km_prospect_perc_feasible' = 'NA','X5km_prospect_count' = 'NA','X5km_prospect_min_dist' = 'NA','X5km_prospect_avg_dist' = 'NA','X5km_prospect_min_bw' = 'NA','X5km_prospect_avg_bw' = 'NA','X5km_prospect_max_bw' = 'NA','X5km_prospect_num_feasible' = 'NA','X5km_prospect_perc_feasible' = 'NA','OnnetCity_tag' = 'NA','Probabililty_Access_Feasibility' = 'NA','Predicted_Access_Feasibility' = 'NA','lm_arc_bw_onwl' = 'NA','connected_cust_tag' = 'NA','connected_building_tag' = 'NA','Service_ID' = 'NA','num_connected_cust' = 'NA','num_connected_building' = 'NA','lm_nrc_mux_onwl' = 'NA','lm_nrc_inbldg_onwl' = 'NA','lm_nrc_nerental_onwl' = 'NA','lm_nrc_bw_onwl' = 'NA','cost_permeter' = 'NA','min_hh_fatg' = 'NA','lm_nrc_ospcapex_onwl' = 'NA','total_cost' = 'NA','city_tier' = 'NA','scenario_1' = 'NA','scenario_2' = 'NA','net_pre_feasible_flag' = 'NA','Network_F_NF_CC_Flag' = 'NA','Network_F_NF_CC' = 'NA','access_check_CC' = 'NA','core_check_CC' = 'NA','mux' = 'NA','HH_0_5km' = 'NA','hh_flag' = 'NA','Network_F_NF_HH_Flag' = 'NA','Network_F_NF_HH' = 'NA','access_check_hh' = 'NA','core_check_hh' = 'NA','HH_0_5_access_rings_F' = 'NA','HH_0_5_access_rings_NF' = 'NA','access_rings_hh' = 'NA','hub_node' = 'NA','core_ring' = 'NA','Network_Feasibility_Check' = 'NA','Orch_LM_Type' = 'NA','Orch_Connection' = 'NA','Orch_Category' = 'NA','Orch_BW' = 'NA','latitude_final' = 'NA','longitude_final' = 'NA','prospect_name' = 'NA','bw_mbps' = 'NA','burstable_bw' = 'NA','resp_city' = 'NA','customer_segment' = 'NA','sales_org' = 'NA','product_name' = 'NA','feasibility_response_created_date' = 'NA','local_loop_interface' = 'NA','last_mile_contract_term' = 'NA','account_id_with_18_digit' = 'NA','opportunity_term' = 'NA','quotetype_quote' = 'NA','connection_type' = 'NA','sum_no_of_sites_uni_len' = 'NA','cpe_variant' = 'NA','cpe_management_type' = 'NA','cpe_supply_type' = 'NA','topology' = 'NA','additional_ip_flag' = 'NA','ip_address_arrangement' = 'NA','ipv4_address_pool_size' = 'NA','ipv6_address_pool_size' = 'NA','lm_arc_bw_prov_ofrf' = 'NA','lm_nrc_bw_prov_ofrf' = 'NA','lm_nrc_mast_ofrf' = 'NA','lm_arc_bw_onrf' = 'NA','lm_nrc_bw_onrf' = 'NA','lm_nrc_mast_onrf' = 'NA','error_code' = 'NA','error_flag' = 'NA','error_msg' = 'NA','time_taken' = 'NA')

      ##########################################################################################
      ##########################################################################################
      # R Packages - Check if needed packages are installed - if not, install them
      ##########################################################################################
      ##########################################################################################
      tryCatch(
        {
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
      #library(shiny)
      library(dplyr)
      library(plyr)
      #library(readxl)
      library(geosphere)
      library(lubridate)
      library(data.table)
      library(sqldf)
      library(randomForest)
      library(RecordLinkage)
      library(jsonlite)
      library(RMySQL)
      library(reshape2)
      #library(sp)
      #library(gdata)
      #library(caret)
      #library(openxlsx)
      #library(stringdist)
        },error=function(e){
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
      ##########################################################################################
      # R code
      ##########################################################################################
      ##########################################################################################
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Read Input JSON File
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      tryCatch(
        {
        #input_data <- dplyr::bind_rows(fromJSON("input_json.json"))

        #input_json_data <- input_data

        # align column names according to the old training format
        colnames(input_data)[colnames(input_data) == 'site_id'] <- 'site_id'
        colnames(input_data)[colnames(input_data) == 'latitude_final'] <- 'Latitude_final'
        colnames(input_data)[colnames(input_data) == 'longitude_final'] <- 'Longitude_final'
        colnames(input_data)[colnames(input_data) == 'bw_mbps'] <- 'BW_mbps'
        colnames(input_data)[colnames(input_data) == 'burstable_bw'] <- 'Burstable_BW'
        colnames(input_data)[colnames(input_data) == 'customer_segment'] <- 'Customer_Segment'
        colnames(input_data)[colnames(input_data) == 'sales_org'] <- 'Sales.Org'
        colnames(input_data)[colnames(input_data) == 'product_name'] <- 'Product.Name'
        colnames(input_data)[colnames(input_data) == 'feasibility_response_created_date'] <- 'Feasibility.Response..Created.Date'

        #Data type formatting for input data
        input_data$Prospect_ID <- input_data$site_id
        input_data$site_id <- NULL
        input_data$Latitude_final <- as.numeric(input_data$Latitude_final)
        input_data$Longitude_final <- as.numeric(input_data$Longitude_final)
        input_data$BW_mbps <- as.numeric(input_data$BW_mbps)
        input_data$Burstable_BW  <- as.numeric(input_data$Burstable_BW)
        input_data$BW_mbps_act <- as.numeric(input_data$BW_mbps)
        input_data$Feasibility.Response..Created.Date <- as.Date(input_data$Feasibility.Response..Created.Date,
                                                                 format = "%Y-%m-%d")

        #Selecting BW - if Burstable is higher then select Burstable BW for Access, LM and Network Feasibility
        input_data$Burstable_BW <- ifelse((is.na(input_data$Burstable_BW)|(input_data$Burstable_BW==0)),0,input_data$Burstable_BW)

        input_data$BW_mbps <- ifelse(input_data$Burstable_BW>input_data$BW_mbps, input_data$Burstable_BW,input_data$BW_mbps)

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

        if(any(is.na(input_data))){
          throw("Input Error")
        }
          },error=function(e){
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

      # Defining input files to be read from server +++++++++++++++++
      training_set <- "onnent_wireline_under.rda"
      model_object_name <- "onnet_wl.rds"

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Database Connection
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      #establishing connection
      tryCatch(
        {
        mydb_abstract_db = dbConnect(MySQL(), 
                                     user='optimus_user', 
                                     password='Tata123', 
                                     dbname='optimus_abstract', 
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
      #List all tables in db instance
      #dbListTables(mydb_abstract_db)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Read Model Object
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      tryCatch(
        {
        rf_model_val <- readRDS(model_object_name)
        }, 
        error=function(e){
          err <<- TRUE
          df_error$error_flag <- 1
          df_error$error_code <- "E4"
          df_error$error_msg <- "Load Error: Error in loading the Model Object"
          df_error <<- cbind(input_json_data,df_error[,!(colnames(df_error) %in% colnames(input_json_data))])
        }
        )
      if(err==TRUE){
        return(df_error)
      }

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Read Original Training data for setting same factor level
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      tryCatch(
        {
        onnet_wireline <- load(training_set)
        onnet_wireline <- get(onnet_wireline)
        }, 
        error=function(e){
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

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Prospect Data - Import
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # pros_data <- readRDS(pros_data)
      # prospect_coords <- pros_data
      tryCatch(
        {
        pros_data = dbSendQuery(mydb_abstract_db, "select Prospect_ID, resp_state, Feasibility_Response_Created_Date, Latitude_final, Longitude_final, Status, Cleaned_BW from Prospect_Rolled_Up_Onnet_Wireline")
        # fetching data from mysql server
        pros_data = fetch(pros_data, n=-1)
        # Column Mapping
        pros_cols <- c("Prospect_ID_2","prospect_state","prospect_date","prospect_lat","prospect_lon",
                       "prospect_status","prospect_bw")

        colnames(pros_data) <- pros_cols

        pros_data$prospect_lat <- as.numeric(pros_data$prospect_lat)
        pros_data$prospect_lon <- as.numeric(pros_data$prospect_lon)

        prospect_coords <- pros_data

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

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # POP Data - Import
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      #pop_data_file_tmp <- read.csv(pop_data_2, na.strings = c("", "#N/A", "<NA>","NA"))
      # sending query to mysql db
      tryCatch(
        {
        pop_data_file = dbSendQuery(mydb_abstract_db, "select seq_no,name,network_location_type,construction_status,building_type,network_location_id,longitude,latitude,site_address,category,services_offered_gde,services_offered_gvpn,services_offered_ias,services_offered_ipl,services_offered_vpls,services_offered_video_connect,services_offered_nde,services_offered_npl,services_offered_priority_ethernet,tcl_access,pop_state from pop_data")

        # fetching data from mysql server
        pop_data_file = fetch(pop_data_file, n=-1)
        # Column Mapping
        pop_cols <- c('POP_ID','pop_name','POP_Network_Location_Type','POP_Construction_Status','POP_Building_Type','pop_network_loc_id','pop_long','pop_lat','pop_address','POP_Category','Services.Offered.GDE','Services.Offered.GVPN','Services.Offered.IAS','Services.Offered.IPL','Services.Offered.VPLS','Services.Offered.Video.Connect','Services.Offered.NDE','Services.Offered.NPL','Services.Offered.Priority.Ethernet','POP_TCL_Access','pop_state')

        colnames(pop_data_file) <- pop_cols

        pop_data_file$pop_lat <- as.numeric(pop_data_file$pop_lat)
        pop_data_file$pop_long <- as.numeric(pop_data_file$pop_long)

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

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # FATG Data - Import
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      #fatg_data_file <- read_excel(fatg_data, na = c("", "#N/A", "<NA>","NA"))
      # sending query to mysql db
      tryCatch(
        {
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

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # HandHole Data - Import
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      #hh_data_file <- read_excel(hh_data, na = c("", "#N/A", "<NA>","NA"))
      # sending query to mysql db
      tryCatch(
        {
        hh_data_file = dbSendQuery(mydb_abstract_db, "select seq_no,num_hh,hh_state,hh_lat,hh_long from hh_data")

        # fetching data from mysql server
        hh_data_file = fetch(hh_data_file, n=-1)
        # Column Mapping
        hh_cols <- c('HH_ID','hh_name','HH_STATE','hh_lat','hh_long')

        colnames(hh_data_file) <- hh_cols
        hh_data_file$hh_lat <- as.numeric(hh_data_file$hh_lat)
        hh_data_file$hh_long <- as.numeric(hh_data_file$hh_long)
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

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Onnet Wireline Customer Data - Import
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      #cust_df <- read_excel(cust_data, na = c("", "#N/A", "<NA>","NA"))
      tryCatch(
        {
        cust_data_file = dbSendQuery(mydb_abstract_db, "select Circuit_ID, cust_name, Longitude, Latitude, Cleaned_customer_Bandwidth, Date_Of_Acceptance from Prospect_Customer_Rolled_Up_data_Onnet_Wireline")
        # fetching data from mysql server
        cust_data_file = fetch(cust_data_file, n=-1)
        # Column Mapping
        cust_cols <- c('SERVICEID','CUST_NAME','Longitude','Latitude','F12','PROVISIONING_START_DATE')

        colnames(cust_data_file) <- cust_cols

        cust_data_file$Latitude <- as.numeric(cust_data_file$Latitude)
        cust_data_file$Longitude <- as.numeric(cust_data_file$Longitude)
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

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # City Master Data - Import
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      #man_city <- read.csv(man_city, na.strings = c("", "#N/A", "<NA>","NA"))
      # sending query to mysql db
      tryCatch(
        {
        man_city = dbSendQuery(mydb_abstract_db, "select seq_no,city_id,city_name,cost_permeter,state_name,refrfstateid,center_x,center_y,isonnetcity from eeplus_city_master_data")

        # fetching data from mysql server
        man_city = fetch(man_city, n=-1)
        # Column Mapping
        man_city_cols <- c('seq_no','City_id','CITY_NAME','cost_permeter','State_Name','refRFstateid','CENTER_X','CENTER_Y','IsOnnetCity')

        colnames(man_city) <- man_city_cols
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

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # ARC BW Rate Cards for LM Costs
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      #bw_fe <- read_excel(paste(arc_bw_ratecard),sheet="FE")
      #bw_ge <- read_excel(paste(arc_bw_ratecard),sheet="GE")
      # sending query to mysql db
      tryCatch(
        {
        bw_all_stack = dbSendQuery(mydb_abstract_db, "select seq_no,sno,Distance,Bandwidth,local_loop_type,price from cq_tblcapexarc_onnet")

        # fetching data from mysql server
        bw_all_stack = fetch(bw_all_stack, n=-1)
        # Column Mapping
        bw_all_stack_cols <- c('seq_no','sno','Distance','BW_mbps','type','value')

        colnames(bw_all_stack) <- bw_all_stack_cols
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

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # HH Chamber Ring - Network Check
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      #hh_data_network <- read.csv(hh_data_network_name)
      # sending query to mysql db
      tryCatch(
        {
        hh_data_network = dbSendQuery(mydb_abstract_db, "select seq_no,chamber_name,latitude,longitude,rings from chamber_ring")

        # fetching data from mysql server
        hh_data_network = fetch(hh_data_network, n=-1)
        # Column Mapping
        hh_data_network_cols <- c('seq_no','chamber_name','latitude','longitude','access_rings_hh')

        colnames(hh_data_network) <- hh_data_network_cols

        hh_data_network$latitude <- as.numeric(hh_data_network$latitude)
        hh_data_network$longitude <- as.numeric(hh_data_network$longitude)
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

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # MUX Info - Service IDs - Network Check
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      #dropporttoservice <- read_excel(dropporttoservice_name, sheet = "dropporttoservice")
      # sending query to mysql db
      tryCatch(
        {
        dropporttoservice = dbSendQuery(mydb_abstract_db, "select seq_no,serviceoriorid,nodename from dropporttoservice")

        # fetching data from mysql server
        dropporttoservice = fetch(dropporttoservice, n=-1)
        # Column Mapping
        dropporttoservice_cols <- c('seq_no','SERVICEORIORID','mux')

        colnames(dropporttoservice) <- dropporttoservice_cols

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

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # MUX Info - Nodenames - Network Check
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Getting coverage for node name
      #nodename_rm <- read_excel(nodename_rm_names, sheet = "Export Worksheet")
      # sending query to mysql db
      # nodename_rm = dbSendQuery(mydb_abstract_db, "select * from tx_node_with_coverage")
      # # fetching data from mysql server
      # nodename_rm = fetch(nodename_rm, n=-1)


      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Access Ring - Network Check
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      #TopologyTerminationReport <- read.csv(TopologyTerminationReport_name,stringsAsFactors = F)

      # Access Ring
      # sending query to mysql db
      tryCatch(
        {
        TopologyTerminationReport_access = dbSendQuery(mydb_abstract_db, "select seq_no,topologyname,bandwidth,nodename,coverage from topology_termination_access_ring_report")

        # fetching data from mysql server
        TopologyTerminationReport_access = fetch(TopologyTerminationReport_access, n=-1)
        top_term_access_cols <- c('seq_no','selected_access_ring','selected_access_ring_Bandwidth','NODENAME','selected_access_ring_Coverage')

        colnames(TopologyTerminationReport_access) <- top_term_access_cols

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

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Core Ring - Network Check
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Core Ring
      # sending query to mysql db
      tryCatch(
        {
        TopologyTerminationReport_core = dbSendQuery(mydb_abstract_db, "select seq_no,topologyname,nodename from topology_termination_core_ring_report")

        # fetching data from mysql server
        TopologyTerminationReport_core = fetch(TopologyTerminationReport_core, n=-1)
        top_term_core_cols <- c('seq_no','core_ring','NODENAME')

        colnames(TopologyTerminationReport_core) <- top_term_core_cols

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

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Hub Ring - Network Check
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Core Ring
      # sending query to mysql db
      tryCatch(
        {
        TopologyTerminationReport_hub = dbSendQuery(mydb_abstract_db, "select seq_no,topologyname,nodename from topology_termination_hub_ring_report")

        # fetching data from mysql server
        TopologyTerminationReport_hub = fetch(TopologyTerminationReport_hub, n=-1)
        top_term_hub_cols <- c('seq_no','hub_ring','hub_node')

        colnames(TopologyTerminationReport_hub) <- top_term_hub_cols

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

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Access Ring Utilization for capacity check- Network Check
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      #Ring_Utilisation_Report <- read.csv(Ring_Utilisation_Report_name,na.strings = c("NA", "", "<NA>"))
      # sending query to mysql db
      tryCatch(
        {
        Ring_Utilisation_Report = dbSendQuery(mydb_abstract_db, "select seq_no,ring_name,topology_type,total_capacity,free_vc4_ts,freevc3,free_vc12_ts,utlpercentage,ring_type, util_available from ring_utilization_report")

        # fetching data from mysql server
        Ring_Utilisation_Report = fetch(Ring_Utilisation_Report, n=-1)
        ring_util_cols <- c('seq_no','RING.NAME','Topology.Type','TOTAL.CAPACITY','Free.VC4.TS','FREEVC3','Free.VC12.TS','UTLPERCENTAGE','RING.TYPE', 'available_BW')

        colnames(Ring_Utilisation_Report) <- ring_util_cols
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

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Chamber Ring data - HandHole Access Rings - Network Check
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      chamber_ring <- hh_data_network


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
                                              between(cust_coords$cust_lat, P_lat - 0.1, P_lat + 0.1) & (cust_coords$cust_date <= TMP$Feasibility.Response..Created.Date | is.na(cust_coords$cust_date)==T)),]

          # cust_coords_sub <- subset(cust_coords,(cust_coords$cust_state == TMP$resp_state) 
        #                           & (cust_coords$cust_date <= TMP$Feasibility.Response..Created.Date | is.na(cust_coords$cust_date)==T) )
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
                                               between(prospect_coords$prospect_lat, P_lat - 0.1, P_lat + 0.1) & (prospect_coords$prospect_date <= TMP$Feasibility.Response..Created.Date)),]

        # prospect_dup_coords_sub <- subset(prospect_coords, 
        #                                   (prospect_coords$prospect_date <= TMP$Feasibility.Response..Created.Date) 
        #                                   & (prospect_coords$prospect_lat >= (TMP$Latitude_final-0.1) & prospect_coords$prospect_lat <= (TMP$Latitude_final+0.1))
        #                                   & (prospect_coords$prospect_lon >= (TMP$Longitude_final-0.1) & prospect_coords$prospect_lon <= (TMP$Longitude_final+0.1)
        #                                      &  (prospect_coords$Prospect_ID != TMP$Prospect_ID )
        #                                   ))

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

      #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Function to check for connected customers and connected buildings for LM costs
      #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

      fn_connected_bldgs <- function(ID){
        TMP <- subset(input_data,input_data$Prospect_ID == ID)
        P_long <- TMP$Longitude_final
        P_lat <- TMP$Latitude_final
        # reducing search space
        cust_coords_sub <- cust_coords[which(between(cust_coords$cust_long, P_long - 0.01, P_long + 0.01) &
                                               between(cust_coords$cust_lat, P_lat - 0.01, P_lat + 0.01) & (cust_coords$cust_date <= TMP$Feasibility.Response..Created.Date | is.na(cust_coords$cust_date)==T)),]
		
		#Creating an empty vector
		name_vec <-   c("V1","CUST_ID","SERVICE_ID","cust_date","cust_lat",
                      "cust_long", "cust_bw","cust_name",colnames(input_data))
		E <- data.frame(matrix(NA, nrow = 1, ncol = length(name_vec)))
		names(E) = name_vec

        # cust_coords_sub <- subset(cust_coords,(cust_coords$cust_state == TMP$resp_state) 
        #                           & (cust_coords$cust_date <= TMP$Feasibility.Response..Created.Date | is.na(cust_coords$cust_date)==T) )

        if(nrow(cust_coords_sub) ==0)
        {return(E)
        } else {
          TMP1 <- distHaversine(TMP[,c("Longitude_final","Latitude_final")],cust_coords_sub[,c("cust_long","cust_lat")])
          TMP1_c <- which(TMP1 <= 100)
          if(length(TMP1_c)==0)
          {return(E)
          }else{
            TMP2 <-as.data.frame(cbind(TMP1[TMP1_c],cust_coords_sub[TMP1_c,],as.data.frame(TMP[rep(1:nrow(TMP),each=length(TMP1_c)),])))
            #print(ID)
            return(TMP2)
            gc()}}}

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
          Ring_Utilisation_Report_n$f_nf <- ifelse(Ring_Utilisation_Report_n$available_BW > req_bw, 1, 0)
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

        if(nrow(df[df$connected_cust_tag>0, ]) > 0){
          # Step 1 : Finding mux of the connected customer (ServiceID --> MUX)
          # Find MUX associated with Service ID of connected customer
          connected_custs_mux <- merge(x = connected_custs,
                                       y = dropporttoservice,
                                       by.x = "SERVICE_ID",
                                       by.y = "SERVICEORIORID",
                                       all.x = T)
          rm(dropporttoservice)

          # Find all unique MUXs of all connected customers
          df_unique_mux <- data.frame(mux = unique(na.omit(connected_custs_mux$mux)))

          # Check if any MUX are found or not
          if(nrow(df_unique_mux)>0){

            # Step 2 : Finding Access ring based on MUX (MUX --> Access ring)
            df_unique_mux <- merge(x = df_unique_mux,
                                   y = TopologyTerminationReport_access,
                                   by.x = "mux",
                                   by.y = "NODENAME",
                                   all.x = T)
            rm(TopologyTerminationReport_access)

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

            # Merge with connected customers to finally check network feasibility
            connected_custs_mux <- merge(x = connected_custs_mux,
                                         y = df_unique_mux,
                                         by = "mux",
                                         all.x = T)
            # store mux info for later merge
            df_mux <- connected_custs_mux[,c("Prospect_ID","mux")]

            # F/ NF flag for each prospect ID
            connected_custs_mux <- connected_custs_mux %>% group_by(Prospect_ID) %>%
              dplyr::summarise(tot_access_f_nf = sum(access_f_nf, na.rm = T),
                               tot_core_f_nf = sum(core_f_nf, na.rm = T))

            connected_custs_mux$Network_F_NF_CC_Flag <- ifelse((connected_custs_mux$tot_access_f_nf > 0 &
                                                                  connected_custs_mux$tot_core_f_nf > 0), 
                                                               1, 0)

            connected_custs_mux$Network_F_NF_CC <- ifelse((connected_custs_mux$tot_access_f_nf > 0 &
                                                             connected_custs_mux$tot_core_f_nf > 0), 
                                                          "Network Feasible on CC", "Network Not Feasible on CC")

            connected_custs_mux$access_check_CC <- ifelse(connected_custs_mux$tot_access_f_nf > 0, 
                                                          "Network Feasible on Access Ring of CC",
                                                          "Network Not Feasible on Access Ring of CC")

            connected_custs_mux$core_check_CC <- ifelse(connected_custs_mux$tot_core_f_nf > 0,
                                                        "Network Feasible on Core Ring of CC", 
                                                        "Network Not Feasible on Core Ring of CC")

            # Merge with main input file
            df <- merge(x = df,
                        y = connected_custs_mux[,c("Prospect_ID",
                                                   "Network_F_NF_CC_Flag","Network_F_NF_CC",
                                                   "access_check_CC","core_check_CC")],
                        by = "Prospect_ID",
                        all.x = T)

            # merge to get mux name info
            df <- merge(x = df,
                        y = df_mux,
                        by = "Prospect_ID",
                        all.x = T)

          }else{
            # If no MUX match found then Network Not Feasible, move to next step to check HH in 0.5km
            df$Network_F_NF_CC_Flag <- 0
            df$Network_F_NF_CC <- "No MUX Found on CC"
            df$access_check_CC <- "No MUX Found on CC"
            df$core_check_CC <- "No MUX Found on CC"
            df$mux <- "No MUX Found on CC"
          }
        }else{
          # If no CC found then Network Not Feasible on CC, move to next step to check HH in 0.5km
          df$Network_F_NF_CC_Flag <- 0
          df$Network_F_NF_CC <- "No CC Found"
          df$access_check_CC <- "No CC Found"
          df$core_check_CC <- "No CC Found"
          df$mux <- "No CC Found"
        }
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
        # Create small DF with Prospect ID and HH
        df_hh <- data.frame(Prospect_ID = df$Prospect_ID, hh = df$HH_0_5km, BW_mbps = df$BW_mbps_2)
        # Step 1: Obtain access ring associated with hand hold ( HH --> Access Ring)
        df_hh <- merge(x = df_hh,
                       y = chamber_ring,
                       by.x = "hh",
                       by.y = "chamber_name",
                       all.x = T)
        rm(chamber_ring)

        # Step 2 : Access ring ----> Hub node
        df_hh <- merge(x = df_hh,
                       y = TopologyTerminationReport_hub,
                       by.x = "access_rings_hh",
                       by.y = "hub_ring",
                       all.x = T)
        rm(TopologyTerminationReport_hub)

        # Step 3 : Hub node ---> Core ring
        df_hh <- merge(x = df_hh,
                       y = TopologyTerminationReport_core,
                       by.x = "hub_node",
                       by.y = "NODENAME",
                       all.x = T)
        rm(TopologyTerminationReport_core)

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
          x["core_ring_hh"],
          x["BW_mbps"],
          Ring_Utilisation_Report))
        rm(Ring_Utilisation_Report)

        df_hh$core_capacity_flag_hh <- unlist(lapply(df_hh$result_c, "[[", 1))
        df_hh$result_c <- NULL

        # N/W F_NF Reason - Show ring names
        HH_0_5_access_rings_NF <- toString(unique(df_hh[df_hh$access_capacity_flag_hh==0,]$access_rings_hh))
        HH_0_5_access_rings_F <- toString(unique(df_hh[df_hh$access_capacity_flag_hh==1,]$access_rings_hh))

        #all name attributes stored separately
        df_names <- df_hh[,c("Prospect_ID","access_rings_hh","hub_node","core_ring")]
		
		df_names <- df_names %>% 
					  group_by(Prospect_ID) %>% 
					  mutate(hub_node = paste0(unique(hub_node), collapse = ","))
    
		df_names <- df_names %>% 
					  group_by(Prospect_ID) %>% 
					  mutate(core_ring = paste0(unique(core_ring), collapse = ","))
    
		df_names <- df_names %>% 
					  group_by(Prospect_ID) %>% 
					  mutate(access_rings_hh = paste0(unique(access_rings_hh), collapse = ","))
    
		df_names <- df_names[!duplicated(df_names),]

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

        df_hh$HH_0_5_access_rings_F <- HH_0_5_access_rings_F
        df_hh$HH_0_5_access_rings_NF <- HH_0_5_access_rings_NF

        # Merge with main input file
        df <- merge(x = df,
                    y = df_hh[,c("Prospect_ID","Network_F_NF_HH_Flag","Network_F_NF_HH",
                                 "access_check_hh","core_check_hh",
                                 "HH_0_5_access_rings_F","HH_0_5_access_rings_NF")],
                    by = "Prospect_ID",
                    all.x = T)
        df <- merge(x = df,
                    y = df_names,
                    by = "Prospect_ID",
                    all.x = T)
        return(df)
      }

      ##########################################################################################
      ##########################################################################################
      # Roll-up & Cleaning for each scenario
      # - Rolling up based on key
      ##########################################################################################
      ##########################################################################################

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # HH data - Roll up
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      hh_coords <- data.table(HH_ID = 1:nrow(hh_data_file),
                              hh_state = as.vector(hh_data_file$HH_STATE),
                              hh_lat=as.vector(as.numeric(hh_data_file$hh_lat)),
                              hh_long=as.vector(as.numeric(hh_data_file$hh_long)))

      #saveRDS(hh_coords, file = file.path(feature_data_location,"hh_data.rds"))

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Customer data - Roll up
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      cust_coords <- data.table(CUST_ID = 1:nrow(cust_data_file),
                                SERVICE_ID = as.vector(cust_data_file$SERVICEID),
                                #cust_state = as.vector(cust_data_file$CUSTOMER_LOCATION_STATE),
                                #cust_city = as.vector(cust_data_file$CUSTOMER_LOCATION_CITY),
                                cust_date = as.Date(cust_data_file$PROVISIONING_START_DATE),
                                cust_lat=as.vector(as.numeric(cust_data_file$Latitude)),
                                cust_long=as.vector(as.numeric(cust_data_file$Longitude)),
                                cust_bw = as.vector(as.numeric(cust_data_file$F12)),
                                cust_name = as.vector(cust_data_file$CUST_NAME))

      #saveRDS(cust_coords, file = file.path(feature_data_location,"cust_data.rds"))

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # MAN CITY data - Roll up
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      man_city <- man_city[!duplicated(man_city$CITY_NAME),]

      #saveRDS(man_city, file = file.path(feature_data_location,"man_city_data.rds"))

      ##########################################################################################
      ##########################################################################################
      # Feature Building
      ##########################################################################################
      ##########################################################################################
      tryCatch(
        {
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Pop related Features
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      pop_features_matrix <- bind_rows(lapply(as.list(input_data$Prospect_ID), fn_pop_distance_calc))

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
      # Remove later
      rm(pop_features_matrix)

      # Change column names
      colnames(input_data)[which(names(input_data) == "DistanceBetween")] <- "POP_DIST_KM"
      colnames(input_data)[which(names(input_data) == "DistanceBetween_service")] <- "POP_DIST_KM_SERVICE"

      # Add 1 more feature
      input_data$POP_DIST_KM_NOT_NULL <- ifelse(input_data$POP_DIST_KM > 0,1,0)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # FATG related Features
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      fatg_features_matrix <- bind_rows(lapply(as.list(input_data$Prospect_ID), fn_fatg_distance_calc))

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
      # Remove later
      rm(fatg_features_matrix)

      # Change column names
      colnames(input_data)[which(names(input_data) == "DistanceBetween")] <- "FATG_DIST_KM"


      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # HH related Features
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      hh_features_matrix <- bind_rows(lapply(as.list(input_data$Prospect_ID), fn_hh_distance_calc_features))

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

      rm(hh_features_matrix)

      # Change column names
      colnames(input_data)[which(names(input_data) == "DistanceBetween")] <- "HH_DIST_KM"

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Customer related Features
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
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

      # Merge features to input data
      input_data <- merge(x= input_data,
                          y=cust_features_matrix,
                          by.x="Prospect_ID",
                          by.y="Prospect_ID",
                          all.x=T)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Prospect related Features
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
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

      # Merge features to input data
      input_data <- merge(x= input_data,
                          y=pros_features_matrix,
                          by.x="Prospect_ID",
                          by.y="Prospect_ID",
                          all.x=T)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # MAN CITY related Features
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      input_data <- merge(x=input_data,y=man_city[,c("CITY_NAME","IsOnnetCity")],by.x="resp_city",by.y="CITY_NAME", all.x = T)

      # Clean MAN CIty feature
      input_data$OnnetCity_tag <- ifelse(is.na(input_data$IsOnnetCity)==T,1,0)

      ##########################################################################################
      ##########################################################################################
      # Feature Selection - Select only required features
      ##########################################################################################
      ##########################################################################################

      # Remove later
      #input_backup <- input_data

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
                    "Feasibility.Response..Created.Date",
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
                    #"Status_2")

      input_data <- input_data[,(names(input_data) %in% sel_cols)]
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

      ##########################################################################################
      ##########################################################################################
      # Input JSON column mapping with training set attribute categories
      ##########################################################################################
      ##########################################################################################
      # local loop interface
      input_data$local_loop_interface <- ifelse((grepl("fast", tolower(input_data$local_loop_interface)) & (grepl("ethernet", tolower(input_data$local_loop_interface)))), "FE",input_data$local_loop_interface)
      input_data$local_loop_interface <- ifelse((grepl("gigabit", tolower(input_data$local_loop_interface)) & (grepl("ethernet", tolower(input_data$local_loop_interface)))), "GE",input_data$local_loop_interface)

      # customer segment
      input_data$Customer_Segment <- ifelse((grepl("enterprise", tolower(input_data$Customer_Segment)) & (grepl("silver", tolower(input_data$Customer_Segment)))), "Enterprise ? Silver",input_data$Customer_Segment)
      input_data$Customer_Segment <- ifelse((grepl("enterprise", tolower(input_data$Customer_Segment)) & (grepl("gold", tolower(input_data$Customer_Segment)))), "Enterprise - Gold",input_data$Customer_Segment)
      input_data$Customer_Segment <- ifelse((grepl("enterprise", tolower(input_data$Customer_Segment)) & (grepl("mes", tolower(input_data$Customer_Segment)))), "Enterprise - MES",input_data$Customer_Segment)
      input_data$Customer_Segment <- ifelse((grepl("enterprise", tolower(input_data$Customer_Segment)) & (grepl("strategic", tolower(input_data$Customer_Segment)))), "Enterprise - Strategic",input_data$Customer_Segment)
      input_data$Customer_Segment <- ifelse((grepl("enterprise", tolower(input_data$Customer_Segment)) & (grepl("system integrators", tolower(input_data$Customer_Segment)))), "Enterprise - System Integrators",input_data$Customer_Segment)
      input_data$Customer_Segment <- ifelse((grepl("enterprise", tolower(input_data$Customer_Segment)) & (grepl("government/psu", tolower(input_data$Customer_Segment)))), "Enterprise ? Government/PSU",input_data$Customer_Segment)
      input_data$Customer_Segment <- ifelse((grepl("enterprise", tolower(input_data$Customer_Segment)) & (grepl("growth accounts", tolower(input_data$Customer_Segment)))), "Enterprise ? Growth Accounts",input_data$Customer_Segment)
      input_data$Customer_Segment <- ifelse((grepl("enterprise", tolower(input_data$Customer_Segment)) & (grepl("direct", tolower(input_data$Customer_Segment)))), "Enterprise-Direct",input_data$Customer_Segment)
      input_data$Customer_Segment <- ifelse(grepl("carriers", tolower(input_data$Customer_Segment)), "Carriers",input_data$Customer_Segment)

      # Sales org
      # input_data$Sales.Org <- ifelse(grepl("enterprise", tolower(input_data$Sales.Org)), "Enterprise",input_data$Sales.Org)
      # input_data$Sales.Org <- ifelse(grepl("service provider", tolower(input_data$Sales.Org)), "Service Provider",input_data$Sales.Org)
      # input_data$Sales.Org <- ifelse(grepl("cso", tolower(input_data$Sales.Org)), "CSO",input_data$Sales.Org)

      # last mile contract term
      # input_data$last_mile_contract_term <- "1 Year"

      ##########################################################################################
      ##########################################################################################
      tryCatch(
        {
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Cleaning all features
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      input_data$BW_mbps <- as.numeric(input_data$BW_mbps)
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

      input_data$Customer_Segment <- ifelse(input_data$Customer_Segment=="","XXX",as.character(input_data$Customer_Segment))

      input_data$POP_Network_Location_Type <- as.factor(input_data$POP_Network_Location_Type)
      input_data$POP_Construction_Status <- as.factor(input_data$POP_Construction_Status)
      input_data$POP_Building_Type <- as.factor(input_data$POP_Building_Type)
      input_data$POP_Category <- as.factor(input_data$POP_Category)
      input_data$POP_TCL_Access <- as.factor(input_data$POP_TCL_Access)
      input_data$FATG_Network_Location_Type <- as.factor(input_data$FATG_Network_Location_Type)
      input_data$FATG_Building_Type <- as.factor(input_data$FATG_Building_Type)
      input_data$FATG_Category <- as.factor(input_data$FATG_Category)
      input_data$FATG_TCL_Access <- as.factor(input_data$FATG_TCL_Access) 
      input_data$FATG_PROW <- as.factor(input_data$FATG_PROW )
      input_data$FATG_Ring_type <- as.factor(input_data$FATG_Ring_type) 
      input_data$Customer_Segment <- as.factor(input_data$Customer_Segment)

      #Recoding feasible and non fesible into 1 and 0
      #input_data$Status.v2 <- as.factor(ifelse(input_data$Status_2=="Feasible",1,0))
      #input_data <- subset(input_data,select=-c(Status_2))

      # level the factors
      input_data$Customer_Segment <- factor(input_data$Customer_Segment, levels = levels(onnet_wireline$Customer_Segment))
      input_data$Product.Name <- factor(input_data$Product.Name, levels = levels(onnet_wireline$Product.Name))
      input_data$POP_Network_Location_Type <- factor(input_data$POP_Network_Location_Type, levels = levels(onnet_wireline$POP_Network_Location_Type))
      input_data$POP_Construction_Status <- factor(input_data$POP_Construction_Status, levels = levels(onnet_wireline$POP_Construction_Status))
      input_data$POP_Building_Type <- factor(input_data$POP_Building_Type, levels = levels(onnet_wireline$POP_Building_Type))
      input_data$POP_Category <- factor(input_data$POP_Category, levels = levels(onnet_wireline$POP_Category))
      input_data$POP_TCL_Access <- factor(input_data$POP_TCL_Access, levels = levels(onnet_wireline$POP_TCL_Access))
      input_data$FATG_Network_Location_Type <- factor(input_data$FATG_Network_Location_Type, levels = levels(onnet_wireline$FATG_Network_Location_Type))
      input_data$FATG_Building_Type <- factor(input_data$FATG_Building_Type, levels = levels(onnet_wireline$FATG_Building_Type))
      input_data$FATG_Category <- factor(input_data$FATG_Category, levels = levels(onnet_wireline$FATG_Category))
      input_data$FATG_TCL_Access <- factor(input_data$FATG_TCL_Access, levels = levels(onnet_wireline$FATG_TCL_Access))
      input_data$FATG_PROW <- factor(input_data$FATG_PROW, levels = levels(onnet_wireline$FATG_PROW))
      input_data$FATG_Ring_type <- factor(input_data$FATG_Ring_type, levels = levels(onnet_wireline$FATG_Ring_type))

      # after levelling whichever are NAs - convert them
      input_data[vec][is.na(input_data[vec])] <- "xxx"
      input_data$Product.Name <- ifelse(is.na(input_data$Product.Name),"Others",as.character(input_data$Product.Name))
      input_data$Customer_Segment <- ifelse(is.na(input_data$Customer_Segment),"XXX",as.character(input_data$Customer_Segment))

      # again level the factors
      input_data$Customer_Segment <- factor(input_data$Customer_Segment, levels = levels(onnet_wireline$Customer_Segment))
      input_data$Product.Name <- factor(input_data$Product.Name, levels = levels(onnet_wireline$Product.Name))
      input_data$POP_Network_Location_Type <- factor(input_data$POP_Network_Location_Type, levels = levels(onnet_wireline$POP_Network_Location_Type))
      input_data$POP_Construction_Status <- factor(input_data$POP_Construction_Status, levels = levels(onnet_wireline$POP_Construction_Status))
      input_data$POP_Building_Type <- factor(input_data$POP_Building_Type, levels = levels(onnet_wireline$POP_Building_Type))
      input_data$POP_Category <- factor(input_data$POP_Category, levels = levels(onnet_wireline$POP_Category))
      input_data$POP_TCL_Access <- factor(input_data$POP_TCL_Access, levels = levels(onnet_wireline$POP_TCL_Access))
      input_data$FATG_Network_Location_Type <- factor(input_data$FATG_Network_Location_Type, levels = levels(onnet_wireline$FATG_Network_Location_Type))
      input_data$FATG_Building_Type <- factor(input_data$FATG_Building_Type, levels = levels(onnet_wireline$FATG_Building_Type))
      input_data$FATG_Category <- factor(input_data$FATG_Category, levels = levels(onnet_wireline$FATG_Category))
      input_data$FATG_TCL_Access <- factor(input_data$FATG_TCL_Access, levels = levels(onnet_wireline$FATG_TCL_Access))
      input_data$FATG_PROW <- factor(input_data$FATG_PROW, levels = levels(onnet_wireline$FATG_PROW))
      input_data$FATG_Ring_type <- factor(input_data$FATG_Ring_type, levels = levels(onnet_wireline$FATG_Ring_type))
      # after levelling whichever are NAs - convert them
      input_data[vec][is.na(input_data[vec])] <- "xxx"

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
                           "X5km_prospect_perc_feasible")

      input_data[,features_factor] = apply(input_data[features_factor], 2, function(x) as.numeric(as.character(x)));

      ##########################################################################################
      # Level mapping with Training data
      ##########################################################################################
      t_data <- onnent_wireline_under
      t_data$Identifier <- "Train"
      t_data$site_id <- "Site_VAL"
      t_extra_cols <- setdiff(colnames(input_data), colnames(t_data))
      i_extra_cols <- setdiff(colnames(t_data), colnames(input_data))
      t_data[,t_extra_cols] <- NA
      input_data[,i_extra_cols] <- NA
      input_data <- rbind(input_data,t_data)
      input_data <- input_data[which(is.na(input_data$Identifier)),]

      ##########################################################################################
      ##########################################################################################
      # Scoring the input data
      ##########################################################################################
      ##########################################################################################

      # Score the inputs
      input_data$Probabililty_Access_Feasibility = predict(rf_model_val,type = "prob",input_data)[,1]
	  
	  ceiling_dec <- function(x, level=2) round(x + 5*10^(-level-1), level)	  
	  input_data$Probabililty_Access_Feasibility <- sapply(input_data$Probabililty_Access_Feasibility, ceiling_dec)
	  input_data$Probabililty_Access_Feasibility <- as.numeric(as.character(input_data$Probabililty_Access_Feasibility))
	  
      # Predicting on cut off selected
      input_data$Predicted_Access_Feasibility <- ifelse(input_data$Probabililty_Access_Feasibility >= 0.75, "Feasible", "Not Feasible")
        }, 
      error=function(e){
        err <<- TRUE
        df_error$error_flag <- 1
        df_error$error_code <- "E8"
        df_error$error_msg <- "Model Error: Error while Scoring the Model. New levels seen in Input"
        df_error <<- cbind(input_json_data,df_error[,!(colnames(df_error) %in% colnames(input_json_data))])
      }
      )
      if(err==TRUE){
        return(df_error)
      }

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Remove data from memory which is not required from here onwards
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      rm(prospect_coords,
         pros_data,
         onnent_wireline_under,
         onnet_wireline,
         pop_data_file,
         fatg_data_file,
         hh_coords,
         hh_data_file
         )

      ##########################################################################################
      ##########################################################################################
      # Last Mile Cost Calculation
      ##########################################################################################
      ##########################################################################################
      tryCatch(
        {
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Getting nearest distance from service pop
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      input_data$local_loop_interface <- ifelse(input_data$local_loop_interface=="GE","GE","FE")

      #In case BW < 50 and it is GE,  we convert to FE
      input_data$local_loop_interface <- ifelse((input_data$BW_mbps<50 
                                                 & input_data$local_loop_interface == "GE"),"FE",
                                                as.character(input_data$local_loop_interface))

      #Rounding bandwidth to nearest 2 
      input_data$BW_mbps_2 <- as.numeric(as.character(input_data$BW_mbps))

      input_data$BW_mbps_2 <- ifelse(input_data$BW_mbps < 2,2,
                                     ifelse(((input_data$BW_mbps%%2==1) & (input_data$BW_mbps <= 100) & (input_data$local_loop_interface == "FE")),(input_data$BW_mbps+1),
                                            ifelse(((input_data$BW_mbps >100) & (input_data$BW_mbps%%50 >0) & (input_data$local_loop_interface == "FE")),plyr::round_any(input_data$BW_mbps,50), 
                                                   ifelse(((input_data$BW_mbps >=50) & (input_data$BW_mbps%%50 >0) & (input_data$local_loop_interface == "GE")),plyr::round_any(input_data$BW_mbps,50),
                                                          input_data$BW_mbps))))

      # Converting metres to Kms
      input_data$POP_DIST_KM_SERVICE <- input_data$POP_DIST_KM_SERVICE/1000*(1.25)
      input_data$POP_DIST_KM <- input_data$POP_DIST_KM/1000

      #Rounding distance to nearest 5 and putting upper limit of 501 and lower limit of 5 kms to it
      input_data$POP_DIST_KM_SERVICE_MOD <- plyr::round_any(input_data$POP_DIST_KM_SERVICE, 5)
      input_data$POP_DIST_KM_SERVICE_MOD <- ifelse(input_data$POP_DIST_KM_SERVICE_MOD > 501,501,ifelse(input_data$POP_DIST_KM_SERVICE_MOD==0,5,input_data$POP_DIST_KM_SERVICE_MOD))

      # Cleaning for ARC BW Rate cards
      # bw_fe_long <- melt(bw_fe,id.vars=c("Distance"))
      # bw_ge_long <- melt(bw_ge,id.vars=c("Distance"))
      # bw_fe_long$type <- "FE"
      # bw_ge_long$type <- "GE"
      # bw_all_stack <- rbind(bw_fe_long,bw_ge_long)
      # bw_all_stack$BW_mbps <- as.numeric(trimws(gsub("X","",bw_all_stack$variable)))

      #Merging rate card with input file to get corresponding rates to the distance
      input_data <- merge(x=input_data,
                          y=bw_all_stack,
                          by.x = c("BW_mbps_2","POP_DIST_KM_SERVICE_MOD","local_loop_interface"),
                          by.y=c("BW_mbps","Distance","type"),
                          all.x=T)

      #Assigning BW-ARC cost
      colnames(input_data)[colnames(input_data) == 'value'] <- 'bw_arc_cost'

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # MUX Cost, In-Building Capex cost, ne rental cost calculations
      # Checking whether prospect is amongst connected customers and connected buildings
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

      #Creating an empty vector
      name_vec <-   c("V1","CUST_ID","SERVICE_ID","cust_date","cust_lat",
                      "cust_long", "cust_bw","cust_name",colnames(input_data))
      E <- data.frame(matrix(NA, nrow = 1, ncol = length(name_vec)))
      names(E) = name_vec

      connected_custs <- rbind(lapply(as.list(as.character(input_data$Prospect_ID)), fn_connected_bldgs))
      connected_custs <- do.call(rbind,connected_custs)

      connected_custs$cust_name <- tolower(connected_custs$cust_name)
      connected_custs$prospect_name <- tolower(connected_custs$prospect_name)
      connected_custs_match <- subset(connected_custs,is.na(connected_custs$cust_name)==F)

      # if no customer is connected then do error handling and add 0 for corresponding features
      if(nrow(connected_custs_match)!=0){
        # See if the prospect is one of our own customer or not
        RecordLinkage_all <- plyr::empty(df)
        for(i in 1 : nrow(connected_custs_match)){
          if (connected_custs_match[i,c("prospect_name")]==""){RecordLinkage <- 0} else {
            RecordLinkage <- RecordLinkage::levenshteinSim(connected_custs_match[i,c("prospect_name")],connected_custs_match[i,c("cust_name")])
          }
          RecordLinkage_all <- rbind(RecordLinkage_all,RecordLinkage)
          #print(i)
        }
        RecordLinkage_all_2 <- as.data.frame(RecordLinkage_all)
        RecordLinkage_all_2 <- RecordLinkage_all_2[2:nrow(RecordLinkage_all_2),]
        connected_custs_match <- cbind(connected_custs_match,RecordLinkage_all_2)

        # Cutoff for similar text match taken at 0.7
        connected_custs_match$connected_cust <- ifelse(connected_custs_match$RecordLinkage_all_2 >= 0.7,1,0)
        connected_custs_match$connected_building <- 1

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
        input_data$num_connected_cust <- ifelse(is.na(input_data$num_connected_cust)==T,0,input_data$num_connected_cust)
        input_data$num_connected_building <- ifelse(is.na(input_data$num_connected_building)==T,0,input_data$num_connected_building)

        # create tags for 2 fields on which checks will be done
        input_data$connected_cust_tag <- ifelse(input_data$num_connected_cust >= 1,1,0)
        input_data$connected_building_tag <- ifelse(input_data$num_connected_building >= 1,1,0)
      }else{
        input_data$connected_cust_tag <- 0
        input_data$connected_building_tag <- 0
        input_data$Service_ID <- 0
        input_data$num_connected_cust <- 0
        input_data$num_connected_building <- 0
      }

      #Assigining MUX cost
      input_data$mux_cost <- ifelse(input_data$connected_cust_tag==1,0,
                                    ifelse(input_data$BW_mbps_2<=350,58810,
                                           ifelse(input_data$BW_mbps_2<=1000, 80611,
                                                  ifelse(input_data$BW_mbps_2<=2000, 623173,
                                                         ifelse(input_data$BW_mbps_2<=5000, 835108, 917744)))))

      #Assigning In Building Capex Costs
      input_data$in_building_capex_cost <- ifelse(input_data$connected_cust_tag==1,0,40000)

      #Assigning NE Rental cost
      input_data$ne_rental_cost <- 0

      #Assigning BW OTC charges
      input_data$bw_otc_cost <- 0

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # OSP Capex Cost Calculation
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

      #Retaining only relevant variables
      osp_cost <- man_city[,c("CITY_NAME","cost_permeter")]
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
      input_data$min_hh_fatg <- pmin(input_data$HH_DIST_KM,input_data$FATG_DIST_KM)
	  # take 25% extra as it's aerial distance
	  input_data$min_hh_fatg <- round(input_data$min_hh_fatg * 1.25)
      input_data$osp_capex_cost <- (input_data$cost_permeter)*(input_data$min_hh_fatg)

      # No OSP Capex if connected cust or connected bldg
      input_data$osp_capex_cost <- ifelse((input_data$connected_cust_tag==1)|(input_data$connected_building_tag==1),0,input_data$osp_capex_cost)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Total Cost Calculation
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      input_data$total_cost <- (input_data$bw_arc_cost+
                                  input_data$mux_cost +
                                  input_data$in_building_capex_cost +
                                  input_data$ne_rental_cost +
                                  input_data$bw_otc_cost +
                                  input_data$osp_capex_cost)
        }, 
      error=function(e){
        err <<- TRUE
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
      input_data$city_tier <- ifelse(input_data$resp_city %in% c('MUMBAI',
                                                                 'PUNE',
                                                                 'CHENNAI',
                                                                 'DELHI',
                                                                 'KOLKATA',
                                                                 'HYDERABAD',
                                                                 'BANGALORE',
                                                                 'AHMEDABAD'), "Tier1", "Non_Tier1")
      # Pre-Feasible scenarios
      input_data$scenario_1 <- ifelse((input_data$city_tier == "Tier1" &
                                         input_data$BW_mbps <= 45), 1, 0)  
      input_data$scenario_2 <- ifelse((input_data$city_tier == "Non_Tier1" &
                                         input_data$BW_mbps <= 2), 1, 0)
      # Pre-Feasible flag
      input_data$net_pre_feasible_flag <- ifelse((input_data$scenario_1+input_data$scenario_2)> 0, 1, 0)

      # Separate cases which are pre-feasible and not pre-feasible
      input_data_pre_f <- input_data[input_data$net_pre_feasible_flag==1, ]
      input_data_pre_nf <- input_data[input_data$net_pre_feasible_flag==0, ]

      # Check only if there is at least one request which is not Pre-Feasible
      if(nrow(input_data_pre_nf)>0){
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # Check Network Feasibility through MUX in Connected Customer for Not Feasible cases
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        input_data_pre_nf <- fn_Network_Feasibility_CC_Check(input_data_pre_nf)

        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # Check Network Feasibility through Handhole within 0.5kms for Not Feasible cases
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++  
        input_data_pre_nf <- fn_Network_Feasibility_HH_Check(input_data_pre_nf)

        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # Combine Pre Feasibile and Not Pre Feasible cases
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # Add extra columns in input_data_pre_f which are there in Pre NF
        pre_nf_col_diff <- setdiff(colnames(input_data_pre_nf),colnames(input_data_pre_f))
        extra_cols_df <- data.frame(matrix(ncol = length(pre_nf_col_diff), nrow = 0))
        colnames(extra_cols_df) <- pre_nf_col_diff

        # Add blank values on these extra columns
        if(nrow(input_data_pre_f)>0){
        input_data_pre_f[pre_nf_col_diff] <- "NA"
        }else{ 
          input_data_pre_f <- cbind(input_data_pre_f,extra_cols_df)
        }
        # Comine requests which are pre-feasible and not pre-feasible
        input_data <- rbind(input_data_pre_f,input_data_pre_nf)

      }else{
        col_extra <- c("Network_F_NF_CC_Flag",
                       "Network_F_NF_CC",
                       "access_check_CC",
                       "core_check_CC",
                       "HH_0_5km",
                       "hh_flag",
                       "Network_F_NF_HH_Flag",
                       "Network_F_NF_HH",
                       "access_check_hh",
                       "core_check_hh",
                       "HH_0_5_access_rings_F",
                       "HH_0_5_access_rings_NF")

        input_data_pre_f[col_extra] <- "NA"
        input_data <- input_data_pre_f
      }


      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Check final Network Feasibility
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++  
      input_data$Network_Feasibility_Check <- ifelse(((input_data$net_pre_feasible_flag == 1) |
                                                        (input_data$Network_F_NF_CC_Flag == 1) |
                                                        (input_data$Network_F_NF_HH_Flag == 1)),
                                                         "Feasible",
                                                         "Not Feasible")
        }, 
      error=function(e){
        err <<- TRUE
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

      # input_data$Orch_BW <- ifelse(input_data$BW_mbps_2<2, "lesser_than_2MB",
      #                              ifelse(input_data$BW_mbps_2==2, "2_MB",
      #                                            ifelse(input_data$BW_mbps_2<=10, "ge_2_10_MB",
      #                                                   ifelse(input_data$BW_mbps_2<=32, "ge_10_32_MB",
      #                                                          "ge_32_MB"))))

      input_data$Orch_BW <- input_data$BW_mbps

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # adjustment for "Capex greater than 175m" Orch_Category
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      input_data$Predicted_Access_Feasibility <- ifelse((input_data$Orch_Category=="Capex greater than 175m")&(input_data$Predicted_Access_Feasibility=="Feasible"), "Feasible with Capex", input_data$Predicted_Access_Feasibility)


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


      if(any(is.na(input_data))){
      input_data[is.na(input_data)] <- "NA"
      }

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

      # Add blank error attributes in case everything runs smoothly
      input_data$error_code <- "NA"
      input_data$error_flag <- 0
      input_data$error_msg <- "No error"

      # Remove cols which are not required or are duplicates in the output
      input_data$bw_mbps <- as.numeric(input_data$BW_mbps_act)

      rem_cols <- c("BW_mbps",
                    "BW_mbps_2",
                    "BW_mbps_act",
                    "Burstable_BW",
                    "Feasibility.Response..Created.Date",
                    "Latitude_final",
                    "Longitude_final",
                    "seq_no",
                    "sno",
                    "Capex",
                    "Status.v2",
                    "Identifier"
                    )

      input_data <- input_data[,!(names(input_data) %in% rem_cols)]

      # Disconnect DB connections once processing done
      lapply(dbListConnections(MySQL()), dbDisconnect)

      time_end <- proc.time() - time_start
      time_end <- time_end[['elapsed']]
      input_data$time_taken <- time_end
      #print(time_end)

      return(input_data)
    }
    '''
    r_model_call_single=robjects.r(rstr)
    r_output_df = r_model_call_single(input_data,path_py)
    py_output_df = pandas2ri.ri2py(r_output_df)
    output_dict = py_output_df.to_dict(orient='records')
    return jsonify(results=output_dict)


# In[ ]:


if __name__ =='__main__':
    app.run(port = 6000, debug = True)


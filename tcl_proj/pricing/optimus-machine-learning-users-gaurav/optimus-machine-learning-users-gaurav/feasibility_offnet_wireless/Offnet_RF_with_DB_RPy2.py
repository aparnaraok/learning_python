
# coding: utf-8

# In[2]:


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


# In[ ]:


path_py = os.path.dirname(os.path.abspath(__file__))


# In[3]:


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


# In[4]:


app = Flask(__name__)

@app.route('/api', methods = ['POST'])

def make_predict_offnet_rf():
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
      #Objective - Access Feasibility check for Offnet RF Scenario
      #Author - Gaurav Vibhandik
      #Create Date - 10/07/2018
      #Version - v1.0

      ##########################################################################################
      # SET WORKING DIRECTORY
      ##########################################################################################
      #setwd("E:/gv_personal_folder/prod_codes/gaurav_ETL/Offnet_RF")
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
      df_error <- data.frame('site_id' = 'NA','interim_BW' = 'NA','prospect_0_5km_Min_DistanceKilometers' = 'NA','prospect_0_5km_Avg_BW_Mbps' = 'NA','prospect_0_5km_Min_BW_Mbps' = 'NA','prospect_0_5km_Max_BW_Mbps' = 'NA','prospect_0_5km_feasibility_pct' = 'NA','prospect_0_5km_Sum_Feasibility_flag' = 'NA','prospect_2km_cust_Count' = 'NA','prospect_2km_Avg_DistanceKilometers' = 'NA','prospect_2km_Avg_BW_Mbps' = 'NA','prospect_2km_Min_BW_Mbps' = 'NA','prospect_2km_Max_BW_Mbps' = 'NA','prospect_2km_Sum_Feasibility_flag' = 'NA','prospect_2km_feasibility_pct' = 'NA','bw_flag_3' = 'NA','bw_flag_32' = 'NA','offnet_0_5km_cust_Count' = 'NA','offnet_0_5km_Min_DistanceKilometers' = 'NA','offnet_0_5km_Avg_BW_Mbps' = 'NA','offnet_0_5km_Min_BW_Mbps' = 'NA','offnet_0_5km_Max_BW_Mbps' = 'NA','offnet_0_5km_Min_accuracy_num' = 'NA','offnet_2km_cust_Count' = 'NA','offnet_2km_Min_DistanceKilometers' = 'NA','offnet_2km_Avg_BW_Mbps' = 'NA','offnet_2km_Min_BW_Mbps' = 'NA','offnet_2km_Min_accuracy_num' = 'NA','offnet_5km_Min_DistanceKilometers' = 'NA','offnet_5km_Avg_BW_Mbps' = 'NA','offnet_5km_Min_BW_Mbps' = 'NA','offnet_5km_Max_BW_Mbps' = 'NA','offnet_5km_Min_accuracy_num' = 'NA','provider_tot_towers' = 'NA','provider_min_dist' = 'NA','closest_provider' = 'NA','closest_provider_site' = 'NA','closest_provider_site_addr' = 'NA','closest_provider_bso_name' = 'NA','Probabililty_Access_Feasibility' = 'NA','Predicted_Access_Feasibility' = 'NA','arc_sify' = 'NA','otc_sify' = 'NA','arc_tikona' = 'NA','otc_tikona' = 'NA','lm_arc_bw_prov_ofrf' = 'NA','lm_nrc_bw_prov_ofrf' = 'NA','cust_count' = 'NA','min_mast_ht' = 'NA','avg_mast_ht' = 'NA','max_mast_ht' = 'NA','nearest_mast_ht' = 'NA','nearest_mast_ht_cost' = 'NA','lm_nrc_mast_ofrf' = 'NA','total_cost' = 'NA','Orch_LM_Type' = 'NA','Orch_Connection' = 'NA','Orch_Category' = 'NA','Orch_BW' = 'NA','latitude_final' = 'NA','longitude_final' = 'NA','prospect_name' = 'NA','bw_mbps' = 'NA','burstable_bw' = 'NA','resp_city' = 'NA','customer_segment' = 'NA','sales_org' = 'NA','product_name' = 'NA','feasibility_response_created_date' = 'NA','local_loop_interface' = 'NA','last_mile_contract_term' = 'NA','account_id_with_18_digit' = 'NA','opportunity_term' = 'NA','quotetype_quote' = 'NA','connection_type' = 'NA','sum_no_of_sites_uni_len' = 'NA','cpe_variant' = 'NA','cpe_management_type' = 'NA','cpe_supply_type' = 'NA','topology' = 'NA','additional_ip_flag' = 'NA','ip_address_arrangement' = 'NA','ipv4_address_pool_size' = 'NA','ipv6_address_pool_size' = 'NA','lm_arc_bw_onwl' = 'NA','lm_nrc_bw_onwl' = 'NA','lm_nrc_mux_onwl' = 'NA','lm_nrc_inbldg_onwl' = 'NA','lm_nrc_ospcapex_onwl' = 'NA','lm_nrc_nerental_onwl' = 'NA','lm_arc_bw_onrf' = 'NA','lm_nrc_bw_onrf' = 'NA','lm_nrc_mast_onrf' = 'NA','error_code' = 'NA','error_flag' = 'NA','error_msg' = 'NA','time_taken' = 'NA')

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
      packages <- c("dplyr","readxl","geosphere","gdata","lubridate","data.table",
                    "sqldf","randomForest","RMySQL")
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
      library(readxl)
      library(geosphere)
      library(lubridate)
      library(data.table)
      library(sqldf)
      library(randomForest)
      library(gdata)
      library(RMySQL)
      library(jsonlite)
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
      # R Code
      ##########################################################################################
      ##########################################################################################
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Read Input JSON File
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      tryCatch(
        {
      #input_data <- dplyr::bind_rows(fromJSON("input_json.json"))

      #input_json_data <- input_data

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

      #*************** File names *************************************
      model_object_name <- "Offnet_RF_Model_mtry_7_nodesize_300_ntree_300.rdata"
      #prospect_data_name <- "prospect_data.rds"

      #service_provider_name <- "Provider_name_Cleanup.xlsx"
      #offnet_rf_customer_file_name <- "Offnet_wireless_customers_updated_from_Ankur's_file.csv"
      # aircel_bs_name <- "aircelbs.csv"
      # airtel_bs_name <- "airtelbs.csv"
      # sify_bs_name <- "sifybs.csv"
      # tikona_bs_name <- "tikonabs.csv"
      # bw_costs <- "RC Wireless_Output_V1.csv"
      # #mast_ht <- "Feasibility Mast Height & CD for Oct16 to Nov17 Responses.xlsx"
      #mast_ht <- "mast_ht_data_all.rds"
      youden_cutoff <-0.72

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Database Connection
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      tryCatch(
        {
      #establishing connection
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
      rf_model <- get(load(model_object_name))
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
      # Prospect Data - Import
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      tryCatch(
        {
      #prospect_data <- readRDS(prospect_data_name)
      prospect_data = dbSendQuery(mydb_abstract_db, "select Provider_Name, Feasibility_Response_Feasibility_Response_Auto_No, Onnet_Offnet,Wireline_or_RF, Status, CustomerLatitude1, CustomerLongitude1, Feasibility_Response_Created_Date, resp_state, Request_no, L1_or_L2, Response_related_to_2, Cleaned_BW, Final_Provider_Name, Feasibility_flag   from Prospect_Rolled_Up_Offnet_RF")
      # fetching data from mysql server
      prospect_data = fetch(prospect_data, n=-1)

      # Column Mapping
      pros_cols <- c("Provider.Name","Feasibility.Response..Feasibility.Response.Auto.No.","Onnet.Offnet","Wireline.or.RF","Status","CustomerLatitude1","CustomerLongitude1","Feasibility.Response..Created.Date","resp_state", "Request_no","L1.or.L2","Response_related_to","BW_mbps","Final_Provider_Name","Feasibility_flag")

      colnames(prospect_data) <- pros_cols

      prospect_data$CustomerLatitude1 <- as.numeric(prospect_data$CustomerLatitude1)
      prospect_data$CustomerLongitude1 <- as.numeric(prospect_data$CustomerLongitude1)
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

      #prospect_coords <- pros_data

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Service Provider Data - Import
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      tryCatch(
        {
      # service_provider <- read_excel(service_provider_name,
      #                                sheet = "Mapped_Name",
      #                                na = c("", "#N/A", "<NA>"))
      # sending query to mysql db
      service_provider = dbSendQuery(mydb_abstract_db, "select * from provider_name_cleanup")

      # fetching data from mysql server
      service_provider = fetch(service_provider, n=-1) 
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
      # Customer Data - Import
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      tryCatch(
        {
      # cust_data <- read.csv(offnet_rf_customer_file_name,
      #                              na.strings = c(""),
      #                              stringsAsFactors = F)

      offnet_cust_data = dbSendQuery(mydb_abstract_db, "select TCL_SERVICE_ID, Commissioning_Date, BW_In_MB, accuracy_num, Longitude, Latitude from Prospect_Customer_Rolled_Up_data_Offnet_RF")

      # fetching data from mysql server
      offnet_cust_data = fetch(offnet_cust_data, n=-1)

      # Column Mapping
      cust_cols <- c("TCL.SERVICE.ID","Commissioning.Date","BW.In.MB","accuracy_num","Longitude","Latitude")

      colnames(offnet_cust_data) <- cust_cols

      offnet_cust_data$Latitude <- as.numeric(offnet_cust_data$Latitude)
      offnet_cust_data$Longitude <- as.numeric(offnet_cust_data$Longitude)
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
      # Aircel Data - Import
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # aircel_data <- read.csv(aircel_bs_name,
      #                         na.strings = c("", "#N/A", "<NA>"),
      #                         stringsAsFactors = F)
      # sending query to mysql db
      #aircel_data = dbSendQuery(mydb_abstract_db, "select * from aircel_bs_data")

      # fetching data from mysql server
      #aircel_data = fetch(aircel_data, n=-1)


      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Airtel Data - Import
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # airtel_data <- read.csv(airtel_bs_name,
      #                         na.strings = c("", "#N/A", "<NA>"),
      #                         stringsAsFactors = F)
      # sending query to mysql db
      #airtel_data = dbSendQuery(mydb_abstract_db, "select * from airtel_bs_data")

      # fetching data from mysql server
      #airtel_data = fetch(airtel_data, n=-1)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Sify Data - Import
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      tryCatch(
        {
      # sify_data <- read.csv(sify_bs_name,
      #                       na.strings = c("", "#N/A", "<NA>"),
      #                       stringsAsFactors = F)
      # sending query to mysql db
      sify_data = dbSendQuery(mydb_abstract_db, "select * from sify_bs_data")

      # fetching data from mysql server
      sify_data = fetch(sify_data, n=-1)
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
      # Tikona Data - Import
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      tryCatch(
        {
      # tikona_data <- read.csv(tikona_bs_name,
      #                         na.strings = c("", "#N/A", "<NA>"),
      #                         stringsAsFactors = F)
      # sending query to mysql db
      tikona_data = dbSendQuery(mydb_abstract_db, "select * from tikona_bs_data")

      # fetching data from mysql server
      tikona_data = fetch(tikona_data, n=-1)
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
      # ARC BW Cost Data - Import
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      tryCatch(
        {
      #arc_bw_cost <- read.csv(bw_costs)
      # sending query to mysql db
      arc_bw_cost = dbSendQuery(mydb_abstract_db, "select bw_mbps,vendor,arc,otc from cq_offnet_vendor_rc")

      # fetching data from mysql server
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

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Mast Height Cost Data - Import
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      tryCatch(
        {
      # Obtaining all columns from feasibility prospect data
      mast_ht_data_all = dbSendQuery(mydb_abstract_db, "select * from Onnet_RF_prospect_coords_2")
      # Fetching data
      mast_ht_data_all = fetch(mast_ht_data_all, n=-1)

      prospect_coords <- mast_ht_data_all[c("prospect_date",
                                            "prospect_lat",
                                            "prospect_lon")]

      prospect_coords_new <- mast_ht_data_all[c("prospect_date",
                                                "prospect_lat",
                                                "prospect_lon",
                                                "prospect_mast_ht")]

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


      ##########################################################################################
      ##########################################################################################
      # FUNTIONS - User defined functions - Add them to source file later
      ##########################################################################################
      ##########################################################################################

      #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Function to calculate features for Prospect locations
      #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      fn_offnet_rf_prospect_distance_calc <- function(ID){
        TMP <- subset(input_data,input_data$Prospect_ID == ID)
        P_long <- TMP$Longitude_final
        P_lat <- TMP$Latitude_final
        prospect_dup_coords_sub <- prospect_data[which(between(prospect_data$CustomerLongitude1, P_long - 0.1, P_long + 0.1) &
                                                           between(prospect_data$CustomerLatitude1, P_lat - 0.1, P_lat + 0.1)),]

        if (nrow(prospect_dup_coords_sub) == 0) {
          #print("99999 error")
          E = c(ID,9999999,0,0,9999999,9999999,9999999,9999999,9999999,9999999,0,0,9999999,9999999,9999999,9999999,9999999)
          return(E)
        }else {
          tryCatch({
            TMP1 <- distHaversine(TMP[,c("Longitude_final","Latitude_final")],prospect_dup_coords_sub[,c("CustomerLongitude1","CustomerLatitude1")])
            dist_condn <- c(500,2000)
            summ <- sapply(dist_condn, function(x){
              TMP1_c <- which(TMP1 <= x)
              data.frame(
                cust_count = as.numeric(length(TMP1_c)),
                avg_dist = as.numeric(mean(TMP1[TMP1_c],na.rm = T)/1000),
                min_dist = as.numeric(min(TMP1[TMP1_c],na.rm = T)/1000),
                avg_bw = as.numeric(mean(as.vector(as.numeric(as.character(prospect_dup_coords_sub$BW_mbps[TMP1_c]))),na.rm = T)),
                min_bw = as.numeric(min(as.vector(as.numeric(as.character(prospect_dup_coords_sub$BW_mbps[TMP1_c]))),na.rm = T)),
                max_bw = as.numeric(max(as.vector(as.numeric(as.character(prospect_dup_coords_sub$BW_mbps[TMP1_c]))),na.rm = T)),
                num_feasible =  as.numeric(length(which(as.vector(prospect_dup_coords_sub$Status[TMP1_c])=="Feasible"))),
                perc_feasible = as.numeric(length(which(as.vector(prospect_dup_coords_sub$Status[TMP1_c])=="Feasible"))/length(TMP1_c)))
            })
            TMP2 <- c(ID,as.vector(unlist(summ)))
            #print(ID)
            return(TMP2)
            gc()},
          error = function(error_message) {
            #print("Error Encountered")
            E = c(ID,9999999,0,0,9999999,9999999,9999999,9999999,9999999,9999999,0,0,9999999,9999999,9999999,9999999,9999999)
            return(E)
          }
          )
        }
      }

      #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Function to calculate features for Prospect locations
      #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

      fn_offnet_RF_customer_distance_calc <- function(P_lat, P_long, p_date ,offnet_cust_data_n){

        p_date <- as.Date(p_date, format = "%Y-%m-%d")
        P_long <- as.numeric(P_long)
        P_lat  <- as.numeric(P_lat)

        # reducing search space ******* Null condition added as missing are considered to be old customers
        offnet_cust_data_n <- offnet_cust_data_n[which(between(offnet_cust_data_n$Longitude, P_long - 0.1, P_long + 0.1) &
                                                         between(offnet_cust_data_n$Latitude, P_lat - 0.1, P_lat + 0.1) &
                                                         offnet_cust_data_n$Commissioning.Date < p_date
        ),] 
        if (nrow(offnet_cust_data_n) == 0) {
          #print("99999 error")
          return (c(
            'offnet_0_5km_cust_Count' = NA ,
            'offnet_0_5km_Avg_DistanceKilometers' = NA ,
            'offnet_0_5km_Min_DistanceKilometers' = NA ,
            'offnet_0_5km_Avg_BW_Mbps' = NA ,
            'offnet_0_5km_Min_BW_Mbps' = NA ,
            'offnet_0_5km_Max_BW_Mbps' = NA ,
            'offnet_0_5km_Min_accuracy_num' = NA ,
            'offnet_2km_cust_Count' = NA ,
            'offnet_2km_Avg_DistanceKilometers' = NA ,
            'offnet_2km_Min_DistanceKilometers' = NA ,
            'offnet_2km_Avg_BW_Mbps' = NA ,
            'offnet_2km_Min_BW_Mbps' = NA ,
            'offnet_2km_Max_BW_Mbps' = NA ,
            'offnet_2km_Min_accuracy_num' = NA ,
            'offnet_5km_cust_Count' = NA ,
            'offnet_5km_Avg_DistanceKilometers' = NA ,
            'offnet_5km_Min_DistanceKilometers' = NA ,
            'offnet_5km_Avg_BW_Mbps' = NA ,
            'offnet_5km_Min_BW_Mbps' = NA ,
            'offnet_5km_Max_BW_Mbps' = NA ,
            'offnet_5km_Min_accuracy_num' = NA
          ))
        }

        else {

          tryCatch( {

            offnet_cust_data_n$offnet_distance_km <- distHaversine(
              c(P_long, P_lat),
              offnet_cust_data_n[, c("Longitude","Latitude")])
            offnet_cust_data_n$offnet_distance_km <- offnet_cust_data_n$offnet_distance_km/ 1000

            for_0_5_km <- offnet_cust_data_n[which(offnet_cust_data_n$offnet_distance_km <= 0.5),]
            for_2_km <- offnet_cust_data_n[which(offnet_cust_data_n$offnet_distance_km <= 2),]
            for_5_km <- offnet_cust_data_n[which(offnet_cust_data_n$offnet_distance_km <= 5),]

            # Summary for 0.5 KM
            if (nrow(for_0_5_km) > 0) {
              offnet_0_5km_cust_Count = nrow(for_0_5_km)
              offnet_0_5km_Avg_DistanceKilometers = mean(for_0_5_km$offnet_distance_km, na.rm = T)
              offnet_0_5km_Min_DistanceKilometers = min(for_0_5_km$offnet_distance_km, na.rm = T)
              offnet_0_5km_Avg_BW_Mbps = mean(for_0_5_km$BW.In.MB, na.rm = T)
              offnet_0_5km_Min_BW_Mbps = min(for_0_5_km$BW.In.MB, na.rm = T)
              offnet_0_5km_Max_BW_Mbps = max(for_0_5_km$BW.In.MB, na.rm = T)
              offnet_0_5km_Min_accuracy_num = min(for_0_5_km$accuracy_num, na.rm = T)
            } else {
              offnet_0_5km_cust_Count = NA
              offnet_0_5km_Avg_DistanceKilometers = NA
              offnet_0_5km_Min_DistanceKilometers = NA
              offnet_0_5km_Avg_BW_Mbps = NA
              offnet_0_5km_Min_BW_Mbps = NA
              offnet_0_5km_Max_BW_Mbps = NA
              offnet_0_5km_Min_accuracy_num = NA
            }

            # Summary for 2 KM
            if (nrow(for_2_km) > 0) {
              offnet_2km_cust_Count = nrow(for_2_km)
              offnet_2km_Avg_DistanceKilometers = mean(for_2_km$offnet_distance_km, na.rm = T)
              offnet_2km_Min_DistanceKilometers = min(for_2_km$offnet_distance_km, na.rm = T)
              offnet_2km_Avg_BW_Mbps = mean(for_2_km$BW.In.MB, na.rm = T)
              offnet_2km_Min_BW_Mbps = min(for_2_km$BW.In.MB, na.rm = T)
              offnet_2km_Max_BW_Mbps = max(for_2_km$BW.In.MB, na.rm = T)
              offnet_2km_Min_accuracy_num = min(for_2_km$accuracy_num, na.rm = T)
            } else {
              offnet_2km_cust_Count = NA
              offnet_2km_Avg_DistanceKilometers = NA
              offnet_2km_Min_DistanceKilometers = NA
              offnet_2km_Avg_BW_Mbps = NA
              offnet_2km_Min_BW_Mbps = NA
              offnet_2km_Max_BW_Mbps = NA
              offnet_2km_Min_accuracy_num = NA
            }

            # Summary for 5 KM
            if (nrow(for_5_km) > 0) {
              offnet_5km_cust_Count = nrow(for_5_km)
              offnet_5km_Avg_DistanceKilometers = mean(for_5_km$offnet_distance_km, na.rm = T)
              offnet_5km_Min_DistanceKilometers = min(for_5_km$offnet_distance_km, na.rm = T)
              offnet_5km_Avg_BW_Mbps = mean(for_5_km$BW.In.MB, na.rm = T)
              offnet_5km_Min_BW_Mbps = min(for_5_km$BW.In.MB, na.rm = T)
              offnet_5km_Max_BW_Mbps = max(for_5_km$BW.In.MB, na.rm = T)
              offnet_5km_Min_accuracy_num = min(for_5_km$accuracy_num, na.rm = T)
            } else {
              offnet_5km_cust_Count = NA
              offnet_5km_Avg_DistanceKilometers = NA
              offnet_5km_Min_DistanceKilometers = NA
              offnet_5km_Avg_BW_Mbps = NA
              offnet_5km_Min_BW_Mbps = NA
              offnet_5km_Max_BW_Mbps = NA
              offnet_5km_Min_accuracy_num = NA
            }
            #print(P_lat)
            return (c(
              'offnet_0_5km_cust_Count' = offnet_0_5km_cust_Count ,
              'offnet_0_5km_Avg_DistanceKilometers' = offnet_0_5km_Avg_DistanceKilometers ,
              'offnet_0_5km_Min_DistanceKilometers' = offnet_0_5km_Min_DistanceKilometers ,
              'offnet_0_5km_Avg_BW_Mbps' = offnet_0_5km_Avg_BW_Mbps ,
              'offnet_0_5km_Min_BW_Mbps' = offnet_0_5km_Min_BW_Mbps ,
              'offnet_0_5km_Max_BW_Mbps' = offnet_0_5km_Max_BW_Mbps ,
              'offnet_0_5km_Min_accuracy_num' = offnet_0_5km_Min_accuracy_num ,
              'offnet_2km_cust_Count' = offnet_2km_cust_Count ,
              'offnet_2km_Avg_DistanceKilometers' = offnet_2km_Avg_DistanceKilometers ,
              'offnet_2km_Min_DistanceKilometers' = offnet_2km_Min_DistanceKilometers ,
              'offnet_2km_Avg_BW_Mbps' = offnet_2km_Avg_BW_Mbps ,
              'offnet_2km_Min_BW_Mbps' = offnet_2km_Min_BW_Mbps ,
              'offnet_2km_Max_BW_Mbps' = offnet_2km_Max_BW_Mbps ,
              'offnet_2km_Min_accuracy_num' = offnet_2km_Min_accuracy_num ,
              'offnet_5km_cust_Count' = offnet_5km_cust_Count ,
              'offnet_5km_Avg_DistanceKilometers' = offnet_5km_Avg_DistanceKilometers ,
              'offnet_5km_Min_DistanceKilometers' = offnet_5km_Min_DistanceKilometers ,
              'offnet_5km_Avg_BW_Mbps' = offnet_5km_Avg_BW_Mbps ,
              'offnet_5km_Min_BW_Mbps' = offnet_5km_Min_BW_Mbps ,
              'offnet_5km_Max_BW_Mbps' = offnet_5km_Max_BW_Mbps ,
              'offnet_5km_Min_accuracy_num' = offnet_5km_Min_accuracy_num
            ))

          }, 
          error = function(error_message) {
            #print("Error Encountered")
            return(c(
              'offnet_0_5km_cust_Count' = NA ,
              'offnet_0_5km_Avg_DistanceKilometers' = NA ,
              'offnet_0_5km_Min_DistanceKilometers' = NA ,
              'offnet_0_5km_Avg_BW_Mbps' = NA ,
              'offnet_0_5km_Min_BW_Mbps' = NA ,
              'offnet_0_5km_Max_BW_Mbps' = NA ,
              'offnet_0_5km_Min_accuracy_num' = NA ,
              'offnet_2km_cust_Count' = NA ,
              'offnet_2km_Avg_DistanceKilometers' = NA ,
              'offnet_2km_Min_DistanceKilometers' = NA ,
              'offnet_2km_Avg_BW_Mbps' = NA ,
              'offnet_2km_Min_BW_Mbps' = NA ,
              'offnet_2km_Max_BW_Mbps' = NA ,
              'offnet_2km_Min_accuracy_num' = NA ,
              'offnet_5km_cust_Count' = NA ,
              'offnet_5km_Avg_DistanceKilometers' = NA ,
              'offnet_5km_Min_DistanceKilometers' = NA ,
              'offnet_5km_Avg_BW_Mbps' = NA ,
              'offnet_5km_Min_BW_Mbps' = NA ,
              'offnet_5km_Max_BW_Mbps' = NA ,
              'offnet_5km_Min_accuracy_num' = NA 
            ))
          })
        }
      }

      #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Function to calculate features for Prospect locations
      #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      fn_offnet_rf_vendor_distance_calc <- function(P_lat,
                                                    P_long,
                                                    vendor_data_n = vendor_data){

        P_long <- as.numeric(P_long)
        P_lat  <- as.numeric(P_lat)

        # reducing BTS search space
        vendor_data_n <- vendor_data_n[which(between(vendor_data_n$Longitude, P_long - 0.1, P_long + 0.1) &
                                               between(vendor_data_n$Latitude, P_lat - 0.1, P_lat + 0.1)
        ),] 

        if (nrow(vendor_data_n) == 0) {
          #print("No BS in 0.1")
          return (c("vendor_min_dist_km" = NA,
                    "vendor_site_id" = NA,
                    "vendor_site_address" = NA,
                    "vendor_bso_name" = NA,
                    "vendor_3km_radius" = NA,
                    "vendor_avg_dist_3km" = NA))
        }

        else {

          tryCatch( {
            # Calculating Distance
            vendor_data_n$vendor_distance_km <- distHaversine(
              c(as.numeric(P_long), as.numeric(P_lat)),
              vendor_data_n[, c("Longitude","Latitude")])

            vendor_data_n$vendor_distance_km <- vendor_data_n$vendor_distance_km/1000

            # Distance to closest BTS Tower
            vendor_min_dist_km <- min(vendor_data_n$vendor_distance_km)
            vendor_site_id <- vendor_data_n$site_id[match(min(vendor_data_n$vendor_distance_km), vendor_data_n$vendor_distance_km)]
            vendor_site_address <- vendor_data_n$site_address[match(min(vendor_data_n$vendor_distance_km), vendor_data_n$vendor_distance_km)]
            vendor_bso_name <- vendor_data_n$bso_name[match(min(vendor_data_n$vendor_distance_km), vendor_data_n$vendor_distance_km)]

            # Number of BTS towers in 3 KM radius
            for_3_km <- vendor_data_n[which(vendor_data_n$vendor_distance_km <= 3),]
            if (nrow(for_3_km) > 0) {
              vendor_3km_radius <- length(unique(for_3_km$Site_ID))
              vendor_avg_dist_3km <- mean(for_3_km$vendor_distance_km, na.rm = T)
            } else {
              vendor_3km_radius = 0
              vendor_avg_dist_3km = NA
            }

            #print(vendor_min_dist_km)
            return (c("vendor_min_dist_km" = vendor_min_dist_km,
                      "vendor_site_id" = vendor_site_id,
                      "vendor_site_address" = vendor_site_address,
                      "vendor_bso_name" = vendor_bso_name,
                      "vendor_3km_radius" = vendor_3km_radius,
                      "vendor_avg_dist_3km" = vendor_avg_dist_3km
            ))

          }, 
          error = function(error_message) {
            #print("Error Encountered")
            return(c("vendor_min_dist_km" = NA,
                     "vendor_site_id" = NA,
                     "vendor_site_address" = NA,
                     "vendor_bso_name" = NA,
                     "vendor_3km_radius" = NA,
                     "vendor_avg_dist_3km" = NA
            ))
          })
        }
      }

      #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Function to find out closest offnet provider
      #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      fn_offnet_rf_find_closest_provider <- function(x){
        closest_provider_idx <- ifelse(sum(is.na(x))==length(x),1,which.min(x))
        return (closest_provider_idx)
      }

      #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Function to identify nearby Mast Heights of historical prospects
      #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      fn_mast_ht_prospects_offnet_rf <- function(ID){
        #TMP <- subset(prospect_coords,prospect_coords$Prospect_ID == ID)
        TMP <- subset(input_data,input_data$Prospect_ID == ID)
        prospect_dup_coords_sub <- subset(prospect_coords_new, 
                                          (prospect_coords_new$prospect_date <= TMP$Feasibility.Response..Created.Date))
        if(nrow(prospect_dup_coords_sub)==0)
        {E = data.frame(Prospect_ID =ID,cust_count =0,min_mast_ht = 0
                        ,avg_mast_ht = 0,max_mast_ht=0,nearest_mast_ht=0)
        return(E)
        } else {
          TMP1 <- distHaversine(TMP[,c("Longitude_final","Latitude_final")],prospect_dup_coords_sub[,c("prospect_lon","prospect_lat")])
          TMP1_c <- which(TMP1 <= 3000)
          if(length(TMP1_c) ==0)
          {E = data.frame(Prospect_ID =ID,cust_count =0,min_mast_ht = 0
                          ,avg_mast_ht = 0,max_mast_ht=0,nearest_mast_ht=0)
          return(E)
          } else {
            TMP1_c_min <- which(TMP1 <= 3000 & TMP1==min(TMP1))
            TMP1_metrics <- prospect_dup_coords_sub[TMP1_c,]
            TMP1_metrics_min <- prospect_dup_coords_sub[TMP1_c_min,]
            cust_count <- nrow(TMP1_metrics)
            min_mast_ht <- min(as.numeric(TMP1_metrics$prospect_mast_ht),na.rm=T)
            max_mast_ht <- max(as.numeric(TMP1_metrics$prospect_mast_ht),na.rm=T)
            avg_mast_ht <- mean(as.numeric(TMP1_metrics$prospect_mast_ht),na.rm=T)
            nearest_mast_ht <- max(as.numeric(TMP1_metrics_min$prospect_mast_ht))
            TMP2 <- data.frame(Prospect_ID =ID,cust_count = as.numeric(cust_count),min_mast_ht = as.numeric(min_mast_ht)
                               ,avg_mast_ht = as.numeric(avg_mast_ht),max_mast_ht=as.numeric(max_mast_ht),nearest_mast_ht=as.numeric(nearest_mast_ht))
            #print(ID)
            return(TMP2)
            gc()}}}

      #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Function for cleaning interim BWs
      #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      interim_BW_func <- function(BW) {

        interim_BW <- as.numeric(BW)
        if(!(BW %in% c(0.064,
                       0.128,
                       0.256,
                       0.512,
                       1.000,
                       2.000)) ) {

          interim_BW <- ifelse(BW < 0.064, 0.064,
                               ifelse(BW < 0.128, 0.128,
                                      ifelse(BW < 0.256, 0.256,
                                             ifelse(BW < 0.512, 0.512,
                                                    ifelse(BW < 1.000, 1.000, 2.000)))))
        }
        return(interim_BW)
      }


      ##########################################################################################
      ##########################################################################################
      # Pre-processing & Cleaning for each scenario
      # - Inclusions & Exclusions
      # - Sanity Checks & Missing value imputation
      # - Logic checks for important fields
      ##########################################################################################
      ##########################################################################################

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Prospect data - pre-processing & cleaning
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Customer data - pre-processing & cleaning
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Vendor data - pre-processing & cleaning
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # a) Renaming fields for merging
      # aircel_data <- dplyr::rename(aircel_data,
      #                              Longitude = X_Coordinates,
      #                              Latitude = Y_Coordinates)
      # airtel_data <- dplyr::rename(airtel_data,
      #                              Longitude = X_Coordinates,
      #                              Latitude = Y_Coordinates)
      # sify_data <- dplyr::rename(sify_data,
      #                            Longitude = X_Coordinates,
      #                            Latitude = Y_Coordinates)
      # tikona_data <- dplyr::rename(tikona_data,
      #                              Longitude = X_Coordinates,
      #                              Latitude = Y_Coordinates)
      # 
      # aircel_data <- fn_clean_lat_long_add(aircel_data, 
      #                                      lat_col = 'Latitude', 
      #                                      long_col = 'Longitude', 
      #                                      lat_round = '', 
      #                                      long_round = '',
      #                                      level_req_flag = 'F') 
      # 
      # airtel_data <- fn_clean_lat_long_add(airtel_data, 
      #                                      lat_col = 'Latitude', 
      #                                      long_col = 'Longitude', 
      #                                      lat_round = '', 
      #                                      long_round = '',
      #                                      level_req_flag = 'F')
      # 
      # sify_data <- fn_clean_lat_long_add(sify_data, 
      #                                    lat_col = 'Latitude', 
      #                                    long_col = 'Longitude', 
      #                                    lat_round = '', 
      #                                    long_round = '',
      #                                    level_req_flag = 'F')
      # 
      # tikona_data <- fn_clean_lat_long_add(tikona_data, 
      #                                      lat_col = 'Latitude', 
      #                                      long_col = 'Longitude', 
      #                                      lat_round = '', 
      #                                      long_round = '',
      #                                      level_req_flag = 'F')

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Mast Height data - pre-processing & cleaning
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Retaining only relevant variables
      # mast_ht_data_all <- mast_ht_data_all[,c("Feasibility Response Auto No.",
      #                                         "Feasibility Response: Created Date",
      #                                         "Pole/Mast Height (m)")]
      # 
      # # Filtering prospect file for only feasibles
      # prospect_feasibles <- subset(prospect_data,prospect_data$Status=="Feasible")
      # 
      # #Merging by feasibility auto response number with the onnet RF file
      # mast_ht_data_all <- merge(x=mast_ht_data_all,
      #                           y=prospect_feasibles,
      #                           by.x="Feasibility Response Auto No.",
      #                           by.y="Feasibility.Response..Feasibility.Response.Auto.No.")
      # 
      # mast_ht_data_all$Feasibility_Response_Created_Date <- lubridate::mdy(mast_ht_data_all$`Feasibility Response: Created Date`)
      # mast_ht_data_all$Prospect_ID <- 1:nrow(mast_ht_data_all)
      # 
      # #Making file for self merge
      # mast_ht_data_all <- subset(mast_ht_data_all,
      #                            #mast_ht_data_all_2$L1.or.L2=="L2" & 
      #                            is.na(mast_ht_data_all$`Pole/Mast Height (m)`)==F)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # ARC BW data - pre-processing & cleaning
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      #Changing column name
      # arc_bw_cost$BW_mbps <- arc_bw_cost$BW..Mbps.
      # 
      # #Converting to wide format
      # arc_bw_cost <- sqldf('select arc_bw_cost.BW_mbps,
      #                      arc_bw_cost.Vendor,
      #                      sum(arc_bw_cost.ARC) as arc,
      #                      sum(arc_bw_cost.OTC) as otc
      #                      from arc_bw_cost
      #                      group by 1,2')
      # 
      # #Filtering only for Sify, Airtel, Tikona and Aircel
      # arc_bw_cost <- subset(arc_bw_cost,arc_bw_cost$Vendor=="Aircel"|arc_bw_cost$Vendor=="Bharti"|arc_bw_cost$Vendor=="Tikona"|arc_bw_cost$Vendor=="Sify")

      #Dividing based on vendor
      #arc_bw_cost_airtel <- subset(arc_bw_cost,arc_bw_cost$vendor=="airtel")
      #arc_bw_cost_aircel <- subset(arc_bw_cost,arc_bw_cost$vendor=="aircel")
      # arc_bw_cost_sify <- subset(arc_bw_cost,arc_bw_cost$vendor=="sify")
      # arc_bw_cost_tikona <- subset(arc_bw_cost,arc_bw_cost$vendor=="tikona")

      #Remove unwanted df
      # rm(arc_bw_cost)

      ##########################################################################################
      ##########################################################################################
      # Roll-up & Cleaning for each scenario
      # - Rolling up based on key
      ##########################################################################################
      ##########################################################################################

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Prospect Data Roll-up
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

      # pros_data will be used as it is for feature creation - no roll-up required
      # following roll-up done for LM cost calculation
      # prospect_coords <- data.table(prospect_date = as.Date(mast_ht_data_all$Feasibility_Response_Created_Date),
      #                               prospect_lat = as.vector(as.numeric(mast_ht_data_all$CustomerLatitude1)),
      #                               prospect_lon =as.vector(as.numeric(mast_ht_data_all$CustomerLongitude1)))
      # 
      # prospect_coords_new <- data.table(prospect_date = as.Date(mast_ht_data_all$Feasibility_Response_Created_Date),
      #                                   prospect_lat = as.vector(as.numeric(mast_ht_data_all$CustomerLatitude1)),
      #                                   prospect_lon =as.vector(as.numeric(mast_ht_data_all$CustomerLongitude1)),
      #                                   prospect_mast_ht = as.vector(mast_ht_data_all$PoleMast_Height_m))

      ##########################################################################################
      ##########################################################################################
      # Feature Building
      ##########################################################################################
      ##########################################################################################

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Prospect related Features
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      tryCatch(
        {
      prospect_feature_matrix <- rbind(lapply(as.list(input_data$Prospect_ID), fn_offnet_rf_prospect_distance_calc))
      prospect_feature_matrix <- do.call(rbind,prospect_feature_matrix)
	  	  
      colnames(prospect_feature_matrix) <- c( 'Prospect_ID',
                                              'prospect_0_5km_cust_Count',
                                              'prospect_0_5km_Avg_DistanceKilometers',
                                              'prospect_0_5km_Min_DistanceKilometers',
                                              'prospect_0_5km_Avg_BW_Mbps',
                                              'prospect_0_5km_Min_BW_Mbps',
                                              'prospect_0_5km_Max_BW_Mbps',
											  'prospect_0_5km_Sum_Feasibility_flag',
                                              'prospect_0_5km_feasibility_pct',                                              
                                              'prospect_2km_cust_Count',
                                              'prospect_2km_Avg_DistanceKilometers',
                                              'prospect_2km_Min_DistanceKilometers',
                                              'prospect_2km_Avg_BW_Mbps',
                                              'prospect_2km_Min_BW_Mbps',
                                              'prospect_2km_Max_BW_Mbps',
                                              'prospect_2km_Sum_Feasibility_flag',
                                              'prospect_2km_feasibility_pct')

      prospect_feature_matrix[prospect_feature_matrix=='Inf'] <- 9999999
      prospect_feature_matrix[prospect_feature_matrix=='-Inf'] <- 9999999
      prospect_feature_matrix[prospect_feature_matrix=='NaN'] <- 9999999
      prospect_feature_matrix[is.na(prospect_feature_matrix)] <- 9999999

      chk <- sapply(prospect_feature_matrix,is.infinite)
      prospect_feature_matrix[chk] <- 9999999

      chk <- sapply(prospect_feature_matrix,is.nan)
      prospect_feature_matrix[chk] <- 9999999

      chk <- sapply(prospect_feature_matrix,is.na)
      prospect_feature_matrix[chk] <- 9999999

      prospect_feature_matrix[ ,c("prospect_0_5km_Avg_DistanceKilometers",
                               "prospect_0_5km_Min_DistanceKilometers",
                               "prospect_2km_Avg_DistanceKilometers",
                               "prospect_2km_Min_DistanceKilometers")][prospect_feature_matrix[ ,c("prospect_0_5km_Avg_DistanceKilometers",
                                                                                                "prospect_0_5km_Min_DistanceKilometers",
                                                                                                "prospect_2km_Avg_DistanceKilometers",
                                                                                                "prospect_2km_Min_DistanceKilometers")]==9999999 ] <- 0

      # Convert the data to numeric
      prospect_feature_matrix <- data.frame(prospect_feature_matrix)
      prospect_feature_matrix[,2:ncol(prospect_feature_matrix)] <- sapply(prospect_feature_matrix[,2:ncol(prospect_feature_matrix)], function(x) as.numeric(as.character(x)))

      # Merge features to input data
      input_data <- merge(x= input_data,
                          y=prospect_feature_matrix,
                          by.x="Prospect_ID",
                          by.y="Prospect_ID",
                          all.x=T)

      input_data$bw_flag_3 <- ifelse(input_data$BW_mbps >= 3, 1, 0)
      input_data$bw_flag_32 <- ifelse(input_data$BW_mbps >= 32, 1, 0)

      rm(prospect_data)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Customer related Features
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      offnet_customer_feature_matrix <- apply(input_data, 1, 
                                              function(x) fn_offnet_RF_customer_distance_calc(
                                                x["Latitude_final"],
                                                x["Longitude_final"],
                                                x["Feasibility.Response..Created.Date"],
                                                offnet_cust_data))

      input_data$offnet_0_5km_cust_Count = as.numeric(offnet_customer_feature_matrix[1,])
      input_data$offnet_0_5km_Avg_DistanceKilometers = as.numeric(offnet_customer_feature_matrix[2,])
      input_data$offnet_0_5km_Min_DistanceKilometers = as.numeric(offnet_customer_feature_matrix[3,])
      input_data$offnet_0_5km_Avg_BW_Mbps = as.numeric(offnet_customer_feature_matrix[4,])
      input_data$offnet_0_5km_Min_BW_Mbps = as.numeric(offnet_customer_feature_matrix[5,])
      input_data$offnet_0_5km_Max_BW_Mbps = as.numeric(offnet_customer_feature_matrix[6,])
      input_data$offnet_0_5km_Min_accuracy_num = as.numeric(offnet_customer_feature_matrix[7,])

      input_data$offnet_2km_cust_Count = as.numeric(offnet_customer_feature_matrix[8,])
      input_data$offnet_2km_Avg_DistanceKilometers = as.numeric(offnet_customer_feature_matrix[9,])
      input_data$offnet_2km_Min_DistanceKilometers = as.numeric(offnet_customer_feature_matrix[10,])
      input_data$offnet_2km_Avg_BW_Mbps = as.numeric(offnet_customer_feature_matrix[11,])
      input_data$offnet_2km_Min_BW_Mbps = as.numeric(offnet_customer_feature_matrix[12,])
      input_data$offnet_2km_Max_BW_Mbps = as.numeric(offnet_customer_feature_matrix[13,])
      input_data$offnet_2km_Min_accuracy_num = as.numeric(offnet_customer_feature_matrix[14,])

      input_data$offnet_5km_cust_Count = as.numeric(offnet_customer_feature_matrix[15,])
      input_data$offnet_5km_Avg_DistanceKilometers = as.numeric(offnet_customer_feature_matrix[16,])
      input_data$offnet_5km_Min_DistanceKilometers = as.numeric(offnet_customer_feature_matrix[17,])
      input_data$offnet_5km_Avg_BW_Mbps = as.numeric(offnet_customer_feature_matrix[18,])
      input_data$offnet_5km_Min_BW_Mbps = as.numeric(offnet_customer_feature_matrix[19,])
      input_data$offnet_5km_Max_BW_Mbps = as.numeric(offnet_customer_feature_matrix[20,])
      input_data$offnet_5km_Min_accuracy_num = as.numeric(offnet_customer_feature_matrix[21,])

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Vendor related Features
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Distance feature for Aircel
      # aircel_feature_matrix <- apply(input_data, 1, 
      #                                function(x) fn_offnet_rf_vendor_distance_calc(
      #                                  x["Latitude_final"],
      #                                  x["Longitude_final"],
      #                                  aircel_data))
      # input_data$aircel_min_dist_km  = as.numeric(aircel_feature_matrix[1,])
      # input_data$aircel_3km_radius   = as.numeric(aircel_feature_matrix[2,])
      # input_data$aircel_avg_dist_3km = as.numeric(aircel_feature_matrix[3,])

      # Distance feature for Airtel
      # airtel_feature_matrix <- apply(input_data, 1, 
      #                                function(x) fn_offnet_rf_vendor_distance_calc(
      #                                  x["Latitude_final"],
      #                                  x["Longitude_final"],
      #                                  airtel_data))
      # 
      # input_data$airtel_min_dist_km  = as.numeric(airtel_feature_matrix[1,])
      # input_data$airtel_3km_radius   = as.numeric(airtel_feature_matrix[2,])
      # input_data$airtel_avg_dist_3km = as.numeric(airtel_feature_matrix[3,])

      # Distance feature for Sify
      sify_feature_matrix <- apply(input_data, 1, 
                                   function(x) fn_offnet_rf_vendor_distance_calc(
                                     x["Latitude_final"],
                                     x["Longitude_final"],
                                     sify_data))

      input_data$sify_min_dist_km  = as.numeric(sify_feature_matrix[1,])
      input_data$sify_site_id  = sify_feature_matrix[2,]
      input_data$sify_site_address  = sify_feature_matrix[3,]
      input_data$sify_bso_name  = sify_feature_matrix[4,]
      input_data$sify_3km_radius   = as.numeric(sify_feature_matrix[5,])
      input_data$sify_avg_dist_3km = as.numeric(sify_feature_matrix[6,])

      # Distance feature for Tikona
      tikona_feature_matrix<- apply(input_data, 1, 
                                    function(x) fn_offnet_rf_vendor_distance_calc(
                                      x["Latitude_final"],
                                      x["Longitude_final"],
                                      tikona_data))

      input_data$tikona_min_dist_km  = as.numeric(tikona_feature_matrix[1,])
      input_data$tikona_site_id  = tikona_feature_matrix[2,]
      input_data$tikona_site_address  = tikona_feature_matrix[3,]
      input_data$tikona_bso_name  = tikona_feature_matrix[4,]
      input_data$tikona_3km_radius   = as.numeric(tikona_feature_matrix[5,])
      input_data$tikona_avg_dist_3km = as.numeric(tikona_feature_matrix[6,])

      # Find Total provider in 3 km radius
      input_data$provider_tot_towers <- #input_data$aircel_3km_radius + 
        #input_data$airtel_3km_radius +
        input_data$sify_3km_radius   +
        input_data$tikona_3km_radius
      # Closest provider distance
      input_data <- transform(input_data,
                              provider_min_dist = pmin(#aircel_min_dist_km,
                                                       #airtel_min_dist_km,
                                                       sify_min_dist_km,
                                                       tikona_min_dist_km,
                                                       na.rm = TRUE))
      # Closest provider name
      df <-input_data[,c(#"aircel_min_dist_km",
                         #"airtel_min_dist_km",
                         "sify_min_dist_km",
                         "tikona_min_dist_km")]
      input_data$closest_provider <- colnames(df)[apply(df , 1, function (x) fn_offnet_rf_find_closest_provider(x))]
      rm(df)

      # Closest provider site info
      input_data$closest_provider_site <- ifelse(input_data$closest_provider=="tikona_min_dist_km",input_data$tikona_site_id,input_data$sify_site_id)

      input_data$closest_provider_site_addr <- ifelse(input_data$closest_provider=="tikona_min_dist_km",input_data$tikona_site_address,input_data$sify_site_address)

      input_data$closest_provider_bso_name <- ifelse(input_data$closest_provider=="tikona_min_dist_km",input_data$tikona_bso_name,input_data$sify_bso_name)

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
      # Feature Cleaning before Scoring/Training the model
      ##########################################################################################
      ##########################################################################################
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

                                #"aircel_avg_dist_3km",
                                #"airtel_avg_dist_3km",
                                "sify_avg_dist_3km",
                                "tikona_avg_dist_3km",

                                "provider_min_dist",

                                #"aircel_min_dist_km",
                                #"airtel_min_dist_km",
                                "sify_min_dist_km",
                                "tikona_min_dist_km"
      )

      input_data[cols_to_impute_99999][is.na(input_data[cols_to_impute_99999])] <- 99999
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

                            "provider_tot_towers",

                            #"aircel_3km_radius" ,
                            #"airtel_3km_radius" ,
                            "sify_3km_radius",
                            "tikona_3km_radius"
      )

      input_data[cols_to_impute_o][is.na(input_data[cols_to_impute_o])] <- 0
      rm(cols_to_impute_o)

      # replace inf with 0
      chk <- sapply(input_data,is.infinite)
      input_data[chk] <- 0

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
      input_data$Sales.Org <- ifelse(grepl("enterprise", tolower(input_data$Sales.Org)), "Enterprise",input_data$Sales.Org)
      input_data$Sales.Org <- ifelse(grepl("service provider", tolower(input_data$Sales.Org)), "Service Provider",input_data$Sales.Org)
      input_data$Sales.Org <- ifelse(grepl("cso", tolower(input_data$Sales.Org)), "CSO",input_data$Sales.Org)

      # last mile contract term
      input_data$last_mile_contract_term <- "1 Year"

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Cleaning all features
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      tryCatch(
        {
      # Grouping categorical variables
      #add new factor level. i.e Others in our example
      if(input_data$Customer_Segment != "Others"){
        # input_data$Customer_Segment = factor(input_data$Customer_Segment,
        #                                      levels=c(levels(input_data$Customer_Segment), "Others"))
        levels(input_data$Customer_Segment)=c(levels(input_data$Customer_Segment), "Others")
      }
      input_data$Customer_Segment[is.na(input_data$Customer_Segment)] <- "Others"
      input_data$Customer_Segment <- case(input_data$Customer_Segment,
                                          'Enterprise ? Silver' = 'Enterprise ? Silver',
                                          'Enterprise - Gold' = 'Enterprise - Gold',
                                          'Enterprise - Strategic' = 'Enterprise - Strategic',
                                          'Enterprise-Direct' = 'Enterprise-Direct',
                                          'Carriers' = 'Carriers',
                                          'Enterprise-Partners Account' = 'Enterprise-Partners Account',
                                          'Enterprise ? Growth Accounts' = 'Enterprise ? Growth Accounts',
                                          'Enterprise ? Government/PSU' = 'Enterprise ? Government/PSU',
                                          'SMB' = 'SMB',
                                          'Enterprise - System Integrators' = 'Enterprise - System Integrators',
                                          default = "Others"
      )

      #add new factor level. i.e Others in our example
      if(input_data$local_loop_interface != "Others"){
        levels(input_data$local_loop_interface)=c(levels(input_data$local_loop_interface), "Others")
      }
      input_data$local_loop_interface[is.na(input_data$local_loop_interface)] <- "Others"
      input_data$local_loop_interface <- case(input_data$local_loop_interface,
                                              "100-Base-TX" = "100-Base-TX",
                                              "FE" = "FE",
                                              "Ethernet" = "Ethernet",
                                              default = "Others"
      )

      #add new factor level. i.e Others in our example
      if(input_data$Product.Name != "Other"){
        levels(input_data$Product.Name)=c(levels(input_data$Product.Name), "Other")
      }
      input_data$Product.Name[is.na(input_data$Product.Name)] <- "Other"
      input_data$Product.Name <- case(input_data$Product.Name,
                                      "Global VPN" = "Global VPN",
                                      "Internet Access Service" = "Internet Access Service",
                                      "Priority Ethernet - Point to Point" = "Priority Ethernet - Point to Point",
                                      "Priority Ethernet - Point to MultiPoint" = "Priority Ethernet - Point to MultiPoint",
                                      "National Dedicated Ethernet" = "National Dedicated Ethernet",
                                      "NPL" = "NPL",
                                      default = "Other"
      )

      #add new factor level. i.e Others in our example
      if(input_data$Sales.Org != "Others"){
        levels(input_data$Sales.Org)=c(levels(input_data$Sales.Org), "Other")
      }
      input_data$Sales.Org[is.na(input_data$Sales.Org)] <- "Others"
      input_data$Sales.Org <- case(input_data$Sales.Org,
                                   "Enterprise" = "Enterprise" ,
                                   "Service Provider" = "Service Provider",
                                   "CSO" = "CSO",
                                   "IT" = "IT",
                                   default = "Others"
      )

      #add new factor level. i.e Others in our example
      if(input_data$last_mile_contract_term != "Others"){
        levels(input_data$last_mile_contract_term)=c(levels(input_data$last_mile_contract_term), "Others")
      }
      input_data$last_mile_contract_term[is.na(input_data$last_mile_contract_term)] <- "Others"
      input_data$last_mile_contract_term[input_data$last_mile_contract_term == "3 Years"] <- "2 Years"
      input_data$last_mile_contract_term <- case(input_data$last_mile_contract_term,
                                                 "1 Year" = "1 Year",
                                                 "2-3 Years" = "2 Years",
                                                 default = "Others"
      )

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
                    "closest_provider",
                    "closest_provider_site",
                    "closest_provider_site_addr",
                    "closest_provider_bso_name",
                    "Customer_Segment",
                    "Product.Name",
                    "BW_mbps",
                    "local_loop_interface",
                    "Feasibility.Response..Created.Date",
                    "Latitude_final",
                    "Longitude_final",
                    "last_mile_contract_term",
                    "bw_flag_3",
                    "bw_flag_32",
                    "provider_tot_towers",
                    "provider_min_dist",
                    "offnet_0_5km_cust_Count",
                    "offnet_0_5km_Min_DistanceKilometers",
                    "offnet_0_5km_Avg_BW_Mbps",
                    "offnet_0_5km_Min_BW_Mbps",
                    "offnet_0_5km_Max_BW_Mbps",
                    "offnet_0_5km_Min_accuracy_num",
                    "offnet_2km_cust_Count",
                    "offnet_2km_Min_DistanceKilometers",
                    "offnet_2km_Avg_BW_Mbps",
                    "offnet_2km_Min_BW_Mbps",
                    "offnet_2km_Min_accuracy_num",
                    "offnet_5km_Min_DistanceKilometers",
                    "offnet_5km_Avg_BW_Mbps",
                    "offnet_5km_Min_BW_Mbps",
                    "offnet_5km_Max_BW_Mbps",
                    "offnet_5km_Min_accuracy_num",
                    "prospect_0_5km_Min_DistanceKilometers",
                    "prospect_0_5km_Avg_BW_Mbps",
                    "prospect_0_5km_Min_BW_Mbps",
                    "prospect_0_5km_Max_BW_Mbps",
                    "prospect_0_5km_feasibility_pct",
                    "prospect_0_5km_Sum_Feasibility_flag",
                    "prospect_2km_cust_Count",
                    "prospect_2km_Avg_DistanceKilometers",
                    "prospect_2km_Avg_BW_Mbps",
                    "prospect_2km_Min_BW_Mbps",
                    "prospect_2km_Max_BW_Mbps",
                    "prospect_2km_Sum_Feasibility_flag",
                    "prospect_2km_feasibility_pct"
                    #"Status"
                     )

      input_data <- input_data[,(names(input_data) %in% sel_cols)]

      # Change the column names according to trained dataset column names
      input_data = dplyr::rename(input_data,
                                 Customer.Segment = Customer_Segment,
                                 Local.Loop.Interface = local_loop_interface,
                                 Last.Mile.Contract.Term = last_mile_contract_term)

      ##########################################################################################
      ##########################################################################################
      # Model Scoring
      ##########################################################################################
      ##########################################################################################
      # Score the inputs
      input_data$Probabililty_Access_Feasibility <- predict(rf_model, newdata = input_data, type = "prob")[,2]
	  
	  ceiling_dec <- function(x, level=2) round(x + 5*10^(-level-1), level)	  
	  input_data$Probabililty_Access_Feasibility <- sapply(input_data$Probabililty_Access_Feasibility, ceiling_dec)
	  input_data$Probabililty_Access_Feasibility <- as.numeric(as.character(input_data$Probabililty_Access_Feasibility))

      # Predicting on cut off selected
      input_data$Predicted_Access_Feasibility <- ifelse(input_data$Probabililty_Access_Feasibility > youden_cutoff, "Feasible", "Not Feasible")
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

      ##########################################################################################
      ##########################################################################################
      # Last Mile Cost Calculation
      ##########################################################################################
      ##########################################################################################
      tryCatch(
        {

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Calculating ARC BW costs based on requested bandwidth
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Merging Input file with Airtel ARC BW costs
      # input_data <- merge(x=input_data,
      #                     y=arc_bw_cost_airtel,
      #                     by.x="BW_mbps",
      #                     by.y="bw_mbps",
      #                     all.x = T)
      # 
      # input_data$vendor<-NULL
      # colnames(input_data)[which(colnames(input_data) == "arc")] <- "arc_airtel"
      # colnames(input_data)[which(colnames(input_data) == "otc")] <- "otc_airtel"

      # Merging Input file with Aircel ARC BW costs
      # input_data <- merge(x=input_data,
      #                     y=arc_bw_cost_aircel,
      #                     by.x="BW_mbps",
      #                     by.y="bw_mbps",
      #                     all.x = T)
      # 
      # input_data$vendor<-NULL
      # colnames(input_data)[which(colnames(input_data) == "arc")] <- "arc_aircel"
      # colnames(input_data)[which(colnames(input_data) == "otc")] <- "otc_aircel"


      # Cleaning interim BWs
      input_data$interim_BW <- apply(input_data, 1, function(x) interim_BW_func(x["BW_mbps"]))

      # Merging Input file with Sify ARC BW costs
      input_data <- merge(x=input_data,
                          y=arc_bw_cost_sify,
                          by.x="interim_BW",
                          by.y="bw_mbps",
                          all.x = T)

      # Calculating ARC BW cost
      input_data$vendor<-NULL
      colnames(input_data)[which(colnames(input_data) == "arc")] <- "arc_sify"
      colnames(input_data)[which(colnames(input_data) == "otc")] <- "otc_sify"

      # Merging Input file with Tikona ARC BW costs
      input_data <- merge(x=input_data,
                          y=arc_bw_cost_tikona,
                          by.x="interim_BW",
                          by.y="bw_mbps",
                          all.x = T)

      input_data$vendor<-NULL
      colnames(input_data)[which(colnames(input_data) == "arc")] <- "arc_tikona"
      colnames(input_data)[which(colnames(input_data) == "otc")] <- "otc_tikona"

      #Finding arc and otc for closest provider
      input_data$arc_closest_provider <- ifelse(input_data$closest_provider=="aircel_min_dist_km",input_data$arc_aircel,
                                                ifelse(input_data$closest_provider=="airtel_min_dist_km",input_data$arc_airtel,
                                                       ifelse(input_data$closest_provider=="sify_min_dist_km",input_data$arc_sify,
                                                              ifelse(input_data$closest_provider=="tikona_min_dist_km",input_data$arc_tikona,0))))

      input_data$otc_closest_provider <- ifelse(input_data$closest_provider=="aircel_min_dist_km",input_data$otc_aircel,
                                                ifelse(input_data$closest_provider=="airtel_min_dist_km",input_data$otc_airtel,
                                                       ifelse(input_data$closest_provider=="sify_min_dist_km",input_data$otc_sify,
                                                              ifelse(input_data$closest_provider=="tikona_min_dist_km",input_data$otc_tikona,0))))

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Finding nearby prospects with corresponding mast heights
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      mast_ht_prospect_matrix <- c(lapply(as.list(input_data$Prospect_ID), fn_mast_ht_prospects_offnet_rf))
      mast_ht_prospect <- do.call(rbind,mast_ht_prospect_matrix)

      #Missing value treatment
      mast_ht_prospect[mast_ht_prospect=='Inf'] <- 0
      mast_ht_prospect[mast_ht_prospect=='-Inf'] <- 0
      mast_ht_prospect[mast_ht_prospect=='NaN'] <- 0
      mast_ht_prospect[is.na(mast_ht_prospect)] <- 0

      chk <- sapply(mast_ht_prospect,is.infinite)
      mast_ht_prospect[chk] <- 0

      chk <- sapply(mast_ht_prospect,is.nan)
      mast_ht_prospect[chk] <- 0

      chk <- sapply(mast_ht_prospect,is.na)
      mast_ht_prospect[chk] <- 0
	  
	  # round off mast heights to nearest higher multiple of 3
	  roundUp <- function(x,m=3) m*ceiling(x / m)
	  mast_ht_prospect$nearest_mast_ht <- sapply(mast_ht_prospect$nearest_mast_ht, roundUp)
	  mast_ht_prospect$nearest_mast_ht <- as.numeric(mast_ht_prospect$nearest_mast_ht)
	  
	  mast_ht_prospect$avg_mast_ht <- sapply(mast_ht_prospect$avg_mast_ht, roundUp)
	  mast_ht_prospect$avg_mast_ht <- as.numeric(mast_ht_prospect$avg_mast_ht)

      #For mast height costs
      mast_ht_prospect$nearest_mast_ht_cost <- ifelse(mast_ht_prospect$cust_count==0,0,
                                                      ifelse(mast_ht_prospect$nearest_mast_ht<6,0,(mast_ht_prospect$nearest_mast_ht)*4700))

      mast_ht_prospect$avg_mast_ht_cost <- ifelse(mast_ht_prospect$cust_count==0,0,
                                                  ifelse(mast_ht_prospect$avg_mast_ht<6,0,(mast_ht_prospect$avg_mast_ht)*4700))

      # merging with input data
      input_data <- merge(x=input_data,
                          y=mast_ht_prospect,
                          by = "Prospect_ID",
                          all.x=T)
      # remove mast ht data
      rm(mast_ht_data_all,prospect_coords, prospect_coords_new)


      # Total LM Cost
      input_data$total_cost <- (as.numeric(input_data$arc_closest_provider) +
                                as.numeric(input_data$otc_closest_provider) +
                                  as.numeric(input_data$avg_mast_ht_cost))
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


      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      # Adding Orchestration columns
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++  
      input_data$Orch_LM_Type <- "Offnet"
      input_data$Orch_Connection <- "Wireless"
      input_data$Orch_Category <- ifelse(input_data$closest_provider=="sify_min_dist_km", "Sify",
                                         ifelse(input_data$closest_provider=="tikona_min_dist_km", "Tikona",
                                                "No Vendor"))

      # input_data$Orch_BW <- ifelse(input_data$BW_mbps<2, "lesser_than_2MB",
      #                              ifelse(input_data$BW_mbps==2, "2_MB",
      #                                     ifelse(input_data$BW_mbps<=10, "ge_2_10_MB",
      #                                            ifelse(input_data$BW_mbps<=32, "ge_10_32_MB",
      #                                                   "ge_32_MB"))))

      input_data$Orch_BW <- input_data$BW_mbps

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

      input_data$lm_arc_bw_onwl <- 0
      input_data$lm_nrc_bw_onwl <- 0
      input_data$lm_nrc_mux_onwl <- 0
      input_data$lm_nrc_inbldg_onwl <- 0
      input_data$lm_nrc_ospcapex_onwl <- 0
      input_data$lm_nrc_nerental_onwl <- 0

      # Offnet RF LM cols
      colnames(input_data)[colnames(input_data) == 'arc_closest_provider'] <- 'lm_arc_bw_prov_ofrf'
      colnames(input_data)[colnames(input_data) == 'otc_closest_provider'] <- 'lm_nrc_bw_prov_ofrf'
      colnames(input_data)[colnames(input_data) == 'avg_mast_ht_cost'] <- 'lm_nrc_mast_ofrf'

      input_data$lm_arc_bw_prov_ofrf <- as.numeric(input_data$lm_arc_bw_prov_ofrf)
      input_data$lm_nrc_bw_prov_ofrf <- as.numeric(input_data$lm_nrc_bw_prov_ofrf)
      input_data$lm_nrc_mast_ofrf <- as.numeric(input_data$lm_nrc_mast_ofrf)

      # Onnet RF LM cols
      input_data$lm_arc_bw_onrf <- 0
      input_data$lm_nrc_bw_onrf <- 0
      input_data$lm_nrc_mast_onrf <- 0

      # Add blank error attributes in case everything runs smoothly
      input_data$error_code <- "NA"
      input_data$error_flag <- 0
      input_data$error_msg <- "No error"

      # Remove cols which are not required or are duplicates in the output
      input_data$bw_mbps <- as.numeric(input_data$bw_mbps)

      rem_cols <- c("BW_mbps",
                    "Customer.Segment",
                    "Last.Mile.Contract.Term",
                    "Local.Loop.Interface",
                    "Product.Name",
                    "Feasibility.Response..Created.Date",
                    "Latitude_final",
                    "Longitude_final")

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
    app.run(port = 7000, debug = True)


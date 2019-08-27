
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
		# NPL POP to POP checks
		##########################################################################################
		##########################################################################################
		##########################################################################################
		# set error parameter
		err <<- FALSE

		input_json_data <- input_data #-->change in API

		##########################################################################################
		# Define Error Output JSON to be thrown in case of any error encountered
		##########################################################################################
		# Define Error response dataframe
		df_error_a <- data.frame('link_id'="NA",'prospect_name'="NA",'bw_mbps'="NA",'burstable_bw'="NA",'bw_mbps_upd'="NA",'product_name'="NA",'feasibility_response_created_date'="NA",'account_id_with_18_digit'="NA",'opportunity_term'="NA",'quotetype_quote'="NA",'sla_varient'="NA",'a_FATG_Building_Type'="NA",'a_FATG_Category'="NA",'a_FATG_DIST_KM'="NA",'a_FATG_Network_Location_Type'="NA",'a_FATG_PROW'="NA",'a_FATG_Ring_type'="NA",'a_FATG_TCL_Access'="NA",'a_HH_0_5_access_rings_F'="NA",'a_HH_0_5_access_rings_NF'="NA",'a_HH_0_5km'="NA",'a_HH_DIST_KM'="NA",'a_Network_F_NF_CC'="NA",'a_Network_F_NF_CC_Flag'="NA",'a_Network_F_NF_HH'="NA",'a_Network_F_NF_HH_Flag'="NA",'a_Network_Feasibility_Check'="NA",'a_OnnetCity_tag'="NA",'a_Orch_BW'="NA",'a_Orch_Category'="NA",'a_Orch_Connection'="NA",'a_Orch_LM_Type'="NA",'a_POP_Building_Type'="NA",'a_POP_Category'="NA",'a_POP_Construction_Status'="NA",'a_POP_DIST_KM'="NA",'a_POP_DIST_KM_SERVICE'="NA",'a_POP_DIST_KM_SERVICE_MOD'="NA",'a_POP_Network_Location_Type'="NA",'a_POP_TCL_Access'="NA",'a_Predicted_Access_Feasibility'="NA",'a_Probabililty_Access_Feasibility'="NA",'a_Product.Name'="NA",'a_SERVICE_ID'="NA",'a_X0.5km_avg_bw'="NA",'a_X0.5km_avg_dist'="NA",'a_X0.5km_cust_count'="NA",'a_X0.5km_max_bw'="NA",'a_X0.5km_min_bw'="NA",'a_X0.5km_min_dist'="NA",'a_X0.5km_prospect_avg_bw'="NA",'a_X0.5km_prospect_avg_dist'="NA",'a_X0.5km_prospect_count'="NA",'a_X0.5km_prospect_max_bw'="NA",'a_X0.5km_prospect_min_bw'="NA",'a_X0.5km_prospect_min_dist'="NA",'a_X0.5km_prospect_num_feasible'="NA",'a_X0.5km_prospect_perc_feasible'="NA",'a_X2km_avg_bw'="NA",'a_X2km_avg_dist'="NA",'a_X2km_cust_count'="NA",'a_X2km_max_bw'="NA",'a_X2km_min_bw'="NA",'a_X2km_min_dist'="NA",'a_X2km_prospect_avg_bw'="NA",'a_X2km_prospect_avg_dist'="NA",'a_X2km_prospect_count'="NA",'a_X2km_prospect_max_bw'="NA",'a_X2km_prospect_min_bw'="NA",'a_X2km_prospect_min_dist'="NA",'a_X2km_prospect_num_feasible'="NA",'a_X2km_prospect_perc_feasible'="NA",'a_X5km_avg_bw'="NA",'a_X5km_avg_dist'="NA",'a_X5km_cust_count'="NA",'a_X5km_max_bw'="NA",'a_X5km_min_bw'="NA",'a_X5km_min_dist'="NA",'a_X5km_prospect_avg_bw'="NA",'a_X5km_prospect_avg_dist'="NA",'a_X5km_prospect_count'="NA",'a_X5km_prospect_max_bw'="NA",'a_X5km_prospect_min_bw'="NA",'a_X5km_prospect_min_dist'="NA",'a_X5km_prospect_num_feasible'="NA",'a_X5km_prospect_perc_feasible'="NA",'a_a_or_b_end'="NA",'a_access_check_CC'="NA",'a_access_check_hh'="NA",'a_city_tier'="NA",'a_connected_building_tag'="NA",'a_connected_cust_tag'="NA",'a_core_check_CC'="NA",'a_core_check_hh'="NA",'a_cost_permeter'="NA",'a_customer_segment'="NA",'a_error_code'="NA",'a_error_flag'="NA",'a_error_msg'="NA",'a_hh_flag'="NA",'a_hh_name'="NA",'a_last_mile_contract_term'="NA",'a_latitude_final'="NA",'a_lm_arc_bw_onrf'="NA",'a_lm_arc_bw_onwl'="NA",'a_lm_arc_bw_prov_ofrf'="NA",'a_lm_nrc_bw_onrf'="NA",'a_lm_nrc_bw_onwl'="NA",'a_lm_nrc_bw_prov_ofrf'="NA",'a_lm_nrc_inbldg_onwl'="NA",'a_lm_nrc_mast_ofrf'="NA",'a_lm_nrc_mast_onrf'="NA",'a_lm_nrc_mux_onwl'="NA",'a_lm_nrc_nerental_onwl'="NA",'a_lm_nrc_ospcapex_onwl'="NA",'a_local_loop_interface'="NA",'a_longitude_final'="NA",'a_min_hh_fatg'="NA",'a_net_pre_feasible_flag'="NA",'a_num_connected_building'="NA",'a_num_connected_cust'="NA",'a_pop_address'="NA",'a_pop_lat'="NA",'a_pop_long'="NA",'a_pop_name'="NA",'a_pop_network_loc_id'="NA",'a_pop_selected'="NA",'a_pop_ui_id'="NA",'a_resp_city'="NA",'a_sales_org'="NA",'a_scenario_1'="NA",'a_scenario_2'="NA",'a_site_id'="NA",'a_time_taken'="NA",'a_total_cost'="NA", 'a_dc_selected'="NA",
								 stringsAsFactors = FALSE)

		df_error_b <- data.frame('b_FATG_Building_Type'="NA",'b_FATG_Category'="NA",'b_FATG_DIST_KM'="NA",'b_FATG_Network_Location_Type'="NA",'b_FATG_PROW'="NA",'b_FATG_Ring_type'="NA",'b_FATG_TCL_Access'="NA",'b_HH_0_5_access_rings_F'="NA",'b_HH_0_5_access_rings_NF'="NA",'b_HH_0_5km'="NA",'b_HH_DIST_KM'="NA",'b_Network_F_NF_CC'="NA",'b_Network_F_NF_CC_Flag'="NA",'b_Network_F_NF_HH'="NA",'b_Network_F_NF_HH_Flag'="NA",'b_Network_Feasibility_Check'="NA",'b_OnnetCity_tag'="NA",'b_Orch_BW'="NA",'b_Orch_Category'="NA",'b_Orch_Connection'="NA",'b_Orch_LM_Type'="NA",'b_POP_Building_Type'="NA",'b_POP_Category'="NA",'b_POP_Construction_Status'="NA",'b_POP_DIST_KM'="NA",'b_POP_DIST_KM_SERVICE'="NA",'b_POP_DIST_KM_SERVICE_MOD'="NA",'b_POP_Network_Location_Type'="NA",'b_POP_TCL_Access'="NA",'b_Predicted_Access_Feasibility'="NA",'b_Probabililty_Access_Feasibility'="NA",'b_Product.Name'="NA",'b_SERVICE_ID'="NA",'b_X0.5km_avg_bw'="NA",'b_X0.5km_avg_dist'="NA",'b_X0.5km_cust_count'="NA",'b_X0.5km_max_bw'="NA",'b_X0.5km_min_bw'="NA",'b_X0.5km_min_dist'="NA",'b_X0.5km_prospect_avg_bw'="NA",'b_X0.5km_prospect_avg_dist'="NA",'b_X0.5km_prospect_count'="NA",'b_X0.5km_prospect_max_bw'="NA",'b_X0.5km_prospect_min_bw'="NA",'b_X0.5km_prospect_min_dist'="NA",'b_X0.5km_prospect_num_feasible'="NA",'b_X0.5km_prospect_perc_feasible'="NA",'b_X2km_avg_bw'="NA",'b_X2km_avg_dist'="NA",'b_X2km_cust_count'="NA",'b_X2km_max_bw'="NA",'b_X2km_min_bw'="NA",'b_X2km_min_dist'="NA",'b_X2km_prospect_avg_bw'="NA",'b_X2km_prospect_avg_dist'="NA",'b_X2km_prospect_count'="NA",'b_X2km_prospect_max_bw'="NA",'b_X2km_prospect_min_bw'="NA",'b_X2km_prospect_min_dist'="NA",'b_X2km_prospect_num_feasible'="NA",'b_X2km_prospect_perc_feasible'="NA",'b_X5km_avg_bw'="NA",'b_X5km_avg_dist'="NA",'b_X5km_cust_count'="NA",'b_X5km_max_bw'="NA",'b_X5km_min_bw'="NA",'b_X5km_min_dist'="NA",'b_X5km_prospect_avg_bw'="NA",'b_X5km_prospect_avg_dist'="NA",'b_X5km_prospect_count'="NA",'b_X5km_prospect_max_bw'="NA",'b_X5km_prospect_min_bw'="NA",'b_X5km_prospect_min_dist'="NA",'b_X5km_prospect_num_feasible'="NA",'b_X5km_prospect_perc_feasible'="NA",'b_a_or_b_end'="NA",'b_access_check_CC'="NA",'b_access_check_hh'="NA",'b_city_tier'="NA",'b_connected_building_tag'="NA",'b_connected_cust_tag'="NA",'b_core_check_CC'="NA",'b_core_check_hh'="NA",'b_cost_permeter'="NA",'b_customer_segment'="NA",'b_error_code'="NA",'b_error_flag'="NA",'b_error_msg'="NA",'b_hh_flag'="NA",'b_hh_name'="NA",'b_last_mile_contract_term'="NA",'b_latitude_final'="NA",'b_lm_arc_bw_onrf'="NA",'b_lm_arc_bw_onwl'="NA",'b_lm_arc_bw_prov_ofrf'="NA",'b_lm_nrc_bw_onrf'="NA",'b_lm_nrc_bw_onwl'="NA",'b_lm_nrc_bw_prov_ofrf'="NA",'b_lm_nrc_inbldg_onwl'="NA",'b_lm_nrc_mast_ofrf'="NA",'b_lm_nrc_mast_onrf'="NA",'b_lm_nrc_mux_onwl'="NA",'b_lm_nrc_nerental_onwl'="NA",'b_lm_nrc_ospcapex_onwl'="NA",'b_local_loop_interface'="NA",'b_longitude_final'="NA",'b_min_hh_fatg'="NA",'b_net_pre_feasible_flag'="NA",'b_num_connected_building'="NA",'b_num_connected_cust'="NA",'b_pop_address'="NA",'b_pop_lat'="NA",'b_pop_long'="NA",'b_pop_name'="NA",'b_pop_network_loc_id'="NA",'b_pop_selected'="NA",'b_pop_ui_id'="NA",'b_resp_city'="NA",'b_sales_org'="NA",'b_scenario_1'="NA",'b_scenario_2'="NA",'b_site_id'="NA",'b_time_taken'="NA",'b_total_cost'="NA",'dist_betw_pops'="NA",'chargeable_distance'="NA",'intra_inter_flag'="NA",'manual_flag'="NA",'Predicted_Access_Feasibility'="NA",'pop2pop_network_flag'="NA",'pop2pop_network_check'="NA",'site_id'="NA",'b_dc_selected'="NA",stringsAsFactors = FALSE)

		df_error <- cbind(df_error_a, df_error_b)
		rm(df_error_a,df_error_b)

		tryCatch(
		  {
			##########################################################################################
			# I. SET ENVIRONMENT
			#
			# R Packages - Check if needed packages are installed - if not, install them
			
			##########################################################################################
			##########################################################################################
			options(digits = 10)
			#options(sqldf.driver = "SQLite")
			# Suppress warnings
			options( warn = -1 )
			packages <- c("dplyr","plyr","readxl","geosphere","lubridate","data.table","randomForest","jsonlite","RMySQL","reshape2", "gdata", "openxlsx", "stringi", "jsonlite")
			if (length(setdiff(packages, rownames(installed.packages()))) > 0) {
			  install.packages(setdiff(packages, rownames(installed.packages())))
			}
			rm(packages)
			
			#time_start <- proc.time()
			##########################################################################################
			# II. LOAD LIBRARIES
			##########################################################################################
			library(dplyr, quietly = TRUE)
			library(geosphere, quietly = TRUE)
			library(gdata, quietly = TRUE)
			library(readxl, quietly = TRUE)
			library(randomForest, quietly = TRUE)
			library(lubridate, quietly = TRUE)
			library(RMySQL, quietly = TRUE)
			library(jsonlite, quietly = TRUE)
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
		#path_py <- "E:/gv_personal_folder/prod_codes/gaurav_ETL/Pricing_NPL_Prod_Code" # --> change here for API
		setwd(path_py)

		#2. Define Filenames

		#3. Input JSON
		JSON_filename <- "input_json_pop_to_pop.json"

		#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		# Read Input JSON File
		#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		#input_data <- dplyr::bind_rows(fromJSON(JSON_filename))  #--> Change here for API
		#input_json_data <- input_data #--Change here

		#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		# Database Connection
		#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		tryCatch(
		  {
			mydb_abstract_db = dbConnect(MySQL(),
										 user='optimus_user', 
										 password='Tata123', 
										 dbname='optimus_abstract', 
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
		if(err==TRUE){
		  return(df_error)
		}

		#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		# Read data from ETL
		#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

		tryCatch(
		  {
			#pop to pop network check
			msb_network = dbSendQuery(mydb_abstract_db,"select BUILDING_CODE_A, BUILDING_CODE_Z, util_available from sdhmsb_tab")
			msb_network = fetch(msb_network, n=-1)
			
		  }
		  , error=function(e) 
		  {
			err <<- TRUE
			df_error$error_flag <- 1
			df_error$error_code <- "E6"
			df_error$error_msg <- "DB Error: Error in querying the DB Tables"
			df_error <<- cbind(input_json_data,df_error[,!(colnames(df_error) %in% colnames(input_json_data))])
		  })
		if(err==TRUE){
		  return(df_error)
		}

		tryCatch(
		  {
			#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
			# select higher BW - port or LL
			#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
			input_data$bw_mbps_upd <- ifelse(input_data$burstable_bw>input_data$bw_mbps, 
											 input_data$burstable_bw,
											 input_data$bw_mbps)
			
			#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
			# If POP is selected in UI
			#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
			# if POP is selected in any site, Access is Feasible
			input_data$Predicted_Access_Feasibility <- ifelse(grepl("yes", tolower(input_data$pop_selected)),"Feasible", input_data$Predicted_Access_Feasibility)
			
			# if POP is selected in any site, Network is Feasible
			input_data$Network_Feasibility_Check <- ifelse(grepl("yes", tolower(input_data$pop_selected)),"Feasible", input_data$Network_Feasibility_Check)
			
			#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
			# If TCL DC is selected in UI
			#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
			# if DC is selected in any site, Access is Feasible
			input_data$Predicted_Access_Feasibility <- ifelse(grepl("yes", tolower(input_data$dc_selected)),"Feasible", input_data$Predicted_Access_Feasibility)
			
			# if DC is selected in any site, Network is Feasible
			input_data$Network_Feasibility_Check <- ifelse(grepl("yes", tolower(input_data$dc_selected)),"Feasible", input_data$Network_Feasibility_Check)
			
			# make all LM cost components as zero of DC is selected
			input_data$lm_arc_bw_onwl <- ifelse(grepl("yes", tolower(input_data$dc_selected)), 0, input_data$lm_arc_bw_onwl)
			input_data$lm_nrc_bw_onwl <- ifelse(grepl("yes", tolower(input_data$dc_selected)), 0, input_data$lm_nrc_bw_onwl)
			input_data$lm_nrc_mux_onwl <- ifelse(grepl("yes", tolower(input_data$dc_selected)), 0, input_data$lm_nrc_mux_onwl)
			input_data$lm_nrc_inbldg_onwl <- ifelse(grepl("yes", tolower(input_data$dc_selected)), 0, input_data$lm_nrc_inbldg_onwl)
			input_data$lm_nrc_ospcapex_onwl <- ifelse(grepl("yes", tolower(input_data$dc_selected)), 0, input_data$lm_nrc_ospcapex_onwl)
			input_data$lm_nrc_nerental_onwl <- ifelse(grepl("yes", tolower(input_data$dc_selected)), 0, input_data$lm_nrc_nerental_onwl)
			
			input_data$lm_arc_bw_prov_ofrf <- ifelse(grepl("yes", tolower(input_data$dc_selected)), 0, input_data$lm_arc_bw_prov_ofrf)
			input_data$lm_nrc_bw_prov_ofrf <- ifelse(grepl("yes", tolower(input_data$dc_selected)), 0, input_data$lm_nrc_bw_prov_ofrf)
			input_data$lm_nrc_mast_ofrf <- ifelse(grepl("yes", tolower(input_data$dc_selected)), 0, input_data$lm_nrc_mast_ofrf)
			
			input_data$lm_arc_bw_onrf <- ifelse(grepl("yes", tolower(input_data$dc_selected)), 0, input_data$lm_arc_bw_onrf)
			input_data$lm_nrc_bw_onrf <- ifelse(grepl("yes", tolower(input_data$dc_selected)), 0, input_data$lm_nrc_bw_onrf)
			input_data$lm_nrc_mast_onrf <- ifelse(grepl("yes", tolower(input_data$dc_selected)), 0, input_data$lm_nrc_mast_onrf)
			
			
			#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
			# Roll-up on Link ID
			#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
			#separate common cols
			common_cols <- c("link_id",
							 "prospect_name",
							 "bw_mbps",
							 "burstable_bw",
							 "bw_mbps_upd",
							 "product_name",
							 "feasibility_response_created_date",
							 "account_id_with_18_digit",
							 "opportunity_term",
							 "quotetype_quote",
							 "sla_varient")
			
			# separate common cols - excluding link_id
			uncommon_cols <- c("prospect_name",
							   "bw_mbps",
							   "burstable_bw",
							   "bw_mbps_upd",
							   "product_name",
							   "feasibility_response_created_date",
							   "account_id_with_18_digit",
							   "opportunity_term",
							   "quotetype_quote",
							   "sla_varient")
			
			input_comm <- input_data[,common_cols]
			input_comm <- input_comm[!duplicated(input_comm), ]
			
			# take uncommon cols separately for a and b separation
			input_uncomm <- input_data[,!(colnames(input_data) %in% uncommon_cols)]
			# separate A-end and B-end dataframes
			input_a <- input_uncomm[grepl("a", tolower(input_uncomm$a_or_b_end)), ]
			input_b <- input_uncomm[grepl("b", tolower(input_uncomm$a_or_b_end)), ]
			# add prefix of a and b in colnames
			colnames(input_a) <- paste("a", colnames(input_a), sep = "_")
			colnames(input_b) <- paste("b", colnames(input_b), sep = "_")
			# merge a and b dfs
			input_data <- merge(input_a, input_b, by.x = "a_link_id", by.y = "b_link_id")
			#change link_id colname
			colnames(input_data)[colnames(input_data) == 'a_link_id'] <- 'link_id'
			# merge with common col df
			input_data <- merge(input_comm, input_data, by = "link_id", all.x = T)
			rm(common_cols,input_comm,input_uncomm,input_a,input_b)
		  }
		  , error=function(e) 
		  {
			err <<- TRUE
			df_error$error_flag <- 1
			df_error$error_code <- "EX"
			df_error$error_msg <- "Rule Error: Error in rollng up data"
			df_error <<- cbind(input_json_data,df_error[,!(colnames(df_error) %in% colnames(input_json_data))])
		  })

		tryCatch(
		  {
			#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
			# Calculate Chargeable Distance - Site A to Site B - point to point - 1.25 markup
			#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
			input_data$a_longitude_final <- as.numeric(input_data$a_longitude_final)
			input_data$b_longitude_final <- as.numeric(input_data$b_longitude_final)
			input_data$a_latitude_final <- as.numeric(input_data$a_latitude_final)
			input_data$b_latitude_final <- as.numeric(input_data$b_latitude_final)
			
			# Chargeable distance taken 25% extra as it is point to point aerial distance
			input_data$dist_betw_pops <- ceiling((distHaversine(input_data[,c("a_longitude_final","a_latitude_final")],input_data[,c("b_longitude_final","b_latitude_final")])/1000)*1.25)
			
			# round off to nearest higher multiple of 5
			input_data$chargeable_distance <- ifelse((input_data$dist_betw_pops%% 5)!=0, 
													 ((input_data$dist_betw_pops %/% 5) * 5) + 5,
													 ((input_data$dist_betw_pops %/% 5) * 5))
			# in case same A and B are selected
			input_data$chargeable_distance <- ifelse(input_data$chargeable_distance==0, 5,input_data$chargeable_distance)
			
			# cap it at max 501kms
			input_data$chargeable_distance <- ifelse(input_data$chargeable_distance>500, 501, input_data$chargeable_distance)
			
			#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
			# Calculate intra_inter_flag
			#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
			input_data$intra_inter_flag <- ifelse(input_data$chargeable_distance>50, "Intercity", "Intracity")
			
			#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
			# Exceptions for Inter-city and Intra-city
			#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
			
			# Rules if Delhi is A-end
			input_data$intra_inter_flag <- ifelse(((grepl("delhi", tolower(input_data$a_resp_city))) & (grepl("gurgaon", tolower(input_data$b_resp_city)) | grepl("gurugram", tolower(input_data$b_resp_city)) | grepl("noida", tolower(input_data$b_resp_city)) | grepl("faridabad", tolower(input_data$b_resp_city)) | grepl("delhi", tolower(input_data$b_resp_city)))),
												   "Intracity",
												  input_data$intra_inter_flag)
			
			# Rules if Delhi is B-end
			input_data$intra_inter_flag <- ifelse(((grepl("delhi", tolower(input_data$b_resp_city))) & (grepl("gurgaon", tolower(input_data$a_resp_city)) | grepl("gurugram", tolower(input_data$a_resp_city)) | grepl("noida", tolower(input_data$a_resp_city)) | grepl("faridabad", tolower(input_data$a_resp_city)) | grepl("delhi", tolower(input_data$a_resp_city)))),
												  "Intracity",
												  input_data$intra_inter_flag)
			
			# Rules if mumbai is A-end
			input_data$intra_inter_flag <- ifelse(((grepl("mumbai", tolower(input_data$a_resp_city))) & (grepl("mumbai", tolower(input_data$b_resp_city)) | grepl("thane", tolower(input_data$b_resp_city)))),
												  "Intracity",
												  input_data$intra_inter_flag)
			
			# Rules if mumbai is B-end
			input_data$intra_inter_flag <- ifelse(((grepl("mumbai", tolower(input_data$b_resp_city))) & (grepl("mumbai", tolower(input_data$a_resp_city)) | grepl("thane", tolower(input_data$a_resp_city)))),
												  "Intracity",
												  input_data$intra_inter_flag)
			
			# Rules if hyderabad is A-end and Secunderabad as B-end
			input_data$intra_inter_flag <- ifelse(((grepl("hyderabad", tolower(input_data$a_resp_city))) & (grepl("secunderabad", tolower(input_data$b_resp_city)))),
												  "Intracity",
												  input_data$intra_inter_flag)
			
			# Rules if hyderabad is B-end and Secunderabad as A-end
			input_data$intra_inter_flag <- ifelse(((grepl("hyderabad", tolower(input_data$b_resp_city))) & (grepl("secunderabad", tolower(input_data$a_resp_city)))),
												  "Intracity",
												  input_data$intra_inter_flag)
			
			# Rules if Chandigarh is A-end and Mohali as B-end
			input_data$intra_inter_flag <- ifelse(((grepl("chandigarh", tolower(input_data$a_resp_city))) & (grepl("mohali", tolower(input_data$b_resp_city)))),
												  "Intracity",
												  input_data$intra_inter_flag)
			
			# Rules if Chandigarh is B-end and Mohali as A-end
			input_data$intra_inter_flag <- ifelse(((grepl("chandigarh", tolower(input_data$b_resp_city))) & (grepl("mohali", tolower(input_data$a_resp_city)))),
												  "Intracity",
												  input_data$intra_inter_flag)
			
			# Rules if Gurgaon is A-end and Noida as B-end
			input_data$intra_inter_flag <- ifelse(((grepl("gurgaon", tolower(input_data$a_resp_city)) | grepl("gurugram", tolower(input_data$a_resp_city))) & (grepl("noida", tolower(input_data$b_resp_city)))),
												  "Intracity",
												  input_data$intra_inter_flag)
			
			# Rules if Gurgaon is B-end and Noida as A-end
			input_data$intra_inter_flag <- ifelse(((grepl("gurgaon", tolower(input_data$b_resp_city)) | grepl("gurugram", tolower(input_data$b_resp_city))) & (grepl("noida", tolower(input_data$a_resp_city)))),
												  "Intracity",
												  input_data$intra_inter_flag)
			
			#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
			# Feasibility check at both ends - if 1 then trigger Manual Feasibility
			#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
			input_data$manual_flag <- ifelse((input_data$a_Predicted_Access_Feasibility=="Feasible")&(input_data$b_Predicted_Access_Feasibility=="Feasible"), 0, 1)
			
			input_data$Predicted_Access_Feasibility <- ifelse(input_data$manual_flag==0,
															  "Feasible",
															  "Not Feasible")
		  }
		  , error=function(e) 
		  {
			err <<- TRUE
			df_error$error_flag <- 1
			df_error$error_code <- "EX"
			df_error$error_msg <- "Rule Error: Error in calculating chargeable distance"
			df_error <<- cbind(input_json_data,df_error[,!(colnames(df_error) %in% colnames(input_json_data))])
		  })

		tryCatch(
		  {
			#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
			# Network Check between POPs
			#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
			# function to check pop to pop network check
			p2p_network_check <- function(pop_a,
										  pop_b,
										  req_bw,
										  msb_network){
			  
			  # link_id <- "3366"
			  # pop_a <- "TINDKRBANGRMVS0001"
			  # pop_b <- "TINDTNCHENANAR0004"
			  # req_bw <- 34
			  
			  msb_network_tmp <- msb_network[which((msb_network$BUILDING_CODE_A==pop_a)&(msb_network$BUILDING_CODE_Z==pop_b)), ]
			  msb_network_tmp$req_bw <- req_bw
			  
			  if(nrow(msb_network_tmp)>0){
				msb_network_tmp$network_p2p_flag <- ifelse(msb_network_tmp$req_bw<=msb_network_tmp$util_available, 1,0)
				p2p_network_check <- sum(msb_network_tmp$network_p2p_flag)
				p2p_network_check <- ifelse(p2p_network_check>0, 1,0)
			  }else{
				p2p_network_check<- 0
			  }
			  return(p2p_network_check)
			}
			
			# call the function to check pop to pop network
			input_data$pop2pop_network_flag <- apply(input_data, 1, function(x) p2p_network_check(
			  x["a_pop_network_loc_id"],
			  x["b_pop_network_loc_id"],
			  x["bw_mbps_upd"],
			  msb_network
			))
			rm(msb_network)
			
			# flag for orchestration
			input_data$pop2pop_network_check <- ifelse(input_data$pop2pop_network_flag==1,
													   "Feasible",
													   "Not Feasible")
			
			# create dummy site_id by concat both site_id's
			input_data$site_id <- paste(input_data$a_site_id, input_data$b_site_id, sep = "_")
		  }
		  , error=function(e) 
		  {
			err <<- TRUE
			df_error$error_flag <- 1
			df_error$error_code <- "EX"
			df_error$error_msg <- "Rule Error: Error in Pop to Pop Network Check"
			df_error <<- cbind(input_json_data,df_error[,!(colnames(df_error) %in% colnames(input_json_data))])
		  })

		##########################################################################################
		# Align datatypes with orchestration -  everything is character
		##########################################################################################
		str_cols <- names(input_data)

		input_data[,which(names(input_data) %in% str_cols)] = apply(input_data[,which(names(input_data) %in% str_cols)], 2, function(x) as.character(x))

		if(any(is.na(input_data))){
		  input_data[is.na(input_data)] <- "NA"
		}

		# Terminating DB connections
		lapply(dbListConnections(MySQL()), dbDisconnect)




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
    app.run(port = 8111, debug = True)


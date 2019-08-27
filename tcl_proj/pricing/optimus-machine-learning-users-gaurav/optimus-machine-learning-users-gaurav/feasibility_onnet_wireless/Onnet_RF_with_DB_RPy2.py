
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

def make_predict_onnet_rf():
    #get the json file as an input
    data = request.get_json(force=True)
    input_data = pd.io.json.json_normalize(data,'input_data')
    # here write your rcode 
    rstr ='''
    function(prospect_data_master,path_py){
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # Code Header ####
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #Objective - Access Feasibility, LM Cost & Network Feasibility check for Onnet RF Scenario

        # Changes to be made: [[Search #*** for items to be replaced]]
        #   1. setwd - file Directory is not atomatically picked up 
        #   4. "prospect_data_func" median imputation of BW. Do we want exact values?
        #   6. LM interim BW not handled 
        #   7. Product.Name level not handled
        #   8. Last mile contract term to be updated to "1 year" for all scrnarios

        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # R Packages - Check if needed packages are installed - if not, install them ####
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # Uncomment for API
        input_json_data <- prospect_data_master

        # Starting main function
        time_start <- proc.time()

        options(digits = 10)
        options(sqldf.driver = "SQLite")
        # Suppress warnings
        options( warn = -1 )

        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # Setting input parameters ####
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #setwd("E:/gv_personal_folder/prod_codes/gaurav_ETL/Onnet_RF")
        setwd(path_py)

        # set error parameter
        err <- FALSE
        # Define Error response dataframe
        df_error <- data.frame('Probabililty_Access_Feasibility' = 'NA',
                               'Predicted_Access_Feasibility' = 'NA',
                               'Network_Feasibility_Check' = 'NA',
                               'lm_arc_bw_onwl' = 'NA',
                               'lm_nrc_bw_onwl' = 'NA',
                               'lm_nrc_mux_onwl' = 'NA',
                               'lm_nrc_inbldg_onwl' = 'NA',
                               'lm_nrc_ospcapex_onwl' = 'NA',
                               'lm_nrc_nerental_onwl' = 'NA',
                               'lm_arc_bw_prov_ofrf' = 'NA',
                               'lm_nrc_bw_prov_ofrf' = 'NA',
                               'lm_nrc_mast_ofrf' = 'NA',
                               'lm_arc_bw_onrf' = 'NA',
                               'lm_nrc_bw_onrf' = 'NA',
                               'lm_nrc_mast_onrf' = 'NA',
                               'Nearest_Mast_ht_cost' = 'NA',
                               'Orch_LM_Type' = 'NA',
                               'Orch_Connection' = 'NA',
                               'Orch_Category' = 'NA',
                               'Orch_BW' = 'NA',
                               'bts_IP_PMP' = 'NA',
                               'interim_BW' = 'NA',
                               'solution_type' = 'NA',
                               'bts_num_BTS' = 'NA',
                               'bts_min_dist_km' = 'NA',
                               'PMP_bts_3km_radius' = 'NA',
                               'P2P_bts_3km_radius' = 'NA',
                               'bts_Closest_infra_provider' = 'NA',
                               'bts_Closest_Site_type' = 'NA',
                               'prospect_0_5km_Min_DistanceKilometers' = 'NA',
                               'prospect_0_5km_Avg_BW_Mbps' = 'NA',
                               'prospect_0_5km_Min_BW_Mbps' = 'NA',
                               'prospect_0_5km_Max_BW_Mbps' = 'NA',
                               'prospect_0_5km_feasibility_pct' = 'NA',
                               'prospect_0_5km_Sum_Feasibility_flag' = 'NA',
                               'prospect_2km_Avg_DistanceKilometers' = 'NA',
                               'prospect_2km_Avg_BW_Mbps' = 'NA',
                               'prospect_2km_Min_BW_Mbps' = 'NA',
                               'prospect_2km_Max_BW_Mbps' = 'NA',
                               'prospect_2km_Sum_Feasibility_flag' = 'NA',
                               'prospect_2km_feasibility_pct' = 'NA',
                               'onnet_0_5km_cust_Count' = 'NA',
                               'onnet_0_5km_Min_DistanceKilometers' = 'NA',
                               'onnet_0_5km_Avg_BW_Mbps' = 'NA',
                               'onnet_2km_cust_Count' = 'NA',
                               'onnet_2km_Avg_DistanceKilometers' = 'NA',
                               'onnet_2km_Avg_BW_Mbps' = 'NA',
                               'onnet_2km_Min_BW_Mbps' = 'NA',
                               'onnet_2km_Max_BW_Mbps' = 'NA',
                               'onnet_5km_cust_Count' = 'NA',
                               'onnet_5km_Avg_DistanceKilometers' = 'NA',
                               'onnet_5km_Avg_BW_Mbps' = 'NA',
                               'onnet_5km_Min_BW_Mbps' = 'NA',
                               'onnet_5km_Max_BW_Mbps' = 'NA',
                               'bts_flag' = 'NA',
                               'Bandwidth' = 'NA',
                               'Interface' = 'NA',
                               'LM_ARC_INR' = 'NA',
                               'LM_OTC_INR' = 'NA',
                               'Mast_3KM_cust_count' = 'NA',
                               'Mast_3KM_min_mast_ht' = 'NA',
                               'Mast_3KM_avg_mast_ht' = 'NA',
                               'Mast_3KM_max_mast_ht' = 'NA',
                               'Mast_3KM_nearest_mast_ht' = 'NA',
                               'Avg_3KM_Mast_ht_cost' = 'NA',
                               'LM_Cost' = 'NA',
                               'Backhaul_Network_check' = 'NA',
                               'Backhaul_Network_check_reason' = 'NA',
                               'Selected_solution_BW' = 'NA',
                               'Sector_network_check' = 'NA',
                               'time_taken' = 'NA')

        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # Defining inputs ####
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        rf_model_name <- "Onnet_RF_Model_mtry_11_nodesize_450_ntree_300.RData"
        train_data_name <- "Train_one_row.rds"

        onnet_RF_model_cutoff <- 0.9166667 

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
        # Read Input JSON File ####
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #prospect_data_master <- dplyr::bind_rows(fromJSON(file.path("./Onnet_RF_Dependencies","input_json_from_portal_IP_Added.json")))

        #input_json_data <- prospect_data_master

        # Throw error in case any input value is null
        tryCatch(
          {
        if(any(is.na(input_json_data))){
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

        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # Database Connection ####
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # Establishing connection
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

        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # Read Model Object ####
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        tryCatch( {
            load(file.path(rf_model_name))
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
        # Read Original Training data for setting same factor level ####
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        tryCatch( {
          train_data_model <- readRDS(file.path(train_data_name))
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
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # Defning all the required functions ####
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # BTS Data columns function ####
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        # Function to calculate angle between two angles
        angle_between <- function(a1, a2) {

          # This function calculates the angle between 2 angles

          angle = 180 - abs(abs(a1 - a2) - 180)  
          return (angle)
        }

        bts_distance_calc <- function(P_lat,
                                      P_long,
                                      bts_data_n = bts_data,
                                      angle_between = angle_between){

          # This fuctions takes lat long for a site and returns the following information
          #   bts_num_BTS = Closest BTS name
          #   bts_min_dist_km = Distance to closest BTS
          #   solution_type = Selected solution type (UBRPMP, UBRP2P and not available)
          #   PMP_bts_3km_radius = Number of PMP towers in 2 KM radius
          #   P2P_bts_3km_radius = Number of P2P towers in 2 KM radius
          #   bts_Closest_infra_provider = Closest tower infra provider
          #   bts_Closest_Site_type = Closest tower Site type
          #   IP_PMP = IP of PMP sector (if found)

          P_long <- as.numeric(P_long)
          P_lat  <- as.numeric(P_lat)
          IP_PMP <- NA

          # Reducing BTS search space
          bts_data_n <- bts_data_n[which(between(bts_data_n$Longitude, P_long - 0.1, P_long + 0.1) &
                                           between(bts_data_n$Latitude, P_lat - 0.1, P_lat + 0.1)
          ),] 

          if (nrow(bts_data_n) == 0) {
            return (list('bts_num_BTS' = NA,
                         'bts_min_dist_km' = NA,
                         'solution_type' = NA,
                         'PMP_bts_3km_radius' = NA,
                         'P2P_bts_3km_radius' = NA,
                         "bts_Closest_infra_provider" = NA,
                         "bts_Closest_Site_type" = NA,
                         "IP_PMP" <- NA
            ))
          }

          else {

            tryCatch( {
              # Calculating Distance
              bts_data_n$bts_distance_km <- distHaversine(
                c(as.numeric(P_long), as.numeric(P_lat)),
                bts_data_n[, c("Longitude","Latitude")])

              bts_data_n$bts_distance_km <- bts_data_n$bts_distance_km/ 1000

              # Calculating angle
              bts_data_n$angle <- bearing(
                bts_data_n[, c("Longitude","Latitude")],
                c(as.numeric(P_long), as.numeric(P_lat)))

              # Fixing negative angles 
              bts_data_n$angle <- ifelse(bts_data_n$angle < 0,(bts_data_n$angle + 360),bts_data_n$angle)

              # Closest BTS Tower 
              bts_num_BTS <- bts_data_n$Site_ID[which.min(bts_data_n$bts_distance_km)]

              # Closest BTS infra provider
              bts_Closest_infra_provider <- bts_data_n$INFRA_PROVIDER[which.min(bts_data_n$bts_distance_km)]
              # Closest BTS Site type
              bts_Closest_Site_type <- bts_data_n$SITE_TYPE[which.min(bts_data_n$bts_distance_km)]

              # Distance to closest BTS Tower
              bts_min_dist_km <- min(bts_data_n$bts_distance_km)

              # Tagging closest BTS as UBRPMP or UBRP2P
              closest_bts <- bts_data_n [which(bts_data_n$Site_ID == bts_num_BTS),]
              closest_bts <- closest_bts[which(closest_bts$pmp_flag == 1),]

              if (nrow(closest_bts) == 0) {
                solution_type = "UBRP2P"
              } else {
                # Checking if in angle range
                closest_bts$Min_angle <- angle_between(as.numeric(closest_bts$AZIMUTH),
                                                       closest_bts$angle)
                closest_bts$angle_range <- ifelse(closest_bts$Min_angle <= (closest_bts$PMP_angle)/2 , 1, 0)

                # Imputing missing with 0 as these were out of range, so degree does not matter
                closest_bts$angle_range[is.na(closest_bts$angle_range)] <- 0

                solution_type <- ifelse(max(closest_bts$angle_range) == 1, "UBR_PMP", "UBRP2P")


                # Added # Picking IP for network check
                if (solution_type == "UBR_PMP") {
                  IP_PMP <- closest_bts$IPADDRESS[which.max(closest_bts$angle_range)]
                }

              }

              # Number of BTS towers in 3 KM radius
              for_3_km <- bts_data_n[which( bts_data_n$bts_distance_km <= 3),]

              if (nrow(for_3_km) > 0) {

                PMP_bts_3km_radius <- 0
                P2P_bts_3km_radius <- 0

                PMP_3KM <- for_3_km[which(for_3_km$pmp_flag == 1),]
                if (nrow(PMP_3KM) > 0) {
                  PMP_bts_3km_radius <- length(unique(PMP_3KM$Site_ID))
                }

                P2P_3KM <- for_3_km[which(for_3_km$pmp_flag == 0),]
                if (nrow(P2P_3KM) > 0) {
                  P2P_bts_3km_radius <- length(unique(P2P_3KM$Site_ID))
                } 

              } else {
                PMP_bts_3km_radius <- 0
                P2P_bts_3km_radius <- 0
              }

              return (list("bts_num_BTS" = bts_num_BTS,
                           "bts_min_dist_km" = bts_min_dist_km,
                           "solution_type" = solution_type,
                           "PMP_bts_3km_radius" = PMP_bts_3km_radius,
                           "P2P_bts_3km_radius" = P2P_bts_3km_radius,
                           "bts_Closest_infra_provider" = bts_Closest_infra_provider,
                           "bts_Closest_Site_type" = bts_Closest_Site_type,
                           "IP_PMP" = IP_PMP
              ))

            }, 
            error = function(error_message) {
              return(list('bts_num_BTS' = NA,
                          'bts_min_dist_km' = NA,
                          'solution_type' = NA,
                          'PMP_bts_3km_radius' = NA,
                          'P2P_bts_3km_radius' = NA,
                          "bts_Closest_infra_provider" = NA,
                          "bts_Closest_Site_type" = NA,
                          "IP_PMP" <- NA
              ))
            })
          }
        }


        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # Prospect Data columns function ####
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        prospect_distance_calc <- function(P_lat, P_long, p_date ,prospect_data_n){

          # This function accepts lat long for a site and returns the following:
          #   prospect_0_5km_cust_Count = Number of historical prospects in 0.5 KM radius
          #   prospect_0_5km_Avg_DistanceKilometers = Avg distance of historical prospects in 0.5 KM radius
          #   prospect_0_5km_Min_DistanceKilometers = Min distance of historical prospects in 0.5 KM radius
          #   prospect_0_5km_Avg_BW_Mbps = Avg BW of historical prospects in 0.5 KM radius
          #   prospect_0_5km_Min_BW_Mbps = Min BW of historical prospects in 0.5 KM radius
          #   prospect_0_5km_Max_BW_Mbps = Max BW of historical prospects in 0.5 KM radius
          #   prospect_0_5km_feasibility_pct = % feasible historical prospects in 0.5 KM radius
          #   prospect_0_5km_Sum_Feasibility_flag = # feasible historical prospects in 0.5 KM radius
          #   prospect_2km_cust_Count = Number of historical prospects in 2 KM radius
          #   prospect_2km_Avg_DistanceKilometers = Avg distance of historical prospects in 2 KM radius
          #   prospect_2km_Min_DistanceKilometers = Min distance of historical prospects in 2 KM radius
          #   prospect_2km_Avg_BW_Mbps = Avg BW of historical prospects in 2 KM radius
          #   prospect_2km_Min_BW_Mbps = Min BW of historical prospects in 2 KM radius
          #   prospect_2km_Max_BW_Mbps = Max BW of historical prospects in 2 KM radius
          #   prospect_2km_Sum_Feasibility_flag = # feasible historical prospects in 0.5 KM radius
          #   prospect_2km_feasibility_pct = % feasible historical prospects in 2 KM radius

          p_date <- as.Date(p_date, format = "%Y-%m-%d")
          P_long <- as.numeric(P_long)
          P_lat  <- as.numeric(P_lat)

          # reducing search space
          prospect_data_n <- prospect_data_n[which(between(prospect_data_n$CustomerLongitude1, P_long - 0.1, P_long + 0.1) &
                                                     between(prospect_data_n$CustomerLatitude1, P_lat - 0.1, P_lat + 0.1) &
                                                     prospect_data_n$Feasibility.Response..Created.Date < p_date
          ),] 
          if (nrow(prospect_data_n) == 0) {
            return (list(
              'prospect_0_5km_cust_Count' = NA,
              'prospect_0_5km_Avg_DistanceKilometers' = NA,
              'prospect_0_5km_Min_DistanceKilometers' = NA,
              'prospect_0_5km_Avg_BW_Mbps' = NA,
              'prospect_0_5km_Min_BW_Mbps' = NA,
              'prospect_0_5km_Max_BW_Mbps' = NA,
              'prospect_0_5km_feasibility_pct' = NA,
              'prospect_0_5km_Sum_Feasibility_flag' = NA,
              'prospect_2km_cust_Count' = NA,
              'prospect_2km_Avg_DistanceKilometers' = NA,
              'prospect_2km_Min_DistanceKilometers' = NA,
              'prospect_2km_Avg_BW_Mbps' = NA,
              'prospect_2km_Min_BW_Mbps' = NA,
              'prospect_2km_Max_BW_Mbps' = NA,
              'prospect_2km_Sum_Feasibility_flag' = NA,
              'prospect_2km_feasibility_pct' = NA

            ))
          }

          else {

            tryCatch( {

              prospect_data_n$prospect_distance_km <- distHaversine(
                c(P_long, P_lat),
                prospect_data_n[, c("CustomerLongitude1","CustomerLatitude1")])
              prospect_data_n$prospect_distance_km <- prospect_data_n$prospect_distance_km/ 1000

              for_0_5_km <- prospect_data_n[which(prospect_data_n$prospect_distance_km <= 0.5),]
              for_2_km <- prospect_data_n[which(prospect_data_n$prospect_distance_km <= 2),]

              # Summary for 0.5 KM
              if (nrow(for_0_5_km) > 0) {
                prospect_0_5km_cust_Count = nrow(for_0_5_km)
                prospect_0_5km_Avg_DistanceKilometers = mean(for_0_5_km$prospect_distance_km, na.rm = T)
                prospect_0_5km_Min_DistanceKilometers = min(for_0_5_km$prospect_distance_km, na.rm = T)
                prospect_0_5km_Avg_BW_Mbps = mean(for_0_5_km$BW_mbps, na.rm = T)
                prospect_0_5km_Min_BW_Mbps = min(for_0_5_km$BW_mbps, na.rm = T)
                prospect_0_5km_Max_BW_Mbps = max(for_0_5_km$BW_mbps, na.rm = T)
                prospect_0_5km_Sum_Feasibility_flag = sum(for_0_5_km$Feasibility_flag, na.rm = T)
                prospect_0_5km_feasibility_pct = sum(for_0_5_km$Feasibility_flag, na.rm = T)/ nrow(for_0_5_km)
              } else {
                prospect_0_5km_cust_Count = NA
                prospect_0_5km_Avg_DistanceKilometers = NA
                prospect_0_5km_Min_DistanceKilometers = NA
                prospect_0_5km_Avg_BW_Mbps = NA
                prospect_0_5km_Min_BW_Mbps = NA
                prospect_0_5km_Max_BW_Mbps = NA
                prospect_0_5km_Sum_Feasibility_flag = NA
                prospect_0_5km_feasibility_pct = NA
              }

              # Summary for 2 KM
              if (nrow(for_2_km) > 0) {
                prospect_2km_cust_Count = nrow(for_2_km)
                prospect_2km_Avg_DistanceKilometers = mean(for_2_km$prospect_distance_km, na.rm = T)
                prospect_2km_Min_DistanceKilometers = min(for_2_km$prospect_distance_km, na.rm = T)
                prospect_2km_Avg_BW_Mbps = mean(for_2_km$BW_mbps, na.rm = T)
                prospect_2km_Min_BW_Mbps = min(for_2_km$BW_mbps, na.rm = T)
                prospect_2km_Max_BW_Mbps = max(for_2_km$BW_mbps, na.rm = T)
                prospect_2km_Sum_Feasibility_flag = sum(for_2_km$Feasibility_flag, na.rm = T)
                prospect_2km_feasibility_pct = sum(for_2_km$Feasibility_flag, na.rm = T)/ nrow(for_2_km)
              } else {
                prospect_2km_cust_Count = NA
                prospect_2km_Avg_DistanceKilometers = NA
                prospect_2km_Min_DistanceKilometers = NA
                prospect_2km_Avg_BW_Mbps = NA
                prospect_2km_Min_BW_Mbps = NA
                prospect_2km_Max_BW_Mbps = NA
                prospect_2km_Sum_Feasibility_flag = NA
                prospect_2km_feasibility_pct = NA
              }

              return (list(
                'prospect_0_5km_cust_Count' = prospect_0_5km_cust_Count,
                'prospect_0_5km_Avg_DistanceKilometers' = prospect_0_5km_Avg_DistanceKilometers,
                'prospect_0_5km_Min_DistanceKilometers' = prospect_0_5km_Min_DistanceKilometers,
                'prospect_0_5km_Avg_BW_Mbps' = prospect_0_5km_Avg_BW_Mbps,
                'prospect_0_5km_Min_BW_Mbps' = prospect_0_5km_Min_BW_Mbps,
                'prospect_0_5km_Max_BW_Mbps' = prospect_0_5km_Max_BW_Mbps,
                'prospect_0_5km_feasibility_pct' = prospect_0_5km_feasibility_pct,
                'prospect_0_5km_Sum_Feasibility_flag' = prospect_0_5km_Sum_Feasibility_flag,
                'prospect_2km_cust_Count' = prospect_2km_cust_Count,
                'prospect_2km_Avg_DistanceKilometers' = prospect_2km_Avg_DistanceKilometers,
                'prospect_2km_Min_DistanceKilometers' = prospect_2km_Min_DistanceKilometers,
                'prospect_2km_Avg_BW_Mbps' = prospect_2km_Avg_BW_Mbps,
                'prospect_2km_Min_BW_Mbps' = prospect_2km_Min_BW_Mbps,
                'prospect_2km_Max_BW_Mbps' = prospect_2km_Max_BW_Mbps,
                'prospect_2km_Sum_Feasibility_flag' = prospect_2km_Sum_Feasibility_flag,
                'prospect_2km_feasibility_pct' = prospect_2km_feasibility_pct
              ))

            }, 
            error = function(error_message) {
              return(list(
                'prospect_0_5km_cust_Count' = NA,
                'prospect_0_5km_Avg_DistanceKilometers' = NA,
                'prospect_0_5km_Min_DistanceKilometers' = NA,
                'prospect_0_5km_Avg_BW_Mbps' = NA,
                'prospect_0_5km_Min_BW_Mbps' = NA,
                'prospect_0_5km_Max_BW_Mbps' = NA,
                'prospect_0_5km_feasibility_pct' = NA,
                'prospect_0_5km_Sum_Feasibility_flag' = NA,
                'prospect_2km_cust_Count' = NA,
                'prospect_2km_Avg_DistanceKilometers' = NA,
                'prospect_2km_Min_DistanceKilometers' = NA,
                'prospect_2km_Avg_BW_Mbps' = NA,
                'prospect_2km_Min_BW_Mbps' = NA,
                'prospect_2km_Max_BW_Mbps' = NA,
                'prospect_2km_Sum_Feasibility_flag' = NA,
                'prospect_2km_feasibility_pct' = NA

              ))
            })
          }
        }


        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # Customer Data columns function ####
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        customer_distance_calc <- function(P_lat, P_long, p_date ,onnet_cust_data_n = onnet_cust_data){

          # This function takes a site lat long and returns the following:
          #   onnet_0_5km_cust_Count = Number of onnet RF customers in 0.5KM
          #   onnet_0_5km_Avg_DistanceKilometers = Avg distance of onnet RF customers in 0.5KM
          #   onnet_0_5km_Min_DistanceKilometers = Min distance of onnet RF customers in 0.5KM
          #   onnet_0_5km_Avg_BW_Mbps = Avg BW of onnet RF customers in 0.5KM
          #   onnet_0_5km_Min_BW_Mbps = Min BW of onnet RF customers in 0.5KM
          #   onnet_0_5km_Max_BW_Mbps = Max BW of onnet RF customers in 0.5KM
          #   onnet_2km_cust_Count = Number of onnet RF customers in 2KM
          #   onnet_2km_Avg_DistanceKilometers = Avg distance of onnet RF customers in 2KM
          #   onnet_2km_Min_DistanceKilometers = Min distance of onnet RF customers in 2KM
          #   onnet_2km_Avg_BW_Mbps = Avg BW of onnet RF customers in 2KM
          #   onnet_2km_Min_BW_Mbps = Min BW of onnet RF customers in 2KM
          #   onnet_2km_Max_BW_Mbps = Max BW of onnet RF customers in 2KM
          #   onnet_5km_cust_Count = Number of onnet RF customers in 5KM
          #   onnet_5km_Avg_DistanceKilometers = Avg distance of onnet RF customers in 5KM
          #   onnet_5km_Min_DistanceKilometers = Min distance of onnet RF customers in 5KM
          #   onnet_5km_Avg_BW_Mbps = Avg BW of onnet RF customers in 5KM
          #   onnet_5km_Min_BW_Mbps = Avg BW of onnet RF customers in 5KM
          #   onnet_5km_Max_BW_Mbps = Avg BW of onnet RF customers in 5KM

          p_date <- as.Date(p_date, format = "%Y-%m-%d")
          P_long <- as.numeric(P_long)
          P_lat  <- as.numeric(P_lat)

          # Reducing search space 
          onnet_cust_data_n <- onnet_cust_data_n[which(between(onnet_cust_data_n$Longitude, P_long - 0.1, P_long + 0.1) &
                                                         between(onnet_cust_data_n$Latitude, P_lat - 0.1, P_lat + 0.1) &
                                                         onnet_cust_data_n$Date.Of.Acceptance < p_date 
          ),] 
          if (nrow(onnet_cust_data_n) == 0) {
            return (list(
              "onnet_0_5km_cust_Count"  = NA,
              "onnet_0_5km_Avg_DistanceKilometers"  = NA,
              "onnet_0_5km_Min_DistanceKilometers"  = NA,
              "onnet_0_5km_Avg_BW_Mbps"  = NA,
              "onnet_0_5km_Min_BW_Mbps"  = NA,
              "onnet_0_5km_Max_BW_Mbps"  = NA,
              "onnet_2km_cust_Count"  = NA,
              "onnet_2km_Avg_DistanceKilometers"  = NA,
              "onnet_2km_Min_DistanceKilometers"  = NA,
              "onnet_2km_Avg_BW_Mbps"  = NA,
              "onnet_2km_Min_BW_Mbps"  = NA,
              "onnet_2km_Max_BW_Mbps"  = NA,
              "onnet_5km_cust_Count"  = NA,
              "onnet_5km_Avg_DistanceKilometers"  = NA,
              "onnet_5km_Min_DistanceKilometers"  = NA,
              "onnet_5km_Avg_BW_Mbps"  = NA,
              "onnet_5km_Min_BW_Mbps"  = NA,
              "onnet_5km_Max_BW_Mbps"  = NA
            ))
          }

          else {

            tryCatch( {

              onnet_cust_data_n$onnet_distance_km <- distHaversine(
                c(P_long, P_lat),
                onnet_cust_data_n[, c("Longitude","Latitude")])
              onnet_cust_data_n$onnet_distance_km <- onnet_cust_data_n$onnet_distance_km/ 1000

              for_0_5_km <- onnet_cust_data_n[which(onnet_cust_data_n$onnet_distance_km <= 0.5),]
              for_2_km <- onnet_cust_data_n[which(onnet_cust_data_n$onnet_distance_km <= 2),]
              for_5_km <- onnet_cust_data_n[which(onnet_cust_data_n$onnet_distance_km <= 5),]

              # Summary for 0.5 KM
              if (nrow(for_0_5_km) > 0) {
                onnet_0_5km_cust_Count = nrow(for_0_5_km)
                onnet_0_5km_Avg_DistanceKilometers = mean(for_0_5_km$onnet_distance_km, na.rm = T)
                onnet_0_5km_Min_DistanceKilometers = min(for_0_5_km$onnet_distance_km, na.rm = T)
                onnet_0_5km_Avg_BW_Mbps = mean(for_0_5_km$BW, na.rm = T)
                onnet_0_5km_Min_BW_Mbps = min(for_0_5_km$BW, na.rm = T)
                onnet_0_5km_Max_BW_Mbps = max(for_0_5_km$BW, na.rm = T)
              } else {
                onnet_0_5km_cust_Count = NA
                onnet_0_5km_Avg_DistanceKilometers = NA
                onnet_0_5km_Min_DistanceKilometers = NA
                onnet_0_5km_Avg_BW_Mbps = NA
                onnet_0_5km_Min_BW_Mbps = NA
                onnet_0_5km_Max_BW_Mbps = NA
              }

              # Summary for 2 KM
              if (nrow(for_2_km) > 0) {
                onnet_2km_cust_Count = nrow(for_2_km)
                onnet_2km_Avg_DistanceKilometers = mean(for_2_km$onnet_distance_km, na.rm = T)
                onnet_2km_Min_DistanceKilometers = min(for_2_km$onnet_distance_km, na.rm = T)
                onnet_2km_Avg_BW_Mbps = mean(for_2_km$BW, na.rm = T)
                onnet_2km_Min_BW_Mbps = min(for_2_km$BW, na.rm = T)
                onnet_2km_Max_BW_Mbps = max(for_2_km$BW, na.rm = T)
              } else {
                onnet_2km_cust_Count = NA
                onnet_2km_Avg_DistanceKilometers = NA
                onnet_2km_Min_DistanceKilometers = NA
                onnet_2km_Avg_BW_Mbps = NA
                onnet_2km_Min_BW_Mbps = NA
                onnet_2km_Max_BW_Mbps = NA
              }

              # Summary for 5 KM
              if (nrow(for_5_km) > 0) {
                onnet_5km_cust_Count = nrow(for_5_km)
                onnet_5km_Avg_DistanceKilometers = mean(for_5_km$onnet_distance_km, na.rm = T)
                onnet_5km_Min_DistanceKilometers = min(for_5_km$onnet_distance_km, na.rm = T)
                onnet_5km_Avg_BW_Mbps = mean(for_5_km$BW, na.rm = T)
                onnet_5km_Min_BW_Mbps = min(for_5_km$BW, na.rm = T)
                onnet_5km_Max_BW_Mbps = max(for_5_km$BW, na.rm = T)
              } else {
                onnet_5km_cust_Count = NA
                onnet_5km_Avg_DistanceKilometers = NA
                onnet_5km_Min_DistanceKilometers = NA
                onnet_5km_Avg_BW_Mbps = NA
                onnet_5km_Min_BW_Mbps = NA
                onnet_5km_Max_BW_Mbps = NA
              }

              return (list(
                "onnet_0_5km_cust_Count" = onnet_0_5km_cust_Count,
                "onnet_0_5km_Avg_DistanceKilometers" = onnet_0_5km_Avg_DistanceKilometers,
                "onnet_0_5km_Min_DistanceKilometers" = onnet_0_5km_Min_DistanceKilometers,
                "onnet_0_5km_Avg_BW_Mbps" = onnet_0_5km_Avg_BW_Mbps,
                "onnet_0_5km_Min_BW_Mbps" = onnet_0_5km_Min_BW_Mbps,
                "onnet_0_5km_Max_BW_Mbps" = onnet_0_5km_Max_BW_Mbps,
                "onnet_2km_cust_Count" = onnet_2km_cust_Count,
                "onnet_2km_Avg_DistanceKilometers" = onnet_2km_Avg_DistanceKilometers,
                "onnet_2km_Min_DistanceKilometers" = onnet_2km_Min_DistanceKilometers,
                "onnet_2km_Avg_BW_Mbps" = onnet_2km_Avg_BW_Mbps,
                "onnet_2km_Min_BW_Mbps" = onnet_2km_Min_BW_Mbps,
                "onnet_2km_Max_BW_Mbps" = onnet_2km_Max_BW_Mbps,
                "onnet_5km_cust_Count" = onnet_5km_cust_Count,
                "onnet_5km_Avg_DistanceKilometers" = onnet_5km_Avg_DistanceKilometers,
                "onnet_5km_Min_DistanceKilometers" = onnet_5km_Min_DistanceKilometers,
                "onnet_5km_Avg_BW_Mbps" = onnet_5km_Avg_BW_Mbps,
                "onnet_5km_Min_BW_Mbps" = onnet_5km_Min_BW_Mbps,
                "onnet_5km_Max_BW_Mbps" = onnet_5km_Max_BW_Mbps
              ))

            }, 
            error = function(error_message) {
              return(list(
                "onnet_0_5km_cust_Count"  = NA,
                "onnet_0_5km_Avg_DistanceKilometers"  = NA,
                "onnet_0_5km_Min_DistanceKilometers"  = NA,
                "onnet_0_5km_Avg_BW_Mbps"  = NA,
                "onnet_0_5km_Min_BW_Mbps"  = NA,
                "onnet_0_5km_Max_BW_Mbps"  = NA,
                "onnet_2km_cust_Count"  = NA,
                "onnet_2km_Avg_DistanceKilometers"  = NA,
                "onnet_2km_Min_DistanceKilometers"  = NA,
                "onnet_2km_Avg_BW_Mbps"  = NA,
                "onnet_2km_Min_BW_Mbps"  = NA,
                "onnet_2km_Max_BW_Mbps"  = NA,
                "onnet_5km_cust_Count"  = NA,
                "onnet_5km_Avg_DistanceKilometers"  = NA,
                "onnet_5km_Min_DistanceKilometers"  = NA,
                "onnet_5km_Avg_BW_Mbps"  = NA,
                "onnet_5km_Min_BW_Mbps"  = NA,
                "onnet_5km_Max_BW_Mbps"  = NA
              ))
            })
          }
        }



        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # Final Data clean up function ####
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        final_cleaning_func <- function(final_prospect_data) {

          # This function takes dataset post BTS, prospect and customer function and does the following:
          #   1. Imputes null with 99999 with distance columns
          #   2. Impute null with 0 for non distance numeric columns
          #   3. Fixing level of categorical variables
          #   4. Dropping columns not required

          # Converting null distances to 99999
          cols_to_impute_99999 <- c( "prospect_0_5km_Avg_DistanceKilometers",
                                     "prospect_0_5km_Min_DistanceKilometers",
                                     "prospect_2km_Avg_DistanceKilometers"  ,
                                     "prospect_2km_Min_DistanceKilometers"  ,
                                     "bts_min_dist_km"                      ,
                                     "onnet_0_5km_Avg_DistanceKilometers"   ,
                                     "onnet_0_5km_Min_DistanceKilometers"   ,
                                     "onnet_2km_Avg_DistanceKilometers"     ,
                                     "onnet_2km_Min_DistanceKilometers"     ,
                                     "onnet_5km_Avg_DistanceKilometers"     ,
                                     "onnet_5km_Min_DistanceKilometers"     
          )

          final_prospect_data[cols_to_impute_99999][is.na(final_prospect_data[cols_to_impute_99999])] <- 99999
          rm(cols_to_impute_99999)

          # Imputing with 0
          cols_to_impute_o <- c( "prospect_0_5km_cust_Count"            ,
                                 "prospect_0_5km_Avg_BW_Mbps"           ,
                                 "prospect_0_5km_Min_BW_Mbps"           ,
                                 "prospect_0_5km_Max_BW_Mbps"           ,
                                 "prospect_0_5km_feasibility_pct"       ,
                                 "prospect_0_5km_Sum_Feasibility_flag"  ,
                                 "prospect_2km_cust_Count"              ,
                                 "prospect_2km_Avg_BW_Mbps"             ,
                                 "prospect_2km_Min_BW_Mbps"             ,
                                 "prospect_2km_Max_BW_Mbps"             ,
                                 "prospect_2km_Sum_Feasibility_flag"    ,
                                 "prospect_2km_feasibility_pct"         ,
                                 'PMP_bts_3km_radius'                   ,
                                 'P2P_bts_3km_radius'                   ,
                                 "onnet_0_5km_cust_Count"               ,
                                 "onnet_0_5km_Avg_BW_Mbps"              ,
                                 "onnet_0_5km_Min_BW_Mbps"              ,
                                 "onnet_0_5km_Max_BW_Mbps"              ,
                                 "onnet_2km_cust_Count"                 ,
                                 "onnet_2km_Avg_BW_Mbps"                ,
                                 "onnet_2km_Min_BW_Mbps"                ,
                                 "onnet_2km_Max_BW_Mbps"                ,
                                 "onnet_5km_cust_Count"                 ,
                                 "onnet_5km_Avg_BW_Mbps"                ,
                                 "onnet_5km_Min_BW_Mbps"                ,
                                 "onnet_5km_Max_BW_Mbps"                
          )

          final_prospect_data[cols_to_impute_o][is.na(final_prospect_data[cols_to_impute_o])] <- 0 
          rm(cols_to_impute_o)


          # Managing input levels
          final_prospect_data$Customer.Segment <- ifelse((grepl("enterprise", tolower(final_prospect_data$Customer.Segment)) & (grepl("silver", tolower(final_prospect_data$Customer.Segment)))), "Enterprise ? Silver",final_prospect_data$Customer.Segment)
          final_prospect_data$Customer.Segment <- ifelse((grepl("enterprise", tolower(final_prospect_data$Customer.Segment)) & (grepl("gold", tolower(final_prospect_data$Customer.Segment)))), "Enterprise - Gold",final_prospect_data$Customer.Segment)
          final_prospect_data$Customer.Segment <- ifelse((grepl("enterprise", tolower(final_prospect_data$Customer.Segment)) & (grepl("mes", tolower(final_prospect_data$Customer.Segment)))), "Enterprise - MES",final_prospect_data$Customer.Segment)
          final_prospect_data$Customer.Segment <- ifelse((grepl("enterprise", tolower(final_prospect_data$Customer.Segment)) & (grepl("strategic", tolower(final_prospect_data$Customer.Segment)))), "Enterprise - Strategic",final_prospect_data$Customer.Segment)
          final_prospect_data$Customer.Segment <- ifelse((grepl("enterprise", tolower(final_prospect_data$Customer.Segment)) & (grepl("system integrators", tolower(final_prospect_data$Customer.Segment)))), "Enterprise - System Integrators",final_prospect_data$Customer.Segment)
          final_prospect_data$Customer.Segment <- ifelse((grepl("enterprise", tolower(final_prospect_data$Customer.Segment)) & (grepl("government/psu", tolower(final_prospect_data$Customer.Segment)))), "Enterprise ? Government/PSU",final_prospect_data$Customer.Segment)
          final_prospect_data$Customer.Segment <- ifelse((grepl("enterprise", tolower(final_prospect_data$Customer.Segment)) & (grepl("growth accounts", tolower(final_prospect_data$Customer.Segment)))), "Enterprise ? Growth Accounts",final_prospect_data$Customer.Segment)
          final_prospect_data$Customer.Segment <- ifelse((grepl("enterprise", tolower(final_prospect_data$Customer.Segment)) & (grepl("direct", tolower(final_prospect_data$Customer.Segment)))), "Enterprise-Direct",final_prospect_data$Customer.Segment)
          final_prospect_data$Customer.Segment <- ifelse(grepl("carriers", tolower(final_prospect_data$Customer.Segment)), "Carriers",final_prospect_data$Customer.Segment)
          final_prospect_data$Customer.Segment <- ifelse((grepl("enterprise", tolower(final_prospect_data$Customer.Segment)) & (grepl("partners", tolower(final_prospect_data$Customer.Segment)))), "Enterprise-Partners Account",final_prospect_data$Customer.Segment)
          final_prospect_data$Customer.Segment <- ifelse(grepl("smb", tolower(final_prospect_data$Customer.Segment)), "SMB",final_prospect_data$Customer.Segment)


          # Grouping categorical variables
          final_prospect_data$Customer.Segment[is.na(final_prospect_data$Customer.Segment)] <- "Others"
          final_prospect_data$Customer.Segment <- case(final_prospect_data$Customer.Segment,
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

          final_prospect_data$bts_Closest_infra_provider[is.na(final_prospect_data$bts_Closest_infra_provider)] <- "Others"
          final_prospect_data$bts_Closest_infra_provider <- case(final_prospect_data$bts_Closest_infra_provider,
                                                                 'ATC' = 'ATC',
                                                                 'Reliance' = 'Reliance',
                                                                 'TTSL' = 'TTSL',
                                                                 'TTML' = 'TTML',
                                                                 'TCL' = 'TCL',
                                                                 default = "Others"
          )


          # Managing level
          final_prospect_data$Local.Loop.Interface <- ifelse((grepl("fast", tolower(final_prospect_data$Local.Loop.Interface)) & (grepl("ethernet", tolower(final_prospect_data$Local.Loop.Interface)))), "FE",final_prospect_data$Local.Loop.Interface)
          final_prospect_data$Local.Loop.Interface <- ifelse((grepl("gigabit", tolower(final_prospect_data$Local.Loop.Interface)) & (grepl("ethernet", tolower(final_prospect_data$Local.Loop.Interface)))), "GE",final_prospect_data$Local.Loop.Interface)

          final_prospect_data$Local.Loop.Interface[is.na(final_prospect_data$Local.Loop.Interface)] <- "Others"
          final_prospect_data$Local.Loop.Interface <- case(final_prospect_data$Local.Loop.Interface,
                                                           '100-Base-TX' = '100-Base-TX',
                                                           'FE' = 'FE',
                                                           'Ethernet' = 'Ethernet',
                                                           '10-Base-T' = '10-Base-T',
                                                           default = "Others"
          )


          final_prospect_data$Product.Name[is.na(final_prospect_data$Product.Name)] <- "Others"
          final_prospect_data$Product.Name <- case(final_prospect_data$Product.Name,
                                                   'Global VPN' = 'Global VPN',
                                                   'Internet Access Service' = 'Internet Access Service',
                                                   'Priority Ethernet - Point to Point' = 'Priority Ethernet - Point to Point',
                                                   'Priority Ethernet - Point to MultiPoint' = 'Priority Ethernet - Point to MultiPoint',
                                                   default = "Others"
          )

          final_prospect_data$bts_Closest_Site_type[is.na(final_prospect_data$bts_Closest_Site_type)] <- "Others"
          final_prospect_data$bts_Closest_Site_type <- case(final_prospect_data$bts_Closest_Site_type,
                                                            'GBT' = 'GBT',
                                                            'RBT' = 'RBT',
                                                            'Roof Top' = 'Roof Top',
                                                            'RTP' = 'RTP',
                                                            'RTT' ='RTT',
                                                            default = "Others"
          )


          # Managing level
          final_prospect_data$Sales.Org <- ifelse(grepl("enterprise", tolower(final_prospect_data$Sales.Org)), "Enterprise",final_prospect_data$Sales.Org)
          final_prospect_data$Sales.Org <- ifelse(grepl("service provider", tolower(final_prospect_data$Sales.Org)), "Service Provider",final_prospect_data$Sales.Org)
          final_prospect_data$Sales.Org <- ifelse(grepl("cso", tolower(final_prospect_data$Sales.Org)), "CSO",final_prospect_data$Sales.Org)
          final_prospect_data$Sales.Org <- ifelse(grepl("it", tolower(final_prospect_data$Sales.Org)), "IT",final_prospect_data$Sales.Org)

          final_prospect_data$Sales.Org[is.na(final_prospect_data$Sales.Org)] <- "Others"
          final_prospect_data$Sales.Org <- case(final_prospect_data$Sales.Org,
                                                'Enterprise' = 'Enterprise',
                                                'Service Provider' = 'Service Provider',
                                                'CSO' = 'CSO',
                                                'IT' = 'IT',
                                                default = "Others"
          )

          final_prospect_data$solution_type[is.na(final_prospect_data$solution_type)] <- "Others"
          final_prospect_data$solution_type <- case(final_prospect_data$solution_type,
                                                    'UBR_PMP' = 'UBR_PMP',
                                                    'UBRP2P' = 'UBRP2P',
                                                    default = "Others"
          )

          #*** Fixing level for last mile contract term
          final_prospect_data$Last.Mile.Contract.Term <- "1 Year"

          # Creaing flags
          final_prospect_data$bts_flag <- ifelse(final_prospect_data$bts_min_dist_km > 3, 0, 1)

          # Dropping columns not required
          cols_to_drop <- c("Feasibility.Response..Feasibility.Response.Auto.No.",
                            # "Feasibility.Response..Created.Date",

                            "onnet_0_5km_Max_BW_Mbps",
                            "onnet_0_5km_Min_BW_Mbps",
                            "onnet_0_5km_Avg_DistanceKilometers",
                            "onnet_2km_Min_DistanceKilometers",
                            "onnet_5km_Min_DistanceKilometers",
                            "prospect_0_5km_Avg_DistanceKilometers",
                            "prospect_0_5km_cust_Count",
                            "prospect_2km_Min_DistanceKilometers",
                            "prospect_2km_cust_Count"
          )

          final_prospect_data <- final_prospect_data[ , -which(names(final_prospect_data) %in% cols_to_drop)]
          final_prospect_data$Identifier <- "VAL"

          return(final_prospect_data)
        }



        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # Onnet RF model scoring function
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        model_scoring_func <- function(final_prospect_data) {

          # This model inputs cleaned data for scoring. It performs the following functions:
          #   1. Import  data row 
          #   2. Appending training row with cleaned data to correct for variable levels (training row is filtered out)
          #   3. Predicting using model object
          #   4. Feasible/ NF decision based on cut off

          final_prospect_data <- select(final_prospect_data,
                                        -Latitude_final,
                                        -Longitude_final,
                                        -prospect_name,
                                        -Burstable_BW,
                                        -resp_city,
                                        # -resp_state,
                                        -Feasibility.Response..Created.Date,
                                        # -last_mile_contract_term,
                                        -Account_id_with_18_Digit,
                                        -opportunityTerm,
                                        -quoteType_quote,
                                        -connection_type,
                                        -sum_no_of_sites_uni_len,
                                        -CPE_Variant,
                                        -CPE_management_type,
                                        -CPE_supply_type,
                                        -topology,
                                        # -pool_size,
                                        # -additional_IP,

                                        -additional_ip_flag,
                                        -ip_address_arrangement,
                                        -ipv4_address_pool_size,
                                        -ipv6_address_pool_size,

                                        -a_site_id,
                                        -a_latitude_final,
                                        -a_longitude_final,
                                        -a_prospect_name,
                                        -a_bw_mbps,
                                        -a_burstable_bw,
                                        -a_resp_city,
                                        # -a_resp_state,
                                        -a_customer_segment,
                                        -a_sales_org,
                                        -a_product_name,
                                        -a_feasibility_response_created_date,
                                        -a_local_loop_interface,
                                        -a_last_mile_contract_term,
                                        -a_account_id_with_18_digit,
                                        -a_opportunity_term,
                                        -a_quotetype_quote,
                                        -a_connection_type,
                                        -a_sum_no_of_sites_uni_len,
                                        -a_cpe_variant,
                                        -a_cpe_management_type,
                                        -a_cpe_supply_type,
                                        -a_topology,
                                        # -a_pool_size,
                                        # -a_additional_ip,

                                        -a_additional_ip_flag,
                                        -a_ip_address_arrangement,
                                        -a_ipv4_address_pool_size,
                                        -a_ipv6_address_pool_size,

                                        -bts_num_BTS,
                                        -bts_IP_PMP
                                        )

          # Fixing level for training dataset
          t_data <- train_data_model
          # t_data$Request_no <- "train_row"
          # t_data$Latitude_final <- 0.0
          # t_data$Longitude_final <- 0.0
          # t_data$Feasibility.Response..Created.Date <- as.Date("2018-04-11")
          # t_data$bts_num_BTS <- "Train_ROW_NA"
          t_data$Identifier <- "Train"
          # t_data$bts_IP_PMP <- "bts_IP_PMP"
          # 
          # t_data$prospect_name <- "prospect_name"
          # t_data$resp_city <- "resp_city"
          # t_data$resp_state <- "resp_state"
          t_data$site_id <- "Site_VAL"
          # 
          # t_data$Status <- "Status"
          # t_data$final_key_level <- "final_key_level"
          # t_data$Provider.Name <- "Provider.Name"
          # t_data$L1.or.L2 <- "L1.or.L2"
          # t_data$Burstable_BW <- 2
          # 
          # t_data$last_mile_contract_term = 'UDP'
          # t_data$Account_id_with_18_Digit = 'UDP'
          # t_data$opportunityTerm = 12
          # t_data$quoteType_quote = 'UDP'
          # t_data$connection_type = 'UDP'
          # t_data$sum_no_of_sites_uni_len = 1
          # t_data$CPE_Variant = 'UDP'
          # t_data$CPE_management_type = 'UDP'
          # t_data$CPE_supply_type = 'UDP'
          # t_data$topology = 'UDP'
          # t_data$pool_size = 100
          # t_data$additional_IP = 5
          # t_data$a_site_id = 'UDP'
          # t_data$a_latitude_final = 0.0
          # t_data$a_longitude_final = 0.0
          # t_data$a_prospect_name = 'UDP'
          # t_data$a_bw_mbps = 200
          # t_data$a_burstable_bw = 200
          # t_data$a_resp_city = 'UDP'
          # t_data$a_resp_state = 'UDP'
          # t_data$a_customer_segment = 'UDP'
          # t_data$a_sales_org = 'UDP'
          # t_data$a_product_name = 'UDP'
          # t_data$a_feasibility_response_created_date = 'UDP'
          # t_data$a_local_loop_interface = 'UDP'
          # t_data$a_last_mile_contract_term = 'UDP'
          # t_data$a_account_id_with_18_digit = 'UDP'
          # t_data$a_opportunity_term = 12
          # t_data$a_quotetype_quote = 'UDP'
          # t_data$a_connection_type = 'UDP'
          # t_data$a_sum_no_of_sites_uni_len = 1
          # t_data$a_cpe_variant = 'UDP'
          # t_data$a_cpe_management_type = 'UDP'
          # t_data$a_cpe_supply_type = 'UDP'
          # t_data$a_topology = 'UDP'
          # t_data$a_pool_size = 100
          # t_data$a_additional_ip = 5

          t_data <- t_data[, which(names(t_data) %in% names(final_prospect_data))]

          final_prospect_data <- rbind(t_data, 
                                       final_prospect_data)

          final_prospect_data <- final_prospect_data[which(final_prospect_data$Identifier == "VAL"),]

          # Reading model
          final_prospect_data$Probabililty_Feasible = predict(rf_model,
                                                              newdata = final_prospect_data,
                                                              type = "prob")[,2]
		  
		  # Added: Rounding up prediction to 2nd decimal place
		  ceiling_dec <- function(x, level=2) round(x + 5*10^(-level-1), level)           
		  final_prospect_data$Probabililty_Feasible <- sapply(final_prospect_data$Probabililty_Feasible, ceiling_dec)
		  final_prospect_data$Probabililty_Feasible <- as.numeric(as.character(final_prospect_data$Probabililty_Feasible))

          # Predicting on cut off selected
          final_prospect_data$Predicted_Status <- ifelse(final_prospect_data$Probabililty_Feasible > onnet_RF_model_cutoff, "Feasible", "Not Feasible")

          return(final_prospect_data)  
        }

        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # Applying functions ####
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        prospect_data <- prospect_data_master

        # Creating original variables for consistency
        prospect_data <- dplyr::mutate(prospect_data,
                                a_site_id = site_id,
                                a_latitude_final = latitude_final,
                                a_longitude_final = longitude_final,
                                a_prospect_name = prospect_name,
                                a_bw_mbps = bw_mbps,
                                a_burstable_bw = burstable_bw,
                                a_resp_city = resp_city,
                                # a_resp_state = resp_state,
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
                                # a_pool_size = pool_size,
                                # a_additional_ip = additional_ip
                                a_additional_ip_flag = additional_ip_flag,
                                a_ip_address_arrangement = ip_address_arrangement,
                                a_ipv4_address_pool_size = ipv4_address_pool_size,
                                a_ipv6_address_pool_size = ipv6_address_pool_size
                                )

        #*** Renaming 
        prospect_data <- dplyr::rename(prospect_data,
                                site_id = site_id,
                                Latitude_final = latitude_final,
                                Longitude_final = longitude_final,
                                prospect_name = prospect_name,
                                BW_mbps = bw_mbps,
                                Burstable_BW = burstable_bw,
                                resp_city = resp_city,
                                # resp_state = resp_state,
                                Customer.Segment = customer_segment,
                                Sales.Org = sales_org,
                                Product.Name = product_name,
                                Feasibility.Response..Created.Date = feasibility_response_created_date,
                                Local.Loop.Interface = local_loop_interface,
                                Last.Mile.Contract.Term = last_mile_contract_term,
                                Account_id_with_18_Digit = account_id_with_18_digit,
                                opportunityTerm = opportunity_term,
                                quoteType_quote = quotetype_quote,
                                connection_type = connection_type,
                                sum_no_of_sites_uni_len = sum_no_of_sites_uni_len,
                                CPE_Variant = cpe_variant,
                                CPE_management_type = cpe_management_type,
                                CPE_supply_type = cpe_supply_type,
                                topology = topology,
                                # pool_size = pool_size,
                                # additional_IP = additional_ip
                                additional_ip_flag = additional_ip_flag,
                                ip_address_arrangement = ip_address_arrangement,
                                ipv4_address_pool_size = ipv4_address_pool_size,
                                ipv6_address_pool_size = ipv6_address_pool_size
                                )


        # Selecting BW (if Burstable BW is available, use it)
        # prospect_data$BW_mbps <- ifelse(is.na(prospect_data$Burstable_BW),
        #                                 prospect_data$BW_mbps, 
        #                                 prospect_data$Burstable_BW  )
		
		##############################################################
		#local loop interface fixed to 100-Base-TX till next model refresh
		
		prospect_data$Local.Loop.Interface <- '100-Base-TX'

        prospect_data$Burstable_BW <- as.numeric(prospect_data$Burstable_BW)

        prospect_data$BW_mbps <- ifelse((prospect_data$BW_mbps > prospect_data$Burstable_BW),
                                        prospect_data$BW_mbps, 
                                        prospect_data$Burstable_BW  )
        # prospect_data$Burstable_BW <- NULL

        # Converting BW and date
        prospect_data$BW_mbps <- as.numeric(prospect_data$BW_mbps)
        prospect_data$Feasibility.Response..Created.Date <- as.Date(prospect_data$Feasibility.Response..Created.Date,
                                                                    format = "%Y-%m-%d")

        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # Obtaing BTS columns
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # Fetching BTS data from database 
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        tryCatch(
        {
        # Sending query to mysql db
        bts_data_file = dbSendQuery(mydb_abstract_db, "select * from bts_data")

        # Fetching data from mysql server
        bts_data_file = fetch(bts_data_file, n=-1)

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
                                SITE_TYPE = site_type
                                )
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
        # Applying BTS Data clean up function 
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        tryCatch(
          {
          prospect_data$result <- apply(prospect_data, 1, function(x) bts_distance_calc(
            x["Latitude_final"],
            x["Longitude_final"],
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

        rm(bts_data_file)
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

        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # Obtaining Prospect columns
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        tryCatch( {
          prospect_data_func = dbSendQuery(mydb_abstract_db, "select * from Prospect_Rolled_Up_Onnet_RF")
          prospect_data_func = fetch(prospect_data_func, n=-1)

        prospect_data_func <- select(prospect_data_func,
                                     Feasibility_Response_Feasibility_Response_Auto_No,
                                     CustomerLongitude1,
                                     CustomerLatitude1,
                                     Feasibility_Response_Created_Date,
                                     BW_mbps,
                                     Status
                                     ) %>%
                              dplyr::rename(Feasibility.Response..Feasibility.Response.Auto.No. = Feasibility_Response_Feasibility_Response_Auto_No,
                                     Feasibility.Response..Created.Date = Feasibility_Response_Created_Date
                                     )

        prospect_data_func$BW_mbps <- as.numeric(prospect_data_func$BW_mbps)
        prospect_data_func$Feasibility.Response..Created.Date <- as.Date(prospect_data_func$Feasibility.Response..Created.Date,
                                                                         format = "%Y-%m-%d")
        prospect_data_func$Feasibility_flag <- ifelse(prospect_data_func$Status == "Feasible", 1 ,0)

        # Imputing with median to avoid error in min/ max (na.rm = T in max min returns a warning if all values are null)
        prospect_data_func$BW_mbps[is.na(prospect_data_func$BW_mbps)] <- median(prospect_data_func$BW_mbps, na.rm = T)

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


        tryCatch( {
        prospect_data$result <- apply(prospect_data, 1, function(x) prospect_distance_calc(
          x["Latitude_final"],
          x["Longitude_final"],
          x["Feasibility.Response..Created.Date"],
          prospect_data_func))

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

        rm(prospect_data_func)

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

        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # Obtaining Customer columns
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        tryCatch( {
          onnet_cust_data = dbSendQuery(mydb_abstract_db, "select * from Prospect_Customer_Rolled_Up_data_Onnet_RF")
          onnet_cust_data = fetch(onnet_cust_data, n=-1)

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


        tryCatch( {
        prospect_data$result <- apply(prospect_data, 1, function(x) customer_distance_calc(
          x["Latitude_final"],
          x["Longitude_final"],
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

        rm(onnet_cust_data)

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
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # Cleaning data for model scoring ####
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        tryCatch( {
        prospect_data <- final_cleaning_func(prospect_data)

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
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # Scoring data using Onnet RF Model  ####
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        tryCatch( {
        prospect_data_SCR <- model_scoring_func(prospect_data)

        prospect_data_SCR <- select(prospect_data_SCR,
                                    site_id,
                                    Probabililty_Feasible,
                                    Predicted_Status)

        prospect_data <- merge(x = prospect_data,
                               y = prospect_data_SCR,
                               by = "site_id")
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


        # rm(prospect_data_SCR)
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # Last Mile cost calculation  ####
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        tryCatch( {
          LM_pricebook = dbSendQuery(mydb_abstract_db, "select * from Onnet_RF_LM_Cleaned")
          LM_pricebook = fetch(LM_pricebook, n=-1)

        #*** Code needs to incorporate interim BWs
        LM_pricebook <- dplyr::rename(LM_pricebook,
                               BW_mbps = Cleaned_Bandwidth)

        LM_pricebook <- LM_pricebook[which(LM_pricebook$Interface == "FE"),]

        #*** Replacing others with UBRP2P
        prospect_data$solution_type <- as.character(prospect_data$solution_type)
        prospect_data$solution_type <- ifelse(prospect_data$solution_type == "Others", "UBRP2P", prospect_data$solution_type)

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

        prospect_data$interim_BW <- apply(prospect_data, 1, function(x) interim_BW_func(
          x["BW_mbps"]))


        prospect_data <- merge(x=prospect_data,
                               y=LM_pricebook,
                               by.x=c("interim_BW","solution_type"),
                               by.y=c("BW_mbps","Provider_Name"),
                               all.x = T)

        prospect_data <- dplyr::rename(prospect_data,
                                LM_OTC_INR = otc_inr,
                                LM_ARC_INR = arc_inr)

        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # Mast height calculations
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        prospect_data$Latitude_final <- as.numeric(prospect_data$Latitude_final)
        prospect_data$Longitude_final <- as.numeric(prospect_data$Longitude_final)
        # prospect_data$prospect_mast_ht <- as.numeric(prospect_data$prospect_mast_ht)

        prospect_coords_1 <- prospect_data
        prospect_coords_1$Prospect_ID <- paste(1:nrow(prospect_coords_1), "SITE", sep = "|")

        prospect_coords_1$prospect_date = prospect_coords_1$Feasibility.Response..Created.Date
        prospect_coords_1$prospect_date <- as.Date(prospect_coords_1$prospect_date,
                                                   format = "%Y-%m-%d")


        prospect_coords_2 = dbSendQuery(mydb_abstract_db, "select * from Onnet_RF_prospect_coords_2")
        prospect_coords_2 = fetch(prospect_coords_2, n=-1)


        prospect_coords_2$prospect_mast_ht <- as.numeric(prospect_coords_2$prospect_mast_ht)

        DistFun <- function(ID){
          ID <- ID
          TMP <- subset(prospect_coords_1,prospect_coords_1$Prospect_ID == ID)
          prospect_dup_coords_sub <- subset(prospect_coords_2, 
                                            (prospect_coords_2$prospect_date <= TMP$prospect_date) 
                                            & (prospect_coords_2$Prospect_ID_2 != TMP$Prospect_ID ))

          if(nrow(prospect_dup_coords_sub) ==0)
          {E = data.frame(Prospect_ID = ID, cust_count =0,min_mast_ht = 999999999
                          ,avg_mast_ht = 999999999,max_mast_ht=999999999,nearest_mast_ht=999999999)
          return(E)
          } else {

            TMP1 <- distHaversine(TMP[,c("Longitude_final",
                                         "Latitude_final")],prospect_dup_coords_sub[,c('prospect_lon',
                                                                                       'prospect_lat')])

               TMP1_c <- which(TMP1 <= 3000)

            if(length(TMP1_c) ==0)
            {E = data.frame(Prospect_ID = ID,cust_count =0,min_mast_ht = 999999999
                            ,avg_mast_ht = 999999999,max_mast_ht=999999999,nearest_mast_ht=999999999)
            return(E)
            } else {
              TMP1_c_min <- which(TMP1 <= 3000 & TMP1 == min(TMP1))
              TMP1_metrics <- prospect_dup_coords_sub[TMP1_c,]
              TMP1_metrics_min <- prospect_dup_coords_sub[TMP1_c_min,]
              cust_count <- nrow(TMP1_metrics)
              min_mast_ht <- min(TMP1_metrics$prospect_mast_ht,na.rm=T)
              max_mast_ht <- max(TMP1_metrics$prospect_mast_ht,na.rm=T)
              avg_mast_ht <- mean(TMP1_metrics$prospect_mast_ht,na.rm=T)
              nearest_mast_ht <- min(TMP1_metrics_min$prospect_mast_ht)
              TMP2 <- data.frame(Prospect_ID = ID,
                                 cust_count = as.numeric(cust_count),
                                 min_mast_ht = as.numeric(min_mast_ht),
                                 avg_mast_ht = as.numeric(avg_mast_ht),
                                 max_mast_ht=as.numeric(max_mast_ht),
                                 nearest_mast_ht=as.numeric(nearest_mast_ht))

              return(TMP2)
              gc()}}}

        DistanceMatrix <- c(lapply(as.list(prospect_coords_1$Prospect_ID), DistFun))

        onnet_rf_mast_ht <- do.call(rbind,DistanceMatrix)

        prospect_coords_1 <- merge(x = prospect_coords_1,
                                   y = onnet_rf_mast_ht,
                                   by = "Prospect_ID")

        # Added : Rounding mast height
		# round off mast heights to nearest higher multiple of 3
		roundUp <- function(x,m=3) m*ceiling(x / m)
		prospect_coords_1$nearest_mast_ht <- sapply(prospect_coords_1$nearest_mast_ht, roundUp)
		prospect_coords_1$nearest_mast_ht <- as.numeric(prospect_coords_1$nearest_mast_ht)

		prospect_coords_1$avg_mast_ht <- sapply(prospect_coords_1$avg_mast_ht, roundUp)
		prospect_coords_1$avg_mast_ht <- as.numeric(prospect_coords_1$avg_mast_ht)

		# Added : Text changed to 0
		prospect_coords_1$nearest_mast_ht_cost <- ifelse(prospect_coords_1$cust_count==0,0,
														 ifelse(prospect_coords_1$nearest_mast_ht<6,0,(prospect_coords_1$nearest_mast_ht)*4700))

		prospect_coords_1$avg_mast_ht_cost <- ifelse(prospect_coords_1$cust_count==0,0,
													 ifelse(prospect_coords_1$avg_mast_ht<6,0,(prospect_coords_1$avg_mast_ht)*4700))

        prospect_coords_1 <- select(prospect_coords_1,
                                    Prospect_ID,
                                    cust_count,
                                    min_mast_ht,
                                    avg_mast_ht,
                                    max_mast_ht,
                                    nearest_mast_ht,
                                    nearest_mast_ht_cost,
                                    avg_mast_ht_cost)

        prospect_coords_1 <- dplyr::rename(prospect_coords_1,
                                    Mast_3KM_cust_count = cust_count,
                                    Mast_3KM_min_mast_ht = min_mast_ht,
                                    Mast_3KM_avg_mast_ht = avg_mast_ht,
                                    Mast_3KM_max_mast_ht = max_mast_ht,
                                    Mast_3KM_nearest_mast_ht = nearest_mast_ht,
                                    Nearest_Mast_ht_cost = nearest_mast_ht_cost,
                                    Avg_3KM_Mast_ht_cost = avg_mast_ht_cost
        )


        # final_prospect_data <- merge(x = final_prospect_data,
        #                              y = prospect_coords_1,
        #                              by = "Request_no")

        #############################################################
        # Change below
        #############################################################
        #############################################################
        prospect_data <- cbind(prospect_data,
                               prospect_coords_1)

        prospect_data$LM_Cost <- sum(as.numeric(prospect_data$Avg_3KM_Mast_ht_cost),
                                     as.numeric(prospect_data$LM_OTC_INR),
                                     as.numeric(prospect_data$LM_ARC_INR),
                                     na.rm = T)

        rm(LM_pricebook,
           DistanceMatrix,
           prospect_coords_1,
           prospect_coords_2)

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
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # Network check
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        tryCatch( {
          Backhaul_data = dbSendQuery(mydb_abstract_db, "select * from Onnet_RF_Backhaul_Check_Rolled_Up")
          Backhaul_data = fetch(Backhaul_data, n=-1)

          sector_data = dbSendQuery(mydb_abstract_db, "select * from Onnet_RF_Sector_Check_Rolled_Up")
          sector_data = fetch(sector_data, n=-1)

        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # Sector and backhaul check   
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        Backhaul_network_check_func <- function(solution_type,
                                                siteID,
                                                Backhaul_data_n) {

          Backhaul_Network_check <- "Not Feasible/ Manual"
          Backhaul_Network_check_reason <- "Site ID is NA"

          # Backhaul check

          if (solution_type == "UBR_PMP") {
            if(!is.na(siteID)) {
              Backhaul_data_n <- Backhaul_data_n[which(Backhaul_data_n$`Site ID` == siteID),]

              if (nrow(Backhaul_data_n) > 0) {
                Backhaul_data_n <- Backhaul_data_n[which(Backhaul_data_n$Backhaul_Status == "Feasible"),]

                if (nrow(Backhaul_data_n) > 0) {
                  Backhaul_Network_check <- "Feasible"
                  Backhaul_Network_check_reason <- "Site ID is feasible"

                } else {
                  Backhaul_Network_check <- "Not Feasible/ Manual"
                  Backhaul_Network_check_reason <- "SiteID is not feasible"
                } 

              } else {
                Backhaul_Network_check <- "Not Feasible/ Manual"
                Backhaul_Network_check_reason <- "SiteID not found in backhaul network data"

              }
            } else {
              Backhaul_Network_check <- "Not Feasible/ Manual"
              Backhaul_Network_check_reason <- "Site ID is NA"
            }

          } else {
            Backhaul_Network_check <- "Not Feasible/ Manual"
            Backhaul_Network_check_reason <- "UBRP2P Solution"
          }

          return(list("Backhaul_Network_check" = Backhaul_Network_check,
                      "Backhaul_Network_check_reason" = Backhaul_Network_check_reason))
        }

        prospect_data$result <- apply(prospect_data, 1, function(x) Backhaul_network_check_func(
          x["solution_type"],
          x["bts_num_BTS"],
          Backhaul_data))

        prospect_data$Backhaul_Network_check = unlist(lapply(prospect_data$result, "[[", 1))
        prospect_data$Backhaul_Network_check_reason = unlist(lapply(prospect_data$result, "[[", 2))
        prospect_data$result <- NULL

        # Sector check
        sector_data <- select(sector_data,
                              ip_address,
                              Selected_solution_BW)

        prospect_data <- merge(x = prospect_data,
                               y = sector_data,
                               by.x = "bts_IP_PMP",
                               by.y = "ip_address",
                               all.x = T)

        prospect_data$Selected_solution_BW[is.na(prospect_data$Selected_solution_BW)] <- 0

        prospect_data$Sector_network_check <- ifelse(prospect_data$BW_mbps <= prospect_data$Selected_solution_BW,
                                                     "Feasible",
                                                     "Not Feasible")

        prospect_data$Network_Feasibility_Check <- ifelse(prospect_data$Selected_solution_BW != 0 |
                                                          prospect_data$Backhaul_Network_check == "Feasible",
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



        tryCatch( {

        # Creating LM columns
        prospect_data$lm_arc_bw_onwl <- 0
        prospect_data$lm_nrc_bw_onwl <- 0
        prospect_data$lm_nrc_mux_onwl <- 0
        prospect_data$lm_nrc_inbldg_onwl <- 0 
        prospect_data$lm_nrc_ospcapex_onwl <- 0
        prospect_data$lm_nrc_nerental_onwl <- 0
        prospect_data$lm_arc_bw_prov_ofrf <- 0
        prospect_data$lm_nrc_bw_prov_ofrf <- 0
        prospect_data$lm_nrc_mast_ofrf <- 0
        prospect_data$lm_arc_bw_onrf <- prospect_data$LM_ARC_INR
        prospect_data$lm_nrc_bw_onrf <- prospect_data$LM_OTC_INR
        prospect_data$lm_nrc_mast_onrf <- prospect_data$Avg_3KM_Mast_ht_cost

        # Creating orchestration columns
        prospect_data$Orch_LM_Type <- "Onnet"
        prospect_data$Orch_Connection <- "Wireless"
        prospect_data$Orch_Category <-ifelse(prospect_data$solution_type == "UBR_PMP",
                                             "UBR PMP ( 2mb and 4 mb - BTS column)",
                                             "UBR P2P - Onnet")
        prospect_data$Orch_BW <- prospect_data$BW_mbps

        # Dropping columns not required
        prospect_data <- select(prospect_data,
                                -BW_mbps,
                                -site_id,
                                -Latitude_final,
                                -Longitude_final,
                                -prospect_name,
                                -Burstable_BW,
                                -resp_city,
                                # -resp_state,
                                -Customer.Segment,
                                -Sales.Org,
                                -Product.Name,
                                -Feasibility.Response..Created.Date,
                                -Local.Loop.Interface,
                                -Last.Mile.Contract.Term,
                                -Account_id_with_18_Digit,
                                -opportunityTerm,
                                -quoteType_quote,
                                -connection_type,
                                -sum_no_of_sites_uni_len,
                                -CPE_Variant,
                                -CPE_management_type,
                                -CPE_supply_type,
                                -topology,
                                # -pool_size,
                                # -additional_IP,

                                -additional_ip_flag,
                                -ip_address_arrangement,
                                -ipv4_address_pool_size,
                                -ipv6_address_pool_size,

                                -Identifier,
                                -row_names,
                                -Prospect_ID)

        # Creating final variables
        prospect_data <- select(prospect_data,
                                a_site_id,
                                a_latitude_final,
                                a_longitude_final,
                                a_prospect_name,
                                a_bw_mbps,
                                a_burstable_bw,
                                a_resp_city,
                                # a_resp_state,
                                a_customer_segment,
                                a_sales_org,
                                a_product_name,
                                a_feasibility_response_created_date,
                                a_local_loop_interface,
                                a_last_mile_contract_term,
                                a_account_id_with_18_digit,
                                a_opportunity_term,
                                a_quotetype_quote,
                                a_connection_type,
                                a_sum_no_of_sites_uni_len,
                                a_cpe_variant,
                                a_cpe_management_type,
                                a_cpe_supply_type,
                                a_topology,
                                # a_pool_size,
                                # a_additional_ip,

                                a_additional_ip_flag,
                                a_ip_address_arrangement,
                                a_ipv4_address_pool_size,
                                a_ipv6_address_pool_size,

                                Probabililty_Feasible,
                                Predicted_Status,
                                Network_Feasibility_Check,
                                lm_arc_bw_onwl,
                                lm_nrc_bw_onwl,
                                lm_nrc_mux_onwl,
                                lm_nrc_inbldg_onwl,
                                lm_nrc_ospcapex_onwl,
                                lm_nrc_nerental_onwl,
                                lm_arc_bw_prov_ofrf,
                                lm_nrc_bw_prov_ofrf,
                                lm_nrc_mast_ofrf,
                                lm_arc_bw_onrf,
                                lm_nrc_bw_onrf,
                                lm_nrc_mast_onrf,
                                Nearest_Mast_ht_cost,
                                Orch_LM_Type,
                                Orch_Connection,
                                Orch_Category,
                                Orch_BW,
                                everything()
                                ) %>%
                          dplyr::rename(
                                site_id = a_site_id,
                                latitude_final = a_latitude_final,
                                longitude_final = a_longitude_final,
                                prospect_name = a_prospect_name,
                                bw_mbps = a_bw_mbps,
                                burstable_bw = a_burstable_bw,
                                resp_city = a_resp_city,
                                # resp_state = a_resp_state,
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
                                # pool_size = a_pool_size,
                                # additional_ip = a_additional_ip,

                                additional_ip_flag = a_additional_ip_flag,
                                ip_address_arrangement = a_ip_address_arrangement,
                                ipv4_address_pool_size = a_ipv4_address_pool_size,
                                ipv6_address_pool_size = a_ipv6_address_pool_size,


                                Predicted_Access_Feasibility = Predicted_Status,
                                Probabililty_Access_Feasibility = Probabililty_Feasible
                                 )

        # Handling NUll
        if (sum(is.na(prospect_data$bts_IP_PMP)) > 0) {
          prospect_data$bts_IP_PMP[is.na(prospect_data$bts_IP_PMP)] <- "Not_in_range"
        }

        if (sum(is.na(prospect_data$bts_num_BTS)) > 0) {
          prospect_data$bts_num_BTS[is.na(prospect_data$bts_num_BTS)] <- "Not_in_range"
        }

        # Handling level
        prospect_data$lm_nrc_mast_onrf[which(prospect_data$lm_nrc_mast_onrf == "No customers within 3 kms")] <- "0"



        # Converting all LM columns to numeric
        prospect_data$lm_arc_bw_onwl  = as.numeric(prospect_data$lm_arc_bw_onwl )
        prospect_data$lm_nrc_bw_onwl = as.numeric(prospect_data$lm_nrc_bw_onwl)
        prospect_data$lm_nrc_mux_onwl = as.numeric(prospect_data$lm_nrc_mux_onwl)
        prospect_data$lm_nrc_inbldg_onwl = as.numeric(prospect_data$lm_nrc_inbldg_onwl)
        prospect_data$lm_nrc_ospcapex_onwl = as.numeric(prospect_data$lm_nrc_ospcapex_onwl)
        prospect_data$lm_nrc_nerental_onwl = as.numeric(prospect_data$lm_nrc_nerental_onwl)
        prospect_data$lm_arc_bw_prov_ofrf = as.numeric(prospect_data$lm_arc_bw_prov_ofrf)
        prospect_data$lm_nrc_bw_prov_ofrf = as.numeric(prospect_data$lm_nrc_bw_prov_ofrf)
        prospect_data$lm_nrc_mast_ofrf = as.numeric(prospect_data$lm_nrc_mast_ofrf)
        prospect_data$lm_arc_bw_onrf = as.numeric(prospect_data$lm_arc_bw_onrf)
        prospect_data$lm_nrc_bw_onrf = as.numeric(prospect_data$lm_nrc_bw_onrf)
        prospect_data$lm_nrc_mast_onrf = as.numeric(prospect_data$lm_nrc_mast_onrf)
        prospect_data$Nearest_Mast_ht_cost = as.numeric(prospect_data$Nearest_Mast_ht_cost)

        # Imputing any null column with 0
        prospect_data$lm_arc_bw_onwl[is.na(prospect_data$lm_arc_bw_onwl)] <- 0
        prospect_data$lm_nrc_bw_onwl[is.na(prospect_data$lm_nrc_bw_onwl)] <- 0
        prospect_data$lm_nrc_mux_onwl[is.na(prospect_data$lm_nrc_mux_onwl)] <- 0
        prospect_data$lm_nrc_inbldg_onwl[is.na(prospect_data$lm_nrc_inbldg_onwl)] <- 0
        prospect_data$lm_nrc_ospcapex_onwl[is.na(prospect_data$lm_nrc_ospcapex_onwl)] <- 0
        prospect_data$lm_nrc_nerental_onwl[is.na(prospect_data$lm_nrc_nerental_onwl)] <- 0
        prospect_data$lm_arc_bw_prov_ofrf[is.na(prospect_data$lm_arc_bw_prov_ofrf)] <- 0
        prospect_data$lm_nrc_bw_prov_ofrf[is.na(prospect_data$lm_nrc_bw_prov_ofrf)] <- 0
        prospect_data$lm_nrc_mast_ofrf[is.na(prospect_data$lm_nrc_mast_ofrf)] <- 0
        prospect_data$lm_arc_bw_onrf[is.na(prospect_data$lm_arc_bw_onrf)] <- 0
        prospect_data$lm_nrc_bw_onrf[is.na(prospect_data$lm_nrc_bw_onrf)] <- 0
        prospect_data$lm_nrc_mast_onrf[is.na(prospect_data$lm_nrc_mast_onrf)] <- 0
        prospect_data$Nearest_Mast_ht_cost[is.na(prospect_data$Nearest_Mast_ht_cost)] <- 0

        # Converting all NA to text
        if (sum(is.na(prospect_data)) > 0) {
          prospect_data[is.na(prospect_data)] <- "NA"
        }

        # Add blank error attributes in case everything runs smoothly
        prospect_data$error_code <- "NA"
        prospect_data$error_flag <- 0
        prospect_data$error_msg <- "No error"


        # Terminating DB connections
        lapply(dbListConnections(MySQL()), dbDisconnect)

        time_end <- proc.time() - time_start
        time_end <- time_end["elapsed"]
        prospect_data$time_taken <- time_end
        print(time_end)

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

        # Returning final table if no error encountered
        return(prospect_data)

         # Ending main function


        x = run_onnet_rf()
        # View(x)
        # print(names(x))

        return(prospect_data)
    }
    '''
    r_model_call_single=robjects.r(rstr)
    r_output_df = r_model_call_single(input_data,path_py)
    py_output_df = pandas2ri.ri2py(r_output_df)
    output_dict = py_output_df.to_dict(orient='records')
    return jsonify(results=output_dict)


# In[ ]:


if __name__ =='__main__':
    app.run(port = 9000, debug = True)


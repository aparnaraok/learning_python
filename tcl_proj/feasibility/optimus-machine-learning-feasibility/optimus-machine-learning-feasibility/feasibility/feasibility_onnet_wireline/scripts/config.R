##########################################################################################
### DEFINE VARS
##########################################################################################

CUTOFF_GE = 100
CUTOFF_FE = 50
adj_fac = 1.25
CONNECT_BUILD_DIST = 50
SHRT_LST_CONN_BUILD = 50

#Manual Feasibility BW cutoff
MANUAL_FEASIBILITY_BW = 1000

##Network

TIER1_CITY_LIST <- c('MUMBAI','PUNE', 'CHENNAI','DELHI', 'KOLKATA', 'HYDERABAD', 'BANGALORE', 'AHMEDABAD')

TIER1_LABEL = "Tier1"
NON_TIER1_LABEL =  "Non_Tier1"

TIER1_PRE_FEASIBLE_BW = 45
NON_TIER1_PRE_FEASIBLE_BW = 2

#####

username ='optimus_user'
pwd ='Tata123'
database ='optimus_abstract_uat2'
hostname = 'INP44XDDB2552'          #'INP44XPDB2790'

PROSPECT_TBL = "Prospect_Rolled_Up_Onnet_Wireline_Refreshed_SP"
CUST_TBL = "Prospect_Customer_Rolled_Up_data_Onnet_Wireline_Refreshed"
CUST_TBL_LIVE = "Prospect_Customer_Rolled_Up_data_Onnet_Wireline_Refreshed_live"

MODEL_DIR = "model/"

CUST_NAME_MATCH_CUTOFF = 0.7
GEO_CODE_SIG_DIG = 4
IN_BUILD_CAPEX = 40000
MODEL_OBJ = paste0(MODEL_DIR, "Onnet_WL_Model_mtry_10_nodesize_100_ntree_250.rds")



logfile = "Onwl_scoring.log"
log_flag = FALSE

## Prospect Id included to merge other columsn from original inout for analysis- Prospect id will not be used for training
# "Prospect_ID",
FEATURE_SET = c("Product.Name","BW_mbps","POP_DIST_KM",
                "POP_DIST_KM_SERVICE","POP_Network_Location_Type","POP_Construction_Status",
                "POP_Building_Type","POP_Category","POP_TCL_Access","FATG_DIST_KM",
                "FATG_Network_Location_Type","FATG_Ring_type", "FATG_Building_Type","FATG_Category",
                "FATG_TCL_Access","FATG_PROW","HH_DIST_KM",
                "X0.5km_cust_count","X0.5km_min_dist","X0.5km_avg_dist","X0.5km_min_bw",
                "X0.5km_max_bw","X0.5km_avg_bw","X2km_cust_count","X2km_min_dist",
                "X2km_avg_dist","X2km_min_bw","X2km_max_bw","X2km_avg_bw",
                "X5km_cust_count","X5km_min_dist","X5km_avg_dist","X5km_min_bw",
                "X5km_max_bw","X5km_avg_bw","X0.5km_prospect_count","X0.5km_prospect_min_dist",
                "X0.5km_prospect_avg_dist","X0.5km_prospect_min_bw","X0.5km_prospect_avg_bw",
                "X0.5km_prospect_max_bw","X0.5km_prospect_num_feasible","X0.5km_prospect_perc_feasible",
                "X2km_prospect_count","X2km_prospect_min_dist","X2km_prospect_avg_dist",
                "X2km_prospect_min_bw","X2km_prospect_avg_bw","X2km_prospect_max_bw",
                "X2km_prospect_num_feasible","X2km_prospect_perc_feasible","X5km_prospect_count",
                "X5km_prospect_min_dist","X5km_prospect_avg_dist","X5km_prospect_min_bw",
                "X5km_prospect_avg_bw","X5km_prospect_max_bw","X5km_prospect_num_feasible",
                "X5km_prospect_perc_feasible","OnnetCity_tag")


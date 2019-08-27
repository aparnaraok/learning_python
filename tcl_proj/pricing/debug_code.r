library(jsonlite)
library(dplyr)

path_py <- "D:\\fp_project\\pricing\\"
setwd(path_py) 

JSON_filename <- "input_json_for_pricing_pool_size.json"
bm_data <- dplyr::bind_rows(fromJSON(JSON_filename))


mydb_abstract_db = dbConnect(MySQL(),
                             user='optimus_user', 
                             password='Tata123', 
                             dbname='optimus_abstract_uat2', 
                             host='INP44XDDB2552')

historical_bm_data = dbSendQuery(mydb_abstract_db,
                                 "select * from Historic_Customer_Type_Upd_GVPN")
historical_bm_data = fetch(historical_bm_data, n=-1)

lapply(dbListConnections(MySQL()), dbDisconnect)

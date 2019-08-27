library(jsonlite)
library(dplyr)

path_py <- "D://fp_project//feasibility//optimus-machine-learning-feasibility//optimus-machine-learning-feasibility//feasibility//feasibility_onnet_wireline"
setwd(path_py) 

JSON_filename <- "input_json_10.json"
bm_data <- dplyr::bind_rows(fromJSON(JSON_filename))


mydb_abstract_db = dbConnect(MySQL(),
                             user='optimus_user', 
                             password='Tata123', 
                             dbname='optimus_abstract_uat2', 
                             host='INP44XDDB2552')

print(mydb_abstract_db)

fatg_data_file <<- load_fatg_data(mydb_abstract_db)
print(fatg_data_file)
create_log(logfile, "Fatg Data Loaded", log_flag)
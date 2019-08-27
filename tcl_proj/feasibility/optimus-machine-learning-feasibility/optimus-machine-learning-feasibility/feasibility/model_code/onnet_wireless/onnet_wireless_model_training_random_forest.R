options(digits = 10)
options(sqldf.driver = "SQLite")
# Suppress warnings
options( warn = -1 )

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Setting input parameters ####
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
path_py <- "C:/Users/MRajakum/Documents/SP/9.Optimus/feasibility/onnet_wireless"
setwd(path_py)
source("onnet_wireless_aux_functions.R")
# set error parameter
err <- FALSE

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
    library(ROCR)
    library(caret)
    
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

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Setting input parameters ####
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
path_py <- "C:/Users/MRajakum/Documents/SP/9.Optimus/feasibility/onnet_wireless"
setwd(path_py)

source("onnet_wireless_model_training_random_forest_aux_function.R")
set.seed(12345)
input_data <- readRDS("4_Prospect_Customer_Features_Prepared.RDS")
dependent_variable <- "Status"

features_to_model <- c('BW_mbps',
                       'prospect_0_5km_Min_DistanceKilometers',
                       'prospect_0_5km_Avg_BW_Mbps',
                       'prospect_0_5km_Min_BW_Mbps',
                       'prospect_0_5km_Max_BW_Mbps',
                       'prospect_0_5km_feasibility_pct',
                       'prospect_0_5km_Sum_Feasibility_flag',
                       'prospect_2km_Avg_DistanceKilometers',
                       'prospect_2km_Avg_BW_Mbps',
                       'prospect_2km_Min_BW_Mbps',
                       'prospect_2km_Max_BW_Mbps',
                       'prospect_2km_Sum_Feasibility_flag',
                       'prospect_2km_feasibility_pct',
                       'bts_min_dist_km',
                       'PMP_bts_3km_radius',
                       'P2P_bts_3km_radius',
                       'onnet_0_5km_cust_Count',
                       'onnet_0_5km_Min_DistanceKilometers',
                       'onnet_0_5km_Avg_BW_Mbps',
                       'onnet_2km_cust_Count',
                       'onnet_2km_Avg_DistanceKilometers',
                       'onnet_2km_Avg_BW_Mbps',
                       'onnet_2km_Min_BW_Mbps',
                       'onnet_2km_Max_BW_Mbps',
                       'onnet_5km_cust_Count',
                       'onnet_5km_Avg_DistanceKilometers',
                       'onnet_5km_Avg_BW_Mbps',
                       'onnet_5km_Min_BW_Mbps',
                       'onnet_5km_Max_BW_Mbps',
                       'bts_flag',
                       'Status',
                       'Product_Name',
                       'Local_Loop_Interface',
                       'final_key_level',
                       'Provider_Name',
                       'L1_or_L2',
                       'solution_type',
                       'bts_Closest_infra_provider',
                       'bts_Closest_Site_type',
                       'Identifier',
                       'bts_within_3km_flag')
# Categorical Variables
fact_col_names <- c("Status",
                    "Product_Name",
                    "Local_Loop_Interface",
                    "Identifier",
                    "final_key_level",
                    "Provider_Name",
                    "L1_or_L2",
                    "solution_type",
                    "bts_Closest_infra_provider",
                    "bts_Closest_Site_type")
############################################
#Partition data into train, test & validation
############################################
validation_data_duration <- 30#$days
input_data[,dependent_variable] <- ifelse(input_data[,dependent_variable] == "Feasible",1,0)
input_data$Feasibility.Response..Created.Date <- as.Date(input_data$Feasibility.Response..Created.Date)

val_indices <- which(input_data$Feasibility.Response..Created.Date > 
                       (max(input_data$Feasibility.Response..Created.Date) - validation_data_duration))
validation_data <- input_data[val_indices,]
validation_data$Identifier <- "Validation"

train_test_data <- input_data[-val_indices,]
train_indices = sample.split(train_test_data[, dependent_variable], SplitRatio = .80)

train_data <-train_test_data[which(train_indices==TRUE),]
train_data$Identifier <- "Train"

test_data <-train_test_data[which(train_indices==FALSE),]
test_data$Identifier <- "Test"

input_data <- rbind(train_data, test_data, validation_data)
rm(train_test_data, train_data, test_data, validation_data, val_indices, train_indices)
gc()
############################################
# Modelling data prep
############################################
# Select feature to model 
model_input_data <- input_data[, which(colnames(input_data) %in% features_to_model)]
residual_input_data <- input_data[, -which(colnames(input_data) %in% features_to_model)]
residual_input_data$final_key_level <- model_input_data$final_key_level

######## Converting to factor and vars
fact_vars <- data.frame(apply(model_input_data[,fact_col_names], 2, as.factor))
num_vars <-  data.frame(apply(model_input_data[, -which(names(model_input_data) %in% fact_col_names)], 2, as.numeric))

model_input_data <- cbind(num_vars, fact_vars)
rm(num_vars, fact_vars)

######## Final test and train data
test_data <- model_input_data[which(model_input_data$Identifier == "Test"),]
val_data <- model_input_data[which(model_input_data$Identifier == "Validation"),]
train_data <- model_input_data[which(model_input_data$Identifier == "Train"),]
train_data$Identifier <- NULL

###### Intialize RF variables
mtry_vec <- 7
nodesize_vec <- c(100)
nodesize_val <- nodesize_vec

#for(ntree in c(200,250,300,350,400,450,500)){
ntree= 500
print(paste0("******** ",ntree))
rf_model = tuneRF(train_data[, -which(names(train_data) %in% c("final_key_level",
                                                               "Provider_Name",
                                                               "L1_or_L2",
                                                               "Status"))],
                  train_data$Status,
                  mtryStart = 7,
                  ntreeTry=ntree,
                  stepFactor=2,
                  # improve=0.05,
                  trace=TRUE,
                  plot=TRUE,
                  doBest  =TRUE)

save(rf_model,file=paste0("Onnet_RF_mtry_",rf_model$mtry,"_ntree_",rf_model$ntree,".RData"))
#}
rf_model <- randomForest(Status ~.,
                         data = train_data[, -which(names(train_data) %in% c("final_key_level",
                                                                             "Provider_Name",
                                                                             "L1_or_L2"))],
                         do.trace = TRUE,
                         ntree = 500,
                         mtry = 7,
                         nodesize = nodesize_val)
# 
# save(rf_model,file="Onnet_RF_mtry_5_ntree_500.RData")

col_exclude <- c("final_key_level",
                 "Provider_Name",
                 "L1_or_L2",
                 "Identifier")
#Predict class
train_data$pred <- predict(rf_model,
                           newdata = train_data[,-which(names(train_data)%in%col_exclude)], 
                           type = "prob")[,2]
oob_pred <- predict(rf_model, type = "prob")[,2]

train_data$Identifier <- "Train"

test_data$pred <- predict(rf_model, 
                          newdata = test_data[,-which(names(test_data)%in%col_exclude)],
                          type = "prob")[,2]

val_data$pred <- predict(rf_model, 
                         newdata = val_data[,-which(names(val_data)%in%col_exclude)],
                         type = "prob")[,2]
actual <- train_data[,c(dependent_variable)]
predicted <- train_data["pred"]
# Calculating AUC
perf_calc = ROCR::prediction(predicted, actual)
auc_calc = ROCR::performance(perf_calc, "auc")

# Calculating performance metrics
pred_tpr_fpr <- performance(perf_calc, "tpr","fpr")
pred_acc <- performance(perf_calc, "acc")
pred_sens <- performance(perf_calc,"sens")
pred_spec <- performance(perf_calc,"spec")

# Creating table to select cutoff
tpr_vec <- unlist(as.vector(pred_tpr_fpr@y.values))
cutoff_vec <- unlist(as.vector(pred_tpr_fpr@alpha.values))
acc_vec <- unlist(pred_acc@y.values[[1]])
sens_vec <- unlist(pred_sens@y.values[[1]])
spec_vec <- unlist(pred_spec@y.values[[1]])

combi <- as.data.frame(cbind(cutoff_vec,tpr_vec,acc_vec,sens_vec,spec_vec))
combi$fpr <- 1- combi$spec_vec
combi$youden <- combi$sens_vec+combi$spec_vec-1
combi <- combi[order(combi$youden,decreasing = T),]

#Operating point
operating_point <- combi[1,c("cutoff_vec")]
print(combi[1,])
print(operating_point)

############ Plot ROC #########################
plot(1-combi$spec_vec, combi$tpr_vec, main = "Onnet RF ROC Curve",xlab="False Positive Rate", ylab="True Positive Rate",col.main="grey50",col.lab="grey60",col="slateblue4")
grid (NULL,NULL, lty = 6, col = "cornsilk2")
points(combi[combi$cutoff_vec==operating_point,"fpr"],combi[combi$cutoff_vec==operating_point,"tpr_vec"], col="red",pch=22)

################################# Assigning Class #############################
train_data$predicted_class <- ifelse(train_data$pred > operating_point, 1, 0)
confusion_mat_train <- table(train_data$Status, train_data$pred > operating_point)
print(confusion_mat_train)
# FALSE  TRUE
# 0 59273  1176
# 1  5439 86460
train_data$accuracy <- (confusion_mat_train[1,1]+confusion_mat_train[2,2])/nrow(train_data)
train_data$tpr <- confusion_mat_train[2,2]/rowSums(confusion_mat_train)["1"]
train_data$fpr <- confusion_mat_train[2,1]/rowSums(confusion_mat_train)["1"]
train_data$tnr <- confusion_mat_train[1,1]/rowSums(confusion_mat_train)["0"]
train_data$fnr <- confusion_mat_train[1,2]/rowSums(confusion_mat_train)["0"]

test_data$predicted_class <- ifelse(test_data$pred > operating_point, 1, 0)
confusion_mat_test <- table(test_data$Status, test_data$pred > operating_point)
print(confusion_mat_test)
# FALSE  TRUE
# 0 11885  3227
# 1  3079 19896
test_data$accuracy <- (confusion_mat_test[1,1]+confusion_mat_test[2,2])/nrow(test_data)
test_data$tpr <- confusion_mat_test[2,2]/rowSums(confusion_mat_test)["1"]
test_data$fpr <- confusion_mat_test[2,1]/rowSums(confusion_mat_test)["1"]
test_data$tnr <- confusion_mat_test[1,1]/rowSums(confusion_mat_test)["0"]
test_data$fnr <- confusion_mat_test[1,2]/rowSums(confusion_mat_test)["0"]

val_data$predicted_class <- ifelse(val_data$pred > operating_point, 1, 0)
confusion_mat_val <- table(val_data$Status, val_data$pred > operating_point)
print(confusion_mat_val)
# FALSE TRUE
# 0  2691  721
# 1   551 2832
val_data$accuracy <- (confusion_mat_val[1,1]+confusion_mat_val[2,2])/nrow(val_data)
val_data$tpr <- confusion_mat_val[2,2]/rowSums(confusion_mat_val)["1"]
val_data$fpr <- confusion_mat_val[2,1]/rowSums(confusion_mat_val)["1"]
val_data$tnr <- confusion_mat_val[1,1]/rowSums(confusion_mat_val)["0"]
val_data$fnr <- confusion_mat_val[1,2]/rowSums(confusion_mat_val)["0"]


train_data$Identifier <- NULL
test_data$Identifier <- NULL
val_data$Identifier <- NULL

train_data$Identifier <- "Train"
test_data$Identifier <- "Test"
val_data$Identifier <- "Val"

combined_data <- rbind(train_data, test_data, val_data)

write.csv(train_data, paste0("Onnet_RF_Train_data_operating_point_",operating_point,".csv"), row.names = F)
write.csv(test_data, paste0("Onnet_RF_Test_data_operating_point_",operating_point,".csv"), row.names = F)
write.csv(val_data, paste0("Onnet_RF_Val_data_operating_point_",operating_point,".csv"), row.names = F)
write.csv(combined_data, paste0("Onnet_RF_ALL_data_operating_point_",operating_point,".csv"), row.names = F)

combined_data_tmp <- merge(combined_data,
                       residual_input_data,
                       by = 'final_key_level')
saveRDS(combined_data_tmp,paste0("5_Scored_data_model_b_operating_point_",operating_point,".RDS"))



# # Creating metric for Train
# train_result <- metric_calculation(train_data[,c(dependent_variable)], train_data["pred"])
# write.csv(train_result$Eval_Metrics, "Train_Cutoff_Metrics.csv", row.names = F)
# 
# # Creating metric for OOB
# OOB_result <- metric_calculation(train_data[,c(dependent_variable)], oob_pred)
# write.csv(OOB_result$Eval_Metrics, "OOB_Cutoff_Metrics.csv", row.names = F)
# 
# # Creating metric for Test
# test_result <- metric_calculation(test_data[,c(dependent_variable)], test_data["pred"])
# write.csv(test_result$Eval_Metrics, "Test_Cutoff_Metrics.csv", row.names = F)
# 
# # Creating metric for Validation
# val_result <- metric_calculation(val_data[,c(dependent_variable)], val_data["pred"])
# write.csv(val_result$Eval_Metrics, "Validation_Cutoff_Metrics.csv", row.names = F)
# 
# write.csv(train_data, "Train_Pred.csv", row.names = F)
# write.csv(data.frame(train_data[dependent_variable], oob_pred),   "OOB_Pred.csv", row.names = F)
# write.csv(test_data, "Test_Pred.csv", row.names = F)
# write.csv(val_data,   "Val_Pred_.csv", row.names = F)
# 
# 
# print(rf_model)
# 
# cat("\t","Train AUC:", "\t",train_result$AUC[[1]], "\n",
#     "\t","OOB AUC:", "\t",OOB_result$AUC[[1]], "\n",
#     "\t","Test AUC:", "\t",test_result$AUC[[1]], "\n",
#     "\t","Val AUC:","\t", val_result$AUC[[1]], "\n")
# 
# cat("Cut off based on Train (Max Youden):", "\n\n")
#     print(head(train_result$Eval_Metrics, 1))
#     
#     cat("Cut off based on OOB (Max Youden):", "\n\n")
#     print(head(OOB_result$Eval_Metrics, 1))
#     
#     cat("Cut off based on Test (Max Youden):", "\n\n")
#     print(head(test_result$Eval_Metrics, 1))
#     
#     cat("Cut off based on Val (Max Youden):", "\n\n")
#     print(head(val_result$Eval_Metrics, 1))
#     
#     cat("Variable Importance:", "\n\n")
#     print(rf_model$importance)
    

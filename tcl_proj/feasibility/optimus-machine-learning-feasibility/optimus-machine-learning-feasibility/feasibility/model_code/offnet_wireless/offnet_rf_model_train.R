options(digits = 10)
options(sqldf.driver = "SQLite")
# Suppress warnings
options( warn = -1 )

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Setting input parameters ####
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
path_py <- "C:/Users/MRajakum/Documents/SP/9.Optimus/feasibility/offnet_wireless"
setwd(path_py)
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
path_py <- "C:/Users/MRajakum/Documents/SP/9.Optimus/feasibility/offnet_wireless"
setwd(path_py)

set.seed(12345)
input_data <- readRDS("4_Offnet_RF_Data_to_Model.RDS")
dependent_variable <- "Status"

features_to_model <- c('BW_mbps',
                       'offnet_0_5km_cust_Count',
                       'offnet_0_5km_Min_DistanceKilometers',
                       'offnet_0_5km_Avg_BW_Mbps',
                       'offnet_0_5km_Min_BW_Mbps',
                       'offnet_0_5km_Max_BW_Mbps',
                       'offnet_2km_cust_Count',
                       'offnet_0_5km_Min_accuracy_num',
                       'offnet_2km_Min_DistanceKilometers',
                       'offnet_2km_Avg_BW_Mbps',
                       'offnet_2km_Min_BW_Mbps',
                       'offnet_2km_Min_accuracy_num',
                       'offnet_5km_Min_DistanceKilometers',
                       'offnet_5km_Avg_BW_Mbps',
                       'offnet_5km_Min_BW_Mbps',
                       'offnet_5km_Max_BW_Mbps',
                       'offnet_5km_Min_accuracy_num',
                       'prospect_0_5km_Min_DistanceKilometers',
                       'prospect_0_5km_Avg_BW_Mbps',
                       'prospect_0_5km_Min_BW_Mbps',
                       'prospect_0_5km_Max_BW_Mbps',
                       'prospect_0_5km_feasibility_pct',
                       'prospect_0_5km_Sum_Feasibility_flag',
                       'prospect_2km_cust_Count',
                       'prospect_2km_Avg_DistanceKilometers',
                       'prospect_2km_Avg_BW_Mbps',
                       'prospect_2km_Min_BW_Mbps',
                       'prospect_2km_Max_BW_Mbps',
                       'prospect_2km_Sum_Feasibility_flag',
                       'prospect_2km_feasibility_pct',
                       'provider_tot_towers',
                       'provider_min_dist',
                       'Product_Name',
                       'Local_Loop_Interface',
                       'Last_Mile_Contract_Term',
                       'Status',
                       'Identifier',
                       'final_key_level')

# Factor vars
fact_col_names <- c("Status",
                    "final_key_level",
                    "Product_Name",
                    "Local_Loop_Interface",
                    "Last_Mile_Contract_Term",
                    "Identifier")

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
model_input_data$row_idx <- c(1:nrow(input_data))
residual_input_data$row_idx <- c(1:nrow(input_data))

######## Converting to factor and vars
model_input_data$bw_flag_3 <- ifelse(model_input_data$BW_mbps >= 3, 1, 0)
model_input_data$bw_flag_32 <- ifelse(model_input_data$BW_mbps >= 32, 1, 0)
fact_vars <- data.frame(apply(model_input_data[,fact_col_names], 2, as.factor))
num_vars <-  data.frame(apply(model_input_data[, -which(names(model_input_data) %in% fact_col_names)], 2, as.numeric))

model_input_data <- cbind(num_vars, fact_vars)
model_input_data <- do.call(data.frame,lapply(model_input_data, function(x) replace(x, is.infinite(x),NA)))
model_input_data <- model_input_data[-which(is.na(model_input_data$offnet_0_5km_Min_accuracy_num)),]
model_input_data <- model_input_data[-which(is.na(model_input_data$offnet_2km_Min_accuracy_num)),]
model_input_data <- model_input_data[-which(is.na(model_input_data$offnet_5km_Min_accuracy_num)),]
rm(num_vars, fact_vars)

######## Final test and train data
test_data <- model_input_data[which(model_input_data$Identifier == "Test"),]
val_data <- model_input_data[which(model_input_data$Identifier == "Validation"),]
train_data <- model_input_data[which(model_input_data$Identifier == "Train"),]
train_data$Identifier <- NULL

col_exclude <- c("final_key_level",
                 "Status",
                 "Local_Loop_Interface",
                 "Last_Mile_Contract_Term",
                 "row_idx")

####### Intialize RF variables
mtry_vec <- 7
nodesize_vec <- c(100)
nodesize_val <- nodesize_vec
tmp <- train_data[, -which(names(train_data) %in% c('final_key_level',"row_idx","Status","Local_Loop_Interface","Last_Mile_Contract_Term"))]
rf_model_opt = tuneRF(tmp,
                  train_data$Status,
                  mtryStart = 7,
                  ntreeTry=300,
                  stepFactor=2,
                  improve=0.05,
                  trace=TRUE,
                  plot=TRUE,
                  doBest  =TRUE)
rf_model <- rf_model_opt
# rf_model <- randomForest(Status ~.,
#                          data = select(train_data, 
#                                        -c('final_key_level',
#                                        'row_idx')),
#                          do.trace = TRUE,
#                          ntree = 300,
#                          mtry = 7,
#                          nodesize = 100)
save(rf_model,file=paste0("20190113_Offnet_RF_mtry_",rf_model$mtry,"_ntree_",rf_model$ntree,".RData"))

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
plot(1-combi$spec_vec, combi$tpr_vec, main = "Offnet RF ROC Curve",xlab="False Positive Rate", ylab="True Positive Rate",col.main="grey50",col.lab="grey60",col="slateblue4")
grid (NULL,NULL, lty = 6, col = "cornsilk2")
points(combi[combi$cutoff_vec==operating_point,"fpr"],combi[combi$cutoff_vec==operating_point,"tpr_vec"], col="red",pch=22)
################################# Assigning Class #############################
train_data$predicted_class <- ifelse(train_data$pred > operating_point, 1, 0)
confusion_mat_train <- table(train_data$Status, train_data$pred > operating_point)
print(confusion_mat_train)
  # FALSE  TRUE
# 0 64936   631
# 1  3077 67238
train_data$accuracy <- (confusion_mat_train[1,1]+confusion_mat_train[2,2])/nrow(train_data)
train_data$tpr <- confusion_mat_train[2,2]/rowSums(confusion_mat_train)["1"]
train_data$fpr <- confusion_mat_train[2,1]/rowSums(confusion_mat_train)["1"]
train_data$tnr <- confusion_mat_train[1,1]/rowSums(confusion_mat_train)["0"]
train_data$fnr <- confusion_mat_train[1,2]/rowSums(confusion_mat_train)["0"]




test_data$predicted_class <- ifelse(test_data$pred > operating_point, 1, 0)
confusion_mat_test <- table(test_data$Status, test_data$pred > operating_point)
print(confusion_mat_test)
# FALSE  TRUE
# 0 13513  2837
# 1  1982 15679
test_data$accuracy <- (confusion_mat_test[1,1]+confusion_mat_test[2,2])/nrow(test_data)
test_data$tpr <- confusion_mat_test[2,2]/rowSums(confusion_mat_test)["1"]
test_data$fpr <- confusion_mat_test[2,1]/rowSums(confusion_mat_test)["1"]
test_data$tnr <- confusion_mat_test[1,1]/rowSums(confusion_mat_test)["0"]
test_data$fnr <- confusion_mat_test[1,2]/rowSums(confusion_mat_test)["0"]

val_data$predicted_class <- ifelse(val_data$pred > operating_point, 1, 0)
confusion_mat_val <- table(val_data$Status, val_data$pred > operating_point)
print(confusion_mat_val)
# FALSE TRUE
# 0  1678  384
# 1   524 2116
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

write.csv(train_data, paste0("Offnet_RF_Train_data_operating_point_",operating_point,".csv"), row.names = F)
write.csv(test_data, paste0("Offnet_RF_Test_data_operating_point_",operating_point,".csv"), row.names = F)
write.csv(val_data, paste0("Offnet_RF_Val_data_operating_point_",operating_point,".csv"), row.names = F)
write.csv(combined_data_tmp, paste0("Offnet_RF_ALL_data_selected_operating_point_",operating_point,".csv"), row.names = F)

combined_data_tmp <- merge(combined_data,
                           residual_input_data,
                           by = 'row_idx')
write.csv(combined_data_tmp, paste0("Offnet_RF_ALL_data_selected_operating_point_",operating_point,".csv"), row.names = F)
saveRDS(combined_data_tmp,paste0("5_Scored_data_selected_operating_point_",operating_point,".RDS"))

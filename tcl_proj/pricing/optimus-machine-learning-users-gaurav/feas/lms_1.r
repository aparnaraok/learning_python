calc_match <- function(prospect_name, cust_name)
{
  RecordLinkage = 0
  print(prospect_name)
  print(cust_name)
  #Connected Building: condition cust_name != NA added
  if(!is.na(prospect_name) & prospect_name != "" & !is.na(cust_name))
  {
    RecordLinkage <- RecordLinkage::levenshteinSim(tolower(prospect_name), tolower(cust_name))
    
  }
  
  return (RecordLinkage)
}

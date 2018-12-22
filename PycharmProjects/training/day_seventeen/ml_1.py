#chi square test..99.5% accuracy
#Correlation

#Using Pearson Correlation coefficient

from scipy.stats import pearsonr
print(pearsonr([1,2,3], [1,2,3.1]))
print(pearsonr([1,2,3], [3,2,1]))

#Detects only linear relationship.
#(0.9996222851612184, 0.017498096813278487)
#(-1.0, 0.0)



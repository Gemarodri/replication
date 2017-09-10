# Running a Chi-Square Test
# Both response variable (Awareness) and explanatory variable () are quantitative variables.In order to perform a Chi-square test, I had to categorize both these variables.

# There exists 4 categories for replication (FullReplication,NoReplication,Enviroment,Package)


# I created a binary categorical variable for Awareness, dividing papers between “FullAwareness” and “not Awarennes”

# Chi square revealed that reproducibility was significantly associated with whether a paper was a aware of limitations. The Chi-square value was 8.63 and the p-value was 0.034, indicating that we should accept the null hypothesis in this instance.

#Imports
import pandas as pd
import numpy as np
import scipy.stats as stats
import seaborn as sns

import matplotlib.pyplot as plt
%matplotlib inline

#Data
Manual_Analysis=[0,1,1,0,1,1,0,1,1,
                 1,0,0,0,0,1,0,0,1,1,
                 1,0,1,1,0,1,0,1,1,0,
                 0,1,0,0,0,0,0,0,0,
                 0,1,0,0,0,0,0,0,1,
                 0,1,0,0,0,1,0,1,0,1,
                 1,1,1,0,1,1,1,0,0,0,
                 0,1,0,1,1,1,1,0,0,1,
                 0,0,0,0,0,0,1,0,0,0,
                 1,0,0,1,0,0,0,1,1,1,
                 0,1,1,1,0,1,0,0,0,1,
                 0,0,1,1,0,0,1,0,1,
                 1,0,0,0,1,0,0,1,1,
                 0,1,0,1,1,1,0,0,1,0,
                 1,0,0,1,0,0,0,0,1,1,
                 1,1,0,1,0,0,1,1,0,0,
                 0,0,1,1,1,1,1,1,0,1,
                 0,1,0,1,1,0,1,0,1,1,
                 1,0,1,0,1,0,0,0,0,1,
                 0,1]
TTV_first=      [1,1,0,1,1,0,0,1,0,
                 0,1,0,0,0,1,1,0,0,0,
                 1,1,0,1,1,0,1,1,0,1,
                 1,0,1,1,0,1,1,1,0,
                 1,0,1,0,0,0,1,0,0,
                 1,1,0,1,0,0,0,1,1,1,
                 0,1,1,0,0,1,0,0,0,0,
                 0,0,1,1,0,1,0,0,0,1,
                 1,1,0,0,0,0,0,0,0,1,
                 0,0,0,0,0,1,0,1,0,0,
                 1,0,1,0,0,0,0,1,0,0,
                 1,0,1,1,0,0,1,1,0,
                 1,0,0,0,0,0,0,0,1,
                 1,0,1,1,1,1,0,1,1,0,
                 0,0,0,1,0,0,0,0,1,1,
                 1,0,1,1,1,1,0,1,0,0,
                 0,1,1,0,0,0,0,0,0,0,
                 1,0,1,0,1,1,1,0,0,0,
                 1,1,0,0,1,0,0,1,1,1,
                 1,1]
TTV_second=     [0,0,1,0,1,0,0,1,0,
                 0,0,0,0,0,0,0,0,0,0,
                 0,1,0,1,0,0,0,1,1,1,
                 1,0,1,0,0,0,1,1,0,
                 0,0,1,0,0,0,0,0,1,
                 0,0,0,0,0,0,0,1,1,1,
                 0,0,0,0,0,1,0,0,0,0,
                 1,0,0,1,0,1,0,0,0,0,
                 1,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,1,0,1,
                 1,0,1,1,0,0,0,1,0,0,
                 0,0,1,0,0,0,1,0,0,
                 0,0,1,0,1,0,0,0,1,
                 0,0,0,0,1,0,0,0,0,0,
                 1,0,0,0,0,0,0,0,1,0,
                 1,0,1,1,0,0,0,0,0,0,
                 0,1,0,0,0,1,0,0,0,0,
                 0,0,0,0,0,0,1,0,0,0,
                 1,1,0,0,1,0,0,1,0,1,
                 1,1]      
SZZ_versioned=  [0,1,1,1,0,1,1,1,1,
                 1,1,1,0,0,0,0,0,0,1,
                 1,0,1,1,0,0,0,1,1,0,
                 0,1,0,0,0,0,0,0,1,
                 1,1,1,1,1,0,0,0,0,
                 0,0,0,0,1,0,1,1,1,0,
                 0,0,1,1,1,0,1,1,1,0,
                 1,1,0,1,1,1,0,1,0,1,
                 0,0,1,1,0,1,1,1,1,1,
                 1,1,0,1,1,0,1,0,0,0,
                 0,1,1,0,1,1,0,1,1,1,
                 0,1,0,1,1,0,0,0,0,
                 0,0,1,1,0,1,0,0,1,
                 0,0,1,0,0,1,0,0,1,1,
                 0,0,1,1,0,1,0,1,0,1,
                 0,0,0,1,1,1,0,0,0,1,
                 1,0,1,1,1,1,0,0,1,0,
                 0,1,1,1,1,0,1,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,
                 0,0]
Repro_Data =    [1,0,0,1,1,1,0,0,1,
                 1,0,0,0,0,1,1,0,0,0,
                 1,1,0,0,0,0,1,0,1,1,
                 0,0,1,1,1,1,1,1,0,
                 0,0,1,0,0,0,1,1,1,
                 0,0,0,1,0,1,1,0,1,1,
                 1,1,0,1,1,1,0,1,1,0,
                 0,0,0,1,0,1,0,1,0,0,
                 1,1,1,0,0,0,0,1,0,1,
                 1,0,0,0,0,1,0,1,1,1,
                 1,1,0,1,0,0,1,1,1,0,
                 0,0,1,0,1,1,0,1,1,
                 0,0,0,1,0,1,1,0,1,
                 1,1,1,0,0,1,1,0,0,0,
                 1,1,0,1,1,0,1,1,1,1,
                 1,0,1,1,1,1,1,1,0,1,
                 1,1,0,0,0,0,0,0,0,1,
                 1,0,0,0,1,1,1,0,1,1,
                 1,1,0,0,1,0,0,0,0,0,
                 0,0]
Repro_Package = [0,0,0,0,1,0,0,0,0,
                 0,0,0,0,1,0,0,0,1,1,
                 0,0,0,0,0,0,0,0,0,0,
                 0,1,1,1,0,0,0,1,0,
                 0,0,1,0,0,1,1,0,0,
                 0,0,0,0,0,0,0,0,1,0,
                 0,0,0,0,1,0,1,0,1,0,
                 0,1,0,1,0,0,0,0,0,0,
                 0,0,0,0,0,0,1,0,1,0,
                 0,0,0,0,1,0,0,1,1,0,
                 0,0,0,1,0,1,0,0,1,0,
                 0,0,0,0,0,1,0,0,1,
                 0,0,0,1,0,0,1,1,0,
                 0,0,0,0,0,0,0,0,0,1,
                 0,0,0,0,0,0,0,0,0,0,
                 0,0,1,1,0,0,0,0,0,0,
                 0,0,1,0,1,0,1,1,0,0,
                 1,0,0,0,0,0,0,0,0,1,
                 0,0,0,0,1,0,0,0,1,0,
                 0,1]
SZZ_original =  [1,0,0,0,1,0,0,0,0,
                 0,0,0,1,0,0,1,1,0,0,
                 0,1,0,0,1,0,0,0,0,0,
                 0,0,1,1,1,1,1,1,1,
                 0,0,0,0,0,1,0,1,0,
                 0,1,1,1,0,1,0,0,0,1,
                 1,1,0,0,0,1,0,0,0,1,
                 0,0,1,0,0,0,0,0,1,0,
                 1,1,0,0,1,0,0,0,0,0,
                 0,0,1,0,0,1,0,1,1,1,
                 1,0,0,1,0,0,1,0,0,0,
                 1,0,1,0,0,1,0,1,1,
                 0,1,0,0,1,0,1,1,0,
                 1,1,0,1,0,0,1,1,0,0,
                 1,1,0,0,1,0,1,0,1,0,
                 1,1,0,0,0,0,0,1,1,0,
                 0,1,0,0,0,0,1,1,0,0,
                 1,0,0,0,0,0,0,1,1,1,
                 1,1,1,0,0,0,0,0,0,0,
                 0,0]
SZZ_improved=   [0,0,1,0,0,0,0,0,0,
                 0,0,1,0,1,1,0,0,1,0,
                 0,0,0,1,0,1,0,0,1,1,
                 1,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,1,0,1,
                 1,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,
                 0,0,0,1,0,1,1,0,0,0,
                 0,0,0,0,0,1,0,0,0,0,
                 0,0,0,1,0,0,0,0,0,0,
                 0,1,1,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,1,0,0,
                 1,0,0,0,0,0,0,0,0,
                 0,0,1,0,1,1,0,0,1,0,
                 0,0,0,0,0,0,0,0,0,0,
                 0,0,1,0,0,0,1,0,0,0,
                 0,0,0,1,0,1,0,0,0,1,
                 0,0,0,0,0,1,0,0,0,0,
                 0,0,0,1,1,1,1,1,1,1,
                 1,1]

#hypothesis 1:  Reproducibility of the papers are independient of the awareness of the authors

# Calculate AW+ and AW-
AW_pos = np.array(TTV_first) & np.array(TTV_second)
AW_neg = np.logical_not(TTV_first).astype(int) & np.logical_not(TTV_second).astype(int)

#Calculate Repro full, repro none
Rfull = np.array(Repro_Data) & np.array(Repro_Package)
Rnone = np.logical_not(Repro_Data) & np.logical_not(Repro_Package)

#Create crosstab 
pos_00 = (AW_pos & Rfull).sum()
pos_01 = (AW_pos & Rnone).sum()
pos_02 = (AW_pos & Repro_Data).sum()
pos_03 = (AW_pos & Repro_Package).sum()
pos_10 = (AW_neg & Rfull).sum()
pos_11 = (AW_neg & Rnone).sum()
pos_12 = (AW_neg & Repro_Data).sum()
pos_13 = (AW_neg & Repro_Package).sum()

#Contingency Table
datah1 = pd.DataFrame([[pos_00,pos_01,pos_02, pos_03],[pos_10,pos_11,pos_12, pos_13]],index=['Awareness','NoAwareness'])
datah1.columns =["Full Repro","No Repro", "Data Repro", "Package Repro"]
colsumh1 =datah1.sum(axis=1) 
sum_datah1 = pd.DataFrame(colsumh1, columns=["row_total"])
datah1 = pd.concat([datah1,sum_datah1],axis=1)

rowsumh1 =datah1.sum(axis=0) 
sum_data = pd.DataFrame(rowsumh1, columns = ["col_total"])
datah1 = pd.concat([datah1,sum_data.T])
print (datah1)

#Colum percentaje
colpcth1= datah1/rowsumh1
print (colpcth1)


#Calculate observed and expected tables
observedh1 = datah1.ix[0:2,0:4]
print (observedh1)
expectedh1 = np.outer(datah1["row_total"][0:2],
                   datah1.ix["col_total"][0:4])/(datah1["row_total"][2])

expectedh1 = pd.DataFrame(expectedh1)
expectedh1.columns = ["Full Repro","No Repro", "Data Repro", "Package Repro"]
expectedh1.index = ['Awareness','NoAwareness']
expectedh1

#Calculate chi-square values
print ('chi-square value, p value, expected counts')
cs1h1 = stats.chi2_contingency(observedh1)
print (cs1h1)


########################################################################
#hypothesis 2:  Reproducibility of the papers are independient of the version used

#Calculate Repro full, repro none
Rfull = np.array(Repro_Data) & np.array(Repro_Package)
Rnone = np.logical_not(Repro_Data) & np.logical_not(Repro_Package)

#Create crosstab 
pos_00 = (SZZ_original & Rfull).sum()
pos_01 = (SZZ_original & Rnone).sum()
pos_02 = (np.array(SZZ_original) & Repro_Data).sum()
pos_03 = (np.array(SZZ_original) & Repro_Package).sum()
pos_10 = (SZZ_versioned & Rfull).sum()
pos_11 = (SZZ_versioned & Rnone).sum()
pos_12 = (np.array(SZZ_versioned)& Repro_Data).sum()
pos_13 = (np.array(SZZ_versioned) & Repro_Package).sum()
pos_20 = (SZZ_improved & Rfull).sum()
pos_21 = (SZZ_improved & Rnone).sum()
pos_22 = (np.array(SZZ_improved) & Repro_Data).sum()
pos_23 = (np.array(SZZ_improved) & Repro_Package).sum()


#Contingency Table
data = pd.DataFrame([[pos_00,pos_01,pos_02, pos_03],[pos_10,pos_11,pos_12, pos_13],[pos_20,pos_21,pos_22, pos_23]],index=['SZZOriginal','SZZ-Mod',"SZZ1-SZZ2"])
data.columns =["Full Repro","No Repro", "Data Repro", "Package Repro"]
colsum =data.sum(axis=1) 
sum_data = pd.DataFrame(colsum, columns=["row_total"])
data = pd.concat([data,sum_data],axis=1)

rowsum =data.sum(axis=0) 
sum_data = pd.DataFrame(rowsum, columns = ["col_total"])
data = pd.concat([data,sum_data.T])
print (data)

#Colum percentaje
colsum=data.sum(axis=0)
colpct= data/colsum
print (colpct)

observed = data.ix[0:3,0:4]

expected = np.outer(data["row_total"][0:3],
                   data.ix["col_total"][0:4])/(data["row_total"][2])

expected = pd.DataFrame(expected)
expected.columns = ["Full Repro","No Repro", "Data Repro", "Package Repro"]
expected.index = ['SZZOriginal','SZZ-Mod',"SZZ1-SZZ2"]
expected

#Calculate chi-square values
print ('chi-square value, p value, expected counts')
cs1 = stats.chi2_contingency(observed)
print (cs1)

############################################################################
#hypothesis 3:  SZZ Version in the papers are independient of the awareness of the authors

# Calculate AW+ and AW-
AW_pos = np.array(TTV_first) & np.array(TTV_second)
AW_neg = np.logical_not(TTV_first).astype(int) & np.logical_not(TTV_second).astype(int)

#Create crosstab 
pos_00 = (SZZ_original & AW_pos).sum()
pos_01 = (SZZ_versioned & AW_pos).sum()
pos_02 = (SZZ_improved & AW_pos).sum()
pos_10 = (SZZ_original & AW_neg).sum()
pos_11 = (SZZ_versioned & AW_neg).sum()
pos_12 = (SZZ_improved & AW_neg).sum()
    
    
#Contingency Table
data = pd.DataFrame([[pos_00,pos_01,pos_02],[pos_10,pos_11,pos_12]],index=['Awareness','NoAwareness'])
data.columns =['SZZOriginal','SZZ-Mod',"SZZ1-SZZ2"]
colsum =data.sum(axis=1) 
sum_data = pd.DataFrame(colsum, columns=["row_total"])
data = pd.concat([data,sum_data],axis=1)

rowsum =data.sum(axis=0) 
sum_data = pd.DataFrame(rowsum, columns = ["col_total"])
data = pd.concat([data,sum_data.T])
print (data)

#Colum percentaje
colsum=data.sum(axis=0)
colpct= data/colsum
print (colpct)

observed = data.ix[0:2,0:3]

expected = np.outer(data["row_total"][0:2],
                   data.ix["col_total"][0:3])/(data["row_total"][2])

expected = pd.DataFrame(expected)
expected.index = ['Awareness','NoAwareness']
expected.columns = ['SZZOriginal','SZZ-Mod',"SZZ1-SZZ2"]
expected

#Calculate chi-square values
print ('chi-square value, p value, expected counts')
cs1 = stats.chi2_contingency(observed)
print (cs1)
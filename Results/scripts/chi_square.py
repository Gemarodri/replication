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
TTV_first=[1,1,0,1,1,1,0,0,1,0,0,1,0,0,0,1,1,0,0,0,1,1,0,1,1,0,1,1,0,0,1,0,1,1,0,1,1,1,1,0,1,0,1,0,0,0,0,1,0,0,1,1,0,1,0,0,0,1,1,1,0,1,1,0,0,1,0,0,0,0,0,0,1,1,0,1,0,0,0,1,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,1,0,1,0,0,0,0,1,0,0,1,0,0,1,1,0,0,1,1,0,1,0,0,0,0,0,0,0,0,1,1,0,1,1,1,1,0,1,1,0,0,0,0,1,0,0,0,0,1,1,1,0,1,1,1,1,0,1,0,0,0,1,1,0,0,0,0,0,0,0,1,0,1,0,1,1,1,0,0,0,1,1,0,0,1,0,0,1,1,1,1,1]
TTV_second=[0,0,1,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,1,0,1,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,1,0,0,0,0,1,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,0,0,1,0,0,1,0,1,1,1]      
SZZ_versioned=[0,1,1,1,1,0,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,0,1,1,0,0,1,1,1,1,0,1,0,0,0,0,1,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,0,1,1,1,0,0,0,1,1,1,0,1,1,1,0,1,1,0,1,1,1,0,1,0,1,0,0,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1,0,0,0,0,1,1,0,1,1,0,1,1,1,0,1,1,0,1,1,0,0,0,0,0,0,1,1,1,0,1,0,0,1,0,0,1,0,0,1,0,0,1,1,0,0,1,1,0,1,0,1,0,1,0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,0,0,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Repro_Data =[1,0,0,1,1,1,1,0,0,1,1,0,0,0,0,1,1,0,0,0,1,1,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,1,0,0,0,0,1,1,1,0,0,0,1,0,1,1,0,1,1,1,1,0,1,1,1,0,1,1,0,0,0,0,1,0,1,0,1,0,0,1,1,1,0,0,0,0,1,0,1,1,0,0,0,0,1,0,1,1,1,1,1,0,1,0,0,1,1,1,0,0,0,0,1,0,1,1,0,1,1,0,0,0,1,1,0,1,1,0,1,1,1,1,0,0,1,1,0,0,0,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,0,0,0,0,0,0,0,1,1,0,0,0,1,1,1,0,1,1,1,1,0,0,1,0,0,0,0,0,0,0]
Repro_Package = [0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,1,1,1,0,0,0,0,1,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,1,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,1,1,0,0,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,1,0,1,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,1]
SZZ_original =[1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,1,1,1,0,1,1,1,0,0,0,0,0,1,1,0,1,0,0,1,1,1,0,1,0,0,0,1,1,1,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,1,0,1,1,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,1,1,1,1,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,1,0,1,1,0,1,0,0,0,1,0,1,1,0,1,1,0,1,0,0,1,1,0,0,1,1,0,0,1,0,1,0,1,0,1,1,0,0,0,0,0,1,1,0,0,1,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0]
SZZ_improved=[0,0,1,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1]
fullawareness = [0] * 192
fullreplication = [0] * 192
noreplication = [0] * 192
noawareness = [0] * 192

#Create DataFrame
for i in [i for i,x in enumerate(TTV_first) if x ==1]:
    if (TTV_second[i]==1):
        fullawareness[i]="1"
for i in [i for i,x in enumerate(TTV_second) if x ==1]:
    if (TTV_first[i]==1):
        fullawareness[i]="1"
for i in [i for i,x in enumerate(Repro_Data) if x ==1]:
    if (Repro_Package[i]==1):
        fullreplication[i]="1"
for i in [i for i,x in enumerate(Repro_Package) if x ==1]:
    if (Repro_Data[i]==1):
        fullreplication[i]="1"
for i in [i for i,x in enumerate(TTV_first) if x ==0]:
    if (TTV_second[i]==0):
        noawareness[i]="1"
for i in [i for i,x in enumerate(TTV_second) if x ==0]:
    if (TTV_first[i]==1):
        noawareness[i]="1"
for i in [i for i,x in enumerate(Repro_Data) if x ==0]:
    if (Repro_Package[i]==0):
        noreplication[i]="1"
for i in [i for i,x in enumerate(Repro_Package) if x ==0]:
    if (Repro_Data[i]==1):
        noreplication[i]="1"

raw_data = {'SZZ_versioned': SZZ_versioned,
        'SZZ_original': SZZ_original,
        'SZZ_improved': SZZ_improved,
        'TTV_first': TTV_first,
        'TTV_second': TTV_second,
        'Repro_Data': Repro_Data,
        'Repro_Package': Repro_Package,
        'FullAwareness': fullawareness,
        'FullReplication': fullreplication,
        'NoReplication': noreplication,
        'NoAwareness': noawareness}
    
df = pd.DataFrame(raw_data)
df

#Contingency table of observed counts
print ('Contingency table')
data = pd.DataFrame([[10,43,39,27],[10,11,27,11]],index=['Awareness','NoAwareness'])
data.columns =["FullReplication","NoReplication", "Enviroment", "Package"]

colsum =data.sum(axis=1) 
sum_data = pd.DataFrame(colsum, columns=["row_total"])
data = pd.concat([data,sum_data],axis=1)

rowsum =data.sum(axis=0) 
sum_data = pd.DataFrame(rowsum, columns = ["col_total"])
data = pd.concat([data,sum_data.T])
print (data)


#Observed and Expected dataframes
print ('Observed table')
observed = data.ix[0:2,0:4]

expected = np.outer(data["row_total"][0:2],
                   data.ix["col_total"][0:4])/(data["row_total"][2])

expected = pd.DataFrame(expected)
expected.columns = ["FullReplication","NoReplication", "Envir", "Package"]
expected.index = ['Awareness','NoAwareness']
print (observed)

#colum percentages
print ("Colum Percentages Table")
colsum = observed.sum(axis=0) #sum values in each colum
colpct=observed/colsum
print (colpct)

# chi-square
print ("chi-square value, p value, expected counts")
cs1= stats.chi2_contingency(observed)
print (cs1)

--------------------------------------------------------------------------------

# Running a Chi-Square Test
# Both response variable (SZZ version of algorithm) and explanatory variable (Replication+Awareness(+)) are quantitative variables.In order to perform a Chi-square test, I had to categorize both these variables.

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
TTV_first=[1,1,0,1,1,1,0,0,1,0,0,1,0,0,0,1,1,0,0,0,1,1,0,1,1,0,1,1,0,0,1,0,1,1,0,1,1,1,1,0,1,0,1,0,0,0,0,1,0,0,1,1,0,1,0,0,0,1,1,1,0,1,1,0,0,1,0,0,0,0,0,0,1,1,0,1,0,0,0,1,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,1,0,1,0,0,0,0,1,0,0,1,0,0,1,1,0,0,1,1,0,1,0,0,0,0,0,0,0,0,1,1,0,1,1,1,1,0,1,1,0,0,0,0,1,0,0,0,0,1,1,1,0,1,1,1,1,0,1,0,0,0,1,1,0,0,0,0,0,0,0,1,0,1,0,1,1,1,0,0,0,1,1,0,0,1,0,0,1,1,1,1,1]
TTV_second=[0,0,1,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,1,0,1,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,1,0,0,0,0,1,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,0,0,1,0,0,1,0,1,1,1]      
SZZ_versioned=[0,1,1,1,1,0,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,0,1,1,0,0,1,1,1,1,0,1,0,0,0,0,1,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,0,1,1,1,0,0,0,1,1,1,0,1,1,1,0,1,1,0,1,1,1,0,1,0,1,0,0,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1,0,0,0,0,1,1,0,1,1,0,1,1,1,0,1,1,0,1,1,0,0,0,0,0,0,1,1,1,0,1,0,0,1,0,0,1,0,0,1,0,0,1,1,0,0,1,1,0,1,0,1,0,1,0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,0,0,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Repro_Data =[1,0,0,1,1,1,1,0,0,1,1,0,0,0,0,1,1,0,0,0,1,1,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,1,0,0,0,0,1,1,1,0,0,0,1,0,1,1,0,1,1,1,1,0,1,1,1,0,1,1,0,0,0,0,1,0,1,0,1,0,0,1,1,1,0,0,0,0,1,0,1,1,0,0,0,0,1,0,1,1,1,1,1,0,1,0,0,1,1,1,0,0,0,0,1,0,1,1,0,1,1,0,0,0,1,1,0,1,1,0,1,1,1,1,0,0,1,1,0,0,0,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,0,0,0,0,0,0,0,1,1,0,0,0,1,1,1,0,1,1,1,1,0,0,1,0,0,0,0,0,0,0]
Repro_Package = [0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,1,1,1,0,0,0,0,1,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,1,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,1,1,0,0,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,1,0,1,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,1]
SZZ_original =[1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,1,1,1,0,1,1,1,0,0,0,0,0,1,1,0,1,0,0,1,1,1,0,1,0,0,0,1,1,1,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,1,0,1,1,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,1,1,1,1,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,1,0,1,1,0,1,0,0,0,1,0,1,1,0,1,1,0,1,0,0,1,1,0,0,1,1,0,0,1,0,1,0,1,0,1,1,0,0,0,0,0,1,1,0,0,1,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0]
SZZ_improved=[0,0,1,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1]
fullawareness = [0] * 192
fullreplication = [0] * 192
noreplication = [0] * 192
noawareness = [0] * 192

#Create DataFrame
for i in [i for i,x in enumerate(TTV_first) if x ==1]:
    if (TTV_second[i]==1):
        fullawareness[i]="1"
for i in [i for i,x in enumerate(TTV_second) if x ==1]:
    if (TTV_first[i]==1):
        fullawareness[i]="1"
for i in [i for i,x in enumerate(Repro_Data) if x ==1]:
    if (Repro_Package[i]==1):
        fullreplication[i]="1"
for i in [i for i,x in enumerate(Repro_Package) if x ==1]:
    if (Repro_Data[i]==1):
        fullreplication[i]="1"
for i in [i for i,x in enumerate(TTV_first) if x ==0]:
    if (TTV_second[i]==0):
        noawareness[i]="1"
for i in [i for i,x in enumerate(TTV_second) if x ==0]:
    if (TTV_first[i]==1):
        noawareness[i]="1"
for i in [i for i,x in enumerate(Repro_Data) if x ==0]:
    if (Repro_Package[i]==0):
        noreplication[i]="1"
for i in [i for i,x in enumerate(Repro_Package) if x ==0]:
    if (Repro_Data[i]==1):
        noreplication[i]="1"

raw_data = {'SZZ_versioned': SZZ_versioned,
        'SZZ_original': SZZ_original,
        'SZZ_improved': SZZ_improved,
        'TTV_first': TTV_first,
        'TTV_second': TTV_second,
        'Repro_Data': Repro_Data,
        'Repro_Package': Repro_Package,
        'FullAwareness': fullawareness,
        'FullReplication': fullreplication,
        'NoReplication': noreplication,
        'NoAwareness': noawareness}
    
df = pd.DataFrame(raw_data)
df

#Contingency table of observed counts
print ('Contingency table')
data = pd.DataFrame([[10,43,39,27],[10,11,27,11]],index=['Awareness','NoAwareness'])
data.columns =["FullReplication","NoReplication", "Enviroment", "Package"]

colsum =data.sum(axis=1) 
sum_data = pd.DataFrame(colsum, columns=["row_total"])
data = pd.concat([data,sum_data],axis=1)

rowsum =data.sum(axis=0) 
sum_data = pd.DataFrame(rowsum, columns = ["col_total"])
data = pd.concat([data,sum_data.T])
print (data)


#Observed and Expected dataframes
print ('Observed table')
observed = data.ix[0:2,0:4]

expected = np.outer(data["row_total"][0:2],
                   data.ix["col_total"][0:4])/(data["row_total"][2])

expected = pd.DataFrame(expected)
expected.columns = ["FullReplication","NoReplication", "Envir", "Package"]
expected.index = ['Awareness','NoAwareness']
print (observed)

#colum percentages
print ("Colum Percentages Table")
colsum = observed.sum(axis=0) #sum values in each colum
colpct=observed/colsum
print (colpct)

# chi-square
print ("chi-square value, p value, expected counts")
cs1= stats.chi2_contingency(observed)
print (cs1)


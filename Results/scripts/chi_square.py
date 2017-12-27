#Imports
import pandas as pd
import numpy as np
import scipy.stats as stats

def sumrowcol( df ):

	colsum =df.sum(axis=1) 
	sum_data = pd.DataFrame(colsum, columns=["row_total"])
	df = pd.concat([df,sum_data],axis=1)

	rowsum = df.sum(axis=0) 
	sum_data = pd.DataFrame(rowsum, columns = ["col_total"])
	df = pd.concat([df,sum_data.T])
	print ('############################################################')
	print ('Print Contingency Table')
	print ('############################################################')
	print (df)
	

	return df

def expected (data,beginrow,endrow,begincol,endcol,columns,index ):
    expected = np.outer(data["row_total"][beginrow:endrow],
                   data.ix["col_total"][begincol:endcol])/(data["row_total"][2])

    expected = pd.DataFrame(expected)
    expected.columns = columns
    expected.index = index
    print (expected)
    
    return expected

def chisquare (observed):
	print ('############################################################')
	print ('chi-square value, p value, expected counts')
	print ('############################################################')
	cs = stats.chi2_contingency(observed)
	print (cs)

#Data
Manual_Analysis=[0,1,1,0,1,1,0,1,1,1,0,0,0,0,1,0,0,1,1,1,0,1,1,0,1,0,1,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0,1,0,1,1,1,1,0,1,1,1,0,0,0,0,1,0,1,1,1,1,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,1,1,1,0,1,1,1,0,1,0,0,0,1,0,0,1,1,0,0,1,0,1,1,0,0,0,1,0,0,1,1,0,1,0,1,1,1,0,0,1,0,1,0,0,1,0,0,0,0,1,1,1,1,0,1,0,0,1,1,0,0,0,0,1,1,1,1,1,1,0,1,0,1,0,1,1,0,1,0,1,1,1,0,1,0,1,0,0,0,0,1,0,1]
TTV_first=      [1,1,0,1,1,0,0,1,0,0,1,0,0,0,1,1,0,0,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,1,0,1,0,1,0,0,0,1,0,0,1,1,0,1,0,0,0,1,1,1,0,1,1,0,0,1,0,0,0,0,0,0,1,1,0,1,0,0,0,1,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,1,0,1,0,0,0,0,1,0,0,1,0,1,1,0,0,1,1,0,1,0,0,0,0,0,0,0,1,1,0,1,1,1,1,0,1,1,0,0,0,0,1,0,0,0,0,1,1,1,0,1,1,1,1,0,1,0,0,0,1,1,0,0,0,0,0,0,0,1,0,1,0,1,1,1,0,0,0,1,1,0,0,1,0,0,1,1,1,1,1]
TTV_second=     [0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,1,1,1,0,1,0,0,0,1,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,1,0,0,0,0,1,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,1,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,0,0,1,0,0,1,0,1,1,1]      
SZZ_versioned=  [0,1,1,1,0,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,0,1,1,0,0,0,1,1,0,0,1,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,0,1,1,1,0,0,0,1,1,1,0,1,1,1,0,1,1,0,1,1,1,0,1,0,1,0,0,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1,0,0,0,0,1,1,0,1,1,0,1,1,1,0,1,0,1,1,0,0,0,0,0,0,1,1,0,1,0,0,1,0,0,1,0,0,1,0,0,1,1,0,0,1,1,0,1,0,1,0,1,0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,0,0,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Repro_Data =    [1,0,0,1,1,1,0,0,1,1,0,0,0,0,1,1,0,0,0,1,1,0,0,0,0,1,0,1,1,0,0,1,1,1,1,1,1,0,0,0,1,0,0,0,1,1,1,0,0,0,1,0,1,1,0,1,1,1,1,0,1,1,1,0,1,1,0,0,0,0,1,0,1,0,1,0,0,1,1,1,0,0,0,0,1,0,1,1,0,0,0,0,1,0,1,1,1,1,1,0,1,0,0,1,1,1,0,0,0,1,0,1,1,0,1,1,0,0,0,1,0,1,1,0,1,1,1,1,0,0,1,1,0,0,0,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,0,0,0,0,0,0,0,1,1,0,0,0,1,1,1,0,1,1,1,1,0,0,1,0,0,0,0,0,0,0]
Repro_Package = [0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,1,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,1,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,1,1,0,0,0,0,1,0,1,0,0,1,0,0,0,0,0,0,1,0,0,1,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,1,0,1,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,1]
SZZ_original =  [1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,1,0,1,0,0,1,1,1,0,1,0,0,0,1,1,1,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,1,0,1,1,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,1,1,1,1,0,0,1,0,0,1,0,0,0,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,1,0,1,0,0,1,1,0,0,1,1,0,0,1,0,1,0,1,0,1,1,0,0,0,0,0,1,1,0,0,1,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0]
SZZ_improved=   [0,0,1,0,0,0,0,0,0,0,0,1,0,1,1,0,0,1,0,0,0,0,1,0,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1]


print ('*************************************************************************************')
print ('********	  		HYPOTHESIS 1	    			     ********')
print ('*************************************************************************************')
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
data = pd.DataFrame([[pos_00,pos_01,pos_02, pos_03],[pos_10,pos_11,pos_12, pos_13]],index=['Awareness','NoAwareness'])
data.columns =["Full Repro","No Repro", "Data Repro", "Package Repro"]

datah1 = sumrowcol(data)

#Observed and Expected values
observedh1 = datah1.ix[0:2,0:4]

columns = ["Full Repro","No Repro", "Data Repro", "Package Repro"]
index = ['Awareness','NoAwareness']
expectedh1 = expected(datah1,0,2,0,4, columns, index)

print ('############################################################')
print ('Residuals Table')
print ('############################################################')
residualsh1 = expectedh1 - observedh1
print(residualsh1)	

#Calculate chi-square
chisquare(observedh1) 

print ('*************************************************************************************')
print ('********	  		HYPOTHESIS 2	    			     ********')
print ('*************************************************************************************')
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

datah2 = sumrowcol(data)

#Observed and Expected values
observedh2 = datah2.ix[0:3,0:4]

columns = ["Full Repro","No Repro", "Data Repro", "Package Repro"]
index = ['SZZOriginal','SZZ-Mod',"SZZ1-SZZ2"]
expectedh2 = expected(datah2,0,3,0,4, columns, index)


print ('############################################################')
print ('Residuals Table')
print ('############################################################')
residualsh2 = expectedh2 - observedh2
print(residualsh2)	

#Calculate chi-square
chisquare(observedh2) 

print ('*************************************************************************************')
print ('********	  		HYPOTHESIS 3	    			     ********')
print ('*************************************************************************************')
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

datah3 = sumrowcol(data)

#Observed and Expected values
observedh3 = datah3.ix[0:2,0:3]

index = ['Awareness','NoAwareness']
columns = ['SZZOriginal','SZZ-Mod',"SZZ1-SZZ2"]
expectedh3 = expected(datah3,0,2,0,3, columns, index)

print ('############################################################')
print ('Residuals Table')
print ('############################################################')
residualsh3 = expectedh3 - observedh3
print(residualsh3)	

#Calculate chi-square
chisquare(observedh3) 


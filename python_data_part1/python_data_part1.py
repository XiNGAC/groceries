import pandas as pd
import numpy as np
from scipy.stats import ttest_ind
df = pd.read_csv("tips.csv")

print (df.head()) #output first 5 lines
print (df.tail()) #output last 5 lines
print (df.columns) #output names of columns
print (df.index) #output names of lines
print (df.ix[10:20, 0:3]) #output data of 0-3 columns in 10-20 lines while columns and lines are contines
print (df.iloc[1,3,5],[2,4]) #output data of the 2 and 4 columns in 1,3,5 lines
print (df.iloc[3]) #output the detail of line 3
print (df.iloc[2:4]) #output the detail of line 2 and 3(line 4 is not in the output)
print (df.iloc[0,1]) #output the element on line 0 column 1
print (df.iat[3,2]) #output the only data of the box in line 3 and column 2
print (df.drop(df.columns[1,2],axis = 1)) #output the data while drop the first 2 columns
print (df.drop(df.columns[[1,2]],axis = 0)) #output the data while drop the first 2 lines
print (df.shape) #output the shape as lines and columns

print (df[df.tip>8]) #select the data which tip is larger than 8
print (df[ (df.tip>7) | ( df.total_bill > 50 )]) #select the data which tip is larger than 7 or total_bill is larger than 50
print (df[ (df.tip>7) & ( df.total_bill > 50 )]) #select the data which tip is larger than 7 and total_bill is larger than 50
print (df[['day','time']][(df.tip>7)|(df.total_bill>100)]) #select only day and time from data which xxxxx

print (df.describe()) #output the describe of data (count,mean,std,min,max)

print (df.T) #matrix transpose

print (df.sort_values(by='tip')) #sort by tip

#data group
group = df.groupby('day') #group by column 'day'
print (group.first()) #output the first line of each group
print (group.last()) #output the last line of each group


Series = pd.Series([0,1,2,3,4,5])  #create a series
Series.replace(0,10000) #replace 0 in Series with 10000
Series.replace([0,1,2,3,4,5], [111,222,333,444,555,666]) #replace the column


#Independent sample t test
t_test = pd.read_excel('test.xlsx')
Group1 = t_test[t_test['group']==1]['data']
Group2 = t_test[t_test['group']==2]['data']
print(ttest_ind(Group1,Group2))
#print result as (t,p-value): (-4.7515451390104353, 0.0014423819408438474) 

#count statistic
count = df['sex'].value_counts()


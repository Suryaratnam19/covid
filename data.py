
# COVID19-daywise cases Visualisation


# Preprocessed the data of day-wise COVID19 cases of various regions
# Plotted charts for country-wise, date-wise and continent-wise COVID cases using the libraries Matplotlib and Plotly to know trends of increase in number of cases


# Data Visualization based on the day-wise data of covid19 cases all over the world between January and March.
# Processed the data according to the condition that, on a particular date, If more than 75% of "number of confirmed cases" is zero, then delete the column.
# Then ploted the graphs or charts: Country Wise, Date Wise, Continent Wise




import numpy as np
import pandas as pd

DataFrame=pd.read_csv(r'time_series_ncov-Confirmed.csv')

DataFrame

df=DataFrame.copy()

df

key=df.describe().keys()

key
"""
Index(['1/22/20', '1/23/20', '1/24/20', '1/25/20', '1/26/20', '1/27/20',
       '1/28/20', '1/29/20', '1/30/20', '1/31/20', '02-01-2020', '02-02-2020',
       '02-03-2020', '02-04-2020', '02-05-2020', '02-06-2020', '02-07-2020',
       '02-08-2020', '02-09-2020', '02-10-2020', '02-11-2020', '02-12-2020',
       '2/13/20', '2/14/20', '2/15/20', '2/16/20', '2/17/20', '2/18/20',
       '2/19/20', '2/20/20', '2/21/20', '2/22/20', '2/23/20', '2/24/20',
       '2/25/20', '2/26/20', '2/27/20', '2/28/20', '2/29/20', '03-01-2020',
       '03-02-2020', '03-03-2020', '03-04-2020', '03-05-2020', '03-06-2020',
       '03-07-2020', '03-08-2020', '03-09-2020', '03-10-2020', '03-11-2020',
       '03-12-2020', '3/13/20', '3/14/20', '3/15/20', '3/16/20', '3/17/20',
       '3/18/20', '3/19/20', '3/20/20', '3/21/20', '3/22/20'],
      dtype='object')
"""


updated_dates=list()

for k in range(len(key)): # for every date in Data
    count=0
    for j in range(487):
        if(df.iloc[j][k+4]==0): count=count+1 # if number of cases = 0 then increase count
    percentage=count/487 # if 0 cases more than 70% days then append to updated_dates
    if(percentage>=0.71): updated_dates.append(key[k])
    

updated_dates
"""
['1/22/20',
 '1/23/20',
 '1/24/20',
 '1/25/20',
 '1/26/20',
 '1/27/20',
 '1/28/20',
 '1/29/20',
 '1/30/20',
 '1/31/20',
 '02-01-2020',
 '02-02-2020',
 '02-03-2020',
 '02-04-2020',
 '02-05-2020',
 '02-06-2020',
 '02-07-2020',
 '02-08-2020',
 '02-09-2020',
 '02-10-2020',
 '02-11-2020',
 '02-12-2020',
 '2/13/20',
 '2/14/20',
 '2/15/20',
 '2/16/20',
 '2/17/20',
 '2/18/20',
 '2/19/20',
 '2/20/20',
 '2/21/20',
 '2/22/20',
 '2/23/20',
 '2/24/20',
 '2/25/20',
 '2/26/20',
 '2/27/20',
 '2/28/20',
 '2/29/20',
 '03-01-2020',
 '03-02-2020']
""" 
 
for i in updated_dates: # drop the dates with 0 cases >70%
	df = df.drop(i, axis = 1)
    
df

df_grouped = df.groupby('Country/Region').sum() # groupby() function is used to split the data into groups based on some criteria

df_grouped



region_dict = dict()

for i in range(487):
    region_dict[df.iloc[i][1]] = region_dict.get(df.iloc[i][1],0) + df.iloc[i][-1]


for region in region_dict: # number of cases in Region
    print("{} with cases:{}".format(region,region_dict[region]))


import matplotlib.pyplot as plt
plt.figure(figsize = (200,100))
plt.pie(region_dict.values())
plt.title('Regionwise confirmed cases')
plt.legend(region_dict.keys(), loc='center left', prop = {'size': 64})
plt.show()


df=pd.read_csv(r'time_series_ncov-Confirmed.csv')
for i in updated_dates:
    df = df.drop(i, axis = 1)


df

df.keys()
"""
Index(['Province/State', 'Country/Region', 'Lat', 'Long', '03-03-2020',
       '03-04-2020', '03-05-2020', '03-06-2020', '03-07-2020', '03-08-2020',
       '03-09-2020', '03-10-2020', '03-11-2020', '03-12-2020', '3/13/20',
       '3/14/20', '3/15/20', '3/16/20', '3/17/20', '3/18/20', '3/19/20',
       '3/20/20', '3/21/20', '3/22/20'],
      dtype='object')
"""

dates = df.keys()[4:]

dates = list(dates)


dates

date_wise = []

for i in dates:
    cases_sum = df_grouped[i].sum() # total cases
    date_wise.append(cases_sum)
    print(f'{i}:{cases_sum}')
"""
03-03-2020:92840
03-04-2020:95120
03-05-2020:97882
03-06-2020:101784
03-07-2020:105821
03-08-2020:109795
03-09-2020:113561
03-10-2020:118592
03-11-2020:125865
03-12-2020:128343
3/13/20:145193
3/14/20:156094
3/15/20:167446
3/16/20:181527
3/17/20:197142
3/18/20:214910
3/19/20:242708
3/20/20:272166
3/21/20:304524
3/22/20:335955
"""


fig=plt.figure(figsize=(15,15))
plt.pie(date_wise)
plt.title('Date-wise cases',size=30)
plt.legend(dates,loc='best')
plt.show()



cases_sum
# 335955


date_wise
"""
[92840,
 95120,
 97882,
 101784,
 105821,
 109795,
 113561,
 118592,
 125865,
 128343,
 145193,
 156094,
 167446,
 181527,
 197142,
 214910,
 242708,
 272166,
 304524,
 335955]
"""


dates
"""
['03-03-2020',
 '03-04-2020',
 '03-05-2020',
 '03-06-2020',
 '03-07-2020',
 '03-08-2020',
 '03-09-2020',
 '03-10-2020',
 '03-11-2020',
 '03-12-2020',
 '3/13/20',
 '3/14/20',
 '3/15/20',
 '3/16/20',
 '3/17/20',
 '3/18/20',
 '3/19/20',
 '3/20/20',
 '3/21/20',
 '3/22/20']
"""



continent = pd.read_csv('data.csv') # continents countries

continent

continent_dict = dict()

for region in region_dict:
    C = continent.loc[continent['Country']==region]
    if len(C)>0: continent_dict[C.iloc[0][0]] = continent_dict.get(C.iloc[0][0],0)+region_dict[region]


continent_dict
"""
{'Asia': 113013,
 'North America': 35349,
 'Oceania': 1316,
 'Europe': 162094,
 'Africa': 1015,
 'South America': 4096}
"""

plt.figure(figsize = (15,15))
plt.pie(continent_dict.values())
plt.title('Continent-wise cases',size=25)
plt.legend(continent_dict.keys(),prop={'size': 15})
plt.show()





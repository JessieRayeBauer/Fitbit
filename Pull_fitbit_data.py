
# coding: utf-8

# # Tutorial: How to acquire your data from Fitbit's API.
# Jan 21, 2018

# Below are examples of the types of data you can aquire from Fitbit's API. To [register your app](https://dev.fitbit.com/apps/new) and set up an API, see this [helpful tutorial](http://pdwhomeautomation.blogspot.com/2015/03/using-fitbit-api-on-raspberry-pi-with.html).
# 
# The codes below were modified from [Paul's Geek Dad Blog](http://pdwhomeautomation.blogspot.com/2015/03/using-fitbit-api-on-raspberry-pi-with.html) 

# Get heart rate data in second intervals. 

# In[1]:


import requests
import json
import pandas as pd
from time import sleep
 
# put the token for your app in between the single quotes
token = '<enter your token here>'
 
# make a list of dates 
# ref: http://stackoverflow.com/questions/993358/creating-a-range-of-dates-in-python
# You can change the start and end date as you want
# Just make sure to use the yyyy-mm-dd format
start_date = '<start date>'
end_date = '<end date>'
datelist = pd.date_range(start = pd.to_datetime(start_date),
                         end = pd.to_datetime(end_date)).tolist()
 
for ts in datelist:
    date = ts.strftime('%Y-%m-%d')
    url = 'https://api.fitbit.com/1/user/-/activities/heart/date/' + date + '/1d/1sec/time/00:00/23:59.json'
    filename = 'HR'+ date +'.json'
    response = requests.get(url=url, headers={'Authorization':'Bearer ' + token})
 
    if response.ok:
        with open(filename, 'w') as f:
            json.dump(response.content, f)
        print (date + ' is saved!')
        sleep(30)
    else:
        print ('The file of %s is not saved due to error!' % date)
        sleep(30)


# Get sleep data.

# In[ ]:


# put the token for your app in between the single quotes
token = '<enter your token>'
 
# make a list of dates 
# ref: http://stackoverflow.com/questions/993358/creating-a-range-of-dates-in-python
# You can change the start and end date as you want
# Just make sure to use the yyyy-mm-dd format
start_date = '<start date>'
end_date = '<end date>'
datelist = pd.date_range(start = pd.to_datetime(start_date),
                         end = pd.to_datetime(end_date)).tolist()

for ts in datelist:
    date = ts.strftime('%Y-%m-%d')
    url = 'https://api.fitbit.com/1/user/-/sleep/date/' + date + '.json'
    filename = 'sleep'+ date +'.json'
    response = requests.get(url=url, headers={'Authorization':'Bearer ' + token})
 
    if response.ok:
        with open(filename, 'w') as f:
            json.dump(response.content, f)
        print (date + ' is saved!')
        sleep(30)
    else:
        print ('The file of %s is not saved due to error!' % date)
        sleep(30)


# In[ ]:


Get step data. 


# In[ ]:


# put the token for your app in between the single quotes
token = '<enter your token>'

# make a list of dates 
# ref: http://stackoverflow.com/questions/993358/creating-a-range-of-dates-in-python
# You can change the start and end date as you want
# Just make sure to use the yyyy-mm-dd format
start_date = '<start date>'
end_date = '<end date>'
datelist = pd.date_range(start = pd.to_datetime(start_date),
                         end = pd.to_datetime(end_date)).tolist()
 
'''
The codes below use a for loop to generate one URL for each day in the datelist,
and then request each day's data and save the data into individual json files.
Because Fitbit limit 150 request per hour, I let the code sleep for 30 seconds 
between each request, to meet this limitation.
'''
for ts in datelist:
    date = ts.strftime('%Y-%m-%d')
    url = 'https://api.fitbit.com/1/user/-/activities/steps/date/' + date + '/today/1d.json'
    filename = 'step'+ date +'.json'
    response = requests.get(url=url, headers={'Authorization':'Bearer ' + token})
 
    if response.ok:
        with open(filename, 'w') as f:
            json.dump(response.content, f)
        print (date + ' is saved!')
        sleep(30)
    else:
        print ('The file of %s is not saved due to error!' % date)
        sleep(30)


# In[ ]:


Get frequent activity data. 


# In[ ]:


# put the token for your app in between the single quotes
token = '<enter your token>' 
# make a list of dates 
# ref: http://stackoverflow.com/questions/993358/creating-a-range-of-dates-in-python
# You can change the start and end date as you want
# Just make sure to use the yyyy-mm-dd format
start_date = '<start date>'
end_date = '<end date>'
datelist = pd.date_range(start = pd.to_datetime(start_date),
                         end = pd.to_datetime(end_date)).tolist()

for ts in datelist:
    date = ts.strftime('%Y-%m-%d')
    url = 'https://api.fitbit.com/1/user/-/activities/frequent.json'
    filename = 'freq'+ date +'.json'
    response = requests.get(url=url, headers={'Authorization':'Bearer ' + token})
 
    if response.ok:
        with open(filename, 'w') as f:
            json.dump(response.content, f)
        print (date + ' is saved!')
        sleep(30)
    else:
        print ('The file of %s is not saved due to error!' % date)
        sleep(30)


# Get activity data.

# In[ ]:


# put the token for your app in between the single quotes
token = '<enter your token>' 
 
# make a list of dates 
# ref: http://stackoverflow.com/questions/993358/creating-a-range-of-dates-in-python
# You can change the start and end date as you want
# Just make sure to use the yyyy-mm-dd format
start_date = '<start date>'
end_date = '<end date>'
datelist = pd.date_range(start = pd.to_datetime(start_date),
                         end = pd.to_datetime(end_date)).tolist()

for ts in datelist:
    date = ts.strftime('%Y-%m-%d')
    url = 'https://api.fitbit.com/1/user/-/activities.json'
    filename = 'best'+ date +'.json'
    response = requests.get(url=url, headers={'Authorization':'Bearer ' + token})
 
    if response.ok:
        with open(filename, 'w') as f:
            json.dump(response.content, f)
        print (date + ' is saved!')
        sleep(30)
    else:
        print ('The file of %s is not saved due to error!' % date)
        sleep(30)


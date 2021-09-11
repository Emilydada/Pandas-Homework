#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[6]:


# Dependencies and Setup
import pandas as pd
import numpy as np
import os

# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)
purchase_data.head()


# ## Player Count

# * Display the total number of players
# 

# In[7]:


purchase_data.describe()


# In[8]:


Total_Players=purchase_data["SN"].nunique()
purchase_data["Total_Players"]=Total_Players
purchase_data[["Total_Players"]].head(1)


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[9]:


Unique_items=purchase_data["Item ID"].nunique()
Average_Price=purchase_data["Price"].mean()
number_of_Purchases=purchase_data["Purchase ID"].count()
Total_Revenue=purchase_data["Price"].sum()
purchase_data["Unique_items"]=Unique_items
purchase_data["Average_Price"]=Average_Price
purchase_data["number_of_Purchases"]=number_of_Purchases
purchase_data["Total_Revenue"]=Total_Revenue
purchase_data[["Unique_items","Average_Price","number_of_Purchases","Total_Revenue"]].head(1)


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[10]:


Gender_total=purchase_data.groupby(['Purchase ID']).Gender.count()
#male=purchase_data["Gender"].value_counts()['Male']
#female=purchase_data["Gender"].value_counts()['Female']
#non_gender_specific = Gender_total - male - female
#male_percent =(male/Gender_total)
#female_percent=(female/Gender_total)
#non_gender_specific_percent = (non_gender_specific/Gender_total)
gendertable=pd.DataFrame()
#gendertable["Players Count"]=gendercount


gendertable=purchase_data.groupby(['SN','Gender']).size().reset_index().rename(columns={0:'count'})
gendercount=gendertable.Gender.value_counts()
genderpercent=gendercount/len(purchase_data)
gendertable=pd.DataFrame()
gendertable["Gender_total"]=gendercount
gendertable["Percentage of Players"]=(genderpercent*100).map("{:.2f}%".format)

gendertable


# In[11]:


Average_total_purchaseprice_perperson= purchase_data.groupby("Gender").Price.sum()/gendertable["Gender_total"]
#female_avgpurchaseprice=Average_purchase_price* female_percent
#female_avgpurchaseprice
Average_total_purchaseprice_perperson


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[12]:


purchase_price=purchase_data.groupby(['Gender']).Price.mean().round(decimals=2)
purchase_avgprice=pd.DataFrame([["Female",3.2],["Male",3.02],["the/Non-Disclosed",3.35]],columns=['Gender','Average Purchase Price'])
purchase_count=purchase_data.groupby(['Gender']).Price.count()

PurchaseSummary=pd.DataFrame
#PurchaseSummary["Purchase Count"]=purchase_count

#PurchaseSummary["Average Purchase Price"]=purchase_price
PurchaseSummary=pd.DataFrame([["Feamle",113,'\$3.2','\$361.94','\$4.47'],["Male",652,'\$3.02','\$1967.64','\$4.07'],["Other/Non-Disclosed",15,'\$3.35','\$50.19','\$4.56']],columns=['Gender','Purchase Count','Average Purchase Price','Total Purchase Price','Avg Total Purchase Per Person'])
PurchaseSummary


# In[ ]:





# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[13]:


bins = [0, 9, 14, 20, 25, 29, 34, 39, 100]
bin_labels = ['<10', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40+']
agegroup=pd.DataFrame

total_count=pd.cut(purchase_data["Age"], bins, labels=bin_labels)
purchase_data["Age Group"]=total_count
agesummary=purchase_data.groupby(["Age Group","SN"]).Age.value_counts()

agesummary.unstack()


# In[ ]:





# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[14]:


bins = [0, 9, 14, 18, 24, 30, 34, 39, 100]
bin_labels = ['<10', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40+']

total_count2=pd.cut(purchase_data["Age"], bins, labels=bin_labels)
purchase_data["Purchase Count"]=total_count
agesummary2=purchase_data["Purchase Count"].value_counts()
#purchasevalue= purchase_data["Price"].sum()
agesummary2


# In[ ]:





# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[15]:


total_purchase_value= purchase_data["Price"].groupby(purchase_data['SN']).sum()
average_purchase_price= purchase_data["Price"].groupby(purchase_data['SN']).mean()
purchase_count=purchase_data["Price"].groupby(purchase_data['SN']).count()
total_purchase_value.nlargest(n=5)
PurchaseTable=pd.DataFrame([["Lisosia93",5,'\$3.79','\$18.96'],["Idastidru52",5,'\$3.86','\$15.45'],["Chamjask73",3,'\$4.61','\$13.83'],["Iral74",4,'\$3.4','\$13.62'],["Iskadarya95 ",3,'\$4.37','\$13.10']],columns=['SN','Purchase Count','Average Purchase Price','Total Purchase Price'])
PurchaseTable


# In[ ]:





# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, average item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[16]:


total_purchase_count= purchase_data["Purchase ID"].groupby(purchase_data['Item ID']).count()
total_purchase_value= purchase_data["Price"].groupby(purchase_data['Item ID']).sum()
popularitems=pd.DataFrame(purchase_data)
#purchase_data["Total Purchase Value"]=total_purchase_value
#purchase_data["Total Purchase Count"]=total_purchase_count
#popularitems=purchase_data  
cols=[4,5,6]
popularitems=popularitems[purchase_data.columns[cols]]
popularitems["Total Purchase Price"]=total_purchase_value
popularitems['Total Purchase Count']=total_purchase_count
popularitems=popularitems.sort_values(["Total Purchase Count"],ascending=(False))
popularitems.head(5)


# In[ ]:





# In[ ]:





# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[23]:


popularitemsummary=pd.DataFrame(popularitems)
popularitemsummary=popularitems.sort_values(["Total Purchase Price"],ascending=(False))
popularitemsummary.head(5)


# In[ ]:





# In[ ]:





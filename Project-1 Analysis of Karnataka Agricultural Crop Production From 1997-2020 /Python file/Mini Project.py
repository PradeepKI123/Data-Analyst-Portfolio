#!/usr/bin/env python
# coding: utf-8

# # Analysis of Karnataka Agriculture crop production
# 

# ### Objectives :

# ##### 1) To study about highest and lowest crop production in an year.
# ##### 2) To determine most common choice  cop in Karnataka for agriculture?
# ##### 3)  To study about district wise total production of crops.
# ##### 4) To know about the best year for agriculture.
# ##### 5) To determine Annual production of crops from 2010-11 to 2019-20
# ##### 6) To determine the highest Crop production ever received in a year in District
# ##### 7) Analysis of crop production in Dakshin Kannada and Udupi

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# In[2]:


data=pd.read_csv("Agriculture_Karnataka.csv")
data


# In[3]:


data.shape


# In[4]:


data.columns


# In[5]:


data.isnull().sum()


# In[6]:


data.dropna(subset=["Production"],axis=0,inplace=True)


# In[7]:


data.isnull().sum()


# In[8]:


data.shape


# In[9]:


data.describe()


# ##### Exploratory data analysis

# ###### Unique count and values for Crops and district in Karnataka

# In[10]:


# list of crops in Karnataka
crop_list=data["Crop"].unique()
print("Total number of crops in Karnataka",len(crop_list))
print("\nWe have following unique crops in the dataset - \n", crop_list)


# In[11]:


district_list=data['District'].unique()
print("Total number of districts in Karnataka : \n ",len(district_list))
print("\nDistricts are: ",district_list)


# ##### Dealing with various units of production:
# ###### We can observe a column named production units which is a measurement of crop production.We need to 
# ###### standardize the uits to one specific unit to do proper measurement.Let us get units we have in out dataset.

# In[12]:


units=data["Production Units"].unique()
units


# In[13]:


# As per internet source we have 1 Ton=4.59 Bales which is Us standard of measurem


# In[14]:


def unit_standardization(df):
    if df["Production Units"]=="Nuts":
        new_production=df["Production"] / 50
        return new_production
    elif df["Production Units"]=="Tonnes":
        return df["Production"]
    else:
        new_production=df["Production"] / 4.59
        return new_production
data["New Production"]=data.apply(unit_standardization,axis=1)
data.head()


# ###### we can now drop Production and production units as all our units in Tonnes and New production represnts the standard production we calculated
# 

# In[15]:


data.drop(columns=["Production","Production Units"],inplace=True)
data.head()


# ###### Highest and lowest crop production in an year

# In[16]:


year=data.groupby("Year").mean()["New Production"].sort_values(ascending=False).reset_index()
year


# In[17]:


plt.figure(figsize=(8,8))
plt.bar(year["Year"],year["New Production"])
plt.xticks(year["Year"],rotation='vertical',size=10)
plt.xlabel("Year")
plt.ylabel("Total crop production")
plt.title("Crop production from 2010 to 2020")
plt.show()


# ###### Which crop is the most common choice in Karnataka for agriculture?

# In[18]:


data["Crop"].value_counts()


# ###### Best year for Agriculture

# In[19]:


year_list=data["Year"].unique()
year_list


# In[20]:


year_production_list=[]
for year in year_list:
    total_yearly_production=data.loc[data["Year"]==year,"New Production"].sum()
    year_production_list.append(total_yearly_production)
    
year_production_df=pd.DataFrame({"Year":year_list,
                                "Total crop production":year_production_list})
plt.figure(figsize=(8,8))
plt.bar(year_production_df["Year"],year_production_df["Total crop production"])
plt.xticks(year_production_df["Year"],rotation='vertical',size=10)
plt.xlabel("Year")
plt.ylabel("Total crop production")
plt.title("Crop production from 2010 to 2020")
plt.show()


# ###### District wise total production of crops

# In[21]:


total_production=[]
for district in district_list:
    total_crop=data.loc[data["District"]==district,"New Production"].sum()
    total_production.append(total_crop)

total_production_df=pd.DataFrame({"District":district_list,
                                 "Total crop production":total_production})
total_production_df


# In[22]:


plt.figure(figsize=(8,8))
plt.bar(total_production_df["District"],total_production_df["Total crop production"])
plt.xticks(total_production_df["District"],rotation='vertical',size=10)
plt.xlabel("District")
plt.ylabel("Total crop production")
plt.title("District wise Total crop production")
plt.show()


# In[23]:


# From the above bar graph we conclude that Tumkur and Belgaum are the top 2 districts with highest total crop production 
# total of years from 2010 to 2020


# ##### Annual production of crops from 2010-11 to 2019-20

# In[24]:


data.groupby("Year").mean()["New Production"].plot(ylim=(80000,120000),color='k',marker='o',
                                                  markerfacecolor='red',linestyle='-',linewidth=2,figsize=(12,10))
plt.xlabel('Year',fontsize=20)
plt.ylabel("Annual Production",fontsize=20)
plt.title('Annual production of crops from 2010-11 to 2019-20',fontsize=20)
plt.grid()


# ###### Highest Crop production ever received in a year in District

# In[25]:



plt.figure(figsize=(10,8))
data.groupby(["District","Year"])["New Production"].sum().sort_values(ascending=False).plot()
plt.grid()
plt.xticks(rotation='vertical',size=10)
plt.xlabel("District,Year",fontsize=15)
plt.ylabel("Anual crop production",fontsize=15)
plt.title("Highest Crop production ever received in a year in District",fontsize=15)


# ##### Analysis of crop production in Coastal region

# In[26]:


dk=data[data["District"]=="DAKSHIN KANNAD"]
#dk.head(2)


# In[27]:


udp=data[data["District"]=="UDUPI"]
#udp.head(2)


# In[28]:


uk=data[data["District"]=="UTTAR KANNAD"]
#uk.head(2)


# In[29]:


#Average crop production from 2010-11 in Dakshin Kannada
dk_1=dk.groupby("Year").mean()["New Production"].reset_index()
dk_1.rename(columns={'Year':'Year',
                      'New Production':'Average Production DK'},inplace=True)
dk_1.head(2)


# In[30]:


#Average crop production from 2010-11 to 2019-20 in Udupi
udp_1=udp.groupby("Year").mean()["New Production"].reset_index()
udp_1.rename(columns={'Year':'Year',
                      'New Production':'Average Production Udupi'},inplace=True)
udp_1.head(2)


# In[31]:


#Average crop production from 2010-11 to 2019-20 in Uttara Kannada
uk_1=uk.groupby("Year").mean()["New Production"].reset_index()
uk_1.rename(columns={'Year':'Year',
                      'New Production':'Average Production UK'},inplace=True)
uk_1.head(2)


# In[32]:


plt.figure(figsize=(8,5))
plt.plot(dk_1["Year"],dk_1["Average Production DK"],label="Dakshina Kannada")
plt.plot(udp_1["Year"],udp_1["Average Production Udupi"],label="Udupi")
plt.plot(uk_1["Year"],uk_1["Average Production UK"],label="Uttara Kannada")
plt.title("Average crop production in coastal region from 2010 to 2020")
plt.legend(loc='upper left')

plt.show


# In[ ]:





# In[ ]:





# In[63]:


dk_2=dk.groupby("Crop")["New Production"].mean().sort_values(ascending=False)
dk_2.head()


# In[64]:


udp_2=udp.groupby("Crop")["New Production"].mean().sort_values(ascending=False)
udp_2.head()


# In[65]:


uk_2=uk.groupby("Crop")["New Production"].mean().sort_values(ascending=False)
uk_2.head()


# In[36]:


#Anova
dk_anova=data[data["District"]=="DAKSHIN KANNAD"][data["Crop"]=="Arecanut"]
dk_anova.head(2)


# In[37]:


udp_anova=data[data["District"]=="UDUPI"][data["Crop"]=="Arecanut"]
udp_anova.head(2)


# In[38]:


uk_anova=data[data["District"]=="UTTAR KANNAD"][data["Crop"]=="Arecanut"]
uk_anova.head(2)


# In[39]:


#Checking for normality

plt.figure(figsize=(10,4))
a1=dk_anova["New Production"]
a2=udp_anova["New Production"]
a3=uk_anova["New Production"]

plt.subplot(1,3,1)
sns.distplot(a1,color='b')
plt.title("DaKshina Kannada")

plt.subplot(1,3,2)
sns.distplot(a2,color='r')
plt.title("Udupi")

plt.subplot(1,3,3)
sns.distplot(a3,color='g')
plt.title("Uttara Kannada")

plt.show()


# In[40]:


# One way Anova
import scipy.stats as stats
data_1=dk_anova["New Production"]
data_2=udp_anova["New Production"]
data_3=uk_anova["New Production"]
f_value,p_value=stats.f_oneway(data_1,data_2,data_3)
print("F value is : ",f_value)
print("p value is : ",p_value)


# In[41]:


# Significance difference between mean production oh "Maize" in North Karnata and South Karnataka


# In[42]:


north=data.loc[data["District"].isin(['BIDAR','GULBARGA','RAICHUR','BIJAPUR','BAGALKOT','KOPPAL',
                                'GADAG','DHARWAD','BELGAUM','HAVERI','CHITRADURGA', 'BELLARY','YADGIR','DAVANGERE'])]

north.head(5)


# In[43]:


south=data.loc[data["District"].isin(['BANGALORE RURAL','BENGALURU URBAN','CHAMARAJANAGAR','CHIKBALLAPUR','CHIKMAGALUR',
                                      'DAKSHIN KANNAD','HASSAN','KODAGU', 'MANDYA', 'MYSORE','RAMANAGARA', 
                                      'SHIMOGA','TUMKUR','UDUPI','UTTAR KANNAD','KOLAR'])]
south.head(5)


# In[44]:


south_coconut=south[south["Crop"]=="Rice"]
south_coconut.head(1)


# In[45]:


north_coconut=north[north["Crop"]=="Rice"]
north_coconut.head(1)


# In[46]:


north_1=north_coconut.groupby("District").mean()["New Production"].reset_index()
north_1.head()


# In[47]:


south_1=south_coconut.groupby("District").mean()["New Production"].reset_index()
south_1.head()


# In[48]:


#Checking for normality

plt.figure(figsize=(10,5))
b1=north_1["New Production"]
b2=south_1["New Production"]

plt.subplot(1,2,1)
sns.distplot(b1,color='b')
plt.title("North Karnataka")

plt.subplot(1,2,2)
sns.distplot(b2,color='r')
plt.title("South Karnataka")


# In[49]:


from scipy.stats import ttest_ind
b1=north_1["New Production"]
b2=south_1["New Production"]

stat,p=ttest_ind(b1,b2)
print('statistic=%.3f , p_value =%.3f' % (stat ,p))



# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[50]:


dk=data[data["District"]=="DAKSHIN KANNAD"]
dk.head(2)


# In[51]:


dk.groupby("Year").mean()["New Production"].sort_values(ascending=False)


# In[52]:


dk.groupby("Year").mean()["New Production"].plot(ylim=(200000,450000),color='k',marker='*',
                                                  markerfacecolor='green',linestyle='-',linewidth=2,figsize=(12,10))
plt.xlabel('Year',fontsize=20)
plt.ylabel("Annual Production",fontsize=20)
plt.title('Annual production of crops in Dakshina Kannada from 2010-11 to 2019-20',fontsize=15)
plt.grid()


# In[53]:


udp=data[data["District"]=="UDUPI"]
udp.head(2)


# In[54]:


udp.groupby("Year").mean()["New Production"].sort_values(ascending=False)


# In[55]:


udp.groupby("Year").mean()["New Production"].plot(ylim=(120000,300000),color='k',marker='*',
                                                  markerfacecolor='green',linestyle='-',linewidth=2,figsize=(12,10))
plt.xlabel('Year',fontsize=20)
plt.ylabel("Annual Production",fontsize=20)
plt.title('Annual production of crops in Udupi from 2010-11 to 2019-20',fontsize=15)
plt.grid()


# In[56]:


uk=data[data["District"]=="UTTAR KANNAD"]
uk.head(2)


# In[57]:


uk.groupby("Year").mean()["New Production"].sort_values(ascending=False)


# In[58]:



uk.groupby("Year").mean()["New Production"].plot(ylim=(45000,68000),color='k',marker='*',
                                                  markerfacecolor='green',linestyle='-',linewidth=2,figsize=(12,10))
plt.xlabel('Year',fontsize=20)
plt.ylabel("Annual Production",fontsize=20)
plt.title('Annual production of crops in Uttara Kannada from 2010-11 to 2019-20',fontsize=15)
plt.grid()


# In[59]:


coastal_1=data.loc[data["District"].isin(["DAKSHIN KANNAD",'UDUPUI','UTTAR KANNAD'])]
coastal_1


# In[60]:


data.groupby("Crop").mean()["New Production"].sort_values(ascending=False).re


# In[ ]:


coastal_1.groupby("Crop").mean()["New Production"].sort_values(ascending=False)


# In[ ]:





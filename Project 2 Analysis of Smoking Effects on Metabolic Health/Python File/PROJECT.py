#!/usr/bin/env python
# coding: utf-8

# ## To study the smoking effects on metabolic health and Inflammation Markers

# ### Objectives: 

# ###### To build a model which predicts diabetic category using smokers and non smokers body signal
# ###### Comparing the features of smokers and non smokers usind exploratory data analysis.
# ###### To study the associstion of smoking on blood sugar level and dental caries.
# ###### Determing whether smokers cholestrol level influencing on blood pressure.
# 

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ###### ID : serial number given to a person.
# ###### gender: the gender of a person being either female(0) or male(1).
# ###### age : 5-years gap age groups.
# ###### height(cm)
# ###### weight(kg)
# ###### waist(cm) : Waist circumference length
# ###### eyesight(left): Denoted by a value between 0.1-2.5, or 9.9
# ###### eyesight(right): Denoted by a value between 0.1-2.5, or 9.9
# ###### hearing(left): hearing of the person's ear 
# ###### hearing(right): hearing of the person's ear
# ###### systolic : blood pressure.
# ###### relaxation : blood pressure.
# ###### fasting blood sugar: blood sugar before meals level
# ###### Cholesterol : total
# ###### triglyceride
# ###### HDL : cholesterol type
# ###### LDL : cholesterol type
# ###### hemoglobin
# ###### serum creatinine
# ###### AST : glutamic oxaloacetic transaminase type
# ###### ALT : glutamic oxaloacetic transaminase type
# ###### Gtp : γ-GTP
# ###### oral : Oral Examination status (s whether the examinee accepted the oral examination).
# ###### dental caries
# ###### tartar : tartar status
# ###### smoking: smoking status of a person 

# In[2]:


df=pd.read_csv("smoking.csv")
df


# In[3]:


df.info()


# In[4]:


df.isnull().sum()


# In[5]:


df.columns


# In[6]:


def sys_cat(sys_bp):
    if sys_bp>=0 and sys_bp<=90:
        return "Hypotension"
    elif sys_bp>=90 and sys_bp<=120:
        return "Normal"
    elif sys_bp>=120 and sys_bp<=130:
        return "Elevated"
    elif sys_bp>=130 and sys_bp<=140:
        return "Hypertension stage1"
    elif sys_bp>=140 and sys_bp<=150:
        return "Hypertension stage2"
    else:
        return "Hypertension crisis"
    
df['systolic_category']=df['systolic'].apply(sys_cat)


# In[7]:


def rel_cat(rel_bp):
    if rel_bp>=0 and rel_bp<=60:
        return "Hypotension"
    elif rel_bp>=60 and rel_bp<=80:
        return "Normal"
    elif rel_bp>=80 and rel_bp<=90:
        return "Elevated"
    elif rel_bp>=90 and rel_bp<=100:
        return "Hypertension stage1"
    elif rel_bp>=100 and rel_bp<=120:
        return "Hypertension stage2"
    else:
        return "Hypertension crisis"
    
df['relaxation_category']=df['relaxation'].apply(rel_cat)


# In[8]:


def diab_cat(sugar):
    if sugar>=0 and sugar<=80:
        return "Hypoglycemia"
    elif sugar>=80 and sugar<=100:
        return "Normal"
    elif sugar>=100 and sugar<=130:
        return "Pre-Diabetic"
    else:
        return "Diabetic"
    
df['diabetic_category']=df['fasting blood sugar'].apply(diab_cat)


# In[9]:


df['dental caries'] = df['dental caries'].replace({0: 'Yes', 1: 'No'})


# In[10]:


df=df.loc[:,['ID', 'smoking', 'gender', 'age', 'height(cm)', 'weight(kg)',
       'waist(cm)', 'eyesight(left)', 'eyesight(right)', 'hearing(left)',
       'hearing(right)', 'systolic','systolic_category', 'relaxation','relaxation_category','fasting blood sugar',
       'diabetic_category','Cholesterol', 'triglyceride', 'HDL', 'LDL', 'hemoglobin',
       'serum creatinine', 'AST', 'ALT', 'Gtp', 'oral', 'dental caries',
       'tartar']]
df


# In[ ]:





# In[ ]:





# # Exploratary Data Analysis

# In[11]:


df["smoking"].value_counts()


# In[12]:


df["smoking"].value_counts()


# ##### Total number of smokers and non-smokers

# In[13]:


df["smoking"].value_counts().plot.pie(shadow=True,explode=[0,0.1],autopct="%1.1f%%")
plt.title("Number of Smokers and Non-smokers")
plt.show()


# In[14]:


# only 36.7% people smoke
# 63.3% people do not smoke


# In[15]:


df["gender"].value_counts().plot.pie(shadow=True,explode=[0,0.1],autopct="%1.1f%%")
plt.title("Number of Male and Female")
plt.show()


# In[16]:


# Total 63.6% are male 
# 36.4% are female


# In[17]:


smokeYes=df[df["smoking"]=="Yes"]
smokeYes.head(2)


# In[18]:


smokeYes['gender'].value_counts()


# In[19]:


smokeYes["gender"].value_counts().plot.pie(shadow=True,explode=[0,0.1],autopct="%1.1f%%")
plt.title("Number of male and female smokers")
plt.show()


# #### Average age of male and female smokers.

# In[20]:


smokeNo=df[df["smoking"]=="No"]
#smokeNo


# In[21]:


smokeYesW=smokeYes[smokeYes["gender"]=="F"]
#smokeYesW


# In[22]:


smokeYesM=smokeYes[smokeYes["gender"]=="M"]
smokeYesM


# In[23]:


plt.figure(figsize=(8,5))

plt.subplot(1,2,1)
sns.histplot(data=smokeYesM,x='age',kde=True,bins=10)
plt.title("Average age of male smokers")

plt.subplot(1,2,2)

sns.histplot(data=smokeYesW,x='age',kde=True,bins=10)
plt.title("Average age of female smokers")



plt.tight_layout(4)
plt.show()


# In[24]:


w=sum(smokeYesW['age'])/len(smokeYesW['age'])
print('Average age of female smokers',w)


# In[25]:


m=sum(smokeYesM['age'])/len(smokeYesM['age'])
print('Average age male smokers',m)


# ##### Average height of  male and female smokers.

# In[26]:


plt.figure(figsize=(8,5))

plt.subplot(1,2,1)
sns.histplot(data=smokeYesM,x='height(cm)',kde=True,bins=10)
plt.title("Average height of male smokers")



plt.subplot(1,2,2)
sns.histplot(data=smokeYesW,x='height(cm)',kde=True,bins=10)
plt.title("Average height of female smokers")

plt.tight_layout(4)
plt.show()


# In[27]:


w=sum(smokeYesW['height(cm)'])/len(smokeYesW['height(cm)'])
print('Average height of female smokers',w)


# In[28]:


m=sum(smokeYesM['height(cm)'])/len(smokeYesM['height(cm)'])
print('Average Height of male smokers',m)


# ##### Average weight male and female smokers

# In[29]:


plt.figure(figsize=(8,5))

plt.subplot(1,2,1)
sns.histplot(data=smokeYesM,x='weight(kg)',kde=True,bins=10)
plt.title("Average weight of male smokers")

plt.subplot(1,2,2)
sns.histplot(data=smokeYesW,x='weight(kg)',kde=True,bins=10)
plt.title("Average weight of female smokers")



plt.tight_layout(4)
plt.show()


# In[30]:


w=sum(smokeYesW['weight(kg)'])/len(smokeYesW['weight(kg)'])
print('Average weight of female smokers',w)


# In[31]:


m=sum(smokeYesM['weight(kg)'])/len(smokeYesM['weight(kg)'])
print('Average weight of female smokers',m)


# In[32]:


plt.figure(figsize=(10,10))

plt.boxplot([smokeYesM['age'],smokeYesM['height(cm)'], smokeYesM['weight(kg)']], labels=['Age', 'Height', 'Weight'])
plt.title('Box Plot of Age, Height, and Weight of Male Smokers')
plt.ylabel('Count')
plt.grid(True)
plt.show()


# In[33]:


plt.figure(figsize=(10,10))

plt.boxplot([smokeYesW['age'],smokeYesW['height(cm)'], smokeYesW['weight(kg)']], labels=['Age', 'Height', 'Weight'])
plt.title('Box Plot of Age, Height, and Weight of Female Smokers')
plt.ylabel('Count')
plt.grid(True)
plt.show()


# In[34]:


smokeYes.head()


# In[35]:


plt.figure(figsize=(8,8))
plt.subplot(1,2,1)

smokeYes["hearing(left)"].value_counts().plot.pie(shadow=True,explode=[0,0.1],autopct="%1.1f%%")


plt.subplot(1,2,2)
smokeYes["hearing(right)"].value_counts().plot.pie(shadow=True,explode=[0,0.1],autopct="%1.1f%%")

plt.tight_layout(4)
plt.show()


# #### Average cholestrol level of smokers

# In[36]:


smokeYes.groupby('age').mean()['Cholesterol'].plot(ylim=(150,250),color='k',marker='o',
                                                  markerfacecolor='red',linestyle='-',linewidth=2,figsize=(5,5))
plt.xlabel('Age')
plt.ylabel("Cholestrol level")
plt.title("Average cholestrol level of smokers")
plt.grid()
plt.show()



# #### Average cholestrol level of non-smokers

# In[37]:


smokeNo.groupby('age').mean()['Cholesterol'].plot(ylim=(150,250),color='k',marker='o',
                                                  markerfacecolor='red',linestyle='-',linewidth=2,figsize=(5,5))
plt.xlabel('Age')
plt.ylabel("Cholestrol level")
plt.title("Average cholestrol level of Non-smokers")
plt.grid()


plt.show()


# In[38]:


smokeyes=df[df["smoking"]=="Yes"]
smokeyes.head(2)


# In[39]:


smokeno=df[df["smoking"]=="No"]
smokeno.head(2)


# In[40]:


plt.figure(figsize=(12,12))

counts = smokeyes['systolic_category'].value_counts()
counts1= smokeno['systolic_category'].value_counts()

percentages = (counts / counts.sum()) * 100
percentages1 = (counts1 / counts1.sum()) * 100

sorted_categories = percentages.sort_values(ascending=False).index
sorted_categories1 = percentages1.sort_values(ascending=False).index


plt.subplot(1,2,1)

plt.bar(sorted_categories, percentages[sorted_categories])

plt.xlabel('Blood Pressure Category')
plt.ylabel('Percentage')
plt.title('Systolic blood pressure categories distribution of Smokers')
plt.xticks(rotation=45)

for i, v in enumerate(percentages[sorted_categories]):
    plt.text(i, v, f'{v:.1f}%', ha='center', va='bottom')



plt.subplot(1,2,2)

plt.bar(sorted_categories1, percentages1[sorted_categories1])

plt.xlabel('Blood Pressure Category')
plt.ylabel('Percentage')
plt.title('Systolic blood pressure categories distribution of Non smokers')
plt.xticks(rotation=45)

for i, v in enumerate(percentages1[sorted_categories1]):
    plt.text(i, v, f'{v:.1f}%', ha='center', va='bottom')

plt.tight_layout()
plt.show()


# ##### Analysis of  Systoli Blood Pressure Categories Distribution of Smokers 

# In[41]:


counts = smokeyes['systolic_category'].value_counts()

percentages = (counts / counts.sum()) * 100

sorted_categories = percentages.sort_values(ascending=False).index

plt.figure(figsize=(6,6))
plt.bar(sorted_categories, percentages[sorted_categories])

plt.xlabel('Blood Pressure Category')
plt.ylabel('Percentage')
plt.title('Systolic blood pressure categories distribution of Smokers')

plt.xticks(rotation=45)

for i, v in enumerate(percentages[sorted_categories]):
    plt.text(i, v, f'{v:.1f}%', ha='center', va='bottom')

plt.tight_layout()
plt.show()


# ##### Analysis of Systolic Blood Pressure Categories Distribution of Non-smokers

# In[42]:


counts = smokeno['systolic_category'].value_counts()

percentages = (counts / counts.sum()) * 100

sorted_categories = percentages.sort_values(ascending=False).index

plt.figure(figsize=(6,6))
plt.bar(sorted_categories, percentages[sorted_categories])

plt.xlabel('Blood Pressure Category')
plt.ylabel('Percentage')
plt.title('Blood Pressure Categories Distribution of Non-smokers')

plt.xticks(rotation=45)

for i, v in enumerate(percentages[sorted_categories]):
    plt.text(i, v, f'{v:.1f}%', ha='center', va='bottom')

plt.tight_layout()
plt.show()


# In[43]:


plt.figure(figsize=(12,10))

counts = smokeyes['relaxation_category'].value_counts()
counts1= smokeno['relaxation_category'].value_counts()

percentages = (counts / counts.sum()) * 100
percentages1 = (counts1 / counts1.sum()) * 100

sorted_categories = percentages.sort_values(ascending=False).index
sorted_categories1 = percentages1.sort_values(ascending=False).index


plt.subplot(1,2,1)

plt.bar(sorted_categories, percentages[sorted_categories])

plt.xlabel('Blood Pressure Category')
plt.ylabel('Percentage')
plt.title('Relaxation blood pressure categories distribution of Smokers')
plt.xticks(rotation=45)

for i, v in enumerate(percentages[sorted_categories]):
    plt.text(i, v, f'{v:.1f}%', ha='center', va='bottom')



plt.subplot(1,2,2)

plt.bar(sorted_categories1, percentages1[sorted_categories1])

plt.xlabel('Blood Pressure Category')
plt.ylabel('Percentage')
plt.title('Relaxation blood pressure categories distribution of Non smokers')
plt.xticks(rotation=45)

for i, v in enumerate(percentages1[sorted_categories1]):
    plt.text(i, v, f'{v:.1f}%', ha='center', va='bottom')

plt.tight_layout()
plt.show()


# ##### Analysis of Relaxation Blood Pressure Categories Distribution of smokers

# In[44]:


counts = smokeyes['relaxation_category'].value_counts()

percentages = (counts / counts.sum()) * 100

sorted_categories = percentages.sort_values(ascending=False).index

plt.figure(figsize=(6,6))
plt.bar(sorted_categories, percentages[sorted_categories])

plt.xlabel('Blood Pressure Category')
plt.ylabel('Percentage')
plt.title('Blood Pressure Categories Distribution of Non-smokers')

plt.xticks(rotation=45)

for i, v in enumerate(percentages[sorted_categories]):
    plt.text(i, v, f'{v:.1f}%', ha='center', va='bottom')

plt.tight_layout()
plt.show()


# ##### Analysis of Relaxation Blood Pressure Categories Distribution of Non-smokers 

# In[45]:


counts = smokeno['relaxation_category'].value_counts()

percentages = (counts / counts.sum()) * 100

sorted_categories = percentages.sort_values(ascending=False).index

plt.figure(figsize=(6,6))
plt.bar(sorted_categories, percentages[sorted_categories])

plt.xlabel('Blood Pressure Category')
plt.ylabel('Percentage')
plt.title('Blood Pressure Categories Distribution of Non-smokers')

plt.xticks(rotation=45)

for i, v in enumerate(percentages[sorted_categories]):
    plt.text(i, v, f'{v:.1f}%', ha='center', va='bottom')

plt.tight_layout()
plt.show()


# #### Pie chart of diabetes cateogary of smokers and non-smokers

# In[46]:


plt.figure(figsize=(10,10))
plt.subplot(1,2,1)

smokeYes["diabetic_category"].value_counts().plot.pie(shadow=True,autopct="%1.1f%%")
plt.title("Diabetes cateogary of smokers")

plt.subplot(1,2,2)
smokeno["diabetic_category"].value_counts().plot.pie(shadow=True,autopct="%1.1f%%")

plt.title("Diabetes cateogary of non-smokers")
plt.tight_layout(4)
plt.show()


# In[47]:


female=df[df['gender']=='F']
femaleYes=female[female['smoking']=='Yes']
femaleNo=female[female['smoking']=='No']


# ##### Analysis of average HDL level of smoker and non-smoker different age

# In[48]:


plt.figure(figsize=(10,10))
smokeYes.groupby('age').mean()['HDL'].plot(color='k',marker='o',markerfacecolor='red',
                                               linestyle='-',linewidth=2,figsize=(5,5),label='HDL level of smokers')
smokeNo.groupby('age').mean()['HDL'].plot(color='k',marker='o',markerfacecolor='green',
                                               linestyle='-',linewidth=2,figsize=(5,5),label='HDL level of non-smokers')
plt.xlabel('Age')
plt.ylabel("HDL level")
plt.title("HDL level of smokers and Non-smokers")
plt.legend(loc='lower left')
plt.grid()
plt.show()



# ###### Analysis of average LDL level of smoker and non-smoker different age

# In[49]:


plt.figure(figsize=(10,10))
smokeYes.groupby('age').mean()['LDL'].plot(color='k',marker='o',markerfacecolor='red',
                                               linestyle='-',linewidth=2,figsize=(5,5),label='LDL level of smokers')
smokeNo.groupby('age').mean()['LDL'].plot(color='k',marker='o',markerfacecolor='green',
                                               linestyle='-',linewidth=2,figsize=(5,5),label='LDL level of non-smokers')
plt.xlabel('Age')
plt.ylabel("LDL level")
plt.title("LDL level of smokers and Non-smokers")
plt.legend(loc='lower left')
plt.grid()
plt.show()


# ##### Average ALT level of smokers and non smokers in different age.

# In[50]:


plt.figure(figsize=(10,8))

age=df['age'].unique()
altsmokers=smokeYes.groupby('age').mean()['ALT']
altnonsmokers=smokeNo.groupby('age').mean()['ALT']

fig,ax=plt.subplots()
bar_width=1.5

bar_smok_position=[x-bar_width/2 for x in age]
bar_nonsmok_position=[x+bar_width/2 for x in age]

ax.bar(bar_smok_position,altsmokers,bar_width,label='smoker')
ax.bar(bar_nonsmok_position,altnonsmokers,bar_width,label='non smoker')

ax.set_title("Average ALT level of smokers and non smokers")
ax.set_xlabel("Age")
ax.set_ylabel("ALT level")
plt.legend()

plt.show()




# ###### Average ALT level of smokers and non smokers of different age

# In[51]:


plt.figure(figsize=(10,10))

age=df['age'].unique()
astsmokers=smokeYes.groupby('age').mean()['AST']
astnonsmokers=smokeNo.groupby('age').mean()['AST']

fig,ax=plt.subplots()
bar_width=1.5

bar_smok_position=[x-bar_width/2 for x in age]
bar_nonsmok_position=[x+bar_width/2 for x in age]

ax.bar(bar_smok_position,astsmokers,bar_width,label='smoker')
ax.bar(bar_nonsmok_position,astnonsmokers,bar_width,label='non smoker')

ax.set_title("Average AST level of smokers and non smokers")
ax.set_xlabel("Age")
ax.set_ylabel("AST level")
plt.legend()

plt.show()


# In[ ]:





# # Statistical test

# In[52]:


df.columns


# ### To study the association between the smoking status and dental caries

# ##### H0: There is no association between the smoking status and fasting sugar level
# ##### H1:There is association between the smoking status and fasting sugar level

# In[53]:


crosstab=pd.crosstab(df['smoking'],df['dental caries'])
crosstab


# In[54]:


import scipy.stats as stats
stats.chi2_contingency(crosstab)


# ##### We reject null hypothesis , because p-value<0.05.Therefore there is a association between the smoking status and fasting blood sugar level.

# In[55]:


df.columns


# ### Checking whether smoking influesing on systolic blood pressure.

# In[56]:


#Checking for normality of systolic blood pressure

plt.figure(figsize=(10,4))
bp1=smokeyes["systolic"]
bp2=smokeno["systolic"]


plt.subplot(1,2,1)
sns.distplot(bp1,color='b')
plt.title("Systolic blood pressure of smokers")

plt.subplot(1,2,2)
sns.distplot(bp2,color='r')
plt.title("sysytolic blood pressure of non-smokers")

plt.show()


# ###### H0 : Smoking not influesing on systolic blood pressure of smoker
# ###### H1 : Smoking influesing on systolic blood pressure

# In[57]:


from scipy.stats import ttest_ind # t test for relaxation bp
t3=smokeyes['systolic']
t4=smokeno['systolic']
stat,p_value=ttest_ind(t3,t4)
print("statistic= ",stat)
print("p value= ",p_value)

alpha = 0.05
if p_value < alpha:
    print("Smoking influesing on systolic blood pressure")
else:
    print("Smoking not influesing on systolic blood pressure of smoker.")



# In[ ]:





# In[ ]:





# ### Checking whether smoking influesing on  relaxation blood pressure.

# In[58]:


#Checking for normality of relaxation blood pressure
plt.figure(figsize=(10,4))
bp3=smokeyes["relaxation"]
bp4=smokeno["relaxation"]


plt.subplot(1,2,1)
sns.distplot(bp3,color='b')
plt.title("Relaxation blood pressure of smokers")

plt.subplot(1,2,2)
sns.distplot(bp4,color='r')
plt.title("Relaxation blood pressure of non-smokers")

plt.show()


# ###### H0 : Smoking not influesing on relaxation blood pressure of smoker
# ###### H1 : Smoking influesing on relaxation blood pressure

# In[59]:


from scipy.stats import ttest_ind # t test for relaxation bp
t3=smokeyes['relaxation']
t4=smokeno['relaxation']
stat,p=ttest_ind(t3,t4)
print("statistic= ",stat)
print("p value= ",p)

alpha = 0.05
if p_value < alpha:
    print("Smoking influesing on systolic blood pressure")
else:
    print("Smoking not influesing on systolic blood pressure of smoker.")


# In[ ]:





# In[ ]:





# ### Study the association between the smoking status and fasting blood sugar level

# ###### H0: There is no association between the smoking status and fasting sugar level
# ###### H1:There is association between the smoking status and fasting sugar level

# In[60]:


crosstab=pd.crosstab(df['smoking'],df['diabetic_category'])
crosstab


# In[61]:


import scipy.stats as stats
stats.chi2_contingency(crosstab)


# In[ ]:





# ###### Checking whether smokers cholestrol level influencing  systolic blood pressure and relaxation blood pressure

# In[62]:


#using levene's method to test the whether variance of group are equal.


# In[63]:


#levenes test for systolic blood pressure
from scipy.stats import levene

bp1=smokeyes['Cholesterol'][df['systolic_category']=='Hypotension']
bp2=smokeyes['Cholesterol'][df['systolic_category']=='Normal']
bp3=smokeyes['Cholesterol'][df['systolic_category']=='Elevated']
bp4=smokeyes['Cholesterol'][df['systolic_category']=='Hypertension stage1']
bp5=smokeyes['Cholesterol'][df['systolic_category']=='Hypertension stage2']
bp6=smokeyes['Cholesterol'][df['systolic_category']=='Hypertension crisis']


statistic, p_value = levene(bp1,bp2,bp3,bp4,bp5,bp6)


alpha = 0.05 

print('Statistic :',statistic)
print('P-value : ',p_value)

if p_value < alpha:
    print("The variances are significantly different (reject the null hypothesis of equal variances).")
else:
    print("The variances are not significantly different (fail to reject the null hypothesis of equal variances).")


# In[64]:


# levene's test for relaxation blood pressure

bp1=smokeyes['Cholesterol'][df['relaxation_category']=='Hypotension']
bp2=smokeyes['Cholesterol'][df['relaxation_category']=='Normal']
bp3=smokeyes['Cholesterol'][df['relaxation_category']=='Elevated']
bp4=smokeyes['Cholesterol'][df['relaxation_category']=='Hypertension stage1']
bp5=smokeyes['Cholesterol'][df['relaxation_category']=='Hypertension stage2']
bp6=smokeyes['Cholesterol'][df['relaxation_category']=='Hypertension crisis']


statistic, p_value = levene(bp1,bp2,bp3,bp4,bp5,bp6)


alpha = 0.05 

print('Statistic :',statistic)
print('P-value : ',p_value)

if p_value < alpha:
    print("The variances are significantly different (reject the null hypothesis of equal variances).")
else:
    print("The variances are not significantly different (fail to reject the null hypothesis of equal variances).")


# #### Using kruskal-wallis test checking whether smokers cholestrol level influencing systolic blood pressure 

# #### Ho: cholestrol level do not influencing systolic blood pressure 
# #### H1: cholestrol level influencing systolic blood pressure 

# In[65]:


import scipy.stats as stats

bp1=smokeyes['Cholesterol'][df['systolic_category']=='Hypotension']
bp2=smokeyes['Cholesterol'][df['systolic_category']=='Normal']
bp3=smokeyes['Cholesterol'][df['systolic_category']=='Elevated']
bp4=smokeyes['Cholesterol'][df['systolic_category']=='Hypertension stage1']
bp5=smokeyes['Cholesterol'][df['systolic_category']=='Hypertension stage2']
bp6=smokeyes['Cholesterol'][df['systolic_category']=='Hypertension crisis']

# Perform the Kruskal-Wallis test
statistic, p_value = stats.kruskal(bp1,bp2,bp3,bp4,bp5,bp6)


print("Kruskal-Wallis Test")
print("Statistic:", statistic)
print("P-value:", p_value)

# Check the significance level and draw conclusions
alpha = 0.05
if p_value < alpha:
    print("There is a significant difference between the groups.")
else:
    print("There is no significant difference between the groups.")


# In[ ]:





# In[ ]:





# ### Checking whether smokers cholestrol level influencing relaxation blood pressure 

# #### Ho: cholestrol level do not influencing systolic blood pressure 
# #### H1: cholestrol level influencing systolic blood pressure 

# In[66]:


bp1=smokeyes['Cholesterol'][df['relaxation_category']=='Hypotension']
bp2=smokeyes['Cholesterol'][df['relaxation_category']=='Normal']
bp3=smokeyes['Cholesterol'][df['relaxation_category']=='Elevated']
bp4=smokeyes['Cholesterol'][df['relaxation_category']=='Hypertension stage1']
bp5=smokeyes['Cholesterol'][df['relaxation_category']=='Hypertension stage2']
bp6=smokeyes['Cholesterol'][df['relaxation_category']=='Hypertension crisis']

# Perform the Kruskal-Wallis test
statistic, p_value = stats.kruskal(bp1,bp2,bp3,bp4,bp5,bp6)


print("Kruskal-Wallis Test")
print("Statistic:", statistic)
print("P-value:", p_value)

# Check the significance level and draw conclusions
alpha = 0.05
if p_value < alpha:
    print("There is a significant difference between the groups.")
else:
    print("There is no significant difference between the groups.")


# In[67]:


df['diabetic_category'].unique()


# #### Checking whether smokers diabetic level influencing  on  serum creatinine

# In[68]:


# levene's test for relaxation blood pressure

from scipy.stats import levene

sc1=smokeyes['serum creatinine'][df['diabetic_category']=='Hypoglycemia']
sc2=smokeyes['serum creatinine'][df['diabetic_category']=='Normal']
sc3=smokeyes['serum creatinine'][df['diabetic_category']=='Pre-Diabetic']
sc4=smokeyes['serum creatinine'][df['diabetic_category']=='Diabetic']



statistic, p_value = levene(sc1,sc2,sc3,sc4)


alpha = 0.05 

print('Statistic :',statistic)
print('P-value : ',p_value)

if p_value < alpha:
    print("The variances are significantly different (reject the null hypothesis of equal variances).")
else:
    print("The variances are not significantly different (fail to reject the null hypothesis of equal variances).")


# #### Kruskal-Wallis Test for checking whether smokers diabetic level influencing on serum creatine. 

# In[69]:


from scipy.stats import kruskal

sc1=smokeyes['serum creatinine'][df['diabetic_category']=='Hypoglycemia']
sc2=smokeyes['serum creatinine'][df['diabetic_category']=='Normal']
sc3=smokeyes['serum creatinine'][df['diabetic_category']=='Pre-Diabetic']
sc4=smokeyes['serum creatinine'][df['diabetic_category']=='Diabetic']



statistic, p_value = kruskal(sc1,sc2,sc3,sc4)

print("Kruskal-Wallis Test")
print("Statistic:", statistic)
print("P-value:", p_value)

# Check the significance level and draw conclusions
alpha = 0.05
if p_value < alpha:
    print("There is a significant difference between serum creatinine of smokers  .")
else:
    print("There is no significant difference between serum creatinine of smokers.")



# In[ ]:





# In[ ]:





# In[70]:


#Model building


# In[71]:


df.head(3)


# In[72]:


plt.figure(figsize=(40,40))
sns.heatmap(df.corr(),annot=True,cmap='RdYlGn',annot_kws={'size':15})


# In[73]:


from sklearn.metrics import classification_report,PrecisionRecallDisplay,RocCurveDisplay,accuracy_score,f1_score
from sklearn.metrics import precision_score,recall_score,f1_score


# In[74]:


from sklearn.preprocessing import LabelEncoder
for column in df.columns:
    if df[column].dtype==np.number:
        continue
    else:
        df[column]=LabelEncoder().fit_transform(df[column])


# In[75]:


df.columns


# In[76]:


x=df.drop(columns=['ID','eyesight(left)','eyesight(right)','hearing(left)','hearing(right)','fasting blood sugar','diabetic_category'])
y=df['diabetic_category']


# In[77]:


from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.20,random_state=1)


# ##### LogisticRegression

# In[78]:


from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(xtrain,ytrain)


# In[79]:


ypred1=model.predict(xtest)


# In[80]:


from sklearn.metrics import accuracy_score
print("Test Accuracy: ",accuracy_score(ytest,ypred1))
print("Precision: ",precision_score(ytest,ypred1,average='weighted'))


# In[81]:


ypredd=model.predict(xtrain)


# In[82]:


from sklearn.metrics import accuracy_score
print("Train Accuracy: ",accuracy_score(ytrain,ypredd))


# In[83]:


from sklearn.metrics import classification_report
print(classification_report(ytest,ypred1))


# In[84]:


print()


# #### KNN

# In[85]:


from sklearn.neighbors import KNeighborsClassifier 
from sklearn.metrics import f1_score


# In[86]:


clf=KNeighborsClassifier(n_neighbors=5)
clf.fit(xtrain,ytrain)
ypred2=clf.predict(xtest)


# In[87]:


from sklearn.metrics import accuracy_score
print("Test Accuracy: ",accuracy_score(ytest,ypred2))


# In[88]:


ypredd2=clf.predict(xtrain)


# In[89]:


from sklearn.metrics import accuracy_score
print("Train Accuracy: ",accuracy_score(ytrain,ypredd2))


# In[90]:


print(classification_report(ytest,ypred2))


# In[ ]:





# In[91]:


from sklearn.neighbors import KNeighborsClassifier
def elbow(k):
    test_error=[]
    for i in k:
        clf=KNeighborsClassifier(n_neighbors=i)
        clf.fit(xtrain,ytrain)
        tmp=clf.predict(xtest)
        tmp=f1_score(ytest,tmp,average='micro')
        error=1-tmp
        test_error.append(error)
    return test_error


# In[92]:


k=range(6,20)
test=elbow(k)
print(test)


# In[93]:


plt.plot(k,test)
plt.xlabel("K Neighbors")
plt.ylabel("test_error")
plt.title("Elbow curve for test")


# In[94]:


knn=KNeighborsClassifier(n_neighbors=16)
knn.fit(xtrain,ytrain)


# In[95]:


ytrain_prdct=knn.predict(xtrain)
ytest_prdct=knn.predict(xtest)


# In[96]:


print("Test Accuracy :",accuracy_score(ytest_prdct,ytest))
print("Train Accuracy :",accuracy_score(ytrain_prdct,ytrain))


# In[ ]:





# ###### Naive Bayesian Classification

# In[97]:


from sklearn.naive_bayes import GaussianNB
gnb=GaussianNB()
gnb.fit(xtrain,ytrain)


# In[98]:


ypred3=gnb.predict(xtest)
ypredd3=gnb.predict(xtrain)


# In[99]:


from sklearn.metrics import accuracy_score
print("Test Accuracy: ",accuracy_score(ytest,ypred3))
print("Train Accuracy: ",accuracy_score(ytrain,ypredd3))


# In[100]:


print(classification_report(ytest,ypred3))


# ##### RandomForest and DecisionTreeClassifier

# In[101]:


from sklearn.tree import DecisionTreeClassifier
dtree=DecisionTreeClassifier()
dtree.fit(xtrain,ytrain)


# In[102]:


ypred4=dtree.predict(xtest)
ypredd4=dtree.predict(xtrain)


# In[103]:


print("Test Accuracy: ",accuracy_score(ytest,ypred4))
print("Train Accuracy: ",accuracy_score(ytrain,ypredd4))


# In[104]:


print(classification_report(ytest,ypred4))


# ##### Random Forest

# In[105]:


from sklearn.ensemble import RandomForestClassifier
rf=RandomForestClassifier()
rf.fit(xtrain,ytrain)


# In[106]:


ypred5=rf.predict(xtest)
ypredd5=rf.predict(xtrain)


# In[107]:


print("Test Accuracy: ",accuracy_score(ytest,ypred5))
print("Train Accuracy: ",accuracy_score(ytrain,ypredd5))


# In[108]:


# hyperparameter tuning


# # GridSearchCV

# In[110]:


from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV


# In[111]:


param_grid = {
    'n_estimators': [25, 50, 100, 150],
    'max_features': ['sqrt', 'log2', None],
    'max_depth': [3, 6, 9],
    'max_leaf_nodes': [3, 6, 9],
}


# In[113]:


grid_search = GridSearchCV(RandomForestClassifier(),
                           param_grid=param_grid)
grid_search.fit(xtrain, ytrain)
print(grid_search.best_estimator_)


# In[114]:


model_grid = RandomForestClassifier(max_depth=9,
                                    max_features=None,
                                    max_leaf_nodes=9,
                                    n_estimators=150)
model_grid.fit(xtrain, ytrain)
y_pred_grid = model.predict(xtest)
print(classification_report(y_pred_grid, ytest))


# In[116]:


print("Test Accuracy: ",accuracy_score(y_pred_grid, ytest))


# In[118]:


ytrain_pred_grid = model.predict(xtrain)
print("Train Accuracy",accuracy_score(ytrain_pred_grid, ytrain))


# In[119]:


# Randomizedsearch


# In[125]:


param_grid = {
    'n_estimators': [25, 50, 100, 150],
    'max_features': ['sqrt', 'log2', None],
    'max_depth': [9, 12, 15],
    'max_leaf_nodes': [9, 12, 15],
}


# In[126]:


random_search = RandomizedSearchCV(RandomForestClassifier(),
                                   param_grid)
random_search.fit(xtrain, ytrain)
print(random_search.best_estimator_)


# In[128]:


model_random = RandomForestClassifier(max_depth=15,
                                      max_features=None,
                                      max_leaf_nodes=15,
                                      n_estimators=25)
model_random.fit(xtrain, ytrain)
ytest_pred_rand1 = model.predict(xtest)
ytrain_pred_rand1=model.predict(xtrain)
print("Test Accuracy :",accuracy_score(ytest_pred_rand1, ytest))
print("Train Accuracy :",accuracy_score(ytrain_pred_rand1,ytrain))


# # Xgboost

# In[ ]:


params={
    'objective':'multi:softmax',
    'num_class':len(set(y)),
    'max_depth':3,
    'learning_rate':0.1,
    'n_estimators':100
}


# In[134]:


get_ipython().system('pip install xgboost')


# In[135]:


import xgboost as xgb


# In[137]:


model=xgb.XGBClassifier()

model.fit(xtrain,ytrain)
ytest_pred=model.predict(xtest)
ytrain_pred=model.predict(xtrain)

print("Test ACcuracy: ",accuracy_score(ytest_pred,ytest))
print("Train Accuracy: ",accuracy_score(ytrain_pred,ytrain))


# In[ ]:





# In[138]:


booster=['gbtree','gblinear']
base_score=[0.25,0.5,0.75,1]
n_estimators = [100, 500, 900, 1100, 1500]
max_depth = [2, 3, 5, 10, 15]
booster=['gbtree','gblinear']
learning_rate=[0.05,0.1,0.15,0.20]
min_child_weight=[1,2,3,4]

# Define the grid of hyperparameters to search
hyperparameter_grid = {
    'n_estimators': n_estimators,
    'max_depth':max_depth,
    'learning_rate':learning_rate,
    'min_child_weight':min_child_weight,
    'booster':booster,
    'base_score':base_score
    }


# In[140]:


random_cv = RandomizedSearchCV(estimator=xgb.XGBClassifier(),
            param_distributions=hyperparameter_grid,
            cv=5, n_iter=50,
            scoring = 'neg_mean_absolute_error',n_jobs = 4,
            verbose = 5, 
            return_train_score = True,
            random_state=42)


# In[ ]:


random_cv.fit(xtrain,ytrain)

random_cv.best_estimator_


# In[ ]:





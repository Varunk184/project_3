#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import numpy as np
import pandas as pd


# In[2]:


os.chdir('C:\\Users\\varun\\OneDrive\\Desktop\\python\\proj_2')


# In[3]:


survey_raw_df = pd.read_csv('survey_results_public.csv')


# In[4]:


survey_raw_df


# In[15]:


survey_raw_df.columns


# In[9]:


schema_fname='survey_results_schema.csv'
schema_raw=pd.read_csv(schema_fname,index_col='Column').QuestionText


# In[11]:


schema_raw


# In[12]:


schema_raw['YearsCodePro']


# In[25]:


selected_columns=[
    'Country',
    'Age',
    'Gender',
    'EdLevel',
    'UndergradMajor',
    'Hobbyist',
    'Age1stCode',
    'YearsCode',
    'YearsCodePro',
    'LanguageWorkedWith',
    'LanguageDesireNextYear',
    'NEWLearn',
    'NEWStuck',
    'Employment',
    'DevType',
    'WorkWeekHrs',
    'JobSat',
    'JobFactors',
    'NEWOvertime',
    'NEWEdImpt'
]


# In[26]:


len(selected_columns)


# In[27]:


survey_df=survey_raw_df[selected_columns].copy()


# In[28]:


schema = schema_raw[selected_columns]


# In[31]:


survey_df.shape


# In[38]:


survey_df.info()


# In[36]:


survey_df['Age1stCode']=pd.to_numeric(survey_df.Age1stCode,errors='coerce')
survey_df['YearsCode']=pd.to_numeric(survey_df.YearsCode,errors='coerce')
survey_df['YearsCodePro']=pd.to_numeric(survey_df.YearsCodePro,errors='coerce')


# In[37]:


survey_df.describe()


# In[41]:


survey_df.drop(survey_df[survey_df.Age<10].index,inplace=True)
survey_df.drop(survey_df[survey_df.Age>100].index,inplace = True)


# In[42]:


survey_df.drop(survey_df[survey_df.WorkWeekHrs>140].index,inplace=True)


# In[44]:


survey_df['Gender'].value_counts()


# In[45]:


survey_df.sample(10)


# In[95]:


import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

sns.set_style('darkgrid')
sns.set(rc={'figure.figsize':(12,5)})


# In[96]:


survey_df.Country.nunique()


# In[97]:



top_countries=survey_df.Country.value_counts().head(15)
top_countries


# In[98]:


plt.title('Count of Coders in TOP-15 Countries')
sns.set(rc={'figure.figsize':(12,6)})
plt.xticks(rotation=75)
sns.barplot(top_countries.index,top_countries)
plt.show()


# In[99]:


sns.set(rc={'figure.figsize':(12,6)})
plt.xlabel('Age')
#plt.ylabel('Number of respondents')
plt.hist(survey_df['Age'],bins=np.arange(10,80,5),color='purple');


# In[100]:


gender_counts=survey_df.Gender.value_counts()
gender_counts


# In[101]:


plt.figure(figsize=(12,6))
plt.title(schema.Gender)
plt.pie(gender_counts,labels=gender_counts.index,autopct='1.1f%%');


# In[102]:


schema.EdLevel


# In[103]:


survey_df.EdLevel.unique()


# In[104]:


sns.countplot(y=survey_df['EdLevel'])
plt.xticks(rotation=75);
plt.title(schema['EdLevel']);


# In[110]:


udg=survey_df.UndergradMajor
sns.barplot(udg,udg.index)
plt.xticks(rotation=90)


# In[111]:


schema.Employment


# In[112]:


survey_df.Employment.unique()


# In[118]:


a=(survey_df.Employment.value_counts(normalize=True,ascending=True)*100)
sns.barplot(a,a.index);


# In[120]:


survey_df.LanguageWorkedWith


# In[ ]:





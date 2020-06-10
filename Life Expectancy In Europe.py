#!/usr/bin/env python
# coding: utf-8

# In[263]:


import pandas as pd
import matplotlib.pyplot  as plt


# In[264]:


#Importing the csv file

life = pd.read_csv('life_expectancy.csv')


# In[265]:


# Removing the Country Germany (until 1990 former territory of the FRG) as the country does not currently exist in this form.

life = life[life.Country != 'Germany (until 1990 former territory of the FRG)']

#Checking the data to make sure the name has been removed

life


# In[266]:


#Summary statistics for the dataset

life.describe()


# In[ ]:





# In[267]:


# The variables Life_Exp and Work_Hours have been imputing with incorrect decimal so we divide these values by 10 to fix this!

life['Life_Exp'] = life['Life_Exp'] / 10
life['Work_hours'] = life['Work_hours'] / 10


# In[285]:


#Filtering the five countries with the highest life expectancy
life_large.sort_values('Life_Exp', ascending=False, inplace=True)

life.nlargest(5,'Life_Exp')
life_large = life.nlargest(5,'Life_Exp')
life_large


# In[286]:


#Filtering the five countries with the lowest life expectancy
life_small.sort_values('Life_Exp', ascending=False, inplace=True)

life.nsmallest(5,'Life_Exp')
life_small = life.nsmallest(5,'Life_Exp')
life_small


# In[351]:


#Boxplot of the Life Expectancy in Europe. We see also from the boxplot that the median value 
#is around 81 despite that the mean is much loweer to 79.5.

plt.figure(figsize = (4,6))
labels= ['Life Expectancy']
plt.boxplot(life.Life_Exp, labels=labels)

plt.style.use('ggplot')
plt.title('Boxplot of Life Expectancy in Europe')

plt.show()


# In[271]:


#The histogram of the life expectancy, the dashed black line represents the mean value/

plt.style.use('default')

# Since there were some gaps between the default histogram, the below bins have been created to present it in a more elegant way.
bins = [74,75,76,77,78,80,81,82,83]
mean = 79.5
plt.hist(life.Life_Exp, color='b', bins=bins)
plt.axvline(mean, color='k', linestyle='dashed', linewidth=2, label='mean')
plt.title('Histogram of Life Expectancy')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

plt.show()


# In[343]:


#Plotting the countries with the lowest and highest life expectancy in Europe.
#It is observed that countries from the Eastern part of Europe show lower life expectancy.

plt.style.use('ggplot')
plt.xlim((72,85))
mean = 79.5
plt.scatter(life_small.Life_Exp, life_small.Country,s=60)
plt.scatter(life_large.Life_Exp, life_large.Country,s=60)
plt.axvline(mean, color='k', linestyle='dashed', linewidth=2, label='mean')
plt.title('Highest and Lowest Life Expectancy in Europe')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)


# In[273]:


#The histrograms of Crime and Working Hours observe a normal distribution. 
#The histrogram of working hours shows that there is/are some countries where the average working hours are around50.

plt.style.use('ggplot')

fig, axs = plt.subplots(1,2)

bins_crime = [40,80,120,160,200,240,280]
crime = life['Crime'].hist(ax=axs[0], bins=bins_crime)
crime.set_title("Histogram of Crime")
crime.legend()

plt.xticks(bins_crime)

bins_work = [30,32,34,36,38,40,42,44,50]
work = life['Work_hours'].hist(ax=axs[1],bins=bins_work)
work.set_title("Histogram of Working Hours")
work.legend()
plt.xticks(bins_work)

plt.show()


# In[274]:


# Filtering the five countries with the higher rate of working hours. 
#Taking into consideration that Turkey does not belong in the European Union, Greece is the country wth the highest rate.

life.nlargest(5,'Work_hours')
life_work = life.nlargest(5,'Work_hours')
life_work


# In[275]:


# Filtering the five countries with the lower rate of working hours. 

life.nsmallest(5,'Work_hours')
life_work_small = life.nsmallest(5,'Work_hours')
life_work_small


# In[291]:


plt.style.use('ggplot')
mean = 38.3
plt.scatter(life_work.Work_hours, life_work.Country)
plt.scatter(life_work_small.Work_hours, life_work_small.Country)
plt.axvline(mean,color='k', linestyle='dashed', linewidth=2, label='mean')
plt.title('Working Hours in Europe(per week)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)


# In[371]:


plt.style.use('ggplot')
mean = 144
plt.scatter(life.Pollution, life.Life_Exp)
plt.axvline(mean, color='b', linestyle='dashed', linewidth=1.5, label='mean')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.title('Pollution Compared to Life Expectancy')
plt.ylabel('Life Expectancy')
plt.xlabel('Pollution Rate')


# In[200]:


plt.style.use('ggplot')

mean = 38.2

plt.scatter(life.Work_hours, life.Life_Exp)
plt.axvline(mean, color='b', linestyle='dashed', linewidth=1.5, label='mean')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.title('Working Hours Compared to Life Expectancy')
plt.ylabel('Work Hours')
plt.xlabel('Life Expectancy')


# In[198]:


plt.style.use('ggplot')
fig.set_size_inches(10, 5)
plt.figure(figsize=(10,12))

life.sort_values('Life_Exp', ascending=True, inplace=True)

plt.scatter(life.Life_Exp, life.Country)
plt.xlabel('Life Expectancy')
plt.title('Life Expectancy in Europe')


# In[349]:


fig, axs = plt.subplots(2)

fig.suptitle('Higher and Lower Working Hours (per week)')

df = axs[0].scatter(life_work.Work_hours, life_work.Country)
nf = axs[1].scatter(life_work_small.Work_hours, life_work_small.Country)


# In[368]:



boxplot = life.boxplot(column=[ 'Unemployment', 'Crime', 'Savings', 'Pollution'])


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# ## Scraping Data from a Real Website + Pandas
# 
# 

# In[14]:


from bs4 import BeautifulSoup
import requests


# In[16]:


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')


# In[17]:


print(soup)


# In[18]:


soup.find('table')


# In[20]:


soup.find_all('table')[1]


# In[23]:


soup.find_all('table', class_ = 'wikitable sortable')



# In[24]:


table = soup.find_all('table')[1]


# In[25]:


print(table)


# In[32]:


world_titles = table.find_all('th')


# In[33]:


world_titles


# In[34]:


world_table_titles = [title.text.strip() for title in world_titles]
print(world_table_titles )


# In[35]:


import pandas as pd


# In[36]:


df = pd.DataFrame(columns = world_table_titles)
df


# In[38]:


column_data = table.find_all('tr')


# In[49]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data


# In[50]:


df


# In[54]:


df.to_csv(r'C:\Users\USER\OneDrive\Desktop\Python Web Scraping\Folder for output\companies.csv', index = False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





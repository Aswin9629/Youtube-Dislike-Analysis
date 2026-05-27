#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


# In[5]:


df = pd.read_csv('youtube_dislike_dataset[1].csv')
df


# In[6]:


df.head(1)


# In[44]:


df.tail(3)


# In[6]:


df.info()


# In[7]:


df.shape


# In[8]:


null_values = df.isnull().sum()
null_values


# In[41]:


df = df.dropna()


# In[42]:


null_values = df.isnull().sum()
null_values


# In[12]:


df.describe()


# ####  Converting the datatype of column published_at from object to pandas datetime.

# In[7]:


df['published_at'] = pd.to_datetime(df['published_at'])


# In[8]:


df.dtypes


# ####  Creating a new column as 'published_month' using the column published_at (display the months only)

# In[9]:


df['published_month'] = df['published_at'].dt.month


# In[10]:


df['published_month'].head(5)


# ####  Replacing the numbers in the column published_month as names of the months i,e., 1 as 'Jan', 2 as 'Feb' and follows

# In[11]:


months = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
df['published_month'] = df['published_month'].map(months)
df


# ####  Finding the number of videos published each month 
# 

# In[14]:


videos_per_month = df['published_month'].value_counts()
print(videos_per_month)


# In[13]:


df['video_id'].nunique()


# In[38]:


df['channel_id'].nunique()


# In[39]:


df['channel_title'].nunique()


# #### Finding the top10 channel names having the highest number of videos in the dataset and the last10 having lowest number of videos.
# 

# In[20]:


#the rank() function assigns ranks to each unique value based on their count.
#using the 'dense' method this ensures that if there are multiple values with the same count, they will receive the same rank and the next unique value will be assigned the next consecutive rank without leaving gaps. 
channel_names = df['channel_title'].value_counts().rank(method = 'dense',ascending = False).sort_values()
channel_names


# In[44]:


#Top 10 channels 
Top_10 = pd.DataFrame(
    df.groupby('channel_title')['video_id'].count().sort_values(
    ascending=False))
Top_10[:10]


# In[22]:


#last 10
last_10 = pd.DataFrame(df.groupby('channel_title')['video_id'].count().sort_values(ascending=False).tail(10))
last_10[0:10]


# ####  Finding the title of the video which has the maximum number of likes and the video having minimum likes 

# In[28]:


max_likes = df.groupby(by = ['title']).max()[['likes']].sort_values(by = 'likes',ascending = False)
max_likes.iloc[[0]]


# In[31]:


min_likes = df.groupby(by = ['title']).max()[['likes']].sort_values(by = 'likes')
min_likes.iloc[[0]]


# #### Finding the title of the video which has the maximum number of dislikes and the video having minimum dislikes

# In[32]:


max_dislike = df.groupby(by = 'title').max()[['dislikes']].sort_values(by = 'dislikes', ascending = False)

max_dislike.iloc[[0]]


# In[33]:


#min_dislikes
min_dislike = df.groupby(by = 'title').max()[['dislikes']].sort_values(by = 'dislikes')

min_dislike.iloc[[0]]


# #### Seeing that  the number of views have any effect on how many people disliked the video

# In[34]:


x = df['view_count']
y = df['dislikes']
plt.scatter(x,y, c= 'orange' ,edgecolor = 'black', marker = '^',cmap = 'viridis',alpha = 0.2)
plt.xlabel('View_count')
plt.ylabel('dislikes')
plt.title('Effect of views on dislikes')
plt.show()


# # Inference:
# ###### The scatter plot shows the relationship between the number of views (on the x-axis) and the number of dislikes (on the y-axis) for a set of YouTube videos. 
# 
# ##### There is a weak positive correlation between the two variables, meaning that videos with more views tend to have more dislikes. However, there are many outliers, which means that there is not a strong relationship between the two variables.*
# 
# ####   *It is important to note that the scatter plot only shows the correlation between two variables. It does not mean that more views causes more dislikes. There may be other factors that explain the relationship between the two variables.*

# In[46]:


plt.figure(figsize=(8, 6))
plt.scatter(df['view_count'], df['comment_count'], alpha=0.5)
plt.title('Relationship between Views and Comments')
plt.xlabel('View Count')
plt.ylabel('Comment Count')
plt.show()


# In[49]:


import seaborn as sns
# Calculate correlation matrix
correlation_matrix = df[['view_count', 'likes', 'dislikes', 'comment_count']].corr()

# Plotting the heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()


# In[52]:


# Line plot for 'view_count' over time
plt.figure(figsize=(10, 6))
plt.plot(df['published_at'], df['view_count'])
plt.title('Views Over Time')
plt.xlabel('Published Date')
plt.ylabel('View Count')
plt.xticks(rotation=45)
plt.show()


# In[69]:


published_in_sep = df[df['published_month'] == "Sep"]
published_in_sep


# In[70]:


videos_per_month = videos_per_month.to_frame().T
videos_per_month['Sep']


# #### Performing LinearRegression to find the accuracy of the model

# In[18]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score, accuracy_score

features = ['likes', 'dislikes', 'comment_count']  

X = df[features]
y = df['view_count']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)


# In[21]:


predictions = model.predict(X_test)

mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)
print("Mean Squared Error:", mse)
print("R-squared Score:", r2)


# In[57]:


import sqlite3
data=pd.read_csv("youtube_dislike_dataset[1].csv")
df=pd.DataFrame(data)


# In[58]:


conn=sqlite3.connect("youtube_dislike_dataset[1].db")


# In[60]:


df.to_sql('youtube',con=conn,index=True,if_exists='replace')


# In[71]:


import sqlite3

conn = sqlite3.connect("youtube_dislike_dataset[1].db")

cursor = conn.cursor()

cursor.execute("SELECT * FROM youtube")

rows = cursor.fetchall()

for row in rows:
    print(row)
cursor.close()
conn.close()


# In[73]:


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

class PredictiveModel:
    def __init__(self, data, features, target):
        self.data = data
        self.features = features
        self.target = target
        self.X = self.data[self.features]
        self.y = self.data[self.target]
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)
        self.model = LinearRegression()

    def train_model(self):
        self.model.fit(self.X_train, self.y_train)

    def test_model(self):
        predictions = self.model.predict(self.X_test)
        mse = mean_squared_error(self.y_test, predictions)
        r2 = r2_score(self.y_test, predictions)
        print("Mean Squared Error:", mse)
        print(f"R-squared Score: {r2}")
        return mse, r2

    def test_with_new_samples(self, new_samples):
        new_X = new_samples[self.features]
        new_y = new_samples[self.target]
        new_predictions = self.model.predict(new_X)
        new_mse = mean_squared_error(new_y, new_predictions)
        new_r2 = r2_score(new_y, new_predictions)
        print("New Samples Mean Squared Error:", new_mse)
        print(f"New Samples R-squared Score: {new_r2}")
        return new_mse, new_r2

features = ['likes', 'dislikes', 'comment_count']
target = 'view_count'

# Initialize the predictive model
model_instance = PredictiveModel(df, features, target)

# Train the model
model_instance.train_model()

# Test the model on the test set
test_mse, test_r2 = model_instance.test_model()

#Testing with new samples
new_samples_mse, new_samples_r2 = model_instance.test_with_new_samples(df)


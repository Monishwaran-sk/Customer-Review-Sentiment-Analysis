#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Load the dataset
df = pd.read_csv("Reviews.csv")

# Display basic information
print(df.info())
print(df.head())


# In[ ]:





# In[2]:


import os
print(os.getcwd())


# In[3]:


import os
print("Reviews.csv" in os.listdir())


# In[4]:


import os
print("Reviews.csv" in os.listdir())import pandas as pd

# Load the dataset
df = pd.read_csv("Reviews.csv")

# Display basic information about the dataset
print(df.info())
print(df.head())



# In[5]:


import os
print(os.listdir())


# In[6]:


import os
print("Reviews.csv" in os.listdir())


# In[7]:


import os
print("Reviews.csv.zip" in os.listdir())


# In[10]:


import pandas as pd

# Load the dataset
df = pd.read_csv("Reviews.csv.zip")

# Display basic information about the dataset
print(df.info())
print(df.head())


# In[11]:


# Remove duplicate reviews
df.drop_duplicates(subset=['Text'], inplace=True)

# Remove missing values in the 'Text' column
df.dropna(subset=['Text'], inplace=True)

# Convert timestamp to a readable date
df['Time'] = pd.to_datetime(df['Time'], unit='s')

# Keep only necessary columns
df = df[['ProductId', 'Score', 'Time', 'Summary', 'Text']]

# Show dataset after cleaning
print(df.head())


# In[12]:


# Function to classify sentiment based on Score
def classify_sentiment(score):
    if score >= 4:
        return "Positive"
    elif score == 3:
        return "Neutral"
    else:
        return "Negative"

# Apply the function to create a new Sentiment column
df["Sentiment"] = df["Score"].apply(classify_sentiment)

# Display count of each sentiment
print(df["Sentiment"].value_counts())

# Show updated dataset
print(df.head())


# In[13]:


pip install textblob


# In[14]:


from textblob import TextBlob

# Function to analyze sentiment using NLP
def analyze_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity == 0:
        return "Neutral"
    else:
        return "Negative"

# Apply NLP-based sentiment analysis
df["NLP_Sentiment"] = df["Text"].apply(analyze_sentiment)

# Show updated dataset with both methods
print(df.head())


# In[15]:


import seaborn as sns
import matplotlib.pyplot as plt

# Compare the two sentiment analysis methods
sns.countplot(data=df, x="Sentiment", palette="coolwarm")
plt.title("Sentiment Distribution (Based on Score)")
plt.show()

sns.countplot(data=df, x="NLP_Sentiment", palette="coolwarm")
plt.title("Sentiment Distribution (Based on NLP)")
plt.show()


# In[16]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[20]:


# Set the style of the plots
sns.set_style("whitegrid")

# Plot sentiment distribution (based on Score)
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="Sentiment", palette="coolwarm")
plt.title("Sentiment Distribution (Based on Score)")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.show()


# In[ ]:





# In[21]:


print(df["Sentiment"].value_counts())


# In[22]:


def classify_sentiment(score):
    if score >= 4:
        return "Positive"
    elif score == 3:
        return "Neutral"
    else:
        return "Negative"

df["Sentiment"] = df["Score"].apply(classify_sentiment)


# In[23]:


print(df["Sentiment"].value_counts())


# In[ ]:





# In[ ]:





# In[24]:


# Function to classify sentiment based on Score
def classify_sentiment(score):
    if score >= 4:
        return "Positive"
    elif score == 3:
        return "Neutral"
    else:
        return "Negative"

# Apply function to create Sentiment column
df["Sentiment"] = df["Score"].apply(classify_sentiment)

# Check if classification worked
print(df["Sentiment"].value_counts())


# In[25]:


print(df.head())  # Check if 'Sentiment' column is there


# In[26]:


import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

plt.figure(figsize=(8, 5))
ax = sns.countplot(data=df, x="Sentiment", palette="coolwarm")

# Show count values on bars
for p in ax.patches:
    ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2, p.get_height()), 
                ha='center', va='bottom', fontsize=12, color='black')

plt.title("Sentiment Distribution (Based on Score)")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.show()


# In[27]:


import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

plt.figure(figsize=(8, 5))
ax = sns.countplot(data=df, x="Sentiment", hue="Sentiment", palette="coolwarm", legend=False)  # <-- Updated!

# Show count values on bars
for p in ax.patches:
    ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2, p.get_height()), 
                ha='center', va='bottom', fontsize=12, color='black')

plt.title("Sentiment Distribution (Based on Score)")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.show()


# In[28]:


# Convert 'Time' column to datetime format (if not already)
df["Time"] = pd.to_datetime(df["Time"], unit="s")  # Amazon dataset uses UNIX timestamp

# Group by Date and Sentiment
df_time = df.groupby([df["Time"].dt.date, "Sentiment"]).size().unstack()

# Plot sentiment trends over time
plt.figure(figsize=(12, 6))
df_time.plot(kind="line", marker="o", figsize=(12,6), colormap="coolwarm")

plt.title("Sentiment Trends Over Time")
plt.xlabel("Date")
plt.ylabel("Number of Reviews")
plt.legend(title="Sentiment")
plt.show()


# In[29]:


# Get top 10 most reviewed products
top_products = df["ProductId"].value_counts().head(10)

# Plot the data
plt.figure(figsize=(10, 5))
sns.barplot(x=top_products.values, y=top_products.index, palette="coolwarm")
plt.xlabel("Number of Reviews")
plt.ylabel("Product ID")
plt.title("Top 10 Most Reviewed Products")
plt.show()


# In[30]:


sns.barplot(x=top_products.values, y=top_products.index, hue=top_products.index, palette="coolwarm", legend=False)


# In[31]:


pip install wordcloud


# In[32]:


from wordcloud import WordCloud

# Generate word cloud for positive reviews
positive_text = " ".join(df[df["Sentiment"] == "Positive"]["Text"])
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(positive_text)

plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud - Positive Reviews")
plt.show()


# In[33]:


# Generate word cloud for negative reviews
negative_text = " ".join(df[df["Sentiment"] == "Negative"]["Text"])
wordcloud = WordCloud(width=800, height=400, background_color="black").generate(negative_text)

plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud - Negative Reviews")
plt.show()


# In[34]:


df.to_csv("Cleaned_Amazon_Reviews.csv", index=False)


# In[ ]:





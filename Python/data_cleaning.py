#!/usr/bin/env python
# coding: utf-8

# # Data Cleaning
# 
# This notebook contains the cleaning steps of the raw dataset.

# In[11]:


print("Area Type:")
print(clean_df['Area Type'].unique())

print("\nCrime Type:")
print(clean_df['Crime Type'].unique())

print("\nCrime Subtype:")
print(clean_df['Crime Subtype'].unique())

print("\nMeasure:")
print(clean_df['Measure'].unique())

print("\nFinancial Year:")
print(clean_df['Financial Year'].unique())


# In[12]:


clean_df[clean_df['Borough_SNT'].isnull() | 
   clean_df['Area Name'].isnull() | 
   clean_df['Area Code'].isnull()].head(10)


# In[13]:


print("Missing Borough_SNT:")
print(clean_df['Borough_SNT'].isnull().sum())

print("\nMissing Area Name:")
print(clean_df['Area Name'].isnull().sum())

print("\nMissing Area Code:")
print(clean_df['Area Code'].isnull().sum())

print("\nArea Type for missing Borough_SNT:")
print(clean_df.loc[clean_df['Borough_SNT'].isnull(), 'Area Type'].value_counts())


# In[14]:


print(clean_df['Area Code'].value_counts().head(10))


# In[15]:


duplicates = clean_df[clean_df.duplicated(keep=False)]

print("Total duplicate rows:", len(duplicates))

duplicates.sort_values(
    by=['Month_Year', 'Area Name', 'Crime Subtype']
).head(20)


# In[16]:


# Remove exact duplicate rows from clean_df
clean_df = clean_df.drop_duplicates()

print("Original rows:", len(raw_df))
print("Rows after removing duplicates:", len(clean_df))
print("Duplicates remaining:", clean_df.duplicated().sum())


# In[17]:


# Convert Month_Year to datetime
clean_df['Month_Year'] = pd.to_datetime(clean_df['Month_Year'])

print(clean_df['Month_Year'].dtype)
print(clean_df['Month_Year'].head())


# In[18]:


# Clean missing and unknown geographical values

# Replace actual NaN values
clean_df['Borough_SNT'] = clean_df['Borough_SNT'].fillna('Unknown')
clean_df['Area Name'] = clean_df['Area Name'].fillna('Unknown')
clean_df['Area Code'] = clean_df['Area Code'].fillna('Unknown')

# Replace N/K and other "not known" values with Unknown
clean_df = clean_df.replace(
    to_replace=r'(?i)^N/K.*$',
    value='Unknown',
    regex=True
)

# Replace geography-not-known labels
clean_df['Area Type'] = clean_df['Area Type'].replace(
    {
        'Borough (Georgraphy Not Known)': 'Borough',
        'Safer Neighbourhood Teams (Geography Not Known)': 'Safer Neighbourhood Teams'
    }
)

# Replace invalid area code
clean_df['Area Code'] = clean_df['Area Code'].replace('-1', 'Unknown')

print("Missing Values after cleaning:")
print(clean_df.isnull().sum())

print("\nRemaining N/K values:")
print(
    clean_df.astype(str)
    .apply(lambda col: col.str.contains('N/K', case=False, na=False))
    .sum()
)


# In[19]:


print("Shape:", clean_df.shape)

print("\nData Types:")
print(clean_df.dtypes)

print("\nMissing Values:")
print(clean_df.isnull().sum())

print("\nDuplicate Rows:")
print(clean_df.duplicated().sum())


# ## Final Verification

# In[92]:


print("===== FINAL NOTEBOOK CHECK =====")
print("Dataset shape:", clean_df.shape)
print("Offence records:", len(offences_df))
print("Total offence count:", int(offences_df['Count'].sum()))
print("Duplicate rows remaining:", clean_df.duplicated().sum())
print("Missing values:")
print(clean_df.isnull().sum())


# In[93]:


# Save the final cleaned dataset so it can be reused without modifying the raw data.
clean_df.to_csv(
    "MonthlyCrimeDashboard_KnifeCrimeData_Cleaned.csv",
    index=False
)

print("Cleaned dataset saved successfully.")


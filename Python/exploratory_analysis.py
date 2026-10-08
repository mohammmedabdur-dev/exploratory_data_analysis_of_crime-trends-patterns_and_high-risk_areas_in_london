#!/usr/bin/env python
# coding: utf-8

# # Exploratory Analysis
# 
# This notebook contains the statistical analysis, distributions, groupby calculations, percentages, relationships, and findings for Q1–Q10.

# In[20]:


print("Minimum Month:", clean_df['Month_Year'].min())
print("Maximum Month:", clean_df['Month_Year'].max())


# In[21]:


# Display the first five rows to inspect the dataset structure.
clean_df.head()


# In[22]:


print("Number of unique months:", clean_df['Month_Year'].nunique())

print("\nMonths:")
print(clean_df['Month_Year'].sort_values().unique())


# In[23]:


print("Unique Borough/SNT:", clean_df['Borough_SNT'].nunique())
print("Unique Area Names:", clean_df['Area Name'].nunique())
print("Unique Area Codes:", clean_df['Area Code'].nunique())


# In[24]:


print("Crime Types:")
print(clean_df['Crime Type'].value_counts())

print("\nCrime Subtypes:")
print(clean_df['Crime Subtype'].value_counts())

print("\nMeasures:")
print(clean_df['Measure'].value_counts())

print("\nFinancial Years:")
print(clean_df['Financial Year'].value_counts())


# In[25]:


offences_df = clean_df[clean_df['Measure'] == 'Offences'].copy()

print("Offences dataset shape:", offences_df.shape)
print("Measures present:")
print(offences_df['Measure'].value_counts())


# In[26]:


print("Total offence records:", len(offences_df))
print("Total knife-crime offences:", offences_df['Count'].sum())
print("Average offences per record:", offences_df['Count'].mean())
print("Maximum offences in a single record:", offences_df['Count'].max())


# In[27]:


print("\nOffence count statistics:")
print(offences_df['Count'].describe())


# In[28]:


monthly_offences = (
    offences_df
    .groupby('Month_Year')['Count']
    .sum()
    .reset_index()
)

print(monthly_offences)


# In[29]:


print("Number of months:", monthly_offences['Month_Year'].nunique())


# In[30]:


print("\nFirst 5 months:")
print(monthly_offences.head())

print("\nLast 5 months:")
print(monthly_offences.tail())


# In[31]:


highest_month = monthly_offences.loc[
    monthly_offences['Count'].idxmax()
]

lowest_month = monthly_offences.loc[
    monthly_offences['Count'].idxmin()
]

print("Highest offence month:")
print(highest_month)

print("\nLowest offence month:")
print(lowest_month)


# In[32]:


average_monthly = monthly_offences['Count'].mean()

print("Average monthly offences:", average_monthly)


# In[33]:


first_month = monthly_offences.iloc[0]
last_month = monthly_offences.iloc[-1]

percentage_change = (
    (last_month['Count'] - first_month['Count'])
    / first_month['Count']
) * 100

print("First month:", first_month['Month_Year'])
print("First month offences:", first_month['Count'])

print("\nLast month:", last_month['Month_Year'])
print("Last month offences:", last_month['Count'])

print("\nPercentage change:", percentage_change, "%")


# # Question 1 – How does the number of knife-crime offences change over time?

# In[35]:


above_average = monthly_offences[
    monthly_offences['Count'] > average_monthly
]

print("Months above average:")
print(above_average)


# In[36]:


print(
    "Number of months above average:",
    len(above_average)
)


# # Question 2 – Which financial year recorded the highest number of knife-crime offences?

# In[37]:


financial_year_offences = (
    offences_df
    .groupby('Financial Year')['Count']
    .sum()
    .reset_index()
)

print(financial_year_offences)


# In[38]:


financial_year_summary = (
    offences_df
    .groupby('Financial Year')
    .agg(
        Total_Offences=('Count', 'sum'),
        Records=('Count', 'count')
    )
    .reset_index()
)

print(financial_year_summary)


# In[39]:


highest_financial_year = financial_year_summary.loc[
    financial_year_summary['Total_Offences'].idxmax()
]

print("Financial year with highest offences:")
print(highest_financial_year)


# In[40]:


lowest_financial_year = financial_year_summary.loc[
    financial_year_summary['Total_Offences'].idxmin()
]

print("\nFinancial year with lowest offences:")
print(lowest_financial_year)


# In[41]:


fy_order = [
    'fy22-23',
    'fy23-24',
    'fy24-25',
    'fy25-26',
    'fy26-27'
]

financial_year_summary['Financial Year'] = pd.Categorical(
    financial_year_summary['Financial Year'],
    categories=fy_order,
    ordered=True
)

financial_year_summary = (
    financial_year_summary
    .sort_values('Financial Year')
    .reset_index(drop=True)
)

print(financial_year_summary)


# In[42]:


financial_year_summary['Percentage_Change'] = (
    financial_year_summary['Total_Offences']
    .pct_change() * 100
)

print(financial_year_summary)


# In[43]:


complete_fy = financial_year_summary[
    financial_year_summary['Financial Year'].isin([
        'fy23-24',
        'fy24-25',
        'fy25-26'
    ])
].copy()

print("Complete financial years:")
print(complete_fy)


# In[44]:


highest_complete_fy = complete_fy.loc[
    complete_fy['Total_Offences'].idxmax()
]

print("\nHighest complete financial year:")
print(highest_complete_fy)


# In[45]:


first_complete = complete_fy.iloc[0]['Total_Offences']
last_complete = complete_fy.iloc[-1]['Total_Offences']

overall_change = (
    (last_complete - first_complete)
    / first_complete
) * 100

print("FY23-24 offences:", first_complete)
print("FY25-26 offences:", last_complete)
print("Overall change:", overall_change, "%")


# # Question 3 – Which boroughs have the highest number of knife-crime offences?

# In[47]:


#Question 3 :
# Filter only offence records at Borough level
borough_only = clean_df[
    (clean_df['Measure'] == 'Offences') &
    (clean_df['Area Type'] == 'Borough')
].copy()


# In[48]:


# Total knife-crime offences by borough
borough_offences = (
    borough_only
    .groupby('Borough_SNT')['Count']
    .sum()
    .reset_index()
    .sort_values('Count', ascending=False)
)

borough_offences.head(10)


# In[49]:


# Top 10 boroughs
top_10_boroughs = borough_offences.head(10)

print(top_10_boroughs)


# In[51]:


highest_borough = borough_offences.iloc[0]

print("Highest-crime borough:")
print(highest_borough)


# # Question 4 – Which Safer Neighbourhood Teams have the highest knife-crime counts?

# In[52]:


# Filter only Safer Neighbourhood Team offence records
snt_only = clean_df[
    (clean_df['Measure'] == 'Offences') &
    (clean_df['Area Type'] == 'Safer Neighbourhood Teams')
].copy()

snt_only.head()


# In[53]:


# Total knife-crime offences by Safer Neighbourhood Team
snt_offences = (
    snt_only
    .groupby('Area Name')['Count']
    .sum()
    .reset_index()
    .sort_values('Count', ascending=False)
)

snt_offences.head(15)


# In[54]:


# Top 10 Safer Neighbourhood Teams
top_10_snt = snt_offences.head(10)

print(top_10_snt)


# In[56]:


highest_snt = snt_offences.iloc[0]

print("Safer Neighbourhood Team with the highest number of offences:")
print(highest_snt)


# # Question 5 – What is the distribution of knife crime by crime subtype?

# In[57]:


# Question 5: Which knife-crime subtype is most common?
# Use offence records only.
subtype_offences = offences_df.copy()

subtype_offences.head()


# In[58]:


# Total offences by Crime Subtype
crime_subtype = (
    subtype_offences
    .groupby('Crime Subtype')['Count']
    .sum()
    .reset_index()
    .sort_values('Count', ascending=False)
)

print(crime_subtype)


# In[59]:


# Calculate percentage contribution of each crime subtype
# Display total offences by crime subtype
print("Knife-Crime Offences by Crime Subtype:")
print(crime_subtype[['Crime Subtype', 'Count']])


# In[61]:


highest_subtype = crime_subtype.iloc[0]

print("Most common knife-crime subtype:")
print(highest_subtype)


# # Question 6 – How does knife crime with injury compare with overall knife crime?

# In[62]:


# Question 6: How does knife crime with injury compare with overall knife crime?
# Use offence records only.
injury_offences = offences_df.copy()

injury_offences.head()


# In[63]:


# Check available crime subtypes
print(injury_offences['Crime Subtype'].unique())


# In[64]:


# Total offences by crime subtype
injury_count = crime_subtype.loc[
    crime_subtype['Crime Subtype'] == 'Knife Crime with Injury',
    'Count'
].iloc[0]

overall_knife_crime = crime_subtype.loc[
    crime_subtype['Crime Subtype'] == 'Knife Crime',
    'Count'
].iloc[0]

print("Knife Crime:", overall_knife_crime)
print("Knife Crime with Injury:", injury_count)


# In[65]:


# Compare overall knife crime with knife crime with injury

injury_comparison = pd.DataFrame({
    'Crime Category': [
        'Knife Crime',
        'Knife Crime with Injury'
    ],
    'Count': [
        overall_knife_crime,
        injury_count
    ]
})

# Percentage of the overall Knife Crime count represented by each category.
injury_comparison['Percentage_of_Overall'] = (
    injury_comparison['Count'] / overall_knife_crime
) * 100

# Share within the two-category comparison.
injury_comparison['Share_of_Comparison'] = (
    injury_comparison['Count'] /
    injury_comparison['Count'].sum()
) * 100

print("Knife Crime vs Knife Crime with Injury:")
print(injury_comparison)

print(
    f"Knife Crime with Injury represents "
    f"{(injury_count / overall_knife_crime) * 100:.2f}% "
    f"of the overall Knife Crime count."
)


# In[67]:


print("Knife Crime:", overall_knife_crime)
print("Knife Crime with Injury:", injury_count)


# # Question 7 – Which months experience the highest knife-crime offences?

# In[68]:


# Question 7: Is there a seasonal pattern in knife crime?
# Filter only offence records.
monthly_offences = offences_df.copy()

monthly_offences.head()


# In[69]:


# Extract month number and month name
monthly_offences['Month'] = monthly_offences['Month_Year'].dt.month
monthly_offences['Month_Name'] = monthly_offences['Month_Year'].dt.month_name()

monthly_offences[['Month_Year', 'Month', 'Month_Name']].head()


# In[70]:


# Total knife-crime offences by month of year
monthly_pattern = (
    monthly_offences
    .groupby(['Month', 'Month_Name'])['Count']
    .sum()
    .reset_index()
    .sort_values('Month')
)

print(monthly_pattern)


# In[71]:


# Rank months by total offences
monthly_ranked = monthly_pattern.sort_values(
    'Count',
    ascending=False
)

print(monthly_ranked)


# In[73]:


highest_month = monthly_ranked.iloc[0]
lowest_month = monthly_ranked.iloc[-1]

print("Highest month:")
print(highest_month)

print("\nLowest month:")
print(lowest_month)


# # Question 8 – Which areas show the greatest variation in knife crime over time?

# In[74]:


# Question 8: Which areas show the greatest variation in knife crime?
# Use offence records only.
area_time = offences_df.copy()

area_time.head()


# In[75]:


# Total offences for each area in each month
area_monthly = (
    area_time
    .groupby(['Borough_SNT', 'Month_Year'])['Count']
    .sum()
    .reset_index()
)

area_monthly.head()


# In[76]:


# Calculate monthly variation (standard deviation) for each area.
# Use offence records only and exclude non-geographical/unknown areas.

valid_area_monthly = area_monthly[
    ~area_monthly['Borough_SNT'].isin([
        'Unknown',
        'N/K (Legacy Only)',
        'N/K (Legacy Only) N/K'
    ])
].copy()

variation = (
    valid_area_monthly
    .groupby('Borough_SNT')['Count']
    .agg(
        Mean='mean',
        Std_Dev='std',
        Min='min',
        Max='max',
        Months='count'
    )
    .dropna(subset=['Std_Dev'])
    .sort_values('Std_Dev', ascending=False)
)

print("Areas with the greatest monthly variation:")
print(variation.head(10))


# In[77]:


highest_variation = variation.iloc[0]

print("Area with the greatest variation in knife-crime offences:")
print(highest_variation)


# # Question 9 – What percentage of total knife crime is contributed by the highest-crime areas?

# In[79]:


# Question 9: What percentage of total knife crime is contributed by the highest-crime areas?

# Filter only offence records.
area_offences = offences_df.copy()

area_offences.head()


# In[80]:


# Calculate total knife-crime offences for each known area.
valid_area_offences = area_offences[
    ~area_offences['Borough_SNT'].isin([
        'Unknown',
        'N/K (Legacy Only)',
        'N/K (Legacy Only) N/K'
    ])
].copy()

area_totals = (
    valid_area_offences
    .groupby('Borough_SNT')['Count']
    .sum()
    .sort_values(ascending=False)
)

print("Top 10 areas by total knife-crime offences:")
print(area_totals.head(10))


# In[81]:


# Calculate total knife-crime offences across the known geographical areas.
total_knife_crime = area_totals.sum()

# Top 5 areas
top_5_total = area_totals.head(5).sum()
top_5_percentage = (top_5_total / total_knife_crime) * 100

# Top 10 areas
top_10_total = area_totals.head(10).sum()
top_10_percentage = (top_10_total / total_knife_crime) * 100

print(f"Total knife-crime offences in known areas: {total_knife_crime:,}")
print(f"Top 5 areas: {top_5_total:,} offences ({top_5_percentage:.2f}%)")
print(f"Top 10 areas: {top_10_total:,} offences ({top_10_percentage:.2f}%)")


# In[82]:


# Percentage contributed by all areas outside the top 10
other_percentage = 100 - top_10_percentage

print(f"All other known areas: {other_percentage:.2f}%")


# In[83]:


# Top 5 and Top 10 areas
top_5 = area_totals.head(5)
top_10 = area_totals.head(10)

# Calculate offence counts
top_5_count = top_5.sum()
top_10_count = top_10.sum()

# Calculate percentage contribution
top_5_percentage = (top_5_count / total_knife_crime) * 100
top_10_percentage = (top_10_count / total_knife_crime) * 100

print(f"Top 5 areas: {top_5_count:,} offences ({top_5_percentage:.2f}%)")
print(f"Top 10 areas: {top_10_count:,} offences ({top_10_percentage:.2f}%)")


# In[85]:


print("Top 10 highest-crime areas:")
print(top_10)


# # Question 10 – Which areas and periods represent knife-crime hotspots?

# In[86]:


#Question 10:
# Filter only offence records
hotspot_data = clean_df[
    clean_df['Measure'] == 'Offences'
].copy()

hotspot_data.head()


# In[87]:


# Total offences for each area in each month
area_month_hotspots = (
    hotspot_data
    .groupby(['Borough_SNT', 'Month_Year'])['Count']
    .sum()
    .reset_index()
)

# Remove unknown/non-geographical areas from hotspot ranking.
area_month_hotspots = area_month_hotspots[
    ~area_month_hotspots['Borough_SNT'].isin([
        'Unknown',
        'N/K (Legacy Only)',
        'N/K (Legacy Only) N/K'
    ])
].sort_values('Count', ascending=False)

print("Top area-month knife-crime hotspots:")
print(area_month_hotspots.head(20))


# In[88]:


# Top 10 knife-crime hotspots
top_10_hotspots = area_month_hotspots.head(10)

print(top_10_hotspots)


# In[90]:


highest_hotspot = area_month_hotspots.iloc[0]

print("Highest knife-crime hotspot:")
print(highest_hotspot)


# In[91]:


hotspot_area_frequency = (
    top_10_hotspots['Borough_SNT']
    .value_counts()
    .reset_index()
)

hotspot_area_frequency.columns = ['Borough_SNT', 'Number_of_Top10_Hotspots']

print(hotspot_area_frequency)


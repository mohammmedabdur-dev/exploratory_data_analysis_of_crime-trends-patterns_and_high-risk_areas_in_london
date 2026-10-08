#!/usr/bin/env python
# coding: utf-8

# # Data Visualization
# 
# This notebook contains the charts, heatmaps, plots, and geographic visualizations for Q1–Q10.

# # Question 1 – How does the number of knife-crime offences change over time?

# In[34]:


#Question 1 :
plt.figure(figsize=(14, 6))

plt.plot(
    monthly_offences['Month_Year'],
    monthly_offences['Count'],
    marker='o',
    linewidth=2,
    label='Monthly Offences'
)

plt.axhline(
    y=average_monthly,
    linestyle='--',
    linewidth=2,
    label=f'Average: {average_monthly:.0f}'
)

plt.title(
    'Monthly Knife-Crime Offences\n(August 2022 – July 2026)',
    fontsize=16
)

plt.xlabel('Month')
plt.ylabel('Number of Offences')

plt.xticks(rotation=45)

plt.grid(True, alpha=0.3)
plt.legend()

plt.tight_layout()
plt.show()


# # Question 2 – Which financial year recorded the highest number of knife-crime offences?

# In[46]:


# Visualise the calculated results.
plt.figure(figsize=(10, 6))

bars = plt.bar(
    complete_fy['Financial Year'].astype(str),
    complete_fy['Total_Offences']
)

plt.title(
    'Total Knife-Crime Offences by Financial Year\n(Complete Financial Years)',
    fontsize=16
)

plt.xlabel('Financial Year')
plt.ylabel('Total Number of Offences')

plt.grid(
    axis='y',
    alpha=0.3
)

for bar in bars:
    height = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f'{int(height):,}',
        ha='center',
        va='bottom',
        fontsize=10
    )

plt.tight_layout()
plt.show()


# # Question 3 – Which boroughs have the highest number of knife-crime offences?

# In[50]:


# Visualise the calculated results.
plt.figure(figsize=(12, 6))

bars = plt.bar(
    top_10_boroughs['Borough_SNT'],
    top_10_boroughs['Count']
)

plt.title('Top 10 Boroughs by Total Knife-Crime Offences')
plt.xlabel('Borough')
plt.ylabel('Total Knife-Crime Offences')

plt.xticks(rotation=45, ha='right')

# Add values on bars
for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f'{int(bar.get_height()):,}',
        ha='center',
        va='bottom'
    )

plt.tight_layout()
plt.show()


# # Question 4 – Which Safer Neighbourhood Teams have the highest knife-crime counts?

# In[55]:


# Visualise the calculated results.
# Visualise the calculated results.
plt.figure(figsize=(12, 6))

snt_viz = top_10_snt[
    top_10_snt['Area Name'] != 'Unknown'
].head(10)

bars = plt.bar(
    snt_viz['Area Name'],
    snt_viz['Count']
)

plt.title('Top 10 Safer Neighbourhood Teams by Total Knife-Crime Offences')
plt.xlabel('Safer Neighbourhood Team')
plt.ylabel('Total Knife-Crime Offences')

plt.xticks(rotation=45, ha='right')

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f'{int(bar.get_height()):,}',
        ha='center',
        va='bottom'
    )

plt.tight_layout()
plt.show()


# # Question 5 – What is the distribution of knife crime by crime subtype?

# In[60]:


# Visualise the calculated results.
plt.figure(figsize=(12, 6))

bars = plt.bar(
    crime_subtype['Crime Subtype'],
    crime_subtype['Count']
)

plt.title('Distribution of Knife Crime by Crime Subtype')
plt.xlabel('Crime Subtype')
plt.ylabel('Total Offences')

plt.xticks(rotation=45, ha='right')

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f'{int(bar.get_height()):,}',
        ha='center',
        va='bottom'
    )

plt.tight_layout()
plt.show()


# # Question 6 – How does knife crime with injury compare with overall knife crime?

# In[66]:


# Visualise the calculated results.
# Import required libraries.
import matplotlib.pyplot as plt

categories = ['Knife Crime', 'Knife Crime with Injury']
counts = [overall_knife_crime, injury_count]

plt.figure(figsize=(8, 5))
plt.bar(categories, counts)

plt.title('Knife Crime vs Knife Crime with Injury')
plt.xlabel('Crime Category')
plt.ylabel('Number of Offences')
plt.xticks(rotation=15)

plt.tight_layout()
plt.show()


# # Question 7 – Which months experience the highest knife-crime offences?

# In[72]:


# Visualise the calculated results.
plt.figure(figsize=(12, 6))

bars = plt.bar(
    monthly_pattern['Month_Name'],
    monthly_pattern['Count']
)

plt.title('Knife-Crime Offences by Month')
plt.xlabel('Month')
plt.ylabel('Total Knife-Crime Offences')

plt.xticks(rotation=45)

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f'{int(bar.get_height()):,}',
        ha='center',
        va='bottom'
    )

plt.tight_layout()
plt.show()


# # Question 8 – Which areas show the greatest variation in knife crime over time?

# In[78]:


# Visualise the calculated results.
# Import required libraries.
import matplotlib.pyplot as plt

top_variation = variation.head(10)

plt.figure(figsize=(10, 6))
plt.bar(top_variation.index, top_variation['Std_Dev'])

plt.title('Top 10 Areas with Greatest Variation in Monthly Knife-Crime Offences')
plt.xlabel('Area')
plt.ylabel('Standard Deviation of Monthly Offences')
plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.show()


# # Question 9 – What percentage of total knife crime is contributed by the highest-crime areas?

# In[84]:


# Visualise the calculated results.
# Import required libraries.
import matplotlib.pyplot as plt

categories = ['Top 10 Areas', 'All Other Areas']
percentages = [top_10_percentage, other_percentage]

plt.figure(figsize=(8, 5))

bars = plt.bar(categories, percentages)

plt.title('Contribution of Top 10 Areas to Total Knife Crime')
plt.xlabel('Area Group')
plt.ylabel('Percentage of Total Knife Crime (%)')

# Add percentage labels
for bar, value in zip(bars, percentages):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        value + 1,
        f'{value:.2f}%',
        ha='center'
    )

plt.ylim(0, 100)
plt.tight_layout()
plt.show()


# # Question 10 – Which areas and periods represent knife-crime hotspots?

# In[89]:


# Visualise the calculated results.
plt.figure(figsize=(12, 7))

labels = (
    top_10_hotspots['Borough_SNT'].astype(str)
    + ' - '
    + pd.to_datetime(top_10_hotspots['Month_Year']).dt.strftime('%b %Y')
)

bars = plt.barh(
    labels.iloc[::-1],
    top_10_hotspots['Count'].iloc[::-1]
)

plt.title('Top 10 Knife-Crime Hotspots by Area and Month')
plt.xlabel('Total Knife-Crime Offences')
plt.ylabel('Area - Month')

for bar in bars:
    plt.text(
        bar.get_width(),
        bar.get_y() + bar.get_height() / 2,
        f'{int(bar.get_width()):,}',
        va='center',
        ha='left'
    )

plt.tight_layout()
plt.show()


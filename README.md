# Python Data Analysis Project – Knife Crime Exploratory Data Analysis

## Project Overview

This project presents a Python-based Exploratory Data Analysis (EDA) of knife-crime data. The analysis examines knife-crime offences across time, financial years, boroughs, Safer Neighbourhood Teams, crime subtypes, months, areas, and area-month hotspots.

---

## Project Information

### Project Title

**Sprint 1 – Exploratory Data Analysis of Knife Crime**

### Industry Name

**[Enter your industry name]**

### Problem Statement

**[Enter your real-world/industry problem statement]**

### Proposed Solution / Analysis Questions

The project uses Python data analysis to examine the knife-crime dataset and answer the following questions:

1. **How does the number of knife-crime offences change over time?**
2. **Which financial year recorded the highest number of knife-crime offences?**
3. **Which boroughs have the highest number of knife-crime offences?**
4. **Which Safer Neighbourhood Teams have the highest knife-crime counts?**
5. **What is the distribution of knife crime by crime subtype?**
6. **How does knife crime with injury compare with overall knife crime?**
7. **Which months experience the highest knife-crime offences?**
8. **Which areas show the greatest variation in knife crime over time?**
9. **What percentage of total knife crime is contributed by the highest-crime areas?**
10. **Which areas and periods represent knife-crime hotspots?**

---

## Dataset

### Dataset Name

`MonthlyCrimeDashboard_KnifeCrimeData.csv`

### Dataset Source

**[Enter the actual dataset source/resource]**

---

## Tools & Technologies

- Python
- Jupyter Notebook
- NumPy
- Pandas
- Matplotlib

---

## Project Workflow

```text
Industry Selection
        ↓
Problem Identification
        ↓
Dataset Collection
        ↓
Data Cleaning
        ↓
Data Transformation
        ↓
Data Analysis
        ↓
Data Visualization
        ↓
Insights
        ↓
Recommendations
```

---

## Project Structure

```text
Data-Analysis-Python-Project/
│
├── README.md
│
├── Dataset/
│   ├── raw_dataset.csv
│   └── cleaned_dataset.csv
│
├── Notebook/
│   └── Data_Analysis_EDA.ipynb
│
├── Python/
│   ├── data_loading.ipynb
│   ├── data_cleaning.ipynb
│   ├── exploratory_analysis.ipynb
│   └── data_visualization.ipynb
│
├── Visualizations/
│   ├── Monthly Knife-Crime Offences (August 2022 – July 2026).png
│   ├── Total Knife-Crime Offences by Financial Year (Complete Financial Years).png
│   ├── Top 10 Boroughs by Total Knife-Crime Offences.png
│   ├── Top 10 Safer Neighbourhood Teams by Total Knife-Crime Offences.png
│   ├── Distribution of Knife Crime by Crime Subtype.png
│   ├── Knife Crime vs Knife Crime with Injury.png
│   ├── Knife-Crime Offences by Month.png
│   ├── Top 10 Areas with Greatest Variation in Monthly Knife-Crime Offences.png
│   ├── Contribution of Top 10 Areas to Total Knife Crime.png
│   └── Top 10 Knife-Crime Hotspots by Area and Month.png
│
└── Documentation/
    └── Project_Report.pdf
```

---

# Data Analysis & Visualization

The project performs the following analysis and visualizations from the dataset:

### Time-based Analysis

- Monthly knife-crime offence totals.
- Highest and lowest offence months.
- Average monthly offences.
- Change between the first and last month.
- Financial-year offence totals.
- Comparison of complete financial years.

### Borough and Area Analysis

- Total knife-crime offences by borough.
- Top 10 boroughs by total knife-crime offences.
- Total offences by Safer Neighbourhood Team.
- Top 10 Safer Neighbourhood Teams.
- Area-level variation using monthly standard deviation.
- Contribution of the top 5 and top 10 areas to total knife crime.
- Area-month hotspot analysis.

### Crime Subtype Analysis

- Distribution of knife crime by crime subtype.
- Comparison between Knife Crime and Knife Crime with Injury.
- Percentage comparison of Knife Crime with Injury against the Knife Crime count.

### Monthly Pattern Analysis

- Total knife-crime offences by month of the year.
- Ranking of months by total offences.

### Visualizations

The notebook contains the following actual visualizations:

1. **Monthly Knife-Crime Offences (August 2022 – July 2026)**
2. **Total Knife-Crime Offences by Financial Year (Complete Financial Years)**
3. **Top 10 Boroughs by Total Knife-Crime Offences**
4. **Top 10 Safer Neighbourhood Teams by Total Knife-Crime Offences**
5. **Distribution of Knife Crime by Crime Subtype**
6. **Knife Crime vs Knife Crime with Injury**
7. **Knife-Crime Offences by Month**
8. **Top 10 Areas with Greatest Variation in Monthly Knife-Crime Offences**
9. **Contribution of Top 10 Areas to Total Knife Crime**
10. **Top 10 Knife-Crime Hotspots by Area and Month**

> The project contains area-level visualizations, but no separate geographic map visualization was included in the provided notebook.

---

# Key Insights

The following findings are taken from the analysis outputs in the final notebook:

- The dataset contains **60,100 rows** and **11 columns** in the final notebook check.
- There are **48,927 offence records**.
- The total knife-crime offence count is **171,727**.
- The average monthly number of offences is approximately **3,577.65**.
- The highest monthly offence total is **4,510 in May 2024**.
- The lowest monthly offence total is **2,856 in February 2026**.
- The first month in the analysed period, **August 2022**, recorded **3,342 offences**, while **July 2026** recorded **3,418 offences**, representing a **2.27% increase** between those two months.
- Among the complete financial years analysed, **FY24-25** recorded the highest total with **45,880 offences**.
- From **FY23-24 to FY25-26**, the analysis reports an overall decrease of approximately **9.61%**.
- **Newham** recorded the highest total knife-crime offences among the boroughs, with **4,559 offences**.
- The most common crime subtype in the analysis is **Knife Crime**, with **117,969 offences**.
- **Knife Crime with Injury** recorded **29,228 offences**, representing **24.78%** of the overall Knife Crime count used in the comparison.
- **May** had the highest total offences when the data was grouped by month of the year, with **15,380 offences**; **February** had the lowest, with **12,975 offences**.
- **Croydon** had the greatest monthly variation in the area-level analysis, with a standard deviation of approximately **25.09**.
- The top 10 known areas contributed **23.89%** of the total knife-crime offences in known geographical areas, while all other known areas contributed **76.11%**.
- The highest area-month hotspot was **Croydon in September 2023**, with **165 offences**.
- Among the top 10 area-month hotspots, **Croydon and Lambeth each appeared three times**, while Southwark appeared twice.

---

# Recommendations

Based only on the findings from this analysis:

- **Prioritize monitoring of high-offence boroughs**, particularly areas such as Newham, Lambeth, Westminster, Southwark, and Croydon.
- **Pay attention to identified area-month hotspots**, such as Croydon in September 2023, when examining periods with particularly high offence counts.
- **Consider monthly patterns when planning analysis and monitoring**, since the monthly analysis identified differences between months, with May having the highest total and February the lowest.
- **Monitor areas with high monthly variation**, such as Croydon, because larger variation can help identify areas that experience stronger changes in offence levels over time.
- **Continue tracking financial-year trends** to identify whether the decrease observed between FY23-24 and FY25-26 continues in subsequent complete financial years.
- **Use crime-subtype analysis alongside total offence counts** when examining changes in knife crime and knife crime with injury.

---

# Visualization Screenshots

The following screenshots are the actual visualizations generated in the project.

### Monthly Knife-Crime Offences (August 2022 – July 2026)

![Monthly Knife-Crime Offences](Visualizations/Monthly%20Knife-Crime%20Offences%20%28August%202022%20%E2%80%93%20July%202026%29.png)

### Total Knife-Crime Offences by Financial Year (Complete Financial Years)

![Total Knife-Crime Offences by Financial Year](Visualizations/Total%20Knife-Crime%20Offences%20by%20Financial%20Year%20%28Complete%20Financial%20Years%29.png)

### Top 10 Boroughs by Total Knife-Crime Offences

![Top 10 Boroughs](Visualizations/Top%2010%20Boroughs%20by%20Total%20Knife-Crime%20Offences.png)

### Top 10 Safer Neighbourhood Teams by Total Knife-Crime Offences

![Top 10 Safer Neighbourhood Teams](Visualizations/Top%2010%20Safer%20Neighbourhood%20Teams%20by%20Total%20Knife-Crime%20Offences.png)

### Distribution of Knife Crime by Crime Subtype

![Distribution of Knife Crime by Crime Subtype](Visualizations/Distribution%20of%20Knife%20Crime%20by%20Crime%20Subtype.png)

### Knife Crime vs Knife Crime with Injury

![Knife Crime vs Knife Crime with Injury](Visualizations/Knife%20Crime%20vs%20Knife%20Crime%20with%20Injury.png)

### Knife-Crime Offences by Month

![Knife-Crime Offences by Month](Visualizations/Knife-Crime%20Offences%20by%20Month.png)

### Top 10 Areas with Greatest Variation in Monthly Knife-Crime Offences

![Top 10 Areas with Greatest Variation](Visualizations/Top%2010%20Areas%20with%20Greatest%20Variation%20in%20Monthly%20Knife-Crime%20Offences.png)

### Contribution of Top 10 Areas to Total Knife Crime

![Contribution of Top 10 Areas](Visualizations/Contribution%20of%20Top%2010%20Areas%20to%20Total%20Knife%20Crime.png)

### Top 10 Knife-Crime Hotspots by Area and Month

![Top 10 Knife-Crime Hotspots](Visualizations/Top%2010%20Knife-Crime%20Hotspots%20by%20Area%20and%20Month.png)

---

# Author

- **Name:** Hari
- **Student ID:** [Your Student ID]
- **Organization:** Anudip Foundation
- **Course:** AIML
- **Batch Code:** [Your Batch Code]

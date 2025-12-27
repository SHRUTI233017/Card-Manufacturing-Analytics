🏭 CARD MANUFACTURING ANALYTICS

📘 Overview:

This project focuses on improving the Card Manufacturing Process by using data analytics to increase production efficiency and reduce errors.It integrates Python (EDA), SQL (Queries), and Power BI  and Excel (Visualization) with data cleansing and dashboarding to support data-driven decision-making.

## 🔗 Links
[Github]https://github.com/SHRUTI233017/Card-Manufacturing-Analytics                     

[linkedin]https://www.linkedin.com/in/shrutichigare/



🧱 Project Architecture
<img width="1053" height="643" alt="Screenshot 2025-11-03 112524" src="https://github.com/user-attachments/assets/2ed1a0e0-2f25-4546-9c3d-38b68118d01a" />

## Architecture Flow 
 1. Data Collection – Collect raw data from manufacturing logs and secondary sources.   
 2. Load Data into Database – Store in MySQL for structured querying.  
 3. EDA and Data Cleansing – Perform data cleaning, outlier handling, and feature engineering.  
 4. Python EDA and Preprocessing – Use NumPy and Pandas for data processing and analysis.  
 5. Visualization Tools – Power BI and Excel used for visual dashboards.   
 6. Decision Making – Insights drive process improvements and business growth.

📂 Files Description

| File Name | Description |
|------------|-------------|
|Python_EDA.py| Performs EDA, cleans data, handles nulls and outliers, visualizes metrics, and saves cleaned data.|
|Card Manufacturing Quries.sql| SQL queries for analyzing efficiency, rejection trends, and operator performance.|
|Card Manufacturing Analytics.pbix| Power BI dashboard showing production trends and efficiency insights. |
|Card Manufacturing Excel Dashboard.xlsx | Excel-based dashboard for comparison and quick reporting. |
| DA Final Presentation.pptx| Presentation covering business problem, objectives, EDA, and results.|
|Project_Architecture| Architecture diagram showing data collection to decision-making workflow. | 


🧮 Python EDA Highlights

Imported required libraries: `pandas`, `numpy`, `matplotlib`, `seaborn`.  
- Removed duplicate and null values  
- Converted date columns and data types  
- Handled outliers using the **IQR method**  
- Created visualization plots:
  
  1.Box Plot for Outlier Detection  
  2.Histogram for Card Distribution  
  3.Scatter Plot (Printed vs Rejected Cards)  
  4.Correlation Heatmap  

  Added new metric:  
  `Production_Efficiency = (Accepted_Cards / No_of_Cards_Printed) * 100`  

Exported cleaned data to `Cleaned_gsm_cards.csv`

🧾 SQL Query Highlights

1.Daily count of cards printed, accepted, and rejected  
2.Daily production efficiency and rejection rate  
3.Top productive printer and personalization operators  
4.Average embedding errors by date and operator  
5.Rejection rates by batch, material type, and hour of day  
6.Ink and paper combinations with highest acceptance rates  
7.Average cards printed per sheet

📊 Visualization and Reporting

1.Power BI Dashboard: visualizes production KPIs, efficiency trends, and rejection rates.  
<img width="1181" height="666" alt="Screenshot 2025-12-27 195910" src="https://github.com/user-attachments/assets/f690ea30-3dfb-4782-9214-ec4fa4ce898e" />

2.Excel Dashboard: provides tabular insights with charts and filters.  

## 🎯 Business Objective

- Maximize operational efficiency  
- Minimize production errors  
- Improve data accessibility through digital dashboards  
- Achieve 10% profit margin increase and 20% revenue growth within the first year

   
## 📈 Business Insights 

-  Identified high rejection batches and root  causes  
 - Found optimal Ink & Paper combinations with best acceptance rates  
 - Determined top-performing operators   
-  Observed that lamination and embedding stages caused most rejections   
-  Clean data enabled consistent, accurate reporting for management

  
## 🧩 Tools & Technologies  

| Tool | Purpose | 
|------|----------|           
|Python (NumPy, Pandas, Seaborn, Matplotlib)| EDA and preprocessing |                         
|MySQL | Querying and data analysis | 
|Power BI| Interactive visualization |
|Excel | Comparative dashboard and reports |
|PowerPoint| Presentation and project summary |

## 📘 Project Outcome

- Data cleaning and analytics workflow  
- Identified and reduced process inefficiencies   
- Enhanced production monitoring through dashboards  
- Enabled faster, data-backed business decisions  

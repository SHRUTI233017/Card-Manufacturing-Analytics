# Import libraries
import pandas as pd  # Data manipulation
import numpy as np  # Numerical operations
import matplotlib.pyplot as plt  # Visualizations
import seaborn as sns  # Statistical plots
from scipy.stats import skew, kurtosis  # Skewness and kurtosis

# Reading data from an Excel file
data = pd.read_excel(r"C:\Users\User\Downloads\Card Manufacturing Porject_213\New folder\GSM_CARDS.xlsx")
# Displaying the data types of each column in the DataFrame
print(data.dtypes)
print(data.info())
print(data.columns) 
print(data.shape)


# Finding and removing duplicate rows
duplicate = data.duplicated(keep=False)
print(f"Total duplicate rows found: {sum(duplicate)}")
data = data.drop_duplicates()  # Removing duplicate rows


# Checking for missing values
missing_values = data.isnull().sum()
print(missing_values)

# Handling missing values by calculating No_of_Quarter_Cards
data['No_of_Quarter_Cards'] = data['No_of_Cards_Printed'] - data['No_of_Half_Cards'] 
print(data.isnull().sum())


#Date & Type Conversion
data['Printing_Date_Time'] = pd.to_datetime(data['Printing_Date_Time'], format='%d-%m-%Y %H:%M')
data['Lamination_Date_Time'] = pd.to_datetime(data['Lamination_Date_Time'], format='%d-%m-%Y %H:%M')


data['No_of_Half_Cards'] = data['No_of_Half_Cards'].astype('int64')
data['Rejected_Cards'] = data['Rejected_Cards'].astype('int64')
data['No_of_Quarter_Cards'] = data['No_of_Quarter_Cards'].astype('int64')

print(data[['Printing_Date_Time', 'Lamination_Date_Time']].head())



# Descriptive Analysis
print(data.describe()) 

# Outlier Detection
columns_to_plot = ['No_of_Cards_Printed', 'Accepted_Cards', 'Rejected_Cards', 'No_of_Half_Cards', 'No_of_Quarter_Cards']

# Create a box plot for each column to check for outliers
plt.figure(figsize=(12, 8))
data[columns_to_plot].boxplot()
plt.title('Box Plot for Outlier Detection')
plt.ylabel('Values')
plt.xticks(rotation=45)
plt.show()

# Replace outliers using the IQR method
columns_to_clean = ['No_of_Cards_Printed', 'Accepted_Cards', 'Rejected_Cards', 'No_of_Half_Cards', 'No_of_Quarter_Cards']

for col in columns_to_clean:
    IQR = data[col].quantile(0.75) - data[col].quantile(0.25)
    lower_limit = data[col].quantile(0.25) - (IQR * 1.5)
    upper_limit = data[col].quantile(0.75) + (IQR * 1.5)
    data[col] = np.where(data[col] > upper_limit, upper_limit, 
                         np.where(data[col] < lower_limit, lower_limit, data[col]))
    
# Melt the DataFrame for plotting
melted_data = data[columns_to_clean].melt(var_name='Card Type', value_name='Value')

# Create the box plot for all columns
plt.figure(figsize=(10, 6))
sns.boxplot(x='Card Type', y='Value', data=melted_data)
plt.title('Box Plot for Various Card Types')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#------------------ UNIVARIATE ANALYSIS ------------------
plt.figure(figsize=(6,4))
sns.histplot(data['No_of_Cards_Printed'], bins=20, kde=True, color='blue')
plt.title("Distribution of Cards Printed")
plt.xlabel("No. of Cards Printed")
plt.ylabel("Frequency")
plt.show()

# ------------------ BIVARIATE ANALYSIS ------------------
plt.figure(figsize=(6,4))
sns.scatterplot(x='No_of_Cards_Printed', y='Rejected_Cards', data=data, color='blue', alpha=0.6)
sns.regplot(x='No_of_Cards_Printed', y='Rejected_Cards', data=data, scatter=False, color='red')  # 🔹 adds trendline
plt.title("Printed vs Rejected Cards", fontsize=12, fontweight='bold')
plt.xlabel("No. of Cards Printed")
plt.ylabel("Rejected Cards")
plt.grid(True, linestyle='----', alpha=0.5)
plt.show()


#Correlation Heatmap
selected_cols = ['No_of_Cards_Printed', 'Accepted_Cards', 'Rejected_Cards', 'No_of_Half_Cards', 'No_of_Quarter_Cards']
plt.figure(figsize=(6,4))
sns.heatmap(data[selected_cols].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Between Production Metrics")
plt.show()

# ------------------ MULTIVARIATE ANALYSIS ------------------
# Rejected Cards by Ink Type and Paper Type
plt.figure(figsize=(10,5))
sns.barplot(x='Ink_Type', y='Rejected_Cards', hue='Paper_Type', data=data, ci=None)
plt.title("Rejected Cards by Ink Type and Paper Type")
plt.xticks(rotation=45)
plt.show()

# ------------------ BUSINESS INSIGHTS ------------------
# Average rejected cards by Ink Type and Paper Type
avg_rejected = data.groupby(['Ink_Type', 'Paper_Type'])['Rejected_Cards'].mean().reset_index()
print(avg_rejected.sort_values('Rejected_Cards'))

# ------------------ EFFICIENCY METRIC ------------------
data['Production_Efficiency'] = (data['Accepted_Cards'] / data['No_of_Cards_Printed']) * 100
print(data[['Batch_ID', 'Production_Efficiency']].nlargest(5, 'Production_Efficiency'))

# ------------------ CORRELATION WITH REJECTED CARDS ------------------
correlation_result = data[selected_cols].corr()['Rejected_Cards'].sort_values(ascending=False)
print("\nCorrelation with Rejected Cards:\n", correlation_result)

# ---------------------------------------------- Save Cleaned Data ----------------------------------------------
output_file_path = r"C:\Users\User\Downloads\Cleaned_gsm_cards.csv"
data.to_csv(output_file_path, index=False)
print(f"Cleaned data saved to: {output_file_path}")


# Define output file path (CSV instead of Excel)
output_file_path = r"C:\Users\User\Downloads\Cleaned_gsm_cards.csv"

# Save as CSV
data.to_csv(output_file_path, index=False)

# Confirmation message
print(f"Cleaned data saved to: {output_file_path}")

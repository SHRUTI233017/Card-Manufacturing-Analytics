create database  Manufacturing;
use Manufacturing;
select * from gsm_cards;

#1. Daily Count of Cards Printed, Accepted, and Rejected
SELECT 
    DATE(Printing_Date_Time) AS Daily_count, 
    SUM(No_of_Cards_Printed) AS Total_Cards_Printed,
    SUM(Accepted_Cards) AS Total_Accepted_Cards, 
    SUM(Rejected_Cards) AS Total_Rejected_Cards  
FROM gsm_cards
GROUP BY Daily_count
ORDER BY Total_Cards_Printed DESC;

#2.What was the daily production efficiency (percentage of accepted cards) for each day?
SELECT 
    DATE(Printing_DT) AS Print_Date,
    ROUND(SUM(Accepted_Cards) / SUM(No_of_Cards_Printed) * 100, 2) AS Daily_Production_Efficiency
FROM gsm_cards
GROUP BY Print_Date
order by Daily_Production_Efficiency desc;

#3. Identify Days with High Rejection Rate (Error Identification)
SELECT 
    DATE(Printing_DT) AS Rejection_Date,
    ROUND(SUM(Rejected_Cards) / SUM(No_of_Cards_Printed) * 100, 2) AS Rejection_Rate
FROM gsm_cards
GROUP BY Rejection_Date;

#4. Trend of Accepted Cards Over Time
SELECT 
    DATE(Printing_DT) AS Date,
    SUM(Accepted_Cards) AS Accepted_Cards
FROM gsm_cards
GROUP BY Date
ORDER BY Accepted_Cards DESC;

#5.What is the average number of embedding errors each day?
SELECT 
    DATE(Printing_DT) AS Date,
    ROUND(AVG(Embedding_Errors), 2) AS Avg_Embedding_Errors
FROM gsm_cards
GROUP BY Date
ORDER BY Date;

#6. Which printer operators had the highest average embedding errors?
SELECT 
    Printer_Operator_ID,
    ROUND(AVG(Embedding_Errors), 2) AS Avg_Embedding_Errors
FROM gsm_cards
GROUP BY Printer_Operator_ID
ORDER BY Avg_Embedding_Errors DESC;

#7. Rejection Rate by Personalization Operator
SELECT 
    Personalization_Operator_ID,
    ROUND(SUM(Rejected_Cards) * 100 / SUM(No_of_Cards_Printed), 2) AS Rejection_Rate
FROM gsm_cards
GROUP BY Personalization_Operator_ID
ORDER BY Rejection_Rate DESC;

#8. Who are the most productive printer operators based on card acceptance percentage?
SELECT 
    Printer_Operator_ID,
    ROUND(sum((Accepted_Cards / No_of_Cards_Printed) * 100), 2) AS Avg_Productive_Operators
FROM gsm_cards
GROUP BY Printer_Operator_ID
ORDER BY Avg_Productive_Operators DESC
LIMIT 5;

#9. Which batches had the highest rejection rates?
SELECT 
    Batch_ID,
    SUM(Rejected_Cards) AS Total_Rejected,
    ROUND(SUM(Rejected_Cards) / SUM(No_of_Cards_Printed) * 100, 2) AS Rejection_Rate
FROM gsm_cards
GROUP BY Batch_ID
ORDER BY Rejection_Rate DESC
LIMIT 10;

#10. How many cards were printed per sheet on average?
SELECT 
    ROUND(AVG(No_of_Cards_Printed / No_of_Sheets_Used), 2) AS Avg_Cards_Per_Sheet
FROM gsm_cards;

#11. How many cards are printed during each hour of the day?
SELECT 
    HOUR(Printing_DT) AS Hour,
    SUM(No_of_Cards_Printed) AS Total_Cards
FROM gsm_cards
GROUP BY Hour
ORDER BY Hour;

#12. Which ink and paper type combinations had the highest acceptance rates?
SELECT 
    Ink_Type, 
    Paper_Type,
    ROUND(SUM(Accepted_Cards) * 100 / SUM(No_of_Cards_Printed), 2) AS Acceptance_rates
FROM gsm_cards
GROUP BY Ink_Type, Paper_Type
ORDER BY Acceptance_rates;

#13. Which ink and paper type combinations produced the most cards?
SELECT 
    Ink_Type, 
    Paper_Type,
    SUM(No_of_Cards_Printed) AS Total_Cards		
FROM gsm_cards
GROUP BY Ink_Type, Paper_Type
ORDER BY Total_Cards DESC;
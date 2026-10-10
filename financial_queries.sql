-- Query 1: Isolate underperforming departments operating on low profit margins
SELECT 
    Department,
    SUM(Revenue) AS Total_Department_Revenue,
    SUM(Operating_Cost) AS Total_Department_Cost,
    ROUND((SUM(Revenue) - SUM(Operating_Cost)), 2) AS Absolute_Gross_Profit,
    ROUND(((SUM(Revenue) - SUM(Operating_Cost)) / SUM(Revenue)) * 100, 2) AS Profit_Margin_Pct
FROM corporate_financials
GROUP BY Department
ORDER BY Profit_Margin_Pct ASC;

-- Query 2: Segment regions that generated above-average corporate revenue margins
WITH Corporate_Average AS (
    SELECT AVG(Revenue) AS avg_rev FROM corporate_financials
)

SELECT 
    Region,
    COUNT(Transaction_ID) AS Volume_Of_Transactions,
    SUM(Revenue) AS Total_Regional_Sales
FROM corporate_financials, Corporate_Average
GROUP BY Region
HAVING SUM(Revenue) > (SELECT avg_rev FROM Corporate_Average)
ORDER BY Total_Regional_Sales DESC;

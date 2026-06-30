-- Top 5 Products by Total Sales
SELECT
    Product,
    SUM(Total_Sales) AS Total_Revenue
FROM sales_data
GROUP BY Product
ORDER BY Total_Revenue DESC
LIMIT 5;

-- Highest Revenue Category
SELECT
    Category,
    SUM(Total_Sales) AS Total_Revenue
FROM sales_data
GROUP BY Category
ORDER BY Total_Revenue DESC;

-- Highest Sales by City
SELECT
    City,
    SUM(Total_Sales) AS Total_Sales
FROM sales_data
GROUP BY City
ORDER BY Total_Sales DESC;

-- Top 10 Customers
SELECT
    Customer_Name,
    SUM(Total_Sales) AS Total_Sales
FROM sales_data
GROUP BY Customer_Name
ORDER BY Total_Sales DESC
LIMIT 10;

-- Monthly Sales Trend
SELECT
    DATE_FORMAT(Order_Date, '%Y-%m') AS Month,
    SUM(Total_Sales) AS Total_Sales
FROM sales_data
GROUP BY DATE_FORMAT(Order_Date, '%Y-%m')
ORDER BY Month;

-- Average Order Value by Category
SELECT
    Category,
    ROUND(AVG(Total_Sales), 2) AS Average_Order_Value
FROM sales_data
GROUP BY Category
ORDER BY Average_Order_Value DESC;

-- Sales by Age Group
SELECT
    CASE
        WHEN Age BETWEEN 18 AND 25 THEN '18-25'
        WHEN Age BETWEEN 26 AND 35 THEN '26-35'
        WHEN Age BETWEEN 36 AND 45 THEN '36-45'
        WHEN Age BETWEEN 46 AND 55 THEN '46-55'
        ELSE '56+'
    END AS Age_Group,
    SUM(Total_Sales) AS Total_Sales
FROM sales_data
GROUP BY Age_Group
ORDER BY Total_Sales DESC;
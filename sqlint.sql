--Interview Scenario 1: Join Columns having Unique Values
-- Create TableA
drop table TableB;
CREATE TABLE TableA (
    ID INT PRIMARY KEY
);

-- Insert values into TableA
INSERT INTO TableA (ID) VALUES (1), (2), (3), (4), (5);

-- Create TableB
CREATE TABLE TableB (
    ID INT PRIMARY KEY
);

-- Insert values into TableB
INSERT INTO TableB (ID) VALUES (1), (2), (4);

-- INNER JOIN: Returns only the rows where there is a match in both tables
SELECT TableA.ID AS A_ID, TableB.ID AS B_ID
FROM TableA
INNER JOIN TableB ON TableA.ID = TableB.ID;

-- LEFT JOIN: Returns all rows from the left table (TableA), and the matched rows from the right table (TableB)
SELECT TableA.ID AS A_ID, TableB.ID AS B_ID
FROM TableA
LEFT JOIN TableB ON TableA.ID = TableB.ID;

-- RIGHT JOIN: Returns all rows from the right table (TableB), and the matched rows from the left table (TableA)
SELECT TableA.ID AS A_ID, TableB.ID AS B_ID
FROM TableA
RIGHT JOIN TableB ON TableA.ID = TableB.ID;

-- FULL OUTER JOIN: Returns all rows when there is a match in either table
-- If there is no match, the result will contain NULL values for columns from the table without a match
SELECT TableA.ID AS A_ID, TableB.ID AS B_ID
FROM TableA
FULL OUTER JOIN TableB ON TableA.ID = TableB.ID;

-- CROSS JOIN: Returns the Cartesian product of both tables (all possible combinations of rows)
SELECT TableA.ID AS A_ID, TableB.ID AS B_ID
FROM TableA
CROSS JOIN TableB;
-------------------------------------------------------------------------------
--now Scenario 2: Join columns having duplicate values using above table
-- Create TableX
CREATE TABLE TableX (
    ID INT PRIMARY KEY,
    ValueX VARCHAR(255)
);

-- Insert values into TableX
INSERT INTO TableX (ID, ValueX) VALUES 
    (1, 'Apple'),
    (2, 'Banana'),
    (3, 'Orange'),
    (4, 'Apple'),
    (5, 'Grapes');

-- Create TableY
CREATE TABLE TableY (
    ID INT PRIMARY KEY,
    ValueY VARCHAR(255)
);

-- Insert values into TableY
INSERT INTO TableY (ID, ValueY) VALUES 
    (1, 'Red'),
    (2, 'Yellow'),
    (3, 'Orange'),
    (4, 'Green'),
    (6, 'Purple');

   
   -- INNER JOIN: Returns only the rows where there is a match in both tables
SELECT TableX.ID, TableX.ValueX, TableY.ValueY
FROM TableX
INNER JOIN TableY ON TableX.ID = TableY.ID;

-- LEFT JOIN: Returns all rows from the left table (TableX), and the matched rows from the right table (TableY)
SELECT TableX.ID, TableX.ValueX, TableY.ValueY
FROM TableX
LEFT JOIN TableY ON TableX.ID = TableY.ID;

-- RIGHT JOIN: Returns all rows from the right table (TableY), and the matched rows from the left table (TableX)
SELECT TableX.ID, TableX.ValueX, TableY.ValueY
FROM TableX
RIGHT JOIN TableY ON TableX.ID = TableY.ID;

-- FULL OUTER JOIN: Returns all rows when there is a match in either table
-- If there is no match, the result will contain NULL values for columns from the table without a match
SELECT TableX.ID, TableX.ValueX, TableY.ValueY
FROM TableX
FULL OUTER JOIN TableY ON TableX.ID = TableY.ID;

----------------------------------------------------------------------
--Scenario 3: One Join table contains Null Value
-- Create TableW
CREATE TABLE W (
    ID INT PRIMARY KEY,
    ValueW VARCHAR(255)
);

-- Insert values into TableW
INSERT INTO W (ID, ValueW) VALUES 
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, NULL);

-- Create TableE
CREATE TABLE E (
    ID INT PRIMARY KEY,
    ValueE VARCHAR(255)
);

-- Insert values into TableE
INSERT INTO E (ID, ValueE) VALUES 
    (1, '1'),
    (2, '1'),
    (3, '2'),
    (4, '3'),
    (5, '4'),
    (6, '5');
   
   -- INNER JOIN: Returns only the rows where there is a match in both tables
SELECT W.ID, W.ValueW, E.ValueE
FROM W
INNER JOIN E ON W.ID = E.ID;

-- LEFT JOIN: Returns all rows from the left table (TableW), and the matched rows from the right table (TableE)
SELECT W.ID, W.ValueW, E.ValueE
FROM W
LEFT JOIN E ON W.ID = E.ID;

-- RIGHT JOIN: Returns all rows from the right table (TableE), and the matched rows from the left table (TableW)
SELECT W.ID, W.ValueW, E.ValueE
FROM W
RIGHT JOIN E ON W.ID = E.ID;

-- FULL OUTER JOIN: Returns all rows when there is a match in either table
-- If there is no match, the result will contain NULL values for columns from the table without a match
SELECT W.ID, W.ValueW, E.ValueE
FROM W
FULL OUTER JOIN E ON W.ID = E.ID;


create table ecommerce(dept varchar(50),txnmonth varchar(50),txnamount int);
insert into ecommerce values('Electronics','Jan',1000);
insert into ecommerce values('Electronics','Feb',2000);
insert into ecommerce values('Electronics','Mar',2500);
insert into ecommerce values('Textile','Jan',1000);
insert into ecommerce values('Textile','Feb',2000);
insert into ecommerce values('Textile','Mar',1500);
insert into ecommerce values('Sports','Jan',600);
insert into ecommerce values('Sports','Feb',200);
insert into ecommerce values('Sports','Mar',500);

SELECT a.*
FROM (
    SELECT e.* ,
           RANK() OVER (PARTITION BY dept ORDER BY txnamount ASC) AS ranks
    FROM ecommerce e 
) AS a
WHERE ranks = 3 ;

with cte1 as (
select sum(e.txnamount) as total_txn,dept
from ecommerce e 
group by dept
)
,cte2  as (
select *,dense_RANK() OVER ( ORDER BY total_txn ASC) AS rank_min,
dense_RANK() OVER (ORDER BY total_txn desc) AS rank_max
from cte1
)SELECT MAX(CASE WHEN rank_min = 1 THEN dept END) AS minimum_transaction
 ,MAX(CASE WHEN rank_max = 1 THEN dept END) AS maximum_transaction
FROM cte2;

WITH cte1
AS (
 SELECT dept
 , SUM(txnamount) AS total_txnamount
 FROM ecommerce
 GROUP BY dept
 )
 ,cte2
AS (
 SELECT *
 ,DENSE_RANK() OVER (ORDER BY total_txnamount DESC) AS drnk_max
 ,DENSE_RANK() OVER (ORDER BY total_txnamount ASC) AS drnk_min
 FROM cte1
 )
SELECT MAX(CASE WHEN drnk_min = 1 THEN dept END) AS minimum_transaction
 ,MAX(CASE WHEN drnk_max = 1 THEN dept END) AS maximum_transaction
FROM cte2;


--Data Engineering Interview Questions SQL:

--1. Assume you're given a table containing job postings from various companies on the LinkedIn platform. Write a query to retrieve the count of companies that have posted duplicate job listings. 
--Duplicate job listings are defined as two job listings within the same company that share identical titles and descriptions.
---- Create the jobs table
CREATE TABLE jobs (
 job_id INT,
 company_id INT,
 title VARCHAR(100),
 description TEXT
);

-- Insert data into the jobs table
INSERT INTO jobs (company_id, title, job_id, description) VALUES
(827, 'Business Analyst', 248, 'Business analyst evaluates past and current business data with the primary goal of improving decision-making processes within organizations.'),
(845, 'Business Analyst', 149, 'Business analyst evaluates past and current business data with the primary goal of improving decision-making processes within organizations.'),
(345, 'Data Analyst', 945, 'Data analyst reviews data to identify key insights into a business''s customers and ways the data can be used to solve problems.'),
(345, 'Data Analyst', 164, 'Data analyst reviews data to identify key insights into a business''s customers and ways the data can be used to solve problems.'),
(244, 'Data Engineer', 172, 'Data engineer works in a variety of settings to build systems that collect, manage, and convert raw data into usable information for data scientists and business analysts to interpret.'),
(827, 'Data Scientist', 256, 'Data scientist uses data to understand and explain the phenomena around them, and help organizations make better decisions.'),
(244, 'Software Engineer', 365, 'Software engineers design and create computer systems and applications to solve real-world problems.'),
(400, 'Business Intelligence Analyst', 674, 'Business intelligence analyst reviews data to produce finance and market intelligence reports.'),
(827, 'Data Scientist', 245, 'Data scientist uses data to understand and explain the phenomena around them, and help organizations make better decisions.'),
(244, 'Software Engineer', 301, 'Software engineers design and create computer systems and applications to solve real-world problems.');

select * from jobs

with cte as(
select company_id,
row_number() over(partition by company_id,title,description ) as rk
from jobs
)
select count(*) from cte where rk>1;


--
--Imagine there's a Customer table with various columns. The data in the "Names" column is not right – there are extra special characters inserted in between the names.
--
--You have to Clean the Data.

CREATE  table Customer (
 Id INT,
 Name VARCHAR(255),
 Status VARCHAR(50)
);


INSERT INTO Customer (Id, Name, Status)
VALUES
 (1, 'R*a#d_h.i@k*a', 'Active'),
 (2, 'J#a*n%e', 'Inactive'),
 (3, 'B$o*b', 'Active'),
 (4, 'S*h$y@a)m&a*l_a', 'Inactive'),
 (5, 'V*hashtag#e*n#ka$t', 'Active');

select 
 REGEXP_REPLACE(Name, '[^a-zA-Z ]', '') AS name
from customer;


--
-- Write an SQL query that shows how many players had their first gaming session 
-- and then their second one within two days. (2 Consecutive days).

CREATE TABLE PlayerSessions (
 PlayerID INTEGER,
 LoginDate DATE,
 Duration INTEGER
);

INSERT INTO PlayerSessions (PlayerID, LoginDate, Duration) VALUES
(1, '2023-11-01', 60),(1, '2023-11-02', 45), (2, '2023-11-01', 30),
(2, '2023-11-02', 60),(3, '2023-11-01', 75),(3, '2023-11-03', 90),
(4, '2023-11-01', 40),(4, '2023-11-02', 55),(5, '2023-11-01', 80),
(5, '2023-11-02', 70);

select * from PlayerSessions;

with cte as (
select playerid,logindate,
dense_rank() over(partition by logindate order by logindate) as rnk
from PlayerSessions
)
select c.playerid from cte c join PlayerSessions s2 on c.playerid=s2.playerid
AND c.LoginDate = s2.LoginDate +1
Where rnk in (1 , 2);

--or using datediff and lag

WITH LoginChanges AS (
    SELECT 
        playerid,
        logindate,
        LAG(logindate) OVER (PARTITION BY playerid ORDER BY logindate) AS prev_logindate
    FROM PlayerSessions
)
SELECT DISTINCT c.playerid
FROM LoginChanges c
JOIN PlayerSessions ps ON c.playerid = ps.playerid
WHERE DATEDIFF(day,c.prev_logindate,c.logindate) = 1



CREATE TABLE ProductPurchases (
 CATEGORY_ID INTEGER,
 PRODUCT_ID INTEGER,
 PRODUCT_AMOUNT DECIMAL(10, 2),
 PRODUCT_PURCHASE_DATE DATE
);

INSERT INTO ProductPurchases (CATEGORY_ID, PRODUCT_ID, PRODUCT_AMOUNT, PRODUCT_PURCHASE_DATE) VALUES
 (1, 101, 50.00, '2023-11-01'),
 (1, 102, 30.50, '2023-11-01'),
 (2, 201, 75.25, '2023-11-02'),
 (2, 202, 40.00, '2023-11-02'),
 (3, 301, 20.75, '2023-11-03'),
 (3, 302, 55.80, '2023-11-03'),
 (1, 103, 45.90, '2023-11-04'),
 (2, 203, 60.00, '2023-11-04'),
 (3, 303, 35.50, '2023-11-05');
--
--Write a query to retrieve the first purchase date, 
--last purchase date, amount of the first purchase date, 
--amount of the last purchase date, and total purchase amount for each category, 

select * from productpurchases;

with cte as
(
select category_id, product_purchase_date,product_amount,
dense_rank() over(partition by category_id order by product_purchase_date asc) as first_purchase_date,
dense_rank() over(partition by category_id order by product_purchase_date desc) as second_purchase_date
from productpurchases pc
), cte2 as (
select *,sum(product_amount) as total_amount from cte 
group by category_id,product_purchase_date,product_amount,first_purchase_date,second_purchase_date
)
select category_id,
min(case when first_purchase_date=1 then product_purchase_date end) as first_purchase_date,
max(case when second_purchase_date=2 then product_purchase_date end) as second_purchase_date
from cte,cte2
;


WITH CTE AS 
( Select CATEGORY_ID,
FIRST_VALUE(PRODUCT_AMOUNT) OVER (PARTITION BY CATEGORY_ID ORDER BY PRODUCT_PURCHASE_DATE) AS AMOUNT_FIRST_PURCHASE,
FIRST_VALUE(PRODUCT_AMOUNT) OVER (PARTITION BY CATEGORY_ID ORDER BY PRODUCT_PURCHASE_DATE DESC) AS AMOUNT_LAST_PURCHASE
FROM PRODUCTPURCHASES),
CTE2 as (
SELECT CATEGORY_ID,
MIN(PRODUCT_PURCHASE_DATE) AS FIRST_PURCHASE_DATE,
MAX(PRODUCT_PURCHASE_DATE) AS LAST_PURCHASE_DATE,
SUM(PRODUCT_AMOUNT) AS TOTAL_PURCHASE_AMOUNT
FROM ProductPurchases GROUP BY category_id)
Select distinct CTE2.CATEGORY_ID, CTE2.FIRST_PURCHASE_DATE,
CTE2.LAST_PURCHASE_DATE, CTE2.TOTAL_PURCHASE_AMOUNT,
CTE.AMOUNT_FIRST_PURCHASE, CTE.AMOUNT_LAST_PURCHASE
From CTE, CTE2
Where CTE.CATEGORY_ID = CTE2.CATEGORY_ID
;


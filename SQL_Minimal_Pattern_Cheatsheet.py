'''
=============================================================================
 SQL MINIMAL PATTERN CHEATSHEET â€” UE20CS903
 Databases & SQL Â· PES University Bengaluru
 37 patterns Â· 10 groups Â· 158 questions covered Â· 11 ESA papers
=============================================================================
'''

=============================================================================
GROUP 1 â€” WINDOW FUNCTIONS  (8 patterns Â· ~35 questions)
Mnemonic: TRAP-LFNA
   T â€” Top-N per group
   R â€” Rolling/Moving average
   A â€” Accumulate (Running total)
   P â€” Previous row (LAG)
   L â€” %rank filter (PERCENT_RANK)
   F â€” First value (FIRST_VALUE)
   N â€” Nth value / NTILE / CUME_DIST / LEAD
   A â€” Avg-vs-group (AVG OVER PARTITION)
=============================================================================

-----------------------------------------------------------------------------
P01 Â· TOP N PER GROUP
Papers : Feb 2025, Aug 2023, Dec 2023, Jul 2021, May 2025, Mar 2024
Trigger: 'top 3 per location', 'top 5 countries per year',
         'highest runtime per genre'
Insight: Use DENSE_RANK (not RANK) so ties don't skip ranks.
         rnk <= 3 means top 3.
-----------------------------------------------------------------------------
SELECT *
FROM (
    SELECT *,
           DENSE_RANK() OVER (PARTITION BY group_col
                              ORDER BY rank_col DESC) AS rnk
    FROM table_name
) t
WHERE rnk <= N
ORDER BY group_col, rnk;

-----------------------------------------------------------------------------
P02 Â· ROLLING / MOVING AVERAGE
Papers : Feb 2025, Dec 2023, Mar 2024
Trigger: '3-year moving average', '3-month moving average', 'rolling avg'
Insight: 'ROWS BETWEEN 2 PRECEDING AND CURRENT ROW' = window of 3 rows.
         Change 2 to N-1 for an N-period window.
-----------------------------------------------------------------------------
SELECT col, year_col,
       AVG(metric) OVER (
           PARTITION BY group_col
           ORDER BY year_col
           ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
       ) AS rolling_avg
FROM table_name;

-----------------------------------------------------------------------------
P03 Â· RUNNING TOTAL (Cumulative SUM)
Papers : House+Sales, May 2025, Dec 2023, Jun 2024
Trigger: 'running total', 'cumulative salary', 'cumulative revenue',
         'cumulative count'
Insight: UNBOUNDED PRECEDING = from the very first row of the partition.
         No PARTITION BY = single running total across all rows.
-----------------------------------------------------------------------------
SELECT col,
       SUM(metric) OVER (
           PARTITION BY group_col
           ORDER BY order_col
           ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
       ) AS running_total
FROM table_name;

-----------------------------------------------------------------------------
P04 Â· LAG â€” PREVIOUS ROW VALUE
Papers : Feb 2025, Aug 2023
Trigger: 'previous invoice date', 'previous value', 'compare with last row'
Insight: LAG(col, 1) is the default. LAG(col, 2) gives two rows back.
         LEAD() looks forward instead.
-----------------------------------------------------------------------------
SELECT customerid, invoice_date,
       LAG(invoice_date) OVER (
           PARTITION BY customerid
           ORDER BY invoice_date
       ) AS previous_date
FROM invoice;

-----------------------------------------------------------------------------
P05 Â· PERCENT_RANK â€” TOP X% FILTER
Papers : House+Sales
Trigger: 'top 10%', 'top 5% by price in the group'
Insight: PERCENT_RANK() returns 0 to 1. <= 0.10 means top 10%.
         Ascending ORDER BY = lowest percentile first.
-----------------------------------------------------------------------------
SELECT *
FROM (
    SELECT *,
           PERCENT_RANK() OVER (
               PARTITION BY location
               ORDER BY price DESC
           ) AS pct_rank
    FROM table_name
) t
WHERE pct_rank <= 0.10   -- top 10%
  AND bath > 3;           -- additional filter

-----------------------------------------------------------------------------
P06 Â· FIRST_VALUE â€” EARLIEST / LOWEST PER GROUP
Papers : Jul 2021
Trigger: 'earliest release date in its genre', 'first in group',
         'minimum per partition'
Insight: FIRST_VALUE with ORDER BY ASC = minimum.
         ORDER BY DESC = maximum.
         Use ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
         to see the value on every row.
-----------------------------------------------------------------------------
SELECT movie_title, release_date, genre,
       FIRST_VALUE(release_date) OVER (
           PARTITION BY genre
           ORDER BY release_date ASC
       ) AS first_release_in_genre
FROM movie_genre_view;

-----------------------------------------------------------------------------
P07 Â· AVG OVER PARTITION â€” ROW vs GROUP AVG
Papers : Mar 2021, May 2025
Trigger: 'compare each item price vs restaurant avg',
         'employees earning above their dept avg'
Insight: Window AVG shows both the row value and group average side by side.
         Correlated subquery filters to only above-avg rows.
-----------------------------------------------------------------------------
SELECT name, price,
       AVG(price) OVER (PARTITION BY restaurant_id) AS group_avg,
       price - AVG(price) OVER (PARTITION BY restaurant_id) AS diff_from_avg
FROM food_items;

-- OR as a correlated subquery filter:
SELECT * FROM employees e
WHERE salary > (SELECT AVG(salary) FROM employees
                WHERE department_id = e.department_id);

-----------------------------------------------------------------------------
P08 Â· NTH_VALUE / NTILE / CUME_DIST / LEAD
Papers : Sample GA
Trigger: '2nd lightest per breed', 'weight quartiles', 'percentile',
         'next heaviest'
Insight: These four rarely appear together â€” sample GA uses all of them
         as individual 1-mark window function questions.
-----------------------------------------------------------------------------
-- 2nd value per group:
NTH_VALUE(weight, 2) OVER (PARTITION BY breed ORDER BY weight
    ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)

-- Quartile buckets (1-4):
NTILE(4) OVER (ORDER BY weight)

-- Cumulative distribution (0 to 1) Ã— 100 = percentile:
CAST(CUME_DIST() OVER (ORDER BY weight) * 100 AS UNSIGNED)

-- Next row in group:
LEAD(weight, 1) OVER (PARTITION BY breed ORDER BY weight)


=============================================================================
GROUP 2 â€” SUBQUERY PATTERNS  (5 patterns Â· ~20 questions)
Mnemonic: MNCSM
   M â€” Max/Min in WHERE
   N â€” Not-in (exclusion)
   C â€” Correlated subquery
   S â€” Second-lowest / Nth value via nested MIN
   M â€” Most-recent year filter
=============================================================================

-----------------------------------------------------------------------------
P09 Â· MAX/MIN IN WHERE
Papers : Feb 2025, Dec 2023, House+Sales, Jul 2021
Trigger: 'country with highest X', 'cheapest house in each location',
         'max price record'
Insight: Correlated subquery runs once per outer row.
         Use for 'cheapest in each location', 'highest per dept'.
-----------------------------------------------------------------------------
-- Global max:
SELECT * FROM table_name
WHERE col = (SELECT MAX(col) FROM table_name);

-- Max per group (correlated):
SELECT * FROM table_name t1
WHERE col = (SELECT MIN(col) FROM table_name t2
             WHERE t2.group_col = t1.group_col);

-----------------------------------------------------------------------------
P10 Â· NOT IN SUBQUERY (Exclusion)
Papers : House+Sales, Mar 2024, Jun 2024, Mar 2021, Dec 2023
Trigger: 'customers who have NOT ordered', 'circuits with no races',
         'inactive clients', 'movies without rating'
Insight: Both produce identical results. LEFT JOIN IS NULL is preferred
         for performance. NOT IN is more readable for exams.
-----------------------------------------------------------------------------
-- NOT IN:
SELECT * FROM customers
WHERE customerNumber NOT IN (
    SELECT DISTINCT customerNumber FROM orders);

-- LEFT JOIN IS NULL (same result, faster on large tables):
SELECT c.*
FROM customers c
LEFT JOIN orders o ON c.customerNumber = o.customerNumber
WHERE o.orderNumber IS NULL;

-----------------------------------------------------------------------------
P11 Â· CORRELATED SUBQUERY
Papers : May 2025, Mar 2024
Trigger: 'employees earning above avg of their own dept',
         'Paris office using correlated subquery'
Insight: The inner query references the outer query's row (e.department_id).
         Runs once per outer row. Slower than JOIN but often required by exam.
-----------------------------------------------------------------------------
SELECT first_name, last_name, salary
FROM employees e
WHERE salary > (
    SELECT AVG(salary) FROM employees
    WHERE department_id = e.department_id   -- e. binds to outer row
);

-----------------------------------------------------------------------------
P12 Â· SECOND LOWEST / NTH VALUE VIA NESTED MIN
Papers : Aug 2023
Trigger: 'second lowest budget department', '2nd highest salary'
Insight: Double-nested MIN/MAX for second extremes.
         LIMIT 2 approach is cleaner for 2nd highest.
-----------------------------------------------------------------------------
-- Second lowest:
WHERE col = (
    SELECT MIN(col) FROM table_name
    WHERE col > (SELECT MIN(col) FROM table_name)
);

-- 2nd highest salary:
SELECT MIN(salary)
FROM (SELECT salary FROM employees ORDER BY salary DESC LIMIT 2) t;

-----------------------------------------------------------------------------
P13 Â· MOST RECENT YEAR FILTER
Papers : Feb 2025, Dec 2023
Trigger: 'most recent year available', 'latest year in the data'
Insight: Always use (SELECT MAX(year) FROM ...) instead of hardcoding
         the year â€” the dataset could have any latest year.
-----------------------------------------------------------------------------
SELECT Country_name, Perceptions_of_corruption
FROM world_happiness_report
WHERE year = (SELECT MAX(year) FROM world_happiness_report)
ORDER BY Perceptions_of_corruption ASC
LIMIT 1;


=============================================================================
GROUP 3 â€” AGGREGATION + HAVING  (3 patterns Â· ~15 questions)
Mnemonic: CHG
   C â€” Count-filter (HAVING COUNT > N)
   H â€” Having-avg   (HAVING AVG > N)
   G â€” Group-distinct-rank (COUNT DISTINCT + DENSE_RANK)
=============================================================================

-----------------------------------------------------------------------------
P14 Â· HAVING COUNT > N
Papers : Aug 2023, House+Sales, Mar 2021, May 2025
Trigger: 'depts with more than 2 employees',
         'customers with same first name', 'locations with > 5 houses'
Insight: HAVING filters after GROUP BY. WHERE filters before.
         Never use aggregate in WHERE â€” that's a classic exam trap.
-----------------------------------------------------------------------------
SELECT department, COUNT(*) AS emp_count
FROM employees
GROUP BY department
HAVING COUNT(*) > 2;

-- As subquery (exam often asks this):
SELECT name FROM departments
WHERE code IN (
    SELECT department FROM employees
    GROUP BY department HAVING COUNT(*) > 2);

-----------------------------------------------------------------------------
P15 Â· HAVING AVG > N
Papers : House+Sales, May 2025
Trigger: 'locations where avg price > 100', 'depts with avg salary > X',
         'catalogue items with avg price > 1000'
Insight: HAVING can use any aggregate: AVG, SUM, MAX.
         No alias in HAVING â€” repeat the expression or use the column.
-----------------------------------------------------------------------------
SELECT location, ROUND(AVG(price), 2) AS avg_price
FROM bangalore_houses
GROUP BY location
HAVING AVG(price) > 100
ORDER BY avg_price DESC;

-----------------------------------------------------------------------------
P16 Â· COUNT DISTINCT + DENSE_RANK
Papers : Feb 2025, Aug 2023
Trigger: 'rank customers by unique albums purchased',
         'rank by number of distinct items'
Insight: COUNT DISTINCT inside GROUP BY + DENSE_RANK() in the SELECT.
         The window function operates on the already-grouped result.
-----------------------------------------------------------------------------
SELECT customerid,
       COUNT(DISTINCT albumid) AS unique_albums,
       DENSE_RANK() OVER (
           ORDER BY COUNT(DISTINCT albumid) DESC
       ) AS album_rank
FROM invoice
JOIN invoiceline USING(invoiceid)
JOIN track USING(trackid)
GROUP BY customerid
ORDER BY album_rank;


=============================================================================
GROUP 4 â€” JOIN PATTERNS  (4 patterns Â· ~15 questions)
Mnemonic: MSAL
   M â€” Multi-table JOIN chain
   S â€” Self-join for two-condition comparison
   A â€” Anti-join (LEFT JOIN IS NULL)
   L â€” Level-hierarchy (Self-join 3-level)
=============================================================================

-----------------------------------------------------------------------------
P17 Â· MULTI-TABLE JOIN CHAIN
Papers : House+Sales, Mar 2024, Dec 2023, Jul 2021
Trigger: 'total value of USA Classic Cars orders',
         'customer film rental report'
Insight: Write joins in the direction data flows:
         customer â†’ orders â†’ details â†’ product â†’ category.
         Always alias tables. Add WHERE after all JOINs.
-----------------------------------------------------------------------------
SELECT c.customerName,
       SUM(od.quantityOrdered * od.priceEach) AS total_value
FROM customers c
JOIN orders o        ON c.customerNumber  = o.customerNumber
JOIN orderdetails od ON o.orderNumber     = od.orderNumber
JOIN products p      ON od.productCode    = p.productCode
JOIN productlines pl ON p.productLine     = pl.productLine
WHERE c.country = 'USA' AND pl.productLine = 'Classic Cars'
GROUP BY c.customerNumber, c.customerName
ORDER BY total_value DESC;

-----------------------------------------------------------------------------
P18 Â· SELF-JOIN FOR TWO-CONDITION COMPARISON
Papers : Feb 2025, Dec 2023, Aug 2023
Trigger: 'countries where X > 0.8 in BOTH 2019 AND 2020',
         'customers with same first name'
Insight: The self-join approach (alias a, b) is cleaner for two-year
         conditions. The HAVING approach works for duplicate-value detection.
-----------------------------------------------------------------------------
-- Two-year condition (same table joined to itself):
SELECT DISTINCT a.Country_name
FROM world_happiness_report a
JOIN world_happiness_report b
  ON a.Country_name = b.Country_name
WHERE a.year = 2019 AND a.Freedom_to_make_life_choices > 0.8
  AND b.year = 2020 AND b.Freedom_to_make_life_choices > 0.8;

-- Same first name:
SELECT c1.customerid, c1.firstname
FROM customer c1
WHERE c1.firstname IN (
    SELECT firstname FROM customer
    GROUP BY firstname HAVING COUNT(*) > 1);

-----------------------------------------------------------------------------
P19 Â· LEFT JOIN IS NULL (Anti-join)
Papers : Oct 2021, Mar 2024
Trigger: 'circuits where no races held', 'films never rented'
Insight: LEFT JOIN keeps all left-table rows.
         WHERE right_table.id IS NULL filters to only rows with no match.
         This is the anti-join pattern.
-----------------------------------------------------------------------------
SELECT c.circuitId, c.name
FROM circuits c
LEFT JOIN races r ON c.circuitId = r.circuitId
WHERE r.raceId IS NULL;   -- NULL means no matching row = no race

-----------------------------------------------------------------------------
P20 Â· SELF-JOIN 3-LEVEL HIERARCHY
Papers : Mar 2021
Trigger: 'item + parent + grandparent description', 'reporting manager'
Insight: Each self-join adds one level.
         LEFT JOIN for manager so employees without a manager (CEO) still appear.
-----------------------------------------------------------------------------
-- 3-level catalogue (child â†’ parent â†’ grandparent):
SELECT c1.Catalogue_Entry_Description AS Prod_Desc,
       c2.Catalogue_Entry_Description AS Sub_Prod_Desc,
       c3.Catalogue_Entry_Description AS Main_Prod_Desc
FROM catalogue c1
JOIN catalogue c2 ON c1.Parent_Catalogue_Entry_id = c2.Catalogue_Entry_id
JOIN catalogue c3 ON c2.Parent_Catalogue_Entry_id = c3.Catalogue_Entry_id;

-- Manager lookup (employee â†’ manager):
SELECT e.Employee_name, m.Employee_name AS Manager_Name
FROM resources e
LEFT JOIN resources m ON e.Manager_id = m.Employee_id;


=============================================================================
GROUP 5 â€” DATE OPERATIONS  (4 patterns Â· ~12 questions)
Mnemonic: GCST
   G â€” Group-by-date (DATE_FORMAT / YEAR)
   C â€” Conditional-case (compare two time periods)
   S â€” Span (TIMESTAMPDIFF for tenure)
   T â€” Transform (STR_TO_DATE for non-standard format)
=============================================================================

-----------------------------------------------------------------------------
P21 Â· DATE_FORMAT / YEAR() FOR GROUPING
Papers : Oct 2021, Mar 2021, Mar 2024
Trigger: 'monthly sessions', 'total sales in 2020',
         'max temp per month', 'profitable months'
Insight: DATE_FORMAT('%Y-%m') groups by month.
         DATE_FORMAT('%Y-%m-01') gives a proper date for sorting.
         YEAR() alone groups by year only.
-----------------------------------------------------------------------------
-- Group by year:
SELECT YEAR(Order_Date) AS yr, SUM(Sales)
FROM orders WHERE YEAR(Order_Date) = 2020
GROUP BY YEAR(Order_Date);

-- Group by year-month:
SELECT DATE_FORMAT(Date, '%Y-%m') AS month, MAX(Temp9am)
FROM australiaweather
GROUP BY DATE_FORMAT(Date, '%Y-%m')
ORDER BY month;

-----------------------------------------------------------------------------
P22 Â· CONDITIONAL AVG â€” COMPARE TWO TIME PERIODS
Papers : Oct 2021
Trigger: 'compare Jan 2008 vs Jul 2008 rainfall',
         'compare two months in one row'
Insight: CASE WHEN inside AVG/SUM â€” a pivot pattern.
         Each CASE becomes a separate column.
         Works for any pivot (months, sources, devices).
-----------------------------------------------------------------------------
SELECT
  ROUND(AVG(CASE WHEN DATE_FORMAT(Date, '%Y-%m') = '2008-01'
                 THEN Rainfall END), 2) AS avg_jan,
  ROUND(AVG(CASE WHEN DATE_FORMAT(Date, '%Y-%m') = '2008-07'
                 THEN Rainfall END), 2) AS avg_jul
FROM australiaweather;

-----------------------------------------------------------------------------
P23 Â· TIMESTAMPDIFF FOR TENURE
Papers : May 2025
Trigger: 'tenure in years', 'longest serving employee',
         'years since hire date'
Insight: TIMESTAMPDIFF(YEAR, start, end) gives integer years.
         Use CURDATE() for 'up to today'.
         DATEDIFF() gives difference in days.
-----------------------------------------------------------------------------
SELECT first_name, last_name, hire_date,
       TIMESTAMPDIFF(YEAR, hire_date, CURDATE()) AS tenure_years
FROM employees
ORDER BY tenure_years DESC
LIMIT 3;

-----------------------------------------------------------------------------
P24 Â· STR_TO_DATE FOR NON-STANDARD FORMAT
Papers : Jul 2021
Trigger: 'dates stored as YYYY-DD-MM', 'date format not standard'
Insight: STR_TO_DATE(string, format) converts any string to a proper DATE.
         Wrap in ABS() to always get a positive gap regardless of order.
-----------------------------------------------------------------------------
SELECT mp.name,
       ABS(DATEDIFF(
           STR_TO_DATE(mp.tenure_start,  '%Y-%d-%m'),
           STR_TO_DATE(mla.tenure_start, '%Y-%d-%m')
       )) AS gap_days
FROM mp JOIN mla ON mp.name = mla.name
ORDER BY gap_days DESC LIMIT 1;


=============================================================================
GROUP 6 â€” VIEW + CTE  (2 patterns Â· ~8 questions)
Mnemonic: VC
   V â€” View-then-query
   C â€” CTE-then-rank
=============================================================================

-----------------------------------------------------------------------------
P25 Â· CREATE OR REPLACE VIEW THEN QUERY
Papers : Feb 2025, Aug 2023, House+Sales, May 2025, Oct 2021, Jul 2021
Trigger: 'create a virtual table', 'create a view called X',
         'using the view fetchâ€¦'
Insight: CREATE OR REPLACE is safer than CREATE VIEW
         (won't error if view exists).
         Always add a SELECT after the CREATE to verify it works.
-----------------------------------------------------------------------------
-- Step 1: Create the view:
CREATE OR REPLACE VIEW view_name AS
SELECT col1, col2, aggregate_col
FROM table1 JOIN table2 ON ...
GROUP BY col1, col2;

-- Step 2: Query the view (can add WHERE, ORDER BY, window functions):
SELECT *
FROM view_name
WHERE condition
ORDER BY col;

-----------------------------------------------------------------------------
P26 Â· CTE + WINDOW FUNCTION
Papers : House+Sales
Trigger: 'use CTE and window function',
         'top 5 customers total payments using CTE'
Insight: CTE (WITH clause) names an intermediate result.
         Then use DENSE_RANK in the main SELECT.
         Can chain multiple CTEs: WITH a AS (...), b AS (...) SELECT...
-----------------------------------------------------------------------------
WITH customer_totals AS (
    SELECT customerNumber, customerName,
           SUM(amount) AS total_payments
    FROM customers JOIN payments USING(customerNumber)
    GROUP BY customerNumber, customerName
)
SELECT *,
       DENSE_RANK() OVER (ORDER BY total_payments DESC) AS payment_rank
FROM customer_totals
ORDER BY payment_rank
LIMIT 5;


=============================================================================
GROUP 7 â€” STRING + TYPE FUNCTIONS  (4 patterns Â· ~8 questions)
Mnemonic: CSNL
   C â€” Cast-money    (CAST + REPLACE for $ strings)
   S â€” Split-name    (SUBSTRING_INDEX + LOCATE)
   N â€” NULL-avoid    (NULLIF to prevent divide-by-zero)
   L â€” LIKE-filter   (LIKE + LOWER + CONCAT)
=============================================================================

-----------------------------------------------------------------------------
P27 Â· CAST(REPLACE()) FOR MONEY STRINGS
Papers : Feb 2025, Dec 2023, Jul 2021
Trigger: 'Average_Covered_Charges stored as $12345.67',
         'money column stored as text'
Insight: REPLACE removes the $ character.
         CAST converts the resulting string to DECIMAL.
         Wrap both in AVG/SUM for aggregation.
-----------------------------------------------------------------------------
-- Convert '$1234.56' to DECIMAL for arithmetic:
AVG(CAST(REPLACE(Average_Covered_Charges, '$', '') AS DECIMAL(15,2)))

-- Full example â€” insurance coverage ratio:
SELECT Provider_Id,
    AVG(CAST(REPLACE(Average_Covered_Charges,    '$', '') AS DECIMAL(15,2))) /
    (AVG(CAST(REPLACE(Average_Total_Payments,    '$', '') AS DECIMAL(15,2))) +
     AVG(CAST(REPLACE(Average_Medicare_Payments, '$', '') AS DECIMAL(15,2)))) AS ratio
FROM inpatient1
GROUP BY Provider_Id;

-----------------------------------------------------------------------------
P28 Â· SUBSTRING_INDEX + LOCATE â€” SPLIT A STRING
Papers : Mar 2024
Trigger: 'extract first and last name from full name', 'split on space'
Insight: SUBSTRING_INDEX(str, delim, 1) takes everything before first space.
         LOCATE finds the position of the space.
         SUBSTRING takes from position+1 to end.
-----------------------------------------------------------------------------
SELECT Customer_Name,
       SUBSTRING_INDEX(Customer_Name, ' ', 1) AS first_name,
       SUBSTRING(Customer_Name,
                 LOCATE(' ', Customer_Name) + 1) AS last_name
FROM orders;

-----------------------------------------------------------------------------
P29 Â· NULLIF â€” AVOID DIVIDE BY ZERO
Papers : Mar 2021
Trigger: 'bsearch as % of gsearch', 'ratio that could be 0 in denominator'
Insight: NULLIF(expr, 0) returns NULL if expr = 0, avoiding division-by-zero.
         Any arithmetic on NULL returns NULL, which is safe.
-----------------------------------------------------------------------------
ROUND(
    SUM(CASE WHEN source='bsearch' THEN 1 ELSE 0 END) /
    NULLIF(SUM(CASE WHEN source='gsearch' THEN 1 ELSE 0 END), 0),
4) AS b_pct_of_g

-----------------------------------------------------------------------------
P30 Â· LIKE + LOWER + CONCAT
Papers : Feb 2025, Aug 2023, Jul 2021
Trigger: 'genre starts with s', 'customers with same first name',
         'display full name'
Insight: Always LOWER() before LIKE to avoid case issues.
         DATE_FORMAT('%D %M %Y') gives '1st January 1999' format.
-----------------------------------------------------------------------------
-- Filter by starting letter:
WHERE LOWER(g.name) LIKE 's%'

-- Full name display:
CONCAT(first_name, ' ', last_name) AS full_name

-- Date formatted string:
CONCAT(first_name, ' Joined on ', DATE_FORMAT(hire_date, '%D %M %Y'))


=============================================================================
GROUP 8 â€” DDL + TCL  (3 patterns Â· ~5 questions)
Mnemonic: AAT
   A â€” Alter-add    (ALTER TABLE ADD COLUMN)
   A â€” Assert/Check (CREATE TABLE with CHECK constraint)
   T â€” Transaction  (TCL SAVEPOINT + ROLLBACK)
=============================================================================

-----------------------------------------------------------------------------
P31 Â· ALTER TABLE ADD COLUMN
Papers : Oct 2021
Trigger: 'add a new column with default value',
         'add Pressure9pm INT NOT NULL DEFAULT 1001'
Insight: Syntax: ALTER TABLE name ADD COLUMN col_name DATATYPE
                 [NOT NULL] [DEFAULT value].
         NOT NULL + DEFAULT works together.
-----------------------------------------------------------------------------
ALTER TABLE australiaweather
ADD COLUMN Pressure9pm INT NOT NULL DEFAULT 1001;

-- Verify:
DESCRIBE australiaweather;

-----------------------------------------------------------------------------
P32 Â· CREATE TABLE WITH CHECK CONSTRAINT
Papers : Sample GA
Trigger: 'create table with check constraints',
         'course_duration <= 21', 'title IN (list)'
Insight: CHECK() can be: comparison (<=, >=), IN list, or BETWEEN.
         Goes after the column type.
         Can also be table-level: CONSTRAINT chk_name CHECK (expr).
-----------------------------------------------------------------------------
CREATE TABLE Course (
    Course_ID         INT PRIMARY KEY,
    Course_Name       VARCHAR(100),
    course_duration   INT CHECK (course_duration <= 21),
    course_title      VARCHAR(20) CHECK (course_title IN ('Python','SQL','STATS')),
    course_start_date DATE
);

-----------------------------------------------------------------------------
P33 Â· TCL BLOCK â€” SAVEPOINT + ROLLBACK
Papers : Mar 2021
Trigger: 'undo accidental update', 'transaction control', 'SET autocommit'
Insight: Sequence:
         SET autocommit=0 â†’ SAVEPOINT name â†’ (changes)
         â†’ ROLLBACK TO SAVEPOINT name â†’ COMMIT.
         ROLLBACK alone undoes everything since last COMMIT.
-----------------------------------------------------------------------------
SET autocommit = 0;                   -- disable auto-commit
SELECT * FROM clients;                -- see original data

SAVEPOINT a;                          -- bookmark this state

UPDATE clients                        -- accidental change
SET client_Country = 'India';

SELECT * FROM clients;                -- verify the change

ROLLBACK TO SAVEPOINT a;              -- undo back to bookmark

SELECT * FROM clients;                -- verify restored

COMMIT;                               -- finalise


=============================================================================
GROUP 9 â€” RATIO + PERCENTAGE  (3 patterns Â· ~6 questions)
Mnemonic: RAP
   R â€” Ratio-of-avgs         (ratio from AVG aggregates)
   A â€” Aggregate-percentage  (conversion rate / CVR)
   P â€” Pivot-percentage      (conditional pivot â€” two sources side by side)
=============================================================================

-----------------------------------------------------------------------------
P34 Â· RATIO FROM AVG AGGREGATES
Papers : Feb 2025, Dec 2023, Jul 2021
Trigger: 'insurance coverage ratio', 'ratio of averages'
Insight: Ratio = numerator / denominator.
         When columns are money strings, wrap each in
         CAST(REPLACE(...,'$','') AS DECIMAL).
         The whole expression goes inside ROUND(..., decimals).
-----------------------------------------------------------------------------
SELECT Provider_Id, Provider_Name,
    ROUND(
        AVG(CAST(REPLACE(col_a,'$','') AS DECIMAL(15,2))) /
        (AVG(CAST(REPLACE(col_b,'$','') AS DECIMAL(15,2))) +
         AVG(CAST(REPLACE(col_c,'$','') AS DECIMAL(15,2)))),
    6) AS ratio
FROM inpatient1
GROUP BY Provider_Id, Provider_Name
ORDER BY ratio DESC;

-----------------------------------------------------------------------------
P35 Â· CONVERSION RATE (CVR)
Papers : Mar 2021
Trigger: 'conversion rate from sessions to orders',
         'CVR = unique orders / unique sessions'
Insight: LEFT JOIN so sessions with no orders still count in denominator.
         COUNT DISTINCT prevents double-counting.
         Multiply by 100 for percentage.
-----------------------------------------------------------------------------
SELECT
    COUNT(DISTINCT s.session_id)  AS Sessions,
    COUNT(DISTINCT o.order_id)    AS Orders,
    ROUND(COUNT(DISTINCT o.order_id) /
          COUNT(DISTINCT s.session_id) * 100, 4) AS Conversion
FROM sessions_website s
LEFT JOIN orders o ON s.session_id = o.session_id
WHERE s.source_UTM    = 'gsearch'
  AND s.campaign_UTM  = 'nonbrand'
  AND s.visited_at   <= '2020-08-24';

-----------------------------------------------------------------------------
P36 Â· CONDITIONAL PIVOT â€” TWO SOURCES SIDE BY SIDE
Papers : Mar 2021
Trigger: 'gsearch vs bsearch sessions by device per month',
         'compare two groups in one row'
Insight: SUM(CASE WHEN condition THEN 1 ELSE 0 END) counts rows matching
         a condition. Divide one count by another for a ratio.
         NULLIF protects the denominator.
-----------------------------------------------------------------------------
SELECT DATE_FORMAT(visited_at, '%Y-%m-01') AS month,
    SUM(CASE WHEN source='gsearch' AND device='desktop' THEN 1 ELSE 0 END) AS g_dtop,
    SUM(CASE WHEN source='bsearch' AND device='desktop' THEN 1 ELSE 0 END) AS b_dtop,
    ROUND(
        SUM(CASE WHEN source='bsearch' AND device='desktop' THEN 1 ELSE 0 END) /
        NULLIF(SUM(CASE WHEN source='gsearch' AND device='desktop' THEN 1 ELSE 0 END), 0),
    4) AS b_pct_of_g_dtop
FROM sessions_website
WHERE campaign_UTM = 'nonbrand'
GROUP BY DATE_FORMAT(visited_at, '%Y-%m-01')
ORDER BY month;


=============================================================================
GROUP 10 â€” SET OPERATIONS  (1 pattern Â· ~3 questions)
Mnemonic: U â€” Union (stack two result sets)
=============================================================================

-----------------------------------------------------------------------------
P37 Â· UNION â€” COMBINE TWO SELECT RESULTS
Papers : Jun 2024, Sample GA
Trigger: 'reviewers and movies in a single list',
         'employees from dept 60 AND dept 90'
Insight: UNION removes duplicates. UNION ALL keeps all rows (faster).
         Both SELECTs must have the same number of columns.
         ORDER BY goes at the very end, once.
-----------------------------------------------------------------------------
-- Stack two result sets (removes duplicates):
SELECT name AS label FROM reviewer
UNION
SELECT title FROM movie
ORDER BY label;

-- Keep duplicates with UNION ALL:
SELECT employee_id, first_name, salary, department_id
FROM employees WHERE department_id = 60
UNION ALL
SELECT employee_id, first_name, salary, department_id
FROM employees WHERE department_id = 90
ORDER BY salary;

'''
=============================================================================
END OF CHEATSHEET
=============================================================================
'''

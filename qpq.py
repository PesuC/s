'''
World Happiness Report SQL Queries
-- 3a. Country with the lowest perception of corruption in the most recent year
SELECT Country_name, Perceptions_of_corruption, year FROM world_happiness_report WHERE year=(SELECT MAX(year) FROM world_happiness_report) AND Perceptions_of_corruption IS NOT NULL ORDER BY Perceptions_of_corruption ASC LIMIT 1;

-- 3b. Top 5 countries with highest social support for every year
SELECT year, Country_name, Social_support, rn FROM (SELECT year, Country_name, Social_support, ROW_NUMBER() OVER(PARTITION BY year ORDER BY Social_support DESC) rn FROM world_happiness_report WHERE Social_support IS NOT NULL) ranked WHERE rn<=5 ORDER BY year ASC, Social_support DESC;

-- 3c. Countries where freedom to make life choices was greater than 0.8 in both 2019 and 2020
SELECT Country_name FROM world_happiness_report WHERE Freedom_to_make_life_choices>0.8 AND year IN (2019,2020) GROUP BY Country_name HAVING COUNT(DISTINCT year)=2;

-- 3d. Yearly average of Negative_Affect from lowest to highest
SELECT year, AVG(Negative_affect) AS avg_negative_affect FROM world_happiness_report GROUP BY year ORDER BY avg_negative_affect ASC;

-- 3e. Country with the highest Healthy_life_expectancy_at_birth
SELECT Country_name, year, Healthy_life_expectancy_at_birth FROM world_happiness_report WHERE Healthy_life_expectancy_at_birth=(SELECT MAX(Healthy_life_expectancy_at_birth) FROM world_happiness_report);

-- 3f. 3-year rolling average of Positive_affect for each country
SELECT Country_name, year, Positive_affect, AVG(Positive_affect) OVER(PARTITION BY Country_name ORDER BY year ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS rolling_avg_3yr FROM world_happiness_report ORDER BY Country_name, year;

-- 3g. Country with the lowest Social_support in the most recent year (using subquery)
SELECT Country_name, Social_support, year FROM world_happiness_report WHERE year=(SELECT MAX(year) FROM world_happiness_report) AND Social_support=(SELECT MIN(Social_support) FROM world_happiness_report WHERE year=(SELECT MAX(year) FROM world_happiness_report));

-- 3h. Providers with total discharges and average covered charges, total payments and medicare payments
SELECT Provider_Name, SUM(Total_Discharges) AS total_discharges, AVG(CAST(REPLACE(Average_Covered_Charges,'$','') AS DECIMAL(15,2))) AS avg_covered_charges, AVG(CAST(REPLACE(Average_Total_Payments,'$','') AS DECIMAL(15,2))) AS avg_total_payments, AVG(CAST(REPLACE(Average_Medicare_Payments,'$','') AS DECIMAL(15,2))) AS avg_medicare_payments FROM inpatient1 GROUP BY Provider_Name ORDER BY total_discharges DESC;

-- 3i. Insurance coverage ratio for each provider from lowest to highest
SELECT Provider_Name, AVG(CAST(REPLACE(Average_Covered_Charges,'$','') AS DECIMAL(15,2)))/NULLIF(AVG(CAST(REPLACE(Average_Total_Payments,'$','') AS DECIMAL(15,2)))+AVG(CAST(REPLACE(Average_Medicare_Payments,'$','') AS DECIMAL(15,2))),0) AS insurance_coverage_ratio FROM inpatient1 GROUP BY Provider_Name ORDER BY insurance_coverage_ratio ASC;

sales Table Queries

-- 4a. Customers who share the same first name
SELECT customerid, firstname, lastname, country FROM customer WHERE firstname IN (SELECT firstname FROM customer GROUP BY firstname HAVING COUNT(*)>1) ORDER BY firstname, lastname;

-- 4b. Customer ID, invoice date and previous invoice date for every customer
SELECT customerid, invoicedate, LAG(invoicedate) OVER(PARTITION BY customerid ORDER BY invoicedate) AS previous_invoicedate FROM invoice ORDER BY customerid, invoicedate;

-- 4c. Total tracks per genre where unit price > 0.9 and genre starts with 'S'
SELECT g.name AS genre_name, COUNT(t.trackid) AS total_tracks FROM track t JOIN genre g ON t.genreid=g.genreid WHERE t.unitprice>0.9 AND g.name LIKE 's%' GROUP BY g.name ORDER BY total_tracks DESC;

-- 4d. Rank customers based on number of unique albums purchased
SELECT i.customerid, COUNT(DISTINCT t.albumid) AS unique_albums_purchased, RANK() OVER(ORDER BY COUNT(DISTINCT t.albumid) DESC) AS customer_rank FROM invoice i JOIN invoiceline il ON i.invoiceid=il.invoiceid JOIN track t ON il.trackid=t.trackid GROUP BY i.customerid ORDER BY customer_rank;

-- 4e. Total tracks billed per composer in descending order
SELECT t.composer, SUM(il.quantity) AS total_tracks_billed FROM track t JOIN invoiceline il ON t.trackid=il.trackid WHERE t.composer IS NOT NULL GROUP BY t.composer ORDER BY total_tracks_billed DESC;

-- 4f. Create a view showing customer ID, billing city, customer city and albums billed per invoice
DROP VIEW IF EXISTS customer_album_orders;

CREATE VIEW customer_album_orders AS SELECT c.customerid, i.invoiceid, i.billingcity, c.city AS customer_city, COUNT(DISTINCT t.albumid) AS albums_billed FROM customer c JOIN invoice i ON c.customerid=i.customerid JOIN invoiceline il ON i.invoiceid=il.invoiceid JOIN track t ON il.trackid=t.trackid GROUP BY c.customerid, i.invoiceid, i.billingcity, c.city;

SELECT * FROM customer_album_orders ORDER BY customerid, invoiceid;

boxes/warehouse
-- Q3a) Box code with city name
SELECT b.code AS box_code,w.city FROM boxes b JOIN warehouses w ON b.warehouse=w.code;

-- Q3b) Warehouse codes with number of boxes
SELECT warehouse,COUNT(*) AS num_boxes FROM boxes GROUP BY warehouse;

-- Q3c) Saturated warehouses (boxes > capacity)
SELECT w.code FROM warehouses w JOIN (SELECT warehouse,COUNT(*) AS box_count FROM boxes GROUP BY warehouse) b ON w.code=b.warehouse WHERE b.box_count>w.capacity;

-- Q3d) Boxes in Chicago (subquery)
SELECT code FROM boxes WHERE warehouse IN (SELECT code FROM warehouses WHERE city='Chicago');

-- Q3e) All employee data including department data
SELECT e.*,d.* FROM employees e JOIN departments d ON e.department=d.code;

-- Q3f) Employee name, last name with department name and budget
SELECT e.name,e.last_name,d.name AS dept_name,d.budget FROM employees e JOIN departments d ON e.department=d.code;

-- Q3g) Employees in departments with budget > $60,000
SELECT e.name,e.last_name FROM employees e JOIN departments d ON e.department=d.code WHERE d.budget>60000;

-- Q3h) Departments with more than 2 employees (subquery)
SELECT name FROM departments WHERE code IN (SELECT department FROM employees GROUP BY department HAVING COUNT(*)>2);

-- Q3i) Employees in department with second lowest budget
SELECT e.name,e.last_name FROM employees e JOIN departments d ON e.department=d.code WHERE d.budget=(SELECT DISTINCT budget FROM departments ORDER BY budget ASC LIMIT 1 OFFSET 1);

-- Q3j) Number of employees per department
SELECT department AS dept_code,COUNT(*) AS num_employees FROM employees GROUP BY department;

movies/films
-- Q4a) Films with rental rate > average
SELECT title,rental_rate FROM film WHERE rental_rate>(SELECT AVG(rental_rate) FROM film);

-- Q4b) Movies starting with K or Q in English (subquery)
SELECT title FROM film WHERE (title LIKE 'K%' OR title LIKE 'Q%') AND language_id IN (SELECT language_id FROM language WHERE name='English');

-- Q4c) Cumulative revenue per customer
SELECT c.customer_id,c.first_name,c.last_name,p.payment_date,p.amount,SUM(p.amount) OVER(PARTITION BY c.customer_id ORDER BY p.payment_date) AS cumulative_revenue FROM customer c JOIN payment p ON c.customer_id=p.customer_id ORDER BY c.customer_id,p.payment_date;

-- Q4d) Customers spending more than average on rentals
SELECT c.customer_id,c.first_name,c.last_name,SUM(p.amount) AS total_spent FROM customer c JOIN payment p ON c.customer_id=p.customer_id GROUP BY c.customer_id,c.first_name,c.last_name HAVING SUM(p.amount)>(SELECT AVG(total) FROM (SELECT SUM(amount) AS total FROM payment GROUP BY customer_id) avg_tbl);

-- Q4e) Top 5 customers by highest total payments
SELECT c.customer_id,c.first_name,c.last_name,SUM(p.amount) AS total_payment FROM customer c JOIN payment p ON c.customer_id=p.customer_id GROUP BY c.customer_id,c.first_name,c.last_name ORDER BY total_payment DESC LIMIT 5;

-- Q4f) Customer names and film titles they rented
SELECT c.first_name,c.last_name,f.title FROM customer c JOIN rental r ON c.customer_id=r.customer_id JOIN inventory i ON r.inventory_id=i.inventory_id JOIN film f ON i.film_id=f.film_id ORDER BY c.last_name,c.first_name;

-- Q4g) Film with most actors
SELECT f.title,COUNT(fa.actor_id) AS actor_count FROM film f JOIN film_actor fa ON f.film_id=fa.film_id GROUP BY f.film_id,f.title ORDER BY actor_count DESC LIMIT 1;

-- Q4h) Film categories whose average length is above overall average
SELECT c.name AS category,AVG(f.length) AS avg_length FROM film f JOIN film_category fc ON f.film_id=fc.film_id JOIN category c ON fc.category_id=c.category_id GROUP BY c.name HAVING AVG(f.length)>(SELECT AVG(length) FROM film) ORDER BY avg_length DESC;

-- Q4i) Animation or Children films with id 50-100, sorted
SELECT f.film_id,f.title,c.name AS category_name FROM film f JOIN film_category fc ON f.film_id=fc.film_id JOIN category c ON fc.category_id=c.category_id WHERE c.name IN ('Animation','Children') AND f.film_id BETWEEN 50 AND 100 ORDER BY f.film_id;

 Superstore DB
-- Q3a) Total sales per region and ship mode in 2020
SELECT region,ship_mode,SUM(sales) AS total_sales FROM orders WHERE YEAR(order_date)=2020 GROUP BY region,ship_mode ORDER BY region,ship_mode;

-- Q3b) Print first and last name from customer_name column
SELECT customer_name,SUBSTRING_INDEX(customer_name,' ',1) AS first_name,SUBSTRING_INDEX(customer_name,' ',-1) AS last_name FROM orders;

-- Q3c) Segments where total sales exceed average across all segments
SELECT segment,SUM(sales) AS total_sales FROM orders GROUP BY segment HAVING SUM(sales)>(SELECT AVG(seg_total) FROM (SELECT SUM(sales) AS seg_total FROM orders GROUP BY segment) t);

-- Q3d) Month with highest average discount rate
SELECT MONTH(order_date) AS month_num,AVG(discount) AS avg_discount FROM orders GROUP BY MONTH(order_date) ORDER BY avg_discount DESC LIMIT 1;

-- Q3e) Moving average of sales per product over 3-month period
SELECT product_name,MONTH(order_date) AS month,SUM(sales) AS monthly_sales,AVG(SUM(sales)) OVER(PARTITION BY product_name ORDER BY MONTH(order_date) ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS moving_avg_3m FROM orders GROUP BY product_name,MONTH(order_date);

-- Q3f) Best-selling category (by quantity)
SELECT category,SUM(quantity) AS total_qty FROM orders GROUP BY category ORDER BY total_qty DESC LIMIT 1;

-- Q3f) Most profitable category
SELECT category,SUM(profit) AS total_profit FROM orders GROUP BY category ORDER BY total_profit DESC LIMIT 1;

-- Q3g) Top 5 most profitable months
SELECT DATE_FORMAT(order_date,'%Y-%m') AS month,SUM(profit) AS total_profit FROM orders GROUP BY DATE_FORMAT(order_date,'%Y-%m') ORDER BY total_profit DESC LIMIT 5;

-- Q3h) Country that sold the most products
SELECT country,SUM(quantity) AS total_products_sold FROM orders GROUP BY country ORDER BY total_products_sold DESC LIMIT 1;


Orders Schema (ClassicModels)
-- Q4a) Employees in Paris office (Method I: Correlated Subquery)
SELECT * FROM employees e WHERE EXISTS (SELECT 1 FROM offices o WHERE o.officeCode=e.officeCode AND o.city='Paris');

-- Q4a) Employees in Paris office (Method II: JOIN)
SELECT e.* FROM employees e JOIN offices o ON e.officeCode=o.officeCode WHERE o.city='Paris';

-- Q4b) Total value by USA customers for Classic Cars, sorted desc
SELECT c.customerName,SUM(od.quantityOrdered*od.priceEach) AS total_value FROM customers c JOIN orders o ON c.customerNumber=o.customerNumber JOIN orderdetails od ON o.orderNumber=od.orderNumber JOIN products p ON od.productCode=p.productCode JOIN productlines pl ON p.productLine=pl.productLine WHERE c.country='USA' AND pl.productLine='Classic Cars' GROUP BY c.customerName ORDER BY total_value DESC;

-- Q4c) Motorcycles not scale 1:18, sorted by scale then name
SELECT productName AS Bike_Name,productScale AS Scale,productDescription AS Description FROM products WHERE productLine='Motorcycles' AND productScale!='1:18' ORDER BY productScale ASC,productName ASC;

-- Q4d) Customers who have not ordered any products
SELECT c.customerNumber,c.customerName FROM customers c LEFT JOIN orders o ON c.customerNumber=o.customerNumber WHERE o.orderNumber IS NULL;

-- Q4e) Create VIEW TRAIN_ORDERS for 2003 Trains product line
CREATE VIEW TRAIN_ORDERS AS SELECT o.orderNumber,o.orderDate,o.shippedDate,o.customerNumber FROM orders o JOIN orderdetails od ON o.orderNumber=od.orderNumber JOIN products p ON od.productCode=p.productCode WHERE YEAR(o.orderDate)=2003 AND p.productLine='Trains';

AustraliaWeather

-- Q3a) Average rainfall and evaporation per Location (exclude NULL evaporation)
SELECT Location,AVG(Rainfall) AS Avg_Rainfall,AVG(CAST(Evaporation AS DECIMAL(10,2))) AS Avg_Evaporation FROM australiaweather WHERE Evaporation IS NOT NULL GROUP BY Location;

-- Q3b) Max temperature morning and afternoon per location per month
SELECT Location,MONTH(STR_TO_DATE(Date,'%Y-%m-%d')) AS Month,MAX(Temp9am) AS Max_Morning_Temp,MAX(Temp3pm) AS Max_Afternoon_Temp FROM australiaweather GROUP BY Location,MONTH(STR_TO_DATE(Date,'%Y-%m-%d')) ORDER BY Location,Month;

-- Q3c) Add column Pressure9pm (INT, DEFAULT 1001, NOT NULL)
ALTER TABLE australiaweather ADD COLUMN Pressure9pm INT NOT NULL DEFAULT 1001;

-- Q3d) Compare avg rainfall Jan 2008 vs July 2008
SELECT AVG(CASE WHEN MONTH(STR_TO_DATE(Date,'%Y-%m-%d'))=1 AND YEAR(STR_TO_DATE(Date,'%Y-%m-%d'))=2008 THEN Rainfall END) AS Avg_Rainfall_Jan_2008,AVG(CASE WHEN MONTH(STR_TO_DATE(Date,'%Y-%m-%d'))=7 AND YEAR(STR_TO_DATE(Date,'%Y-%m-%d'))=2008 THEN Rainfall END) AS Avg_Rainfall_Jul_2008 FROM australiaweather;

-- Q3e) Total daily humidity, compare avg humidity Jan 2009 vs Feb 2009
SELECT AVG(CASE WHEN MONTH(STR_TO_DATE(Date,'%Y-%m-%d'))=1 AND YEAR(STR_TO_DATE(Date,'%Y-%m-%d'))=2009 THEN (Humidity9am+Humidity3pm) END) AS Avg_Total_Humidity_Jan,AVG(CASE WHEN MONTH(STR_TO_DATE(Date,'%Y-%m-%d'))=2 AND YEAR(STR_TO_DATE(Date,'%Y-%m-%d'))=2009 THEN (Humidity9am+Humidity3pm) END) AS Avg_Total_Humidity_Feb FROM australiaweather;

-- Q3f) Highest morning pressure per location per month with filters
SELECT Location,MONTH(STR_TO_DATE(Date,'%Y-%m-%d')) AS Month,MAX(Pressure9am) AS Highest_Morning_Pressure FROM australiaweather WHERE Evaporation IS NOT NULL AND Temp9am BETWEEN 14 AND 30 GROUP BY Location,MONTH(STR_TO_DATE(Date,'%Y-%m-%d')) HAVING MAX(Humidity9am)<=70 ORDER BY Location,Month;

Formula 1 Racing
-- Q4a) Circuits where no races have been held (Method I: LEFT JOIN)
SELECT c.* FROM circuits c LEFT JOIN races r ON c.circuitId=r.circuitId WHERE r.raceId IS NULL;

-- Q4a) Circuits where no races have been held (Method II: NOT EXISTS)
SELECT c.* FROM circuits c WHERE NOT EXISTS (SELECT 1 FROM races r WHERE r.circuitId=c.circuitId);

-- Q4a) Circuits where no races have been held (Method III: NOT IN)
SELECT * FROM circuits WHERE circuitId NOT IN (SELECT DISTINCT circuitId FROM races);

-- Q4b) Driver with shortest lap time
SELECT d.driverId,d.forename,d.surname,d.nationality,lt.milliseconds AS shortest_lap_ms FROM laptimes lt JOIN drivers d ON lt.driverId=d.driverId WHERE lt.milliseconds=(SELECT MIN(milliseconds) FROM laptimes);

-- Q4c) Rank drivers by accumulated points
SELECT d.driverId,d.forename,d.surname,SUM(r.points) AS total_points,RANK() OVER(ORDER BY SUM(r.points) DESC) AS driver_rank FROM results r JOIN drivers d ON r.driverId=d.driverId GROUP BY d.driverId,d.forename,d.surname ORDER BY total_points DESC;

-- Q4d) Create view driver details with total races played, sorted desc
CREATE VIEW driver_race_count AS SELECT d.driverId,d.forename,d.surname,d.dob,d.nationality,COUNT(DISTINCT r.raceId) AS total_races FROM drivers d LEFT JOIN results r ON d.driverId=r.driverId GROUP BY d.driverId,d.forename,d.surname,d.dob,d.nationality ORDER BY total_races DESC;

-- Q4e) Report: race details with driver, points, laps, duration
SELECT ra.raceId,ra.name AS race_name,d.forename,d.surname,re.points,re.laps,re.milliseconds FROM races ra JOIN results re ON ra.raceId=re.raceId JOIN drivers d ON re.driverId=d.driverId ORDER BY ra.raceId,re.points DESC;

-- SECTION B – Project / Marketing / Indian Food

-- Q3a) Reporting manager, client and project for every employee
SELECT r.employee_name,r.manager_name,p.project_name,c.client_name FROM resources r JOIN projects p ON r.project_id=p.project_id JOIN clients c ON p.client_id=c.client_id;

-- Q3b) Inactive clients (no active projects)
SELECT c.client_id,c.client_name,c.client_country FROM clients c LEFT JOIN projects p ON c.client_id=p.client_id WHERE p.project_id IS NULL;

-- Q3c) Conversion rate (CVR) for gsearch nonbrand sessions
SELECT COUNT(DISTINCT s.session_id) AS Sessions,COUNT(DISTINCT o.order_id) AS Orders,COUNT(DISTINCT o.order_id)/COUNT(DISTINCT s.session_id)*100 AS Conversion FROM sessions_website s LEFT JOIN orders o ON s.session_id=o.session_id WHERE s.utm_source='gsearch' AND s.utm_campaign='nonbrand' AND s.created_at<='2020-08-24';

-- Q3d) Monthly session volume by device, gsearch vs bsearch
SELECT DATE_FORMAT(created_at,'%Y-%m-01') AS month_start_date,SUM(CASE WHEN utm_source='gsearch' AND device_type='desktop' THEN 1 ELSE 0 END) AS g_dtop_sessions,SUM(CASE WHEN utm_source='bsearch' AND device_type='desktop' THEN 1 ELSE 0 END) AS b_dtop_sessions,SUM(CASE WHEN utm_source='bsearch' AND device_type='desktop' THEN 1 ELSE 0 END)/SUM(CASE WHEN utm_source='gsearch' AND device_type='desktop' THEN 1 ELSE 0 END) AS b_pct_of_g_dtop,SUM(CASE WHEN utm_source='gsearch' AND device_type='mobile' THEN 1 ELSE 0 END) AS g_mob_sessions,SUM(CASE WHEN utm_source='bsearch' AND device_type='mobile' THEN 1 ELSE 0 END) AS b_mob_sessions,SUM(CASE WHEN utm_source='bsearch' AND device_type='mobile' THEN 1 ELSE 0 END)/SUM(CASE WHEN utm_source='gsearch' AND device_type='mobile' THEN 1 ELSE 0 END) AS b_pct_of_g_mob FROM sessions_website WHERE utm_campaign='nonbrand' AND created_at BETWEEN '2012-08-01' AND '2012-12-22' GROUP BY DATE_FORMAT(created_at,'%Y-%m-01');

-- Q3e(i)) Rank dishes by cook_time (longest first)
SELECT name,ingredients,cook_time,RANK() OVER(ORDER BY cook_time DESC) AS rnk FROM indian_food;

-- Q3e(ii)) Dish with minimum cook time per course type
WITH ranked AS (SELECT name,ingredients,cook_time,course,ROW_NUMBER() OVER(PARTITION BY course ORDER BY cook_time ASC) AS rn FROM indian_food) SELECT name,ingredients,cook_time,course FROM ranked WHERE rn=1;


-- SECTION C – Clothing DB + Transactions

-- Q4a(i)) 5% discount on accessories (old and new price)
SELECT c.Catalogue_Entry_Description,p.price AS Old_Price,p.price*0.95 AS New_Price FROM products p JOIN catalogue c ON p.catalogue_entry_id=c.catalogue_entry_id WHERE c.Catalogue_Entry_Description LIKE '%Accessories%' OR c.parent_catalogue_entry_id IN (SELECT catalogue_entry_id FROM catalogue WHERE Catalogue_Entry_Description LIKE '%Accessories%');

-- Q4a(ii)) Catalogue items with average price > 1000
SELECT catalogue_entry_id,AVG(price) AS avg_price FROM products GROUP BY catalogue_entry_id HAVING AVG(price)>1000;

-- Q4a(iii)) Count products per catalogue_entry_id
SELECT catalogue_entry_id,COUNT(*) AS product_count FROM products GROUP BY catalogue_entry_id;

-- Q4a(iv)) Self-join: item, sub-category, main category
SELECT c1.Catalogue_Entry_Description AS Prod_Desc,c2.Catalogue_Entry_Description AS Sub_Prod_Desc,c3.Catalogue_Entry_Description AS Main_Prod_Desc FROM catalogue c1 JOIN catalogue c2 ON c1.parent_catalogue_entry_id=c2.catalogue_entry_id JOIN catalogue c3 ON c2.parent_catalogue_entry_id=c3.catalogue_entry_id;

-- Q4a(v)) Complete details of available Adidas shirts
SELECT p.*,c.Catalogue_Entry_Description,s.size_name,cl.color_name FROM products p JOIN catalogue c ON p.catalogue_entry_id=c.catalogue_entry_id JOIN sizes s ON p.size_id=s.size_id JOIN colors cl ON p.color_id=cl.color_id WHERE p.product_name LIKE '%Adidas%' AND c.Catalogue_Entry_Description LIKE '%Shirt%';

-- Q4b) Transaction Control: Undo accidental update
SET autocommit=0;
SAVEPOINT a;
UPDATE clients SET client_country='India';
ROLLBACK TO SAVEPOINT a;
SELECT * FROM clients;

-- SECTION B – Open University + InpatientCharges

-- Q3a) Students >150 credits more likely to withdraw? Analyse
SELECT CASE WHEN c.module_presentation_length>150 THEN 'More_credits' ELSE 'Fewer_Credits' END AS Credits,COUNT(DISTINCT si.id_student) AS student_withdraw_count FROM studentinfo si JOIN studentregistration sr ON si.id_student=sr.id_student JOIN courses c ON sr.code_module=c.code_module AND sr.code_presentation=c.code_presentation WHERE sr.date_unregistration IS NOT NULL GROUP BY CASE WHEN c.module_presentation_length>150 THEN 'More_credits' ELSE 'Fewer_Credits' END;

-- Q3b) Regions with least enrollments
SELECT si.region,COUNT(*) AS enrollment_count FROM studentinfo si GROUP BY si.region ORDER BY enrollment_count ASC;

-- Q3c) Students with assessments + students without (LEFT JOIN)
SELECT si.id_student,a.code_module,a.code_presentation,a.assessment_type,sa.date_submitted AS date FROM studentinfo si LEFT JOIN studentassessment sa ON si.id_student=sa.id_student LEFT JOIN assessments a ON sa.id_assessment=a.id_assessment;

-- Q3d) Discharges per provider, least on top (Inpatient)
SELECT provider_id,Provider_Name,SUM(Total_Discharges) AS total_discharges FROM InpatientCharges GROUP BY provider_id,Provider_Name ORDER BY total_discharges ASC;

-- Q3e) Insurance coverage ratio by provider
SELECT provider_id,Provider_Name,(AVG(Average_Covered_Charges)/(AVG(Average_Covered_Charges)+AVG(Average_Total_Payments)+AVG(Average_Medicare_Payments)))*100 AS Insurance_coverage_ratio FROM InpatientCharges GROUP BY provider_id,Provider_Name ORDER BY Insurance_coverage_ratio DESC;


-- SECTION C – Sports / Elections / Music / Movies

-- Q4a(i)) Arsenal wins both home and away
SELECT h.opponent FROM home h JOIN away a ON h.opponent=a.opponent WHERE h.goals_scored>h.goals_conceded AND a.goals_scored>a.goals_conceded;

-- Q4a(ii)) Person MP+MLA with longest gap between elections
SELECT mp.name,ABS(DATEDIFF(STR_TO_DATE(mp.date,'%Y-%d-%m'),STR_TO_DATE(mla.date,'%Y-%d-%m'))) AS gap_days FROM MP mp JOIN MLA mla ON mp.name=mla.name ORDER BY gap_days DESC LIMIT 1;

-- Q4a(iii)) Songs with longest length using window functions
SELECT songName,artisteName,songLength,artist_id FROM (SELECT *,RANK() OVER(ORDER BY songLength DESC) AS rnk FROM Song_artiste) ranked WHERE rnk=1;

-- Q4a(iv)) Create view movie_details
CREATE VIEW movie_details AS SELECT m.movieTitle,m.movieRating,g.genreType,m.movieRuntime FROM Movie m JOIN Movie_Genre mg ON m.movieID=mg.movieID JOIN Genre g ON mg.genreID=g.genreID;

-- Q4a(iv)) Highest runtime movie per genre
SELECT movieTitle,movieRating,genreType,movieRuntime,ranking FROM (SELECT *,RANK() OVER(PARTITION BY genreType ORDER BY movieRuntime DESC) AS ranking FROM movie_details) t WHERE ranking=1;

--restaurants  queries
-- Q4a(v)) Movies with max runtime excluding 'Two imprisoned men'
SELECT m.movieID,m.movieTitle,g.genreType,m.movieRuntime FROM Movie m JOIN Movie_Genre mg ON m.movieID=mg.movieID JOIN Genre g ON mg.genreID=g.genreID WHERE m.movieRuntime=(SELECT MAX(movieRuntime) FROM Movie WHERE movieTitle!='Two imprisoned men') AND m.movieTitle!='Two imprisoned men';

-- Q4a(vi)) Movie details with earliest release date per genre
SELECT m.movieTitle,m.movieRating,g.genreType,m.movieReleaseDate,FIRST_VALUE(m.movieReleaseDate) OVER(PARTITION BY g.genreType ORDER BY m.movieReleaseDate) AS first_release_date_of_genre FROM Movie m JOIN Movie_Genre mg ON m.movieID=mg.movieID JOIN Genre g ON mg.genreID=g.genreID;

-- Q3a) Restaurants with at least one order
SELECT DISTINCT r.restaurant_id,r.restaurant_name FROM restaurants r JOIN orders o ON r.restaurant_id=o.restaurant_id ORDER BY r.restaurant_name;

-- Q3b) Customers who have not placed any orders
SELECT COUNT(*) AS customers_without_orders FROM customers c LEFT JOIN orders o ON c.customer_id=o.customer_id WHERE o.order_id IS NULL;

-- Q3c) Top 3 most expensive food items in each restaurant
SELECT ranked.restaurant_id,ranked.food_id,ranked.food_name,ranked.price,ranked.price_rank FROM (SELECT fi.*,DENSE_RANK() OVER(PARTITION BY restaurant_id ORDER BY price DESC) AS price_rank FROM food_items fi) ranked WHERE ranked.price_rank<=3 ORDER BY ranked.restaurant_id,ranked.price DESC;

-- Q3d) Average rating per restaurant
SELECT r.restaurant_id,r.restaurant_name,AVG(o.restaurant_rating) AS avg_rating FROM restaurants r JOIN orders o ON r.restaurant_id=o.restaurant_id GROUP BY r.restaurant_id,r.restaurant_name ORDER BY avg_rating DESC;

-- Q3d) Average rating per delivery partner
SELECT dp.delivery_partner_id,dp.partner_name,AVG(o.delivery_rating) AS avg_rating FROM delivery_partners dp JOIN orders o ON dp.delivery_partner_id=o.delivery_partner_id GROUP BY dp.delivery_partner_id,dp.partner_name ORDER BY avg_rating DESC;

-- Q3e) Average price of vegetarian dishes per restaurant
SELECT r.restaurant_id,r.restaurant_name,AVG(fi.price) AS avg_veg_price,COUNT(fi.food_id) AS num_veg_items FROM restaurants r JOIN food_items fi ON r.restaurant_id=fi.restaurant_id WHERE fi.type='Veg' GROUP BY r.restaurant_id,r.restaurant_name ORDER BY avg_veg_price DESC;

-- Q3f) Top 3 cuisines by total order amount
SELECT r.cuisine,SUM(o.total_amount) AS total_revenue,COUNT(o.order_id) AS order_count FROM restaurants r JOIN orders o ON r.restaurant_id=o.restaurant_id GROUP BY r.cuisine ORDER BY total_revenue DESC LIMIT 3;

-- Q3g) Compare item price with restaurant average
SELECT r.restaurant_name,fi.food_name,fi.price,AVG(fi.price) OVER(PARTITION BY fi.restaurant_id) AS avg_price_in_restaurant,fi.price-AVG(fi.price) OVER(PARTITION BY fi.restaurant_id) AS diff_from_avg,CASE WHEN fi.price>AVG(fi.price) OVER(PARTITION BY fi.restaurant_id) THEN 'Above Avg' WHEN fi.price<AVG(fi.price) OVER(PARTITION BY fi.restaurant_id) THEN 'Below Avg' ELSE 'At Avg' END AS comparison FROM food_items fi JOIN restaurants r ON fi.restaurant_id=r.restaurant_id ORDER BY r.restaurant_name,fi.price DESC;


-- SECTION C – Movies Database

-- Q4a) Movies released before 1998
SELECT mov_title FROM movie WHERE mov_year<1998 ORDER BY mov_year;

-- Q4b) All reviewers and movies in one list
SELECT rev_name AS name,'Reviewer' AS entity_type FROM reviewer UNION ALL SELECT mov_title AS name,'Movie' AS entity_type FROM movie ORDER BY entity_type,name;

-- Q4c) Cumulative count of reviews per movie
SELECT m.mov_title,r.rev_id,r.rev_stars,COUNT(*) OVER(PARTITION BY r.mov_id ORDER BY r.rev_id) AS cumulative_reviews FROM rating r JOIN movie m ON r.mov_id=m.mov_id ORDER BY m.mov_title,r.rev_id;

-- Q4d) Movies without any rating (using subquery)
SELECT mov_title FROM movie WHERE mov_id NOT IN (SELECT mov_id FROM rating WHERE rev_stars IS NOT NULL);

-- Q4e) Actors in 'Annie Hall'
SELECT a.* FROM actor a JOIN movie_cast mc ON a.act_id=mc.act_id JOIN movie m ON mc.mov_id=m.mov_id WHERE m.mov_title='Annie Hall';

-- Q4f) Movies with the lowest ratings
SELECT rev.rev_name,m.mov_title,r.rev_stars FROM rating r JOIN movie m ON r.mov_id=m.mov_id JOIN reviewer rev ON r.rev_id=rev.rev_id WHERE r.rev_stars=(SELECT MIN(rev_stars) FROM rating WHERE rev_stars IS NOT NULL);

-- Q4g) Actors not appearing in any movies between 1990 and 2000
SELECT a.act_fname,a.act_lname,m.mov_title,m.mov_year FROM actor a JOIN movie_cast mc ON a.act_id=mc.act_id JOIN movie m ON mc.mov_id=m.mov_id WHERE a.act_id NOT IN (SELECT mc2.act_id FROM movie_cast mc2 JOIN movie m2 ON mc2.mov_id=m2.mov_id WHERE m2.mov_year BETWEEN 1990 AND 2000) ORDER BY a.act_lname,a.act_fname,m.mov_year;

-- Q4h) Years with movies rated 3 or 4 stars
SELECT DISTINCT m.mov_year FROM movie m JOIN rating r ON m.mov_id=r.mov_id WHERE r.rev_stars IN (3,4) ORDER BY m.mov_year ASC;


-- Q3a) Total & Average Salary by Department
SELECT d.department_name,SUM(e.salary) AS total_salary,AVG(e.salary) AS avg_salary FROM departments d JOIN employees e ON d.department_id=e.department_id GROUP BY d.department_id,d.department_name ORDER BY total_salary DESC;

-- Q3b) Top 3 Employees by Tenure
SELECT first_name,last_name,hire_date,TIMESTAMPDIFF(YEAR,hire_date,CURDATE()) AS tenure_years FROM employees ORDER BY tenure_years DESC LIMIT 3;

-- Q3c) Employees on More Than One Project
SELECT e.first_name,e.last_name,COUNT(DISTINCT ep.project_id) AS total_projects FROM employees e JOIN employee_projects ep ON e.employee_id=ep.employee_id GROUP BY e.employee_id,e.first_name,e.last_name HAVING COUNT(DISTINCT ep.project_id)>1 ORDER BY e.first_name,e.last_name;

-- Q3d) Project Budget + Average Employee Salary
SELECT p.project_id,p.project_name,p.budget,AVG(e.salary) AS avg_employee_salary,COUNT(DISTINCT e.employee_id) AS num_employees FROM projects p JOIN employee_projects ep ON p.project_id=ep.project_id JOIN employees e ON ep.employee_id=e.employee_id GROUP BY p.project_id,p.project_name,p.budget ORDER BY p.budget DESC;

-- Q3e) Bonus-Eligible Employees (Above Average) + Rank
SELECT first_name,last_name,salary,RANK() OVER(ORDER BY salary DESC) AS salary_rank FROM employees WHERE salary>(SELECT AVG(salary) FROM employees) ORDER BY salary DESC;

-- Q3f) Top 3 Projects by Total Salary Cost
SELECT p.project_name,p.budget,SUM(e.salary) AS total_salary_cost,COUNT(DISTINCT e.employee_id) AS num_employees FROM projects p JOIN employee_projects ep ON p.project_id=ep.project_id JOIN employees e ON ep.employee_id=e.employee_id GROUP BY p.project_id,p.project_name,p.budget ORDER BY total_salary_cost DESC LIMIT 3;

-- Q3g) Top 3 Highest-Paid Employees per Department
SELECT first_name,last_name,salary,department_id FROM (SELECT e.*,DENSE_RANK() OVER(PARTITION BY department_id ORDER BY salary DESC) AS rk FROM employees e) ranked WHERE rk<=3 ORDER BY department_id,salary DESC;

-- Q3h) Cumulative Salary by Hire Date
SELECT first_name,last_name,hire_date,salary,SUM(salary) OVER(ORDER BY hire_date) AS cumulative_salary FROM employees ORDER BY hire_date;


-- SECTION C

-- Q4a) Departments with ≥ 10 High-Earners
SELECT d.department_name,d.location,COUNT(e.employee_id) AS qualifying_employees FROM departments d JOIN employees e ON d.department_id=e.department_id WHERE e.salary>60000 GROUP BY d.department_id,d.department_name,d.location HAVING COUNT(e.employee_id)>=10 ORDER BY qualifying_employees DESC;

-- Q4b) Highest Salary in Marketing
SELECT e.first_name,e.last_name,e.salary FROM employees e JOIN departments d ON e.department_id=d.department_id WHERE d.department_name='Marketing' AND e.salary=(SELECT MAX(e2.salary) FROM employees e2 JOIN departments d2 ON e2.department_id=d2.department_id WHERE d2.department_name='Marketing');

-- Q4c) Min/Max/Avg Salary per Department (≥ 5 Employees)
SELECT d.department_name,MIN(e.salary) AS min_salary,MAX(e.salary) AS max_salary,AVG(e.salary) AS avg_salary,COUNT(e.employee_id) AS num_employees FROM departments d JOIN employees e ON d.department_id=e.department_id GROUP BY d.department_id,d.department_name HAVING COUNT(e.employee_id)>=5 ORDER BY avg_salary DESC;

-- Q4d) Salary > Finance Department Average (Subquery)
SELECT e.first_name,e.last_name,d.department_name,e.salary FROM employees e JOIN departments d ON e.department_id=d.department_id WHERE e.salary>(SELECT AVG(e2.salary) FROM employees e2 JOIN departments d2 ON e2.department_id=d2.department_id WHERE d2.department_name='Finance') ORDER BY e.salary DESC;

-- Q4e) Create View HighSalaryEmployees
CREATE OR REPLACE VIEW HighSalaryEmployees AS SELECT e.first_name,e.last_name,e.salary,d.department_name FROM employees e JOIN departments d ON e.department_id=d.department_id WHERE (e.department_id,e.salary) IN (SELECT department_id,MAX(salary) FROM employees GROUP BY department_id);

-- Q4e) Display HighSalaryEmployees View
SELECT * FROM HighSalaryEmployees ORDER BY department_name;

-- Q4f) Employees on Above-Average-Budget Projects
SELECT DISTINCT e.first_name,e.last_name,p.project_name,p.budget FROM employees e JOIN employee_projects ep ON e.employee_id=ep.employee_id JOIN projects p ON ep.project_id=p.project_id WHERE p.budget>(SELECT AVG(budget) FROM projects) ORDER BY p.budget DESC,e.first_name;
'''
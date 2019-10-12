# ############
# Basic Select
# ############

# https://www.hackerrank.com/challenges/weather-observation-station-3/problem
SELECT DISTINCT CITY FROM STATION WHERE id % 2 = 0;

# https://www.hackerrank.com/challenges/weather-observation-station-4/problem
SELECT COUNT(CITY) - COUNT(DISTINCT CITY) from STATION;

# https://www.hackerrank.com/challenges/weather-observation-station-5/problem
SELECT CITY, LENGTH(CITY) as len FROM STATION ORDER BY len ASC, CITY ASC limit 1;
SELECT CITY, LENGTH(CITY) as len FROM STATION ORDER BY len DESC, CITY ASC limit 1;

# https://www.hackerrank.com/challenges/weather-observation-station-6/problem
SELECT CITY FROM STATION WHERE CITY REGEXP '^[aeiouAEIOU]';

# https://www.hackerrank.com/challenges/weather-observation-station-7/problem
SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP '[aeiouAEIOU]$';

# https://www.hackerrank.com/challenges/weather-observation-station-8/problem
SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP '^[aeiouAEIOU].*[aeiouAEIOU]$';

# https://www.hackerrank.com/challenges/weather-observation-station-9/problem
SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP '^[^aeiouAEIOU]';

# https://www.hackerrank.com/challenges/weather-observation-station-10/problem
SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP '[^aeiouAEIOU]$';

# https://www.hackerrank.com/challenges/weather-observation-station-11/problem
SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP '^[^aeiouAEIOU]' OR CITY REGEXP '[^aeiouAEIOU]$';

# https://www.hackerrank.com/challenges/weather-observation-station-12/problem
SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP '^[^aeiouAEIOU].*[^aeiouAEIOU]$';

# https://www.hackerrank.com/challenges/more-than-75-marks/problem
SELECT NAME FROM STUDENTS WHERE MARKS > 75 ORDER BY RIGHT(NAME, 3) ASC, ID ASC;

# https://www.hackerrank.com/challenges/name-of-employees/problem
SELECT NAME FROM EMPLOYEE ORDER BY NAME ASC;

# https://www.hackerrank.com/challenges/salary-of-employees/problem
SELECT NAME FROM EMPLOYEE WHERE SALARY > 2000 AND MONTHS < 10 ORDER BY EMPLOYEE_ID ASC;


# ###############
# Advanced Select
# ###############

# https://www.hackerrank.com/challenges/what-type-of-triangle/problem
SELECT CASE
WHEN A + B <= C OR A + C <= B OR C + B <= A THEN 'Not A Triangle'
WHEN A = B AND B = C THEN 'Equilateral'
WHEN A = B OR B = C OR A = C THEN 'Isosceles'
ELSE 'Scalene'
END
FROM TRIANGLES;

# https://www.hackerrank.com/challenges/the-pads/problem
SELECT CONCAT(NAME, '(', SUBSTR(OCCUPATION, 1, 1) ,')') as N FROM OCCUPATIONS ORDER BY N;
SELECT CONCAT('There are a total of ', COUNT(OCCUPATION), ' ', LOWER(OCCUPATION), 's.') FROM OCCUPATIONS
GROUP BY OCCUPATION
ORDER BY COUNT(OCCUPATION), OCCUPATION;

# https://www.hackerrank.com/challenges/occupations/problem ???
SET @r1=0, @r2=0, @r3=0, @r4=0;
SELECT MIN(DOCTOR), MIN(PROFESSOR), MIN(SINGER), MIN(ACTOR)
FROM(
  SELECT CASE WHEN OCCUPATION = 'Doctor' THEN (@r1:=@r1+1)
              WHEN OCCUPATION = 'Professor' THEN (@r2:=@r2+1)
              WHEN OCCUPATION = 'Singer' THEN (@r3:=@r3+1)
              WHEN OCCUPATION = 'Actor' THEN (@r4:=@r4+1) END AS RowNumber,
    CASE WHEN OCCUPATION = 'Doctor' THEN Name END AS Doctor,
    CASE WHEN OCCUPATION = 'Professor' THEN Name END AS Professor,
    CASE WHEN OCCUPATION = 'Singer' THEN Name END AS Singer,
    CASE WHEN OCCUPATION = 'Actor' THEN Name END AS Actor
  FROM OCCUPATIONS
  ORDER BY NAME
) Temp
GROUP BY RowNumber;

# https://www.hackerrank.com/challenges/binary-search-tree-1/problem ???
SELECT N, CASE WHEN P IS NULL THEN 'Root'
WHEN(SELECT COUNT(*) FROM BST WHERE P = A.N) > 0 THEN 'Inner'
ELSE 'Leaf'
END
FROM BST A
ORDER BY N;

# https://www.hackerrank.com/challenges/the-company/problem
SELECT COMPANY_CODE, FOUNDER,
(SELECT COUNT(DISTINCT LEAD_MANAGER_CODE) FROM LEAD_MANAGER WHERE COMPANY_CODE = C.COMPANY_CODE),
(SELECT COUNT(DISTINCT SENIOR_MANAGER_CODE) FROM SENIOR_MANAGER WHERE COMPANY_CODE = C.COMPANY_CODE),
(SELECT COUNT(DISTINCT MANAGER_CODE) FROM MANAGER WHERE COMPANY_CODE = C.COMPANY_CODE),
(SELECT COUNT(DISTINCT EMPLOYEE_CODE) FROM EMPLOYEE WHERE COMPANY_CODE = C.COMPANY_CODE)
FROM COMPANY C
ORDER BY COMPANY_CODE;


# ###########
# Aggregation
# ###########

# https://www.hackerrank.com/challenges/revising-aggregations-the-count-function/problem
SELECT COUNT(*) FROM CITY WHERE POPULATION > 100000;

# https://www.hackerrank.com/challenges/revising-aggregations-sum/problem
SELECT SUM(POPULATION) FROM CITY WHERE DISTRICT = "California";

# https://www.hackerrank.com/challenges/revising-aggregations-the-average-function/problem
SELECT AVG(POPULATION) FROM CITY WHERE DISTRICT = "California";

# https://www.hackerrank.com/challenges/average-population/problem
SELECT FLOOR(AVG(POPULATION)) FROM CITY;

# https://www.hackerrank.com/challenges/japan-population/problem
SELECT SUM(POPULATION) FROM CITY WHERE COUNTRYCODE = "JPN";

# https://www.hackerrank.com/challenges/population-density-difference/problem
SELECT MAX(POPULATION) - MIN(POPULATION) FROM CITY LIMIT 1;

# https://www.hackerrank.com/challenges/earnings-of-employees/problem
SELECT MAX(SALARY*MONTHS), COUNT(*) FROM EMPLOYEE WHERE (SALARY*MONTHS) = (SELECT MAX(SALARY*MONTHS) FROM EMPLOYEE);

# https://www.hackerrank.com/challenges/weather-observation-station-2/problem
SELECT ROUND(SUM(LAT_N), 2), ROUND(SUM(LONG_W), 2) FROM STATION;

# https://www.hackerrank.com/challenges/weather-observation-station-13/problem
SELECT ROUND(SUM(LAT_N), 4) FROM STATION WHERE LAT_N > 38.7880 AND LAT_N < 137.2345;

# https://www.hackerrank.com/challenges/weather-observation-station-14/problem
SELECT ROUND(MAX(LAT_N), 4) FROM STATION WHERE LAT_N < 137.2345;

# https://www.hackerrank.com/challenges/weather-observation-station-15/problem
SELECT ROUND(LONG_W, 4) FROM STATION WHERE LAT_N IN (SELECT MAX(LAT_N) FROM STATION WHERE LAT_N < 137.2345);

# https://www.hackerrank.com/challenges/weather-observation-station-16/problem
SELECT ROUND(MIN(LAT_N), 4) FROM STATION WHERE LAT_N > 38.7780;

# https://www.hackerrank.com/challenges/weather-observation-station-17/problem
SELECT ROUND(LONG_W, 4) FROM STATION WHERE LAT_N IN (SELECT MIN(LAT_N) FROM STATION WHERE LAT_N > 38.7780);

# https://www.hackerrank.com/challenges/weather-observation-station-18/problem
SELECT ROUND((MAX(LAT_N) - MIN(LAT_N))+(MAX(LONG_W) - MIN(LONG_W)), 4) FROM STATION;

# https://www.hackerrank.com/challenges/weather-observation-station-19/problem
SELECT ROUND(SQRT(POWER(MIN(LAT_N)-MAX(LAT_N),2)+POWER(MIN(LONG_W)-MAX(LONG_W),2)),4) FROM STATION;

# https://www.hackerrank.com/challenges/the-blunder/problem
SELECT CEIL(AVG(SALARY) - AVG(REPLACE(SALARY, '0', ''))) FROM EMPLOYEES;

# https://www.hackerrank.com/challenges/weather-observation-station-20/problem
SELECT ROUND(S.LAT_N, 4) FROM STATION S
    WHERE
        (SELECT COUNT(LAT_N) FROM STATION WHERE LAT_N > S.LAT_N)
        = (SELECT COUNT(LAT_N) FROM STATION WHERE LAT_N < S.LAT_N);


# ##########
# Basic Join
# ##########



# #############
# Advanced Join
# #############



# #################
# Alternate Queries
# #################




# ~~~> https://github.com/BlakeBrown/HackerRank-Solutions/tree/master/SQL

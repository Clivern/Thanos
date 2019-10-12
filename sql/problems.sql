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



# ###########
# Aggregation
# ###########



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

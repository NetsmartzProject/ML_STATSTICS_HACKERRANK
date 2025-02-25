

# Query the list of CITY names from STATION that do not end with vowels. Your result cannot contain duplicates.




# SELECT DISTINCT CITY
# FROM STATION
# WHERE RIGHT(CITY, 1) NOT IN ('a', 'e', 'i', 'o', 'u');


# SELECT DISTINCT CITY: This selects the CITY column from the STATION table and ensures that only unique city names are returned.

# FROM STATION: Specifies the table to retrieve data from, which is STATION.

# WHERE RIGHT(CITY, 1) NOT IN ('a', 'e', 'i', 'o', 'u'):

# RIGHT(CITY, 1): This function extracts the rightmost character (the last letter) of the CITY string.

# NOT IN ('a', 'e', 'i', 'o', 'u'): This condition filters the results, including only those cities where the last letter is not one of the vowels ('a', 'e', 'i', 'o', 'u').


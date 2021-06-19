# Data Modelling with PostgreSQL
## Overview 
In this project we will analyze a data set based on a sample of serial killers from the Radford/FGCU Serial Killer Database (https://www.fgcu.edu/skdb/). To analyze the data, the first thing we need to do is ETL process, once the data is populated in PostgreSQL database, we will answer below questions by writing PostgreSQL queries.
- Find the number of killers by motive and age is between 15 to 30.
- Find the number of female killers born after 1950 and motive of crime is enjoyment or power.
- Find the average age of killers for both male and female when they committed first kill.
- Find the ratio of male killers to female killers where age at last kill is greater than 50 years old.

## Dataset 
Source data is in csv format.
some sample records:
[![dataset.jpg](https://i.postimg.cc/VvWtq0PB/dataset.jpg)](https://postimg.cc/XBXX3JJp)

## Schema
### Target Tables
Killers_bio – contains data about killers basic information.
~~~
columns: killerID,YearBorn,Race,Sex
~~~
Killers_additional_details – contains additional details of killer’s data.
~~~
columns: KillerID,AgeFirstKill,AgeLastKill,Motive,Sentence,InsanityPlea
~~~

## Project Scripts
- sql_queries_script.py -> this script file contains sql commands to create and drop target tables. It also contains sql queries for inserting records into a table.
- create_db_and_tables.py -> Executing this script will create mysparkdb database and target tables in PostgreSQL environment 
- ETL.ipynb -> a Jupiter notebook to process data from source dataset to target tables step by step.
- ETL.py –> complete ETL python script which takes data from input files and loads into target tables.
- test_query_tables.ipynb -> a Jupiter notebook to test target tables and it also contains sql solutions to the questions stated in overview.

## Execution steps
~~~
Step 1:  python create_db_and_tables.py
Step 2 : python ETL.py
~~~

## Environment
Python 3.6 or above

PostgresSQL 9.5 or above

psycopg2 - PostgreSQL database adapter for Python

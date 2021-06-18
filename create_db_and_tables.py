#!/usr/bin/env python
# coding: utf-8

import psycopg2
from sql_queries_script import create_table_queries, drop_table_queries


def create_database():
    """
    Establishes database connection and return's the connection and cursor references.
    """
    conn = psycopg2.connect("host=127.0.0.1 dbname=postgres user=postgres password=1234")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # create myspark database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS mysparkdb")
    cur.execute("CREATE DATABASE mysparkdb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()    
    
    # connect to myspark database
    conn = psycopg2.connect("host=127.0.0.1 dbname=mysparkdb user=postgres password=1234")
    cur = conn.cursor()
    
    return cur, conn


def drop_tables(cur, conn):
    """
    Drops tables defined in sql_queries_script.py
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    creates tables defined in sql_queries_script.py
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()

		
def main():
    """
    Driver main function.
    """
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    print("Table dropped successfully!!")

    create_tables(cur, conn)
    print("Table created successfully!!")

    conn.close()


if __name__ == "__main__":
    main()





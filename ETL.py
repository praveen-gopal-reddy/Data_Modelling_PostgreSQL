#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import glob
import os
import psycopg2
from sql_queries_script import *


def to_process_killers_data(cur,filepath):
    df = pd.read_csv(filepath, index_col=None, header=0)
    for value in df.values:
        KillerID,AgeFirstKill,AgeLastKill,YearBorn,Motive,Sex,Race,Sentence,InsanityPlea=value

        #insert killers bio records
        killers_data=(KillerID,YearBorn,Race,Sex)
        cur.execute(killers_bio_table_insert,killers_data)

        #insert killers additional details records
        killers_data_add=(KillerID,AgeFirstKill,AgeLastKill,Motive,Sentence,InsanityPlea)
        cur.execute(killers_additional_table_insert,killers_data_add)

    print(f"Records inserted for file {filepath}")


def  load_data(cur,conn,filepath,func):
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.csv'))
        for f in files:
            all_files.append(os.path.abspath(f))
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))
    
    for i, datafile in enumerate(all_files, 1):
            func(cur, datafile)
            conn.commit()
            print('{}/{} files processed.'.format(i, num_files))


def main():
    """
    Driver function for loading killers bio and killers details into Postgres database
    """
    conn = psycopg2.connect("host=127.0.0.1 dbname=mysparkdb user=postgres password=1234")
    cur = conn.cursor()
    load_data(cur, conn, filepath=r'C:\Users\PG\Documents\data engineer\projects-portfolio\postgresql', func=to_process_killers_data)
    conn.close()


if __name__ == "__main__":
    main()
    print("\n\nFinished processing!!!\n\n")


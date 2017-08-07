#!/usr/bin/env python

import sqlite3
import pandas as pd


data_file =  "../data/selfspy.sqlite"
conn = sqlite3.connect(data_file)

cur = conn.cursor()
query = "SELECT name FROM sqlite_master WHERE type='table';"
cur.execute(query)

print cur.fetchall()

# close 
def closeConn():
    cur.close()
    conn.close()

query = "SELECT * from process limit 5;"
cur.execute(query)
print cur.fetchall()

df = pd.read_sql_query(query, conn)

df.head()


def get_keys():
    query = "SELECT * from keys;"
    keys_df = pd.read_sql_query(query, conn)
    return keys_df

def get_process():
    query = "SELECT * from process;"
    process_df = pd.read_sql_query(query, conn)
    return process_df

keys_df = get_keys()
# print keys_df.head()

process_df = get_process()
print get_process()

closeConn()
from typing import Tuple
from numpy import NAN, empty
from pandas.core.dtypes.missing import isna
import tabula
import pydoc
import pyodbc 
import pandas as pd
import configparser

_config = configparser.ConfigParser()
_config.read('blackList.config')

server = _config.get('blackList','server')
database = _config.get('blackList','database')
username = _config.get('blackList','username')
password = _config.get('blackList','password')

pdfFile = _config.get('blackList','pdfFile')




tabula.convert_into(pdfFile, "Black_List.csv", output_format="csv", pages='all')

table = tabula.read_pdf(pdfFile,pages = "all")

# tabula.convert_into("c:/Black_List.pdf", "Black_List.csv", all = True)
# data = pd.read_csv(r'c:/Black_List.csv')   

# convert PDF into CSV file

# Connect to SQL Server 

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

# conn = pydoc.connect('Driver = {ODBC Driver 17 for SQL Server};'
#                     'Server = 10.129.153.42;'
#                     'Database = PPIVThailiCOATest;'
#                     'Trusted_Connection = yes;'
# )

cursor = conn.cursor()

#Insert Dataframe into table

truncateQuery = "Truncate table BlackList"
cursor.execute(truncateQuery)

for tables in table:
    df = pd.DataFrame(tables)
    for row in df.itertuples():
        # insert_book(row[0],row[1],row[2],row[3],row[4],row[5])
        query = "INSERT INTO BlackList VALUES(?,?,?,?,?)"
        args = (row[1],int(row[2]),str(row[3]),str(row[4]),str(row[5]))
        cursor.execute(query,args)
        conn.commit()
       

# conn.commit()
conn.close

# def insert_book(S_No,BLACKLIST_NO,BLACKLIST_DATE,BORROWER_NAME,ASSOCIATED_PERSON_FIRM_COMPANIES):
    
#     query = "INSERT INTO BlackList(S_NO,BLACKLIST_NO,BLACKLIST_DATE,BORROWER_NAME,ASSOCIATED_PERSON_AND_FIRM_OR_COMPANIES)" \
#             "VALUES(%d,%d,%s,%s,%s)"
#     args = (S_No,BLACKLIST_NO,BLACKLIST_DATE,BORROWER_NAME,ASSOCIATED_PERSON_FIRM_COMPANIES)
#     conn.execute(query,args)
#     conn.commit()


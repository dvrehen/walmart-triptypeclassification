import pandas as pd
pd.set_option('max_rows', 10)

#Set up the SQL connection
import pyodbc
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=LINK;DATABASE=WalmartKaggle;UID=Kaggle;PWD=Kaggle')

# Query database and load the returned results in pandas data frame
df = pd.read_sql('select * from dbo.lineitem_sales where TripType is not null order by VisitNumber', conn)
df_predict = pd.read_sql('select * from dbo.lineitem_sales where TripType is null order by VisitNumber', conn)
#df = pd.read_sql('select TOP 1000 * from dbo.lineitem_sales where TripType is not null order by VisitNumber, FinelineNumberID', conn)

df_departmentid = pd.read_sql('select ID from dbo.dim_department order by ID', conn)
df_finelinenumberid = pd.read_sql('select ID from dbo.dim_finelinenumber order by ID', conn)
df_upcprefix = pd.read_sql('select ID from dbo.dim_upc_prefix order by ID', conn)
#df.isnull().sum()

df.to_pickle('input\\df.dat')
df_predict.to_pickle('input\\df_predict.dat')
df_departmentid.to_pickle('input\\df_departmentid.dat')
df_finelinenumberid.to_pickle('input\\df_finelinenumberid.dat')
df_upcprefix.to_pickle('input\\df_upcprefix.dat')

df = pd.read_pickle('input\\df.dat')
df_predict = pd.read_pickle('input\\df_predict.dat')
df_departmentid = pd.read_pickle('input\\df_departmentid.dat')
df_finelinenumberid = pd.read_pickle('input\\df_finelinenumberid.dat')
df_upcprefix = pd.read_pickle('input\\df_upcprefix.dat')

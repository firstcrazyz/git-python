import pyodbc
import psycopg2
import json
import pandas as pd
from datetime import datetime as dt,timedelta
from sqlalchemy import create_engine

def get_insert_data():
    non_pg = create_engine("postgresql://postgres:P%40ssw0rd@10.29.24.251:5432/non_db")
    ncim_pg = create_engine("postgresql://postgres:P%40ssw0rd@10.29.24.251:5432/ncim")
    rth_pg = create_engine("postgresql://postgres:P%40ssw0rd@10.29.24.251:5432/rthsrv11")
    
    query_non = """SELECT id,TRIM(lotno)as lotno,TRIM(type) as type,TRIM(productcode)as productcode,processname,starttime,endtime,inputqty,surplusinqty,outputqty,upddate FROM public.lotprogress"""
    query_ncim = """SELECT * FROM public.ablotno"""
    query_rth_in = """SELECT * FROM trwa.fractionstockin"""
    query_rth_out = """SELECT * FROM trwa.fractionstockout"""
    
    
    data_non = pd.read_sql_query(query_non,non_pg)
    data_ncim = pd.read_sql_query(query_ncim,ncim_pg)
    data_rthin = pd.read_sql_query(query_rth_in,rth_pg)
    data_rthout = pd.read_sql_query(query_rth_out,rth_pg)

    merged_df = pd.merge(data_ncim,data_non,on=['Lotno','Type','Outputqty'],how='left',indicator=True)
    print(merged_df)
    # join_data =
    # print(join_data)
    # join_result = join_data[join_data["_merge"] == "left_only"]
    # join_result =join_result.rename(columns={
    #     "prodfamily_x":"prodfamily",
    #     "line_x":"line",
    #     "actualrun_x":"actualrun",
    #     "upddate_x":"upddate",
    #     "operator_x":"operator",
    #     "operatorname_x":"operatorname"
    # })
    # # print(join_result)z
    # column_11 = ["type" ,"prodfamily" ,"line" ,"actualrun" ,"upddate" ,"operator" ,"operatorname" ]
    # # join_result[column_11].to_sql('stype',eng_pg,schema="apollo",if_exists = 'append',index=False)
    # # print(join_result)

    non_pg.dispose()
    ncim_pg.dispose()

t1 = get_insert_data()

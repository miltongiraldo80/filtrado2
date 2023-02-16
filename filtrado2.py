
import pandas as pd 
import openpyxl

df=pd.DataFrame


df1=pd.read_excel("raw_scrap28.xlsx", engine="openpyxl",keep_default_na=False, na_values=[""])
df2=pd.read_excel("raw_scrap20.xlsx",engine="openpyxl",keep_default_na=False, na_values=[""])
df1.drop(["ROW_ID","CYCLE_ID","ID","SEGMENTO1","SEGMENTO2","SEGMENTO3","SEGMENTO4","SEGMENTO5","MODELO_HITCH","ip"],axis=1 ,inplace=True)
df2.drop(["ROW_ID","CYCLE_ID","ID","SEGMENTO1","SEGMENTO2","SEGMENTO3","SEGMENTO4","SEGMENTO5","MODELO_HITCH","ip"],axis=1 , inplace=True)




df3=pd.concat([df1,df2])
df3.to_excel("filtrado.xlsx")
print(df3)





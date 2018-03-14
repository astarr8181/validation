#!/usr/bin/env python
import pandas as pd 
import os
import numpy as np 

df = pd.read_csv('c3_svr_ctr_bb.csv')

print(df.dtypes())

forms = ['N336', 'N400', 'N600', 'N600K']

Types = ['MIL', "REG"]

columns =['ID', 'Form', 'Type', 'Location_Code','Action_Month','Data_Type', 'Count']

Location_codes = ['ABQ','AGA','ALB','ANC','ATL',	'BAL', 'BNY', 'BOI',\
'BOS','BUF','CHA','CHI','CHL','CHR','CIN','CLE','CLM','CLT','DAL',\
'DEN','DET','DSM','ELP','FRE','FSA','GRR','HAR','HEL','HHW','HIA',\
'HLG','HOU','IMP','INP','JAC','KAN','KND','LAC','LAW','LIN','LNY',\
'LOS','LOU','LVG','MAN','MEM','MGA','MIA','MIL','MTL','NBC','NEW',\
'NOL','NOR','NYC','OFM','OKC','OKL','OMA','ORL','PHI','PHO','PIT',\
'POM','POO','PRO','QNS','RAL','REN','SAA','SAC','SAJ','SBD','SEA',\
'SEK','SFR','SFV','SLC','SNA','SND','SNJ','SPM','SPO','STA','STL'\
'TAM','TUC','WAS','WIC','WPB','YAK']


Data_types = ['APPROVA','APPROVAL', 'DENIED - FRAU', 'DENIED - FRAUD',\
'DENIED - OTHE', 'DENIED - OTHER', 'Initial Receipt']


for index, row in df.iterrows():
		if any(row['Form'] in s for s in forms):
			pass
		else:
			print('invalid form: ' + row["Form"])
		if any(row['Type'] in s for s in Types):
			pass
		else:
			print('invalid form number: ' + row["Type"])
		if any(row['Location_Code'] in s for s in Location_codes):
			pass
		else:
			print('invalid location code' + row['Location_Code'])
		if any(row['Data_Type'] in s for s in Data_Types):
			pass
		else:
			print('invalid bucket ' + row["Data_Type"])

def check_for_int(df, column): #input data frame and column name as 'column'
	for index, row in df.iterrows():
		try:
			row[column] += 1
		except TypeError: "Record is  not an interger"
		 




df.to_csv('C4_validated.csv')
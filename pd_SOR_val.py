#!/usr/bin/env python
import pandas as pd 
import os
import numpy as np 

form_number_list = ['CRI89','EOIR29','I102','I129','I129F','I129S','I130','I131','I140','I191','I192','I193','I212','I290B',
'I290C','I360','I485','I485J','I526','I539','I601','I601A','I612', 'I687', 'I690','I694', 'I695','I698', 'I700','I730','I765','I817','I821','I821D',
'I824','I829','I829C','I829S','I865','I90','I914','I914A','I918','I918A','I929','MOTIC',
'N565','RECOVE']

Srv_ctr_list = ['AAO', 'CSC', 'IOE','MSC', 'NSC', 'TSC', 'VSC', 'YSC', 'ZAR', 'ZCH',
'ZHN','ZLA', 'ZMI', 'ZNK', 'ZNY', 'ZSF']

		

df = pd.read_csv('c3_svr_ctr_bb.csv')
df = df.apply(pd.to_numeric, errors='ignore')
df.update(df[['Receipts_OCT_SOR','Receipts_NOV_SOR','Receipts_DEC_SOR','Approved_OCT_SOR',\
 'Approved_NOV_SOR', 'Approved_DEC_SOR', 'Denied_Other_OCT_SOR', 'Denied_Other_NOV_SOR', \
 'Denied_Other_DEC_SOR', 'Denied_Fraud_OCT_SOR', 'Denied_Fraud_NOV_SOR', \
 'Denied_Fraud_DEC_SOR', 'Reopened_OCT_SOR', 'Reopened_NOV_SOR','Reopened_DEC_SOR',\
 'CPC_OCT_SOR',	'CPC_NOV_SOR', 'CPC_DEC_SOR', 'CONT_CASES_OCT_SOR',	'CONT_CASES_NOV_SOR',\
 	'CONT_CASES_DEC_SOR']].fillna(0))


print(df.dtypes)

for index, row in df.iterrows():
	if any(row['Service_Center'] in s for s in Srv_ctr_list):
		pass
	else:
		print('invalid service center: ' + row["Service_Center"])

	if any(row['SOR_Form_Number'] in s for s in form_number_list):
		pass
	else:
		print('invalid form number: ' + row["SOR_Form_Number"])

if __name__ == '__main__':
	main()







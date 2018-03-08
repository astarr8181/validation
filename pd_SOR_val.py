#!/usr/bin/env python
import pandas as pd 
import os
import numpy as np 

form_number_list = ['CRI89','EOIR29','I102','I129','I129F','I129S','I130','I131','I140','I191','I192','I193','I212','I290B',
'I290C','I360','I485','I485J','I526','I539','I601','I601A','I612','I690','I694','I698','I730','I765','I817','I821','I821D',
'I824','I829','I829C','I829S','I865','I914','I914A','I918','I918A','I929','MOTIC',
'N565','RECOVE']

Srv_ctr_list = ['AAO', 'CSC', 'IOE','MSC', 'NSC', 'TSC', 'VSC', 'YSC', 'ZAR', 'ZCH',
'ZHN','ZLA', 'ZMI', 'ZNK', 'ZNY', 'ZSF']


df = pd.read_csv('c3_svr_ctr_bb.csv')

for index, row in df.iterrows():
	if any(row['Service_Center'] in s for s in Srv_ctr_list):
		pass
	else:
		print('invalid service center: ' + row["Service_Center"])


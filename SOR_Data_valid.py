#!/usr/bin/env python
import typing as T
import logging

from csv import DictReader
from io import StringIO
import os

form_number_list = ['CRI89','EOIR29','I102','I129','I129F','I129S','I130','I131','I140','I191','I192','I193','I212','I290B',
'I290C','I360','I485','I485J','I526','I539','I601','I601A','I612','I690','I694','I698','I730','I765','I817','I821','I821D',
'I824','I829','I829C','I829S','I865','I914','I914A','I918','I918A','I929','MOTIC',
'N565','RECOVE']

Srv_ctr_list = ['AAO', 'CSC', 'MSC', 'NSC', 'TSC', 'VSC', 'YSC']

class SOR_Form_Numbr(str):
	def __new__(cls, form_number: str):
		if form_number not in form_number_list:
			raise ValueError('invalid form number')
		return super().__new__(cls, form_number)

class PRT_Group(str):
	def __new__(cls, PRT_descript: str):
		if PRT_descript is None:
			raise ValueError("PRT Group is null")
		return super().__new__(cls, PRT_descript)

class Service_Cntr(str):
	def __new__(cls, Svr_ctr: str):
		if Svr_ctr not in Srv_ctr_list:
			raise ValueError('invalid service center code')
		return super().__new__(cls, Svr_ctr)

class C3_data(T.NamedTuple):
    SOR_Form_Number: SOR_Form_Numbr
    PRT_Grouping: PRT_Group
    Service_Center: Service_Cntr
    Receipts_OCT_SOR: int
    Receipts_NOV_SOR: int
    Receipts_DEC_SOR: int
    Approved_OCT_SOR: int
    Approved_NOV_SOR: int
    Approved_DEC_SOR: int
    Denied_Other_OCT_SOR: int
    Denied_Other_NOV_SOR: int
    Denied_Other_DEC_SOR: int
    Denied_Fraud_OCT_SOR: int
    Denied_Fraud_NOV_SOR: int
    Denied_Fraud_DEC_SOR: int
    Reopened_OCT_SOR: int
    Reopened_NOV_SOR: int
    Reopened_DEC_SOR: int
    CPC_OCT_SOR: int
    CPC_NOV_SOR: int
    CPC_DEC_SOR: int
    CONT_CASES_OCT_SOR: int
    CONT_CASES_NOV_SOR: int
    CONT_CASES_DEC_SOR: int


    @classmethod
    def from_row(cls, row: dict):
        return cls(**{
            key: type_(row[key]) for key, type_ in cls._field_types.items()
        })


def validate_csv(reader: DictReader) -> bool:
    for row in reader:
        try:
            C3_data.from_row(row)
        except Exception as e:
            logging.error('type: {} msg: {}'.format(type(e), e))
            return False
    return True

data_root = 
datafile = 
DATA = os.path.direct.join(data_root, datafile)

#.strip()


data_csv_reader = DictReader(StringIO(DATA))


print(validate_csv(mock_data_csv_reader))

print(validate_csv(DictReader('foo')))
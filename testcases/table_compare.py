from time import time,sleep
from datetime import datetime,date,timedelta
from operator import itemgetter
from Database_automation.utilities.spec import Spec
from Database_automation.utilities.datacompare import compare_source_target,table_data


spec:Spec = Spec()
start_time = time()


@spec.map_params
def map_param(data, **kwargs):
    sheet_name = data['database']
    # spec.params = [x for x in sheet_name if x['TC_No.'] == 1]
    spec.params = list(filter(lambda x : x['TC_No.'] == 1 and x['Execution']=='Y', sheet_name))


@spec.setup
def setup(param):
    source_data = table_data(param['Source_query'])


@spec.step
def step(data, param, **kwargs):

    compare_source_target(data, param['Source_file_name'], param['Target_file_name'], param['Source_key'],\
                          param['Target_key'])





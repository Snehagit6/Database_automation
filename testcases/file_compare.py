from time import sleep
from datetime import datetime,date,timedelta
from operator import itemgetter
from utilities.spec import Spec
from utilities.datacompare import compare_source_target
from time import time,sleep

spec:Spec =Spec()
start_time = time()

@spec.map_params
def map_param(data, **kwargs):
    sheet_name = data['files']
    spec.params = [x for x in sheet_name if x['TC_No.'] == 1]


@spec.setup
def setup(param):
    print("Param stored")

@spec.step
def step(data, param):

    compare_source_target(data, param['Source_file_name'], param['Target_file_name'], param['Source_key'],\
                          param['Target_key'])

map_param({})
setup({})
step({})
from time import time, sleep
from datetime import datetime, date, timedelta
from operator import itemgetter

from utilities.spec import Spec
from utilities.datacompare import compare_source_target

spec: Spec = Spec()
start_time = time()


@spec.map_params
def map_param(data, **kwargs):

    spec.sheet_name = 'files'
    spec.params = list(filter(lambda x: x['TC_No.'] == 1 and x['Execution'] == 'Y', data[spec.sheet_name]))


@spec.setup
def setup(param):
    print("Param stored")


@spec.step
def step(sheet_name, param, **kwargs):

    compare_source_target(sheet_name, param['Source_file_name'], param['Target_file_name'], param['Source_key'],\
                          param['Target_key'])

# @spec.step
# def step2(**kwargs):
#     print("Step 2")




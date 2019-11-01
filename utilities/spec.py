from pprint import pprint
from utilities.structuring_data import excel_sheet_data

class Spec():

    '''

    '''

    def __init__(self, **kwargs):
        self.sheet_name = ''
        self.data = {}
        self.params = []


    def map_params(self, func):
        '''

        :param sheet_name: String
        :return:
        '''

        def inner(*args, **kwargs):
            '''

            :param args:
            :param kwargs:
            :return:
            '''
            try:
              self.data = excel_sheet_data()
              func(excel_sheet_data())
            except Exception as e:
                pprint("Exception".format(e.args))

        return inner

    def setup(self, func):
        def inner(*args, **kwargs):

            param = self.params[0]
            func(param)
        return inner

    #Decorator with parameters
    # def decorator(*args, **kwargs):
    #     print("Inside decorator")
    #
    #     def inner(func):
    #         print("Inside inner function")
    #         print("I like", kwargs['like'])
    #         return func
    #
    #     return inner
    #
    # @decorator(like="geeksforgeeks")
    # def func():
    #     print("Inside actual function")
    #
    # func()

    def step(self, func):
        def inner(*args, **kwargs):
            func(self.sheet_name, self.params[0])
        return inner




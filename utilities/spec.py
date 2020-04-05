from pprint import pprint
from utilities.structuring_data import excel_sheet_data

namee = ''
class Spec():

    '''

    '''

    def __init__(self, **kwargs):
        self.sheet_name = ''
        self.data = {}
        self.params = []
        self.list_methods = [[],[],[]]
        self.mapping, self.start, self.cont = 0, 0, 0


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
            if self.start== 0 and self.cont ==0:

                try:
                    self.data = excel_sheet_data()
              # self.list_methods[0].append(func)
              # self.list_methods.append(func.__name__)
                    func(self.data)
                    self.mapping= 1
                except Exception as e:
                    pprint("Exception".format(e.args))
            else :
                return -1

        return inner

    def setup(self, func):
        def inner(*args, **kwargs):
            if self.mapping == 1 and self.cont == 0:
                param = self.params[0]
                # self.list_methods[1].append(func)
                func(param)
                self.start = 1
            else:
                return -1
            # self.list_methods.append(func.__name__)
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

            if self.mapping ==1 and self.start== 1:
                func(self.sheet_name, self.params[0])
                # self.list_methods[2].append(func)
            else:
                return -1
            # self.list_methods.append(func.__name__)

        return inner


    # def execute(self):
    #     for each in self.list_methods[0]:
    #         each(self.data)
    #     for each in self.list_methods[1]:
    #         each(self.params[0])
    #     for each in self.list_methods[2]:
    #         each(self.sheet_name, self.params[0])

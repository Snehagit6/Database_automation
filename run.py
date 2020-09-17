# import runpy
# runpy.run_module("file_compare.py",'__main__')

from inspect import getmembers, isfunction, ismethod
from testcases import file_compare
from utilities.spec import Spec
from Logging.record_process import Logging

logs = Logging()
spec = Spec()

# import runpy

# s = Spec()
# functions_list = [o for o in getmembers(file_compare) if isfunction(o[1])]
# print(functions_list)
# __ = [funct for funct in [file_compare.map_param({}),file_compare.setup({}),file_compare.step({})]]
#
# print( s.list_methods)
# # runpy.run_module(file_compare.py)
#
# def some_magic():
#
#     for i in dir(file_compare):
#         item = getattr(file_compare,i)
#         print(item)
#         if callable(item):
#             item({})
#
# if __name__ == '__main__':
#     some_magic()

from inspect import *
import sys




#
# def some_magic(mod):
#     all_functions = inspect.getmembers(mod, inspect.isfunction)
#     for key, value in all_functions:
#         if str(inspect.signature(value)) == "()":
#             value()
#
# if __name__ == '__main__':
#     some_magic(sys.modules['file_compare'])
# print(dir(file_compare))
# def tester_method(f):
#     f._is_for_test = True #add an arbitrary attribute to the function, completely supported for exactly this reason.
#     return f
#
# def call_all_tester_methods(x):
#     """finds all attributes with a ._is_for_test attribute of their
# own and calls all of them in no guaranteed order"""
#     methods = {}
#     for name in dir(x):
#         attr = getattr(x, name)
#         if getattr(attr, "_is_for_test", False):
#             methods[name] = attr
#     for name, method in methods.items():
#         #print("calling: {}".format(name))
#         method()
#
#
# class Foo(object):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     @tester_method
#     def bar(self,**kwargs):
#         print(self.a)
#
#     @tester_method
#     def foobar(self,**kwargs):
#         print(self.b)
#
#     def othermethod_not_for_test(self,**arg):
#         return self.a  #this is not included in the test case
#
# obj = Foo('hi','bye')
# call_all_tester_methods(obj)

# print(dir(file_compare))

filenames = [_ for _ in os.walk('Database_automation//testcases')]

print(filenames)

logs.info("***** Running test case 1:file_compare ******")
for name in dir(file_compare):

        attr = getattr(file_compare, name)
        if isfunction(attr):
           if 'spec' in getfile(attr):

                        # print({name:attr})

                if attr()==-1:
                    attr, dir(file_compare)[-1] = dir(file_compare)[-1], attr
                    continue


        # if getattr(attr,'decorator_name') == 'param_mapping':
        #     l[0].append(attr)
        #     print(l)
        #     break

# print(file_compare.map_param.decorator_name)
# m =[each for each in dir(file_compare) if each == 'map_param'][0]
# print(file_compare.)



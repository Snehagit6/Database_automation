import os
import csv, openpyxl
from connections import database_connection


def excel_sheet_data():
    try:

        file_name = "D://Database_automation//Database_automation//data//tables_queries.xlsx"
        wb = openpyxl.load_workbook(file_name)
        sheets = wb.sheetnames
        data = {}
        for sheet in sheets:
            s = wb.get_sheet_by_name(sheet)
            headers = [s.cell(row=1, column=j).value for j in range(1, s.max_column + 1)]
            records = [[s.cell(row=i, column=j).value for j in range(1, s.max_column + 1)] \
                       for i in range(2, s.max_row + 1)]
            param = {sheet: [dict(zip(headers, record)) for record in records]}
            data.update(param)
        return (data)

    except FileNotFoundError as e:
        print("File not exists:{}".format(e.args))


def map_params(param):
    pass


def csv_data(file, **kwargs):
    '''

    :param file: Filename(str)
    :param kwargs:
    :return:
    '''
    try:
        with open(file, 'r+') as f1:
            reader = csv.reader(f1, delimiter=',')
            header = next(reader)
            records = [row for row in reader if row]
            param = [dict(zip(header, each)) for each in records]
            return param
    except FileNotFoundError as e:
        print(e.args)


def json_file_read(file):
    pass


def html_file_read(file):
    pass


def table_data(query):
    cursor = database_connection()
    result_set = cursor.execute(query)
    return result_set

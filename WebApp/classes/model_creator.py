#!/usr/bin/env python
# -*- coding: utf-8 -*-
from WebApp.models.databases.mytest.table_models import sh

__author__ = 'ReS4'

from playhouse.reflection import *

TEMPLATE_CLASS = """
class {name}(PeeweeBaseModel):
{columns_value}
"""

TEMPLATE = """
class Sys{name}:
    def __init__(self, {columns_name}):
{columns_value}

    def insert(self):
        try:
            x = {name}.insert(
{insert_params}
            ).execute()
            return x if x else False
        except:
            return False

    def get_all(self):
        try:
            x = {name}.select()
            ls = []
            for i in x:
                ls.append(
                    dict(
{get_all_params}
                    )
                )
            return ls
        except Exception, e:
            print(e)
            return []

    def get_one(self):
        try:
            i = {name}.get({name}.id == self.id)
            return dict(
{get_all_params}
            )
        except Exception, e:
            print(e)
            return dict()

    def delete(self):
        try:
            x = {name}.delete().where({name}.id == self.id).execute()
            return True
        except Exception, e:
            print(e)
            return False

    def update(self, **kwargs):
        try:
            x = {name}.update(**kwargs).where({name}.id == self.id).execute()
            return True
        except Exception, e:
            print(e)
            return False

"""

web_db = MySQLDatabase(
    database="information_schema",
    host=sh.web['mysql']['host'],
    user=sh.web['mysql']['user'],
    passwd=sh.web['mysql']['password'],
    charset="utf8"
)


def get_table_info(tbl_name):
    x = web_db.execute_sql(
        'SELECT `COLUMN_NAME`,`DATA_TYPE` FROM information_schema.`COLUMNS` where `TABLE_SCHEMA`=%s and `TABLE_NAME`=%s',
        [sh.web['mysql']['db'], tbl_name]
    )
    web_db.close()

    d = dict(columns=[], columns_type=[])
    for i in x:
        d['columns'].append(i[0])
        d['columns_type'].append(i[1])

    return d


class ModelCreator:
    def __init__(self, table_name):
        x = get_table_info(table_name)
        self.columns = x['columns']
        self.columns_type = x['columns_type']
        if not self.columns:
            raise Exception("Table not found.")

        self.type_mapping = dict(
            int='IntegerField()',
            varchar='CharField()',
            text='TextField()',
            enum='CharField()',
            tinyint='IntegerField()',
            timestamp='DateTimeField()',
            datetime='DateTimeField()',
            date='DateField()'
        )
        print(TEMPLATE_CLASS.format(name=table_name.capitalize(), columns_value=self.__make_class()))
        print(
            TEMPLATE.format(
                name=table_name.capitalize(),
                columns_name=self.__get_columns_header(),
                columns_value=self.__get_columns_var(),
                insert_params=self.__make_insert_params(),
                get_all_params=self.__make_get_all_params()
            )
        )

    def __make_class(self):
        x = ''
        for i in range(len(self.columns)):
            x += '    {} = {}\n'.format(self.columns[i], self.type_mapping[self.columns_type[i]])

        return x

    def __get_columns_header(self):
        return "=None, ".join(self.columns) + "=None"

    def __get_columns_var(self):
        x = ""
        for i in self.columns:
            x += "        self.{0} = {0}\n".format(i)
        return x

    def __make_insert_params(self):
        x = ""
        for i in self.columns:
            x += "                {0}=self.{0},\n".format(i)
        return x[:-2]

    def __make_get_all_params(self):
        x = ""
        for i in self.columns:
            x += "                        {0}=i.{0},\n".format(i)
        return x[:-2]


# ModelCreator("User")

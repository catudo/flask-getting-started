import decimal
import random
import string
import utils.error_handling as err_exception
from utils.configuration import Configuration
from datetime import datetime, date

from sqlalchemy import inspect



class Utils(object):

    @staticmethod
    def get_file_db_configuration():
        try:
            config = Configuration().settings
            return config
        except Exception as e:
            raise err_exception.ErrorException(
                "Database", 500, "Error getting database configuration", e)

    @staticmethod
    def get_attr_names(model):
        inst = inspect(model)
        attr_names = [c_attr.key for c_attr in inst.mapper.column_attrs]
        return attr_names

    @staticmethod
    def set_model_attr(model, model_attr, params):
        for field in model_attr:
            if field in params:
                setattr(model, field, params[field])
        return model

    @staticmethod
    def map_params(result):
        data = {}

        for e in result._asdict():
            attrib = result.__getattribute__(e)
            if type(attrib) is decimal.Decimal:
                data.update({e: float(attrib)})
            elif type(attrib) is datetime.date or type(attrib) is datetime or type(attrib) is datetime.time or type(attrib) is date:
                data.update({e: attrib.isoformat()})
            else:
                data.update({e: attrib})

        return data

    @staticmethod
    def map_params_all(result):
        data = []
        for record in result:
            data.append(Utils().map_params(record))

        return data

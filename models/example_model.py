import logging
import sys


from sqlalchemy import func, text, exc, cast, CHAR, inspect, outerjoin

from utils.utils import Utils

sys.path.append('../')
from utils.configuration import Configuration
import utils.database as db_connection
import utils.error_handling as err_exception
from schema.core_schema import Example as ExampleTBL, ExampleRelation as ExampleRelationTBL



class Example(object):

    def __init__(self):
        # ===============================================
        # Get the configuration info
        # ===============================================
        config = Configuration().settings
        self.config = config

        conn = self.db_conn()
        self.session = conn


    def db_conn(self):
        try:
            connection_frdb = db_connection.Connection(None, 'postgres')
            connection = connection_frdb.get_db_session()
            return connection
        except Exception as e:
            raise err_exception.ErrorException(
                "Database", 409, "Error connecting to the database", e)

    def __del__(self):
        if self.session:
            self.session.close()

    # get examples from example table
    def get_examples(self, params):

        try:
            response = []

            query = self.session.query(ExampleTBL.example_id,ExampleTBL.client_email,ExampleTBL.created_on, ExampleRelationTBL.is_first_login )\
                .outerjoin(ExampleRelationTBL, ExampleTBL.example_id == ExampleRelationTBL  .example_id)

            if "client_email" in params and params['client_email']:
                query = query.filter(func.lower(ExampleTBL.client_email).like(
                    '%' + func.lower(params['client_email']) + '%'))

            count = query.count()

            result = query

            if count > 0:
                response = Utils.map_params_all(result)

            return response, count
        except exc.SQLAlchemyError as e:
            logging.error('Error getting examples from database {}'.format(e))
            raise Exception(
                'Error getting advisors from database {}'.format(e), 409)
        except Exception as e:
            raise e






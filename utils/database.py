"""
    Connection class
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from sqlalchemy.ext.declarative import declarative_base
import utils.error_handling as err_exception
from utils.utils import Utils

Base = declarative_base()


class Connection(object):

    def __init__(self, session=None, db='postgres'):
        try:
            db_file = Utils.get_file_db_configuration()

            url = db_file[db]['db_url'].format(db_user=db_file[db]['db_user'], db_pass=db_file[db]['db_pass'], db_host=db_file[
                                               db]['db_host'], db_name=db_file[db]['db_name'], db_port=db_file[db]['db_port'])

            engine = create_engine(url, client_encoding='utf8', isolation_level="AUTOCOMMIT", poolclass=NullPool)
            Base.metadata.bind = engine

            self.DBSession = sessionmaker(bind=engine)
        except Exception as e:
            raise err_exception.ErrorException(
                "Database", 409, "Error connecting to the database", e)



    def get_db_session(self):
        session = self.DBSession()
        return session

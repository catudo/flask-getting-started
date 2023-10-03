# coding: utf-8
import sqlalchemy
from sqlalchemy import Column, Date, DateTime, ForeignKey, Index, Integer, \
    String, Text, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base

from utils.utils import Utils

Base = declarative_base()
metadata = Base.metadata

"""
This is an example of how is posible to create tables in a relational database with SQL Alchemy with the differents fields   
and contraints
"""
class Example(Base):
    __tablename__ = u'examples'

    example_id = Column(Integer, primary_key=True,
                       nullable=False, index=True, autoincrement=True)
    client_email = Column(String(50), nullable=False)
    created_by = Column(String(50), nullable=False)
    updated_by = Column(String(50), nullable=False)
    updated_on = Column(DateTime, nullable=False, index=True,
                        server_default=u'NOW()')
    created_on = Column(DateTime, nullable=False, index=True,
                        server_default=u'NOW()')

class ExampleRelation(Base):
    __tablename__ = u'example_relations'

    example_relation_id = Column(Integer, primary_key=True,
                        nullable=False, index=True, autoincrement=True)
    example_id = Column(ForeignKey('examples.example_id'), nullable=True, index=True)
    created_by = Column(String(50), nullable=False)
    updated_by = Column(String(50), nullable=False) 
    updated_on = Column(DateTime, nullable=False, index=True,
                        server_default=u'NOW()')
    created_on = Column(DateTime, nullable=False, index=True,
                        server_default=u'NOW()')
    is_first_login = Column(Boolean, nullable=False, default=True)




db_file = Utils.get_file_db_configuration()
db='postgres'
url = db_file[db]['db_url'].format(db_user=db_file[db]['db_user'], db_pass=db_file[db]['db_pass'], db_host=db_file[
                                               db]['db_host'], db_name=db_file[db]['db_name'], db_port=db_file[db]['db_port'])
engine = create_engine(url, client_encoding='utf8')

insp =sqlalchemy.inspect(engine)
if not insp.has_table("examples"):
    metadata.tables["examples"].create(engine)
    metadata.tables["example_relations"].create(engine)

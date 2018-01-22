import re
import json
from sqlalchemy import Column,String,create_engine,Integer,ForeignKey,Float
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base
import pymysql
class Read(object):
    def __init__(self,path):
        self.path=path
    def read(self):
        with open(self.path,"r",encoding="utf-8") as f:
            contents = f.readlines()
            contents = json.dumps(contents)
            return contents
    def re_content(self):
        content = self.read()
        patter = re.compile(u'INSERT\s[A-Z]{4}\s\S[a-z]*\w[a-z]*\S\s[A-Z]{6}\s\(\S2015\S.*?;')
        content = patter.findall(content)
        return content

    def extract_content(self):
        sql_senetnces = self.re_content()
        for sql_sentence in sql_senetnces:
            Adjust_coefficient.insert(sql_sentence)


Base = declarative_base()
engine = create_engine("mysql+pymysql://root:redhat@localhost/test",encoding="utf-8",echo=True)
DBsession = sessionmaker(engine)
session = DBsession()
class Adjust_coefficient(Base):
    __tablename__ = "adjust_coefficient"
    cycle_id = Column(String(4),nullable=True,default=None,primary_key=True)#nullable 可否为空
    dist = Column(Integer,nullable=True,default=None)
    province = Column(Integer,nullable=True,default=None)
    sample_n = Column(Integer,nullable=True,default=None)
    adjust = Column(Float,nullable=True,default=None)
    grade = Column(String(2),nullable=True,default=None)
    zone_level = Column(String(3),nullable=True,default=None)

    @classmethod
    def conn(cls,s):
        conn=engine.connect().execute(s)

    @classmethod
    def insert(cls,*args):
        return cls.conn(*args)







c=Read(r"C:\Users\M.Cheng\Desktop\adjust_coefficient.sql")
c.extract_content()

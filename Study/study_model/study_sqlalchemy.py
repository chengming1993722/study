from sqlalchemy import Column,String,create_engine,Integer,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base
#<--!SQLAlchemy规定必须要有主键-->
""""
#创建engine，连接数据库
#echo为true将打印所有的sql语句
engine = create_engine("mysql+pymysql://root:redhat@localhost:3306/test",echo=True)
#创建DBSession类型:
DBSession = sessionmaker(bind=engine)


#创建对象的基类
Base = declarative_base()
#定义User对象：
class User(Base):
    #表的名字：
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True)
    name = Column(String(20))
    levels = Column(String(20))
    email = Column(String(50))

session = DBSession()
new_user = User(name='kell',levels="5",email="102017@qq.com")
session.add(new_user)
session.commit()
session.close()
"""
engine = create_engine("mysql+pymysql://root:redhat@localhost:3306/test",encoding="utf_8",echo=True)
DBsession = sessionmaker(engine)
session = DBsession()
Base = declarative_base()
class User(Base):
    __tablename__ = "users"
    __tabl_args__ = {
        "mysql_engine":"InnoDB", #表的引擎
        "mysql_charset":"utf8", #表的编码方式
    }
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(20),nullable=False) #不可为空
    age = Column(Integer,default=0)
    email = Column(String(50),nullable=True)
    #添加角色id外键(关联Role.id)
    role_id = Column(Integer,ForeignKey("Roles.id"))
    #添加关系属性(关联到role_id外键上)
    role = relationship("Role",foreign_keys="User.role_id")
    # 添加关系属性(关联到role_id外键上)，如果用了这种方式，Role模型中的users可以省略
    #role = relationship("Role",foreign_keys="User.role_id",backref="users")
    @classmethod
    def del_data(cls):
        
        try:
            session.query(cls).filter(id !=1).delete()
            print("DELETED")
        except Exception as e:
            print(e)
    @classmethod
    def add_data(cls,**kwargs):

        try:
            data=cls(**kwargs)
            session.add(data)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e



class Role(Base):
    __tablename__ = "Roles"
    __table_args__ = {
        "mysql_engine":"InnoDB",
        "mysql_charset": "utf8"
    }
    id = Column(Integer,primary_key=True)
    name = Column(String(50),unique=True)
    users = relationship("User",foreign_keys="User.role_id")
    @classmethod
    def del_data(self):
        try:
            session.query(self).filter(id !=-1).delete()
        except Exception as e:
            print(e)

    @classmethod
    def add_data(cls,**kwargs):

        try:
            data=cls(**kwargs)
            session.add(data)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e

'''
通用的查询语句
equals:
query.filter(User.name == 'ed')
not equals:
query.filter(User.name!= 'ed')
LIKE:
query.filter(User.name.like('%ed%'))
IN:
query.filter(User.name
.in_(['ed', 'wendy', 'jack']))
# works with query objects too:
query.filter(User.name.in_(session.query(User.name).filter(User.name.like('%ed%'))))
NOT IN:
query.filter(~User.name.in_(['ed', 'wendy', 'jack']))
IS NULL:
query.filter(User.name== None)
# alternatively, if pep8/linters are a concern
query.filter(User.name.is_(None))
IS NOT NULL:
query.filter(User.name!= None)
# alternatively, if pep8/linters are a concern
query.filter(User.name.isnot(None))
AND:
# use and_()
from sqlalchemy import and_
query.filter(and_(User.name== 'ed', User.fullname == 'Ed Jones'))
# or send multiple expressions to .filter()
query.filter(User.name

 == 'ed', User.fullname == 'Ed Jones')
# or chain multiple filter()/filter_by() calls
query.filter(User.name== 'ed').filter(User.fullname == 'Ed Jones')
OR:
from sqlalchemy import or_
query.filter(or_(User.name == 'ed', User.name== 'wendy'))
MATCH:
query.filter(User.name.match('wendy'))
返回列表List和标量Scalar
all()返回一个列表
query = session.query(User).filter(User.name.like('%ed')).order_by(User.id)
query.all()
first()使用限制，返回结果集的第一条作为Scalar
query.first()
one() 如果返回结果集不止一个对象，将raise一个错误。
from sqlalchemy.orm.exc import MultipleResultsFound
try:
    users = query.one()
except MultiResultsFound e:
    print e
没有数据返回时
from sqlalchemy.orm.exc import NoResultFound
try:
    users = query.one()
except NoResultFound, e:
    print e
scalar()调用one()方法，并且成功时返回第一列数据
query.scalar()
使用文本SQL语句
文本字符串可以在查询中灵活使用，通过text()构建。
from sqlalchemy import text
for user in session.query(User).filter(text("id>20")).order_by(text("id")).all()
    print user.name
可以绑定参数，使用params()方法
session.query(User).filter(text("id<:value and name=:name")).params(value=220, name="ed").order_by(User.id).one()
计数方法count()

session.query(User).filter(Usre.name.like("%ed")).count()
也可以使用func.count()来计数

from sqlalchemy import func
session.query(func.count(User.name), User.name).group_by(User.name).all()
'''
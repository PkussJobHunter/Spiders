# coding = utf-8

# 导入:
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(Integer(), primary_key=True)
    username = Column(String(50))
    password = Column(String(50))

# 初始化数据库连接:
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/app')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
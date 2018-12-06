# coding = utf-8

from utils.sqlalchemy import DBSession, User

if __name__ == '__main__':
    # 创建Session:
    session = DBSession()
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    user = session.query(User).one()
    # 打印类型和对象的name属性:
    print('type:', type(user))
    print('username:', user.username)
    # 关闭Session:
    session.close()
    pass
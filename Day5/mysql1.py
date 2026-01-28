from pymysql import  Connection
# Connection 是个类
# 构建连接对象
conn=Connection(
    host="localhost",
    port=3306,
    user='root',
    password='me20070513',
    autocommit=True
)
print(conn.get_server_info())

#获取游标对象
cursor=conn.cursor()
conn.select_db('world')
# cursor.execute('drop table if exists test_mysql;')
# cursor.execute('create table test_mysql (id int,name varchar(20));')
cursor.execute('select * from student')
results=cursor.fetchall()
# results 是个 tuple,成员也是 tuple；类似二维数组
# sql 都是一行一行的
print(results)
# print(type(results))
# for r in results :
#     print(f'{type(r)},{r}')
# 关闭连接
cursor.execute("insert into student values(114514,'方大同',40,'男')")
conn.commit()
conn.close()

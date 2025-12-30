from pymysql import Connection

conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    autocommit=True
)
print(conn.get_server_info())

cursor = conn.cursor()
conn.select_db('test')
# cursor.execute("create table test_pymysql(id int)")

# conn.select_db('world')
# cursor.execute("select * from student")
# results = cursor.fetchall()
# for result in results:
#     print(result)

conn.select_db('world')
# cursor.execute("insert into student values(10001,'周杰伦',31,'男')")
# conn.commit()

cursor.execute("insert into student values(10002,'林俊杰',34,'男')")

conn.close()
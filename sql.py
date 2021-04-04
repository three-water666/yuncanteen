import pymysql

def do(sql):
    #本地
    # db=pymysql.connect(host="localhost",port=3306,user="root",password="",\
    #                     database="yuncanteen",charset="utf8")

    #云数据库
    db = pymysql.connect(host="", port=3306, user="", password="", \
                         database="", charset="utf8")
    cur=db.cursor()
    cur.execute(sql)
    results =cur.fetchall()
    cur.close()
    db.commit()
    db.close()

    return results
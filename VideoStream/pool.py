import pymysql as MYSQL

def connectionPooling():
    db=MYSQL.connect(host="localhost",port=3306,user="root",passwd="1234",db="videostream")
    cmd=db.cursor()
    return db,cmd
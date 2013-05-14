import sys
import MySQLdb

reload(sys)
sys.setdefaultencoding('utf-8')

def getdata ():
    try:
        conn = MySQLdb.connect(host='localhost', user='root', passwd='root', db='test', port=3306, charset='utf8')
        try:
            cur = conn.cursor()
            sql = r'select * from person'
            cur.execute(sql)
            allPerson = cur.fetchall()
        finally:
            cur.close()
            conn.close()
    except Exception, e:
        print '数据库错误:', e
        return

    for rec in allPerson:
        print rec[0],rec[1]

if __name__ == '__main__':
    getdata()
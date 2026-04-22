# try to connect to mysql db 
# pip install mysql-connector-python

import os
from dotenv import load_dotenv
from mysql.connector import connect as dbConnect

load_dotenv()

class Activator:
    @staticmethod
    def CreateNewInstance(type, dic):
        _t = type()
        for k, v in dic.items():
            _t.__setattr__(k,v)
        return _t
    

class DbInfo:
    pass

class cli:
    """
    CLI helper to render color 
    """
    reset = "\033[0m"
    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    blue = "\033[34m"
    magenta = "\033[35m"
    cyan = "\033[36m"
    white = "\033[37m"


    @staticmethod
    def Red(text: str) -> str : 
        return cli.red+ text + cli.reset 
        
    @staticmethod
    def Green(text: str) -> str : 
        return cli.green+ text + cli.reset 
     

connexion = Activator.CreateNewInstance(DbInfo, {
    "server":os.environ.get('MYSQL_SERVER'),
    "user":os.environ.get('MYSQL_USER'),
    "passwd": os.environ.get('MYSQL_PASSWD'),
    "db":os.environ.get('MYSQL_DB_NAME')
})
print(connexion.server, connexion.passwd)
# connection to mysql database 
try:
    cnx = dbConnect(user=connexion.user, database=connexion.db, passwd=connexion.passwd, host=connexion.server)
except:
    print(cli.Red('failed to connect!!!'))
else:
    print(cli.Green("Eureka "), cnx)
    cur = cnx.cursor()
    cur.execute('SELECT CURDATE()')
    row = cur.fetchone()
    print(f"Current date is: {row[0]}")
    cnx.close()



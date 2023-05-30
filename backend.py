# Backend of Project SQL 

import mysql.connector

class ConnectSQL:
    def __init__(self, host, user, password):
        # Start connect to mysql
        self.host = '192.168.116.155' 
        self.user = 'jack' 
        self.password = 'User12345678!!' 
        self.cnx = mysql.connector.connect(host=host,user=user,password=password)
        self.cursor = self.cnx.cursor()
        # END Connect to mysql
        
    def execute_sql_command(self, command):
        self.cursor.execute(command)
        rows = self.cursor.fetchall()
        return '\n'.join([', '.join(map(str, row)) for row in rows])

sql_conn = ConnectSQL('192.168.116.155', 'jack', 'User12345678!!')


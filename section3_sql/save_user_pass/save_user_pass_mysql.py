import mysql.connector
#this is my mysql info...use yours
database_name = 'users_login_info'
mysql_user = 'root'
mysql_password = ''
localhost = '127.0.0.1'
table = 'users_info'
cnx = mysql.connector.connect(user= mysql_user, password= mysql_password, host= localhost, database= database_name)
cursor = cnx.cursor()
repeat = True
correction = False
while repeat:
    username = input('Enter username: ')
    password = input('Enter password: ')
    while correction == False:
        if '@' in username:
            username_by_at_sign = username.split('@')
            if '.' in username_by_at_sign[1]:
                username_host = username_by_at_sign[1].split('.')
                if type(username_host[0]) is str and type(username_host[1]) is str:
                    correction = True
                else:
                    print('This email format is incorrect\n True format is: expression@string.string')
                    username = input('Enter correct username: ')
            else:
                print('This email format is incorrect\n True format is: expression@string.string')
                username = input('Enter correct username: ')
        else:
            print('This email format is incorrect\n True format is: expression@string.string')
            username = input('Enter correct username: ')
    insert = f'INSERT INTO {table} VALUES(%s, %s)'
    cursor.execute(insert, (username, password))
    cnx.commit()
    
    print('Do you want another user add ?(y/n)')
    repeat_answer = input()
    if repeat_answer == 'n':
        repeat = False

cursor.close()
cnx.close()
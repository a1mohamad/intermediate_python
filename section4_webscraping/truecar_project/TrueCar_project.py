import mysql.connector
import requests
from bs4 import BeautifulSoup
def firstn(n):
    num= 0
    brand, model = input('Please insert your brand: ').lower(), input('Please insert your model: ').lower()
    brand, model = brand.replace(' ', '-'), model.replace(' ', '-')
    url = 'http://truecar.com/used-cars-for-sale/listings/%s/%s/' %(brand, model)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    tree = soup.find('div', attrs={'data-test': 'allVehicleListings'})
    all_cars= tree.select("li.mt-2.flex.grow.col-md-6.col-xl-4") + tree.select("li.mt-3.flex.grow.col-md-6.col-xl-4")
    while (num < n and num < len(all_cars)):
        price_tag = all_cars[num].find('div', attrs= {'class' : 'heading-3 my-1 font-bold'})
        price = price_tag.text
        mileage_tag = all_cars[num].find('div', attrs= {'class' : 'truncate text-xs', 'data-test' : 'vehicleMileage'})
        mileage = mileage_tag.text
        yield (price, mileage)
        num += 1
def inserting_mysql(p, m):
    cnx = mysql.connector.connect(user= 'root', password= '', host='127.0.0.1', database=f'{database_name}')
    cursor = cnx.cursor()
    insert = f'INSERT INTO {table_name} Values(%s, %s)'
    cursor.execute(insert, (p, m))
    cnx.commit()
def TrueCar():
    cnx = mysql.connector.connect(user= 'root', password= '', host='127.0.0.1', database=f'{database_name}')
    cursor = cnx.cursor()
    statement = f'SHOW TABLES LIKE \'{table_name}\';'
    cursor.execute(statement)
    result = cursor.fetchone()
    if result:
        stmt1 = f'DELETE FROM {table_name};'
        cursor.execute(stmt1)
        cnx.commit()
        for price, mileage in firstn(20):
            inserting_mysql(price, mileage)
    else:
        creating_table = f'CREATE TABLE {table_name}(Price varchar(30), Mileage varchar(30));'
        cursor.execute(creating_table)
        cnx.commit()
        for price, mileage in firstn(20):
            inserting_mysql(price, mileage)
        
    cnx.commit()
    cursor.close()
    cnx.close()

database_name = input('Database: ')
table_name = input('Table name: ')
TrueCar()
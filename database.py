#!/usr/bin/python


import MySQLdb, datetime, httplib, json, os
# requires MySQLdb python 2 library which is not ported to python 3 yet

class mysql_database:
    def __init__(self):
        credentials_file = os.path.join(os.path.dirname(__file__), "credentials.mysql")
        f = open(credentials_file, "r")
        credentials = json.load(f)
        f.close()
        for key, value in credentials.items(): #remove whitespace
            credentials[key] = value.strip()
            
        self.connection = MySQLdb.connect(credentials["HOST"], credentials["USERNAME"], credentials["PASSWORD"], credentials["DATABASE"])
        self.cursor = self.connection.cursor()

    def execute(self, query, params = []):
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
        except:
            self.connection.rollback()
            raise

    def query(self, query):
        cursor = self.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(query)
        return cursor.fetchall()

    def __del__(self):
        self.connection.close()

class coinstrack:
    def __init__(self):
        self.db = mysql_database()
        self.insert_template = "INSERT INTO MARKET_DATA (POSITION, NAME, TICKER, CATEGORY, AVAILABLE_SUPPLY, MARKETCAP_USD, MARKETCAP_BTC, PRICE_USD, PRICE_BTC, VOLUME24_USD, VOLUME24_BTC, CHANGE1H_USD, CHANGE1H_BTC, CHANGE7H_USD, CHANGE7H_BTC, CHANGE7D_USD, CHANGE7D_BTC, TIME_CMC, TIME_COMPUTER) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        self.update_template =  "UPDATE MARKET_DATA SET REMOTE_ID=%s WHERE ID=%s;"
        self.upload_select_template = "SELECT * FROM MARKET_DATA WHERE REMOTE_ID IS NULL;"

    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def is_none(self, val):
        return val if val != None else "NULL"

    def insert(self, position, name, symbol, category, availableSupply, marketCap_usd, marketCap_btc, price_usd, price_btc, volume_usd, volume_btc, change1h_usd, change1h_btc, change7h_usd, change7h_btc, change7d_usd, change7d_btc, timestamp, created = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")):
        params = ( position, 
            name, 
            symbol, 
            category, 
            availableSupply, 
            marketCap_usd, 
            marketCap_btc, 
            price_usd, 
            price_btc, 
            volume_usd, 
            volume_btc, 
            change1h_usd, 
            change1h_btc, 
            change7h_usd, 
            change7h_btc, 
            change7d_usd, 
            change7d_btc, 
            timestamp, created )
        print(self.insert_template % params)
        self.db.execute(self.insert_template, params)

def get_position(json):
    try:
        return int(json['position'])
    except KeyError:
        return 10000

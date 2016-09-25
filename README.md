# coinstrack

Project Coinstrack is an attempt to build a database of crypto-currency market data from publicly available data using Python &amp; MySQL

Hopefully the indications below will be clear and complete enough so you can also make it work on your system.


1. REQUIREMENTS / INSTALLATION

You need python 2.x with the following packages installed: 
sys, os, urllib2, httplib, json, datetime, MySQLdb

You need MySQL installed:

Installation instructions here- 
https://dev.mysql.com/doc/refman/5.6/en/linux-installation.html

This can be helpful as well-
http://www.thegeekstuff.com/2008/07/howto-install-mysql-on-linux/

Now the Python-MySQLdb connector (which will install the MySQLdb dependency):
https://dev.mysql.com/downloads/connector/python/
https://dev.mysql.com/doc/connector-python/en/connector-python-installation.html


2. GETTING THINGS READY

Put the files coin_db_update.py, database.py and credentials.mysql in the same folder. 
Make sure it's in your python path-  

$ echo -e "\nexport PYTHONPATH=\$PYTHONPATH:/path/to/directory" >> ~/.bashrc


3. CREATING THE DATABASE

$ mysql -u yourusername -p

You will be prompted for the password you set in the credentials.mysql file. There would probably be a way to use encryption which would be more secure.


mysql> CREATE DATABASE coinstrack;

Now use this database-
mysql> USE coinstrack;

Create the data table in the database-

CREATE TABLE MARKET_DATA(
    ID BIGINT NOT NULL AUTO_INCREMENT,
    REMOTE_ID BIGINT,
    POSITION INTEGER,
    NAME VARCHAR(30),
    TICKER VARCHAR(8),
    CATEGORY VARCHAR(30),
    AVAILABLE_SUPPLY DECIMAL(20,8),
    MARKETCAP_USD DECIMAL(20,8),
    MARKETCAP_BTC DECIMAL(20,8),
    PRICE_USD DECIMAL(20,8),
    PRICE_BTC DECIMAL(20,8),
    VOLUME24_USD DECIMAL(20,8),
    VOLUME24_BTC DECIMAL(20,8),
    CHANGE1H_USD DECIMAL(20,8),
    CHANGE1H_BTC DECIMAL(20,8),
    CHANGE7H_USD DECIMAL(20,8),
    CHANGE7H_BTC DECIMAL(20,8),
    CHANGE7D_USD DECIMAL(20,8),
    CHANGE7D_BTC DECIMAL(20,8),
    TIME_CMC BIGINT,
    TIME_COMPUTER TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY ( ID )
  );

To check your install, try to run coin_db_update.py manually to make sure there is no error before automating the scraping task.


4. SETTING-UP AUTOMATIC UPDATES

Edit the crontab file in /etc/crontab or /etc/cron.d (depends on the system you use - keep the file name unchanged)
Add the following line to automatically update the data every hour at half past:

30 * * * * computer_username python /path/to/yourpythonprogram/coin_db_update.py

Let it run for a little while to download some data, so you can then use the database!


5. USING THE DATABASE

$ mysql -u yourusername -p

Enter your password (cf. credentials.mysql)

Now specify the database to use-

mysql> USE coinstrack

Enter MySQL commands, e.g.
mysql> select TICKER, PRICE_USD, VOLUME24_BTC, TIME_COMPUTER FROM MARKET_DATA WHERE TICKER= "BTC";


6. NEXT STEPS

Now the data is here, and it would be great to use python to analyse and visualize it. If anyone wants to contribute, you'd be more than welcome!
Contributions on cleaning the code and/or improving this readme are also warmly welcomed.


7. CREDITS

1) Abitfan - https://github.com/abitfan/coinmarketcap-cli
2) Raspberrypi - https://github.com/raspberrypi/weather-station


8. DISCLAIMER

This is amateur code. As such it is prone to bugs and errors. 
Obviously I am NOT responsible for any issue you may encounter that are related to this code or the links in the readme. 
You use this material at your own risk.

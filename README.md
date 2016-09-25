# coinstrack
<br>
<strong>Project coinstrack is an attempt to build a database of crypto-currency market data from publicly available data using Python &amp; MySQL</strong>
<br><br>
It works on my system. Hopefully the indications below will be clear and complete enough so you can also make it work on your system as well.
<br>
<br><br>
<strong>1. REQUIREMENTS / INSTALLATION</strong>
<br><br>
You need python 2.x with the following packages installed: 
<br>sys, os, urllib2, httplib, json, datetime, MySQLdb
<br><br>
You need MySQL installed:<br>

Installation instructions here- <br>
https://dev.mysql.com/doc/refman/5.6/en/linux-installation.html<br>
<br>
This can be helpful as well-<br>
http://www.thegeekstuff.com/2008/07/howto-install-mysql-on-linux/<br>
<br>
Now the Python-MySQLdb connector (which will install the MySQLdb dependency):<br>
https://dev.mysql.com/downloads/connector/python/<br>
https://dev.mysql.com/doc/connector-python/en/connector-python-installation.html
<br>
<br><br>
<strong>2. GETTING THINGS READY</strong>
<br>
<br>
Put the files coin_db_update.py, database.py and credentials.mysql in the same folder. 
<br>Make sure it's in your python path-  
<br>
$ echo -e "\nexport PYTHONPATH=\$PYTHONPATH:/path/to/directory" >> ~/.bashrc
<br>
<br><br>
<strong>3. CREATING THE DATABASE</strong><br><br>
Now launch Mysql-
<br>
<br>
$ mysql -u yourusername -p
<br>
You will be prompted for the password you set in the credentials.mysql file. 
<br>There would probably be a way to use encryption which would be more secure.

<br>
mysql> CREATE DATABASE coinstrack;
<br><br>
Now use this database-<br><br>
mysql> USE coinstrack;<br>
<br>
Create the data table in the database-<br>

mysql> CREATE TABLE MARKET_DATA(
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
<br><br>
To check your install, try to run coin_db_update.py manually to make sure there is no error before automating the scraping task.
<br>
<br><br>
<strong>4. SETTING-UP AUTOMATIC UPDATES</strong>
<br><br>
Edit the crontab file in /etc/crontab or /etc/cron.d (depends on the system you use - keep the file name unchanged)
<br>Add the following line to automatically update the data every hour at half past:
<br><br>
30 * * * * computer_username python /path/to/yourpythonprogram/coin_db_update.py
<br><br>
Let it run for a little while to download some data, so you can then use the database!
<br>
<br><br>
<strong>5. USING THE DATABASE</strong>
<br><br>
$ mysql -u yourusername -p <br>

Enter your password (cf. credentials.mysql)<br>
<br>
Now specify the database to use-<br>

mysql> USE coinstrack<br>
<br>
Enter MySQL commands, e.g.<br>
mysql> select TICKER, PRICE_USD, VOLUME24_BTC, TIME_COMPUTER FROM MARKET_DATA WHERE TICKER= "BTC";
<br>
<br><br>
<strong>6. NEXT STEPS</strong>
<br><br>
Now the data is here, and it would be great to use python to analyze and visualize it. <br>
<br>If anyone wants to contribute, you'd be more than welcome!<br>
Contributions on cleaning the code and/or improving this readme are also warmly welcomed.
<br>
<br><br>
<strong>7. CREDITS</strong>
<br><br>
1) Abitfan - https://github.com/abitfan/coinmarketcap-cli <br>
2) Raspberrypi - https://github.com/raspberrypi/weather-station
<br>
<br><br>
<strong>8. DISCLAIMER</strong>
<br><br>
This is amateur code. As such it is prone to bugs and errors. <br>
Obviously I am NOT responsible for any issue you may encounter that are related to this code or the links in the readme.<br> 
You use this material at your own risk.<br>

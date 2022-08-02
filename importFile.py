import pandas as pd
import mysql.connector as msql
from mysql.connector import Error

covid_data = pd.read_csv('/<full path name>/covid_data_formatted_dates.csv', index_col=False, delimiter = ',')
covid_data.head()

try:
	conn = msql.connect(host='localhost', database='xxx', user='xxx',  
                        password='xxx')#give ur username, password
	if conn.is_connected():
		print("Connected to db")
		cursor = conn.cursor()
		
	for i,row in covid_data.iterrows():
		sql = 'INSERT INTO db_grafana.covid_data (submission_date,state,tot_cases,conf_cases,prob_cases,new_case,pnew_case,tot_death,conf_death,prob_death,new_death,pnew_death,created_at,consent_cases,consent_deaths) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
		cursor.execute(sql, tuple(row))
		print("Record inserted")
		conn.commit()
		
except Error as e:
	print("Error connecting to db", e)


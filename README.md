1. Download grafana for raspberry pi
2. Start grafana server
3. Download docker for raspberry pi, pull down image to create mysql container
4. Create database for covid data
5. Download covid data from CDC, and use excel to reformat dates to YYYY-MM-DD and YYYY-MM-DD HH:MM format for submission_date and created_at fields respectively. This is so that it can be read into a SQL database as a date data type.
6. Create Python virtual environment
7. Write python script to import csv data into database and run, populating the database
8. Add mySQL database as source on grafana (running locally)
9. Create bar chart, timeseries, and table in 3 different dashboards to visualize the data in 3 different ways
10. Modify each of the panels (for example change the default table name) and observe how it changes the dashboard data json file (use jsondiff to visualize these changes to the json)

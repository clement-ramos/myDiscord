import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="my_discord"
)
cursor = db.cursor()
import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    user="root",
    passwd="Minecraft01@",
    database="my_discord"
)
cursor = db.cursor()
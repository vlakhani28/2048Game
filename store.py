import mysql.connector
dbConn = mysql.connector.connect(host="localhost", user="root", passwd="")
cursor = dbConn.cursor()

def saving(fn,ln,age,score):
    cursor.execute("Use game_2048")
    cursor.execute("insert into game(First_Name,Last_Name,Age,Score) VALUES('"+fn+"','"+ln+"','"+str(age)+"','"+str(score)+"')")
    dbConn.commit()
def displaydata():
    cursor.execute("Use game_2048")
    cursor.execute("SELECT * FROM game ORDER BY Score DESC LIMIT 5")
    x = cursor.fetchall()
    return x

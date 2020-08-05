import sqlite3
import time
def login():
    for i in range(3):
        username = input("PLS enter your username: ")
        password = input("PLS enter your favorite video game: ")
        with sqlite3.connect('main.db') as db:
            cursour = db.cursor()
        find_user = ('SELECT * FROM login WHERE username = ? AND password = ?')
        cursour.execute(find_user,[(username), (password)])
        results = cursour.fetchall()
        
        if results:
            for i in results:
                buda = str(i)
                print("Welcome " +buda)
#            return('exist')
            break
        else:
            print("Username and favorite game not recognised")
            again = input("Do u want to try again?(y/n): ")
            if again.lower() == "n":
                print("Good Bye")
                time.sleep(1)
#                return('exit')
                break
login()
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
def newUser():
    found = 0
    while found == 0:
        username = input("Please enter a username:  ")
        with sqlite3.connect('main.db') as db:
            cursour = db.cursor()
        findUser = ('SELECT * FROM login WHERE USERNAME = ?')
        cursour.execute(findUser,[(username)])
        
        
        if cursour.fetchall():
            print("Username Taken, Please try again")
        else:
            found = 1
    name = input("Enter your name: ")
    game = input("Enter your favorite game: ")
    game1 = input("PLS re-enter your favorite game: ")     
    while game != game1:
        print("Your favorite game inputs didn't work. Please try again")
        game = input("Enter your favorite game: ")
        game1 = input("PLS re-enter your favorite game: ")
    insertData = '''INSERT INTO login('username', 'password') 
    VALUES(?,?)'''
    cursour.execute(insertData,[(name),(game)])
    
    time.sleep(2)
    print("Succesfully done")
    db.commit()
#newUser()
login()
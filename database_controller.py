import sqlite3


class DB_Controller:
    
    #2 methoden hinzufügen GetDb für selects und Setdb für insert, update, delete
    #diese methode funkioniert
    def __init__(self):
        self.path = "F:\Ausbildung Fachinformatiker\Berufsschule\Jahresprojekt\sqlite\database\datenbank.db"
        self.verbindung = sqlite3.connect(self.path)
        self.zeiger = self.verbindung.cursor()

    #diese methode funkioniert
    def insertnewplayer(self, nickname, password):
        sql = f"INSERT INTO user_table (nickname, password) VALUES ('{nickname}', '{password}')"   
        self.zeiger.execute(sql)
        self.verbindung.commit()
        
    #diese methode funkioniert
    def checkifplayerexistinDB(self, nickname, password):
        sql = f"SELECT * FROM user_table WHERE nickname = '{nickname}' AND password = '{password}'"
        if(self.zeiger.execute(sql)):
            return True
        else:
            return False
    

    #diese methode funkioniert
    def setnewgameintogametable(self, user_id, game_id):        
        sql = f"INSERT INTO user_game_table (user_id, game_id, game_status) VALUES ({user_id}, {game_id}, 0)"
        self.zeiger.execute(sql)
        self.verbindung.commit()

    def savegame(self):
        print('hello')

    
        
    #def SetGameStatusOnFinished(self, game_number):
        #sql = ""
        #verbindung = sqlite3.connect("F:\Ausbildung Fachinformatiker\Berufsschule\Jahresprojekt\sqlite\database\datenbank.db")
        #zeiger = verbindung.cursor()
                
controller = DB_Controller()
#controller.savegame()
#controller.setnewgameintogametable(1, 1)
#controller.insertnewplayer('test', 'test')

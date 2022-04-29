import sqlite3
import os
import globals
from datetime import datetime
from sqlite.init_database import init_command
from board import Board


class DB_Controller:
    
    #2 methoden hinzufügen GetDb für selects und Setdb für insert, update, delete
    #diese methode funkioniert
    def __init__(self):
        self.path = os.path.join(os.path.abspath(os.curdir),"sqlite/datenbank.db")
        self.verbindung = sqlite3.connect(self.path)
        self.zeiger = self.verbindung.cursor()
        sql = "SELECT name FROM sqlite_master WHERE type='table' AND name='user_table'"
        result = self.zeiger.execute(sql).fetchone()
        self.verbindung.commit()
        if result == None:
            self.initDatabase()
            #führe init_methode aus
        print("End of init")
        
    def initDatabase(self):
        for command in init_command:
            print(command)
            result = self.zeiger.execute(command)
            self.verbindung.commit()

    #diese methode funkioniert
    def insertnewplayer(self, nickname, password):
        sql = f"INSERT INTO user_table (nickname, password) VALUES ('{nickname}', '{password}')" 
        result = self.zeiger.execute(sql)
        self.verbindung.commit()
        if result.rowcount == 1:
            return True
        else:
            return False
        
        
    #diese methode funkioniert
    def checkifplayerexistinDB(self, nickname, password):
        sql = f"SELECT * FROM user_table WHERE nickname = '{nickname}' AND password = '{password}'"
        if(self.zeiger.execute(sql)):
            result = self.zeiger.fetchone()
            if result:
                id = result[0]
                globals.setUser(nickname, id)
                return True
            else:
                return False    

    #diese methode funkioniert
    def setnewgameintogametable(self, user_id):
        time = datetime.now().strftime("%d.%m.%Y, %H:%M:%S")
        sql = f"INSERT INTO user_game_table (user_id,game_status, saved_date) VALUES ({user_id}, 0, '{time}')"
        self.zeiger.execute(sql)
        self.verbindung.commit()
        return self.zeiger.lastrowid

    def loadSavedGames(self, user_id):
        sql = sql = f"SELECT * FROM user_game_table WHERE user_id = '{user_id}'"
        self.zeiger.execute(sql)
        return self.zeiger.fetchall()


    def savefilegame(self,userid, board : Board, currentplayer):
        id = None
        if globals.saveGameNumber != None:
            sql = f"DELETE FROM savefile_table WHERE game_number = {globals.saveGameNumber}"
            self.zeiger.execute(sql)
            time = datetime.now().strftime("%d.%m.%Y, %H:%M:%S")  
            timesql = f"UPDATE user_game_table SET saved_date = '{time}' WHERE game_number= {globals.saveGameNumber} and user_id = {userid}"
            self.zeiger.execute(timesql)
            self.verbindung.commit()
            id = globals.saveGameNumber
        else:
            id = self.setnewgameintogametable(userid)
            globals.setSaveGameNumber(id)
        for columnIndex,column in enumerate(board.get2dArray()):
            for rowIndex, field in enumerate(column):
                if(field.getPawn() != None):
                    team = field.getPawn().getTeam()
                    sql = f"INSERT INTO savefile_table (user_id, game_number, figur_team, figur_column, figur_row, current_player) VALUES ({userid}, {id}, '{team}', {columnIndex}, {rowIndex}, '{currentplayer}')"
                    self.zeiger.execute(sql)
                    self.verbindung.commit()

    def loadSaveFileGame(self,userId, gameNumber):
        globals.setSaveGameNumber(gameNumber)
        sql = f"SELECT * FROM savefile_table WHERE game_number = {gameNumber} AND user_id = {userId}"
        return self.zeiger.execute(sql).fetchall()

    def setgamestatusonfinished(self, game_number):
        sql = f"UPDATE user_game_table SET game_status = 1 WHERE game_number = {game_number}"
        result = self.zeiger.execute(sql)
        self.verbindung.commit()
        if result.rowcount == 1:
            return True
        else:
            return False

    def loadfilegame(self, game_id):
        sql = f"SELECT * FROM savefile_table WHERE game_number = {game_id}"
        self.zeiger.execute(sql)
        inhalt = self.zeiger.fetchall()
        print(inhalt)

                
#controller = DB_Controller()
#controller.loadfilegame(8)
#controller.savegame()
#controller.setnewgameintogametable(1, 1)
#controller.insertnewplayer('test', 'test')

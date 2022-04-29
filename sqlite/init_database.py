init_command = ["CREATE TABLE [game_table]([game_id] INT64(2, 25) PRIMARY KEY NOT NULL UNIQUE,[game_name] VARCHAR2(25, 25) NOT NULL);", "CREATE TABLE [leaderboard_table]([user_id] INT64(5, 25) NOT NULL,[game_id] INT64(5, 25) NOT NULL,[playing_strength] INT64(3, 25) NOT NULL,[win_loss] INT64(2, 25) NOT NULL);", "CREATE TABLE [savefile_table]([user_id] INT64(2, 25) NOT NULL,[game_number] INT64(5, 25) NOT NULL,[figur_team] INT64(2, 25) NOT NULL,[figur_row] VARCHAR2(250, 25) NOT NULL,[figur_column] VARCHAR2(250, 25) NOT NULL);", "CREATE TABLE [user_game_table]([game_number] INTEGER PRIMARY KEY AUTOINCREMENT,[user_id] INT64(2, 25) NOT NULL,[game_id] INT64(2, 25) NOT NULL,[game_status] INT64(2, 25) NOT NULL, [saved_date] VARCHAR2(50,25) NOT NULL)", "CREATE TABLE [user_table]([id] INTEGER PRIMARY KEY AUTOINCREMENT,[nickname] VARCHAR2(50,25) NOT NULL,[password] VARCHAR2(50,25) NOT NULL);"]

import json
import sqlite3
import threading
import time


conn = sqlite3.connect('../database/database.db')
cursor = conn.cursor()

def writeToDatabase():
    try:
        while True:
            with open("data.json", "r") as jsonFile:
                data = json.load(jsonFile)
            jsonFile.close()
            x_value = time.strftime("%I:%M:%S", time.localtime())
            total_1 = data['lane_1']
            total_2 = data['lane_2']
            total_3 = data['lane_3']
            total_4 = data['lane_4']
            query = f'''
            insert into signal
            values
            ("{x_value}", {total_1},{total_2},{total_3},{total_4});
            '''
            cursor.execute(query)
            conn.commit()
            print(x_value, total_1, total_2, total_3, total_3)
            time.sleep(10)
    except KeyboardInterrupt:
                  print("KeyboardInterrupt: Closing cursor and connection.")
                  

    except Exception as e:
                  print(f"An error occurred: {e}")

    finally:
                 if cursor:
                     cursor.close()
                 if conn:
                     conn.close()
        
if __name__ == "__main__":
    writeToDatabase()
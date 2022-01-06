
import sqlite3
  
  
# Function for Convert Binary Data 
# to Human Readable Format
def convertToBinaryData(filename):
      
    # Convert binary format to images 
    # or files data
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData
  
  
def insertBLOB(First_name, Last_name, photo, mail):
    try:
          
        # Using connect method for establishing
        # a connection
        sqliteConnection = sqlite3.connect('SQLite_data.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
          
        # insert query
        sqlite_insert_blob_query = """ INSERT INTO Person
        
                                  (First_name, Last_name, img, mail) VALUES (?, ?, ?, ?)"""
          
        # Converting human readable file into 
        # binary data
        empPhoto = convertToBinaryData(photo)
          
        # Convert data into tuple format
        data_tuple = (First_name, Last_name, empPhoto, mail)
          
        # using cursor object executing our query
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()
  
    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
      
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("the sqlite connection is closed")
            
insertBLOB("Aya", "Ben Khedher", "C:\miniprojet\images\Aya.jpg", "ayabenkhedher84@gmail.com")           
insertBLOB("Elon", "Musk", "C:\miniprojet\images\ElonMask.jpg", "elonmask@gmail.com")  
insertBLOB("Messi", "lional", "C:\miniprojet\images\Messi.jfif", "messilional@gmail.com")
insertBLOB("Steve", "Jobs", "C:\miniprojet\images\Steve_Jobs.jpg", "stevejobs@gmail.com")
insertBLOB("Wissal", "Daoued", "C:\miniprojet\images\Wissal.jpg", "daoudwissal2000@gmail.com")




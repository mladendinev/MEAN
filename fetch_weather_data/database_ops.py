import pymongo

class dbOperations:
    def __init__(self, database):
        try:
            if database == "local":
                self.client = pymongo.MongoClient('localhost', 27017)
                self.db = self.client['weather_data']
            else:
                raise Exception("Non existent database")
        except Exception as e:
            raise ValueError("Invalid database option")

    def insertData(self, dataJson, collection):
        try:
            self.db[collection].insert(dataJson)
        except Exception as e:
            print ("Insert operation exception", e)
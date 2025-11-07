from db import db_conn
import pandas as pd


class User:
    # CONSTRUCTOR
    def __init__(self, name="", cpf="", age=0, height=0):
        self.name = name
        self.cpf = cpf
        self.age = age
        self.height = height
        self.users = db_conn["users"]

    # INSERT RECORD
    def insert_one_record(self):
        if not self.record_exists(self.cpf):
            user_data = dict(
                name=self.name, cpf=self.cpf, age=self.age, height=self.height
            )
            self.users.insert_one(user_data)
        else:
            raise Exception("Record already exists!")

    # FIND RECORD(S)
    def search_record(self, cpf=""):
        if cpf != "":
            user = list(self.users.find({"cpf": cpf}, {"_id": 0}))[0]
            return user
        else:
            print(f"{' User List ':=^40}")
            print(pd.DataFrame(self.users.find({}, {"_id": 0})))

    # UPDATE RECORD
    def update_record(self, cpf):
        user = self.search_record(cpf)

        if self.name != "":
            user["name"] = self.name
        if self.cpf != "":
            user["cpf"] = self.cpf
        if self.age != 0:
            user["age"] = self.age
        if self.height != 0:
            user["height"] = self.height

        if not self.record_exists(self.cpf):
            self.users.update_one({"cpf": cpf}, {"$set": user})
        else:
            raise Exception("CPF already exists!")

    # LIST ALL RECORDS
    def list_records(self):
        print(f"{' User List ':=^40}")
        print(pd.DataFrame(self.users.find({}, {"_id": 0})))

    # CHECK IF RECORD EXISTS IN DB
    def record_exists(self, cpf) -> bool:
        data = dict(cpf=cpf)
        if self.users.count_documents(data) > 0:
            return True
        return False

    # DELETE SPECIFIC RECORD
    def delete_record(self, cpf):
        self.users.find_one_and_delete({"cpf": cpf})
        # self.users.delete_one({"_id": ObjectId("607f020ee2dd4f554c912cd3")})  # Example with ObjectId

    # DELETE ALL RECORDS
    def clear_database(self):
        self.users.delete_many({})


# Testing methods
user = User("Bruno", "", 25, 1.30)
# user.clear_database()
# user.insert_one_record()
user.update_record("022")
# user.list_records()
# user.search_record()
# user.delete_record("01234")


import datetime



class contact:
    def __init__(self, id, name, phone, email, birthyear):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email
        self.age = datetime.datetime.today().year - birthyear


# import datetime
# year = datetime.datetime.today().year


    






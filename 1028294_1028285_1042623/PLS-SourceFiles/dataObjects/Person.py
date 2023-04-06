class Person:
    objectKey = -1
    userName = ""
    password = ""
    isAdmin = False
    
    def __init__(self, username, password):
        self.userName = username
        self.password = password
        print("Inititalize person\n")
    
    def Login(username, password):
        users = [{"userName": "admin", "password": "admin123"}, {"userName": "michael", "password": "admin123"}, {"userName": "jeremey", "password": "admin123"} ]
        
        for el in users:
            if el["userName"] == username and el["password"] == password:
                return True
        return False
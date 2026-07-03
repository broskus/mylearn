
class Database:
    def __init__(self):
        self.connection = None
    
    def connect(self):
        self.connection = "Connected"
        return self.connection
    
    def disconnect(self):
        self.connection = None

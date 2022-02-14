class client():
    def __init__(self, ip, name, connection):
        self.ip = ip
        self.name = name
        self.last_message = ""
        self.last_message_time = 0
        self.connection_obj = connection

    def close_connection(self):
        self.connection_obj.close()

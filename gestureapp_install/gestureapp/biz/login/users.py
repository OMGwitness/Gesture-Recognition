class UserDAO:
    def __init__(self):
        self.users_data = ["zhangguangjie", "liutaorong", "liuzirui", "qiujunchao"]    
    
    def validate(self, username):
        return username.lower() in self.users_data
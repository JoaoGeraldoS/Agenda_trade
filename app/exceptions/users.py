class UserExists(Exception):
    def __init__(self, message: str):
        self.message = message


class UserInvalideCredentials(Exception):
    def __init__(self, message):
        self.message = message

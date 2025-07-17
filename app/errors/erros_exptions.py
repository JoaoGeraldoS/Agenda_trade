class IsNotNoneException(Exception):
    def __init__(self, message):
        self.message = message

class InvalidCredentials(Exception):
    def __init__(self, message):
        self.message = message
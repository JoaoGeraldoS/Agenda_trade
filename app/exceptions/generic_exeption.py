class NotFound(Exception):
    def __init__(self, message):
        self.message = message

class BadRequest(Exception):
    def __init__(self, message):
        self.message = message
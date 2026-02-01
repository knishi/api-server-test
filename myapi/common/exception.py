class AppError(Exception):
    """Base API Exception."""
    code = 500
    message = "An unknown error occurred."

    def __init__(self, message=None):
        if message:
            self.message = message
        super().__init__(self.message)

class ItemNotFound(AppError):
    code = 404
    message = "Item not found."

class InvalidInput(AppError):
    code = 400
    message = "Invalid input received."

class IMDBException(Exception):
    def __init__(self, *args):
        super().__init__(*args)

        # print('Printing Errors:')
        # print(errors)

class IMDBConnectionError(Exception):
    def __init__(self, message, status_code, *args):
        super().__init__(message, *args)
        self.status_code = status_code

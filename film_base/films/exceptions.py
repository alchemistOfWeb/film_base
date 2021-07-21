class IMDBException(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class IMDBConnectionError(Exception):
    def __init__(self, message, status_code, *args):
        super().__init__(message, *args)
        self.status_code = status_code

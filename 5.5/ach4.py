class ConnectionError(Exception):
    ...


class DatabaseConnection:
    def connect(self, login, password):
        self._fl_connection_open = True
        raise ConnectionError

    def close(self):
        self._fl_connection_open = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


with DatabaseConnection() as db:
    ...

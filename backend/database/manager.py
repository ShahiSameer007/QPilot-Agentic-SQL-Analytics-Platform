from abc import ABC, abstractmethod


class DatabaseManager(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def test_connection(self):
        pass

    @abstractmethod
    def execute_query(self, query, params=None):
        pass

    @abstractmethod
    def list_tables(self):
        pass

    @abstractmethod
    def describe_table(self, table_name):
        pass

    @abstractmethod
    def get_schema(self):
        pass
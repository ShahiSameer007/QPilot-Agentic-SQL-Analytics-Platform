import logging

import psycopg

from backend.config import settings
from backend.database.manager import DatabaseManager


logger = logging.getLogger(__name__)


class PostgreSQLConnector(DatabaseManager):
    """
    PostgreSQL implementation of the DatabaseManager interface.
    """

    def __init__(self):
        self.connection = None

    def connect(self):
        """
        Establish a connection to the PostgreSQL database.
        """

        try:
            self.connection = psycopg.connect(
                host=settings.DB_HOST,
                port=settings.DB_PORT,
                dbname=settings.DB_NAME,
                user=settings.DB_USER,
                password=settings.DB_PASSWORD,
            )

            logger.info("Successfully connected to PostgreSQL.")
            return self.connection

        except psycopg.Error:
            logger.exception("Failed to connect to PostgreSQL.")
            raise

    def disconnect(self):
        """
        Close the PostgreSQL database connection.
        """

        if self.connection is None:
            logger.warning("No active PostgreSQL connection to close.")
            return

        try:
            self.connection.close()
            logger.info("PostgreSQL connection closed successfully.")

        except psycopg.Error:
            logger.exception("Failed to close PostgreSQL connection.")
            raise

        finally:
            self.connection = None

    def test_connection(self):
        pass

    def execute_query(self, query, params=None):
        pass

    def list_tables(self):
        pass

    def describe_table(self, table_name):
        pass

    def get_schema(self):
        pass
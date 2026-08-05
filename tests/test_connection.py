import logging

from backend.database.connectors.postgres import PostgreSQLConnector


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(name)s | %(message)s"
)


def main():
    connector = PostgreSQLConnector()

    try:
        connector.connect()
        connector.disconnect()
        print("Connection test passed.")

    except Exception as e:
        print(f"Connection test failed: {e}")


if __name__ == "__main__":
    main()
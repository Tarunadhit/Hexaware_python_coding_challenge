import os


class PropertyUtil:
    @staticmethod
    def getPropertyString():
        server_name = "DESKTOP-SRA8EHN"
        database_name = "hospital"
        trusted_connection = "yes"
        return f"Driver={{SQL Server}};Server={server_name};Database={database_name};Trusted_Connection={trusted_connection};"

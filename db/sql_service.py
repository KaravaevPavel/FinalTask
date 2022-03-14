class SQLService:

    def __init__(self, connection):
        self.cursor = connection.cursor()

    def get_first_name(self, email):
        query = f"SELECT Firstname FROM lc_customers WHERE Email='{email}'"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result[0]

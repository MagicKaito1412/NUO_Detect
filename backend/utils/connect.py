import psycopg2


conn = psycopg2.connect(dbname='nuo_detect',
                        user='u1',
                        password='1',
                        host='127.0.0.1')
cur = conn.cursor()


def db_transaction(func):
    """ Decorator """
    def call(*args, **kwargs):
        """ Actual wrapping """
        global conn
        global cur
        try:
            result = func(conn, cur, *args, **kwargs)
        except psycopg2.DatabaseError as result:
            print(result)
            if conn is not None:
                conn.close()
            conn = psycopg2.connect(dbname='nuo_detect',
                                    user='u1',
                                    password='1',
                                    host='127.0.0.1')
            cur = conn.cursor()
        return result
    return call

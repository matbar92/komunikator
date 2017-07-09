from mysql.connector import connect

def connect_to_db(): #polaczenie cnx i cursor
    cnx = connect(
        user='root',
        password='coderslab',
        database='communicator_db'
    );

    cursor = cnx.cursor()

    return cnx, cursor


def close_connection(cnx, cursor):
    cnx.commit()
    cursor.close()
    cnx.close()


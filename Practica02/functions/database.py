import mysql.connector
import constants.db_config as connection_parameters
import constants.sql_statements as sql_statements
from classes.disc import Disc


# Crea la conexión de la base de datos.
def db_connect():
    db_connection = mysql.connector.connect(
        host=connection_parameters.DB_HOST,
        port=connection_parameters.DB_PORT,
        user=connection_parameters.DB_USER,
        password=connection_parameters.DB_PASSWORD,
        database=connection_parameters.DB_DATABASE_NAME
    )
    return db_connection


def get_validated_disks():
    disc_list = []  # Para almacenar los objetos Disc que se devolverán.
    sql = sql_statements.SQL_SELECT_VALIDATED_DISCS
    db_connection = db_connect()
    db_cursor = db_connection.cursor()
    db_cursor.execute(sql)
    temp_list = db_cursor.fetchall()
    db_cursor.close()
    db_connection.close()

    for tuple_disc in temp_list:
        disc = Disc()
        disc.id_disc = tuple_disc[0]
        disc.title = tuple_disc[1]
        disc.performer = tuple_disc[2]
        disc.music_style = tuple_disc[3]
        disc.tracks = int(tuple_disc[4])
        disc.price = float(tuple_disc[5])
        disc.email = tuple_disc[6]
        disc_list.append(disc)
    return disc_list


# Obtiene el listado de los discos
def get_all_disks():
    disc_list = []  # Para almacenar los objetos Disc que se devolverán.
    sql = sql_statements.SQL_SELECT_ALL_DISCS
    db_connection = db_connect()
    db_cursor = db_connection.cursor()
    db_cursor.execute(sql)
    temp_list = db_cursor.fetchall()
    db_cursor.close()
    db_connection.close()

    for tuple_disc in temp_list:
        disc = Disc()
        disc.id_disc = tuple_disc[0]
        disc.title = tuple_disc[1]
        disc.performer = tuple_disc[2]
        disc.music_style = tuple_disc[3]
        disc.tracks = int(tuple_disc[4])
        disc.price = float(tuple_disc[5])
        disc.email = tuple_disc[6]
        disc_list.append(disc)
    return disc_list


# Obtiene el disco con el id que se facilita y lo devuelve.
def get_disc_by_id(id_disc):
    sql = sql_statements.SQL_SELECT_DISC_BY_ID
    values = (id_disc,)
    db_conn = db_connect()
    db_cursor = db_conn.cursor()
    db_cursor.execute(sql, values)
    row = db_cursor.fetchone()
    db_conn.disconnect()
    disc = Disc()
    disc.id_disc = int(row[0])
    disc.title = row[1]
    disc.performer = row[2]
    disc.music_style = row[3]
    disc.tracks = int(row[4])
    disc.price = float(row[5])
    disc.email = row[6]
    return disc


# actualiza en la base de datos el disco pasado por parametro.
def update_disc(disc):
    sql = sql_statements.SQL_UPDATE_DISC
    values = (disc.title, disc.performer, disc.music_style, disc.tracks, disc.price, disc.id_disc)
    db_connection = db_connect()
    db_cursor = db_connection.cursor()
    db_cursor.execute(sql, values)
    db_connection.commit()
    db_cursor.close()
    db_connection.close()
    return


# Añade el disco a la base de datos y devuelve el mismo disco con el id cumplimentado.
def insert_disc(disc):
    sql = sql_statements.SQL_INSERT_DISC
    values = (disc.title, disc.performer, disc.music_style, disc.tracks, disc.price, disc.email)
    db_connection = db_connect()
    db_cursor = db_connection.cursor()
    db_cursor.execute(sql, values)
    db_connection.commit()
    generated_id = db_cursor.lastrowid
    db_cursor.close()
    db_connection.close()
    disc.id_disc = generated_id
    return disc


# Marca un disco como borrado.
def delete_disc(disc_id):
    sql = sql_statements.SQL_DELETE_DISC
    values = (disc_id,)
    db_connection = db_connect()
    db_cursor = db_connection.cursor()
    db_cursor.execute(sql, values)
    db_connection.commit()
    db_cursor.close()
    db_connection.close()
    return


# Marca un anuncio como validado.
def validate_disc(disc_id):
    sql = sql_statements.SQL_VALIDATE_DISC
    values = (disc_id,)
    db_connection = db_connect()
    db_cursor = db_connection.cursor()
    db_cursor.execute(sql, values)
    db_connection.commit()
    db_cursor.close()
    db_connection.close()
    return


# Añade el código de validación en la base de datos.
def insert_validation_code(disc_id, validation_code):
    sql = sql_statements.SQL_INSERT_VALIDATION_CODE
    values = (disc_id, validation_code)
    db_connection = db_connect()
    db_cursor = db_connection.cursor()
    db_cursor.execute(sql, values)
    db_connection.commit()
    db_cursor.close()
    db_connection.close()
    return


# Cuando se valide un anuncio, se eliminará de la tabla de los códigos de validacion. Un anuncio
# solo se puede validar 1 vez.
def delete_validation_code(disc_id):
    sql = sql_statements.SQL_DELETE_VALIDATION_CODE
    values = (disc_id,)
    db_connection = db_connect()
    db_cursor = db_connection.cursor()
    db_cursor.execute(sql, values)
    db_connection.commit()
    db_cursor.close()
    db_connection.close()


# Comprueba si el codigo de validación se corresponde al disco.    
def check_validation_code(disc_id, validation_code):
    sql = sql_statements.SQL_SELECT_VALIDATION_CODE
    values = (disc_id, validation_code)
    db_connection = db_connect()
    db_cursor = db_connection.cursor()
    db_cursor.execute(sql, values)
    lst_validation_codes = db_cursor.fetchall()
    db_cursor.close()
    db_connection.close()
    return len(lst_validation_codes) > 0

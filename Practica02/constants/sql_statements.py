'''
Creación de tabla

CREATE TABLE table_disc (
    id INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(200) NOT NULL,
    performer VARCHAR(100) NOT NULL,
    music_style VARCHAR(100) NOT NULL,
    tracks INT NOT NULL DEFAULT 1,
    price DECIMAL(6,2) NOT NULL DEFAULT 0.0,
    email VARCHAR(250) NOT NULL,
    deleted TINYINT NOT NULL DEFAULT 0,
    validated TINYINT NOT NULL DEFAULT 0,
    PRIMARY KEY (id));
'''
# Sentencias SQL table_disc
SQL_SELECT_ALL_DISCS = ("SELECT id, title, performer, music_style, tracks, price, email "
                  "FROM table_disc; ")

SQL_SELECT_VALIDATED_DISCS = ("SELECT id, title, performer, music_style, tracks, price, email "
                  "FROM table_disc "
                  "WHERE deleted = 0 AND validated = 1;")


SQL_SELECT_DISC_BY_ID = ("SELECT id, title, performer, music_style, tracks, price, email "
                    "FROM table_disc "
                    "WHERE deleted = 0 AND id = %s;")

SQL_INSERT_DISC = ("INSERT INTO table_disc (title, performer, music_style, tracks, price, email) "
              "VALUES (%s, %s, %s, %s, %s, %s);")

SQL_UPDATE_DISC = ("UPDATE table_disc "
              "SET title = %s, performer = %s, music_style = %s, tracks = %s, price = %s, email = %s "
              "WHERE id = %s AND deleted = 0")

SQL_DELETE_DISC = ("UPDATE table_disc "
              "SET deleted = 1 "
              "WHERE id = %s")

SQL_VALIDATE_DISC = ("UPDATE table_disc "
                     "SET validated = 1 "
                     "WHERE id = %s;")

'''
Creación de tabla:

CREATE TABLE table_validation (
    id INT NOT NULL,
    code VARCHAR(200) NOT NULL,
    PRIMARY KEY (id));

'''

# Sentencias table_validation

SQL_INSERT_VALIDATION_CODE = ("INSERT INTO table_validation (id, code) "
                              "VALUES (%s, %s);")

SQL_DELETE_VALIDATION_CODE = ("DELETE FROM table_validation "
                              "WHERE id = %s;")

SQL_SELECT_VALIDATION_CODE = ("SELECT * "
                              "FROM table_validation "
                              "WHERE id = %s AND code = %s")

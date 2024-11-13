import sqlite3
import os, sys

if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(__file__)
path = f'{base_path}\database.db' 
print(path)

def connect():
    connection = sqlite3.connect(path)

    cursor = connection.cursor()

    cursor.execute('''
    create table IF NOT EXISTS cutting (
    type_reel integer NOT NULL check (type_reel in (70, 100, 150, 166)),
    type_roller integer NOT NULL check (type_roller in (840, 1050)),
    count_70 integer check (count_70 >= 0),
    count_100 integer check (count_100 >= 0),
    count_150 integer check (count_150 >= 0),
    count_166 integer check (count_166 >= 0),
    PRIMARY KEY (type_reel, type_roller));
    ''')

    cursor.execute('SELECT count(*) FROM cutting')

    if cursor.fetchall()[0][0] == 0:
        cursor.execute('INSERT INTO cutting VALUES (70, 840, 7, 3, 0, 0)')
        cursor.execute('INSERT INTO cutting VALUES (100, 840, 0, 8, 0, 0)')
        cursor.execute('INSERT INTO cutting VALUES (150, 840, 0, 0, 5, 0)')
        cursor.execute('INSERT INTO cutting VALUES (166, 840, 0, 1, 0, 4)')
        cursor.execute('INSERT INTO cutting VALUES (70, 1050, 12, 0, 1, 0)')
        cursor.execute('INSERT INTO cutting VALUES (100, 1050, 0, 10, 0, 0)')
        cursor.execute('INSERT INTO cutting VALUES (150, 1050, 0, 0, 7, 0)')
        cursor.execute('INSERT INTO cutting VALUES (166, 1050, 1, 0, 1, 5)')

    cursor.execute('''
    create table IF NOT EXISTS winding (
    class text NOT NULL check (class in ('standart', 'econom')),
    type_reel integer NOT NULL check (type_reel in (70, 100, 150, 166)),
    thickness integer NOT NULL check (thickness in (8, 16)),
    time real check (time > 0),
    PRIMARY KEY (class, type_reel, thickness));
    ''')

    cursor.execute('SELECT count(*) FROM winding')

    if cursor.fetchall()[0][0] == 0:
        cursor.execute('INSERT INTO winding VALUES ("econom", 70, 16, 30)')
        cursor.execute('INSERT INTO winding VALUES ("econom", 100, 16, 30)')
        cursor.execute('INSERT INTO winding VALUES ("econom", 150, 16, 30)')
        cursor.execute('INSERT INTO winding VALUES ("econom", 166, 16, 30)')
        cursor.execute('INSERT INTO winding VALUES ("econom", 70, 8, 29)')
        cursor.execute('INSERT INTO winding VALUES ("econom", 100, 8, 30)')
        cursor.execute('INSERT INTO winding VALUES ("econom", 150, 8, 30)')
        cursor.execute('INSERT INTO winding VALUES ("econom", 166, 8, 30)')
        cursor.execute('INSERT INTO winding VALUES ("standart", 70, 16, 30)')
        cursor.execute('INSERT INTO winding VALUES ("standart", 100, 16, 30)')
        cursor.execute('INSERT INTO winding VALUES ("standart", 150, 16, 30)')
        cursor.execute('INSERT INTO winding VALUES ("standart", 166, 16, 30)')
        cursor.execute('INSERT INTO winding VALUES ("standart", 70, 8, 20)')
        cursor.execute('INSERT INTO winding VALUES ("standart", 100, 8, 35)')
        cursor.execute('INSERT INTO winding VALUES ("standart", 150, 8, 30)')
        cursor.execute('INSERT INTO winding VALUES ("standart", 166, 8, 30)')

    cursor.execute('''
    create table IF NOT EXISTS thickness (
    card real NOT NULL,
    thickness real NOT NULL,
    count integer NOT NULL,
    PRIMARY KEY (card, thickness));
    ''')

    cursor.execute('SELECT count(*) FROM thickness')

    if cursor.fetchall()[0][0] == 0:
        cursor.execute('INSERT INTO thickness VALUES (0.6, 1, 2)')
        cursor.execute('INSERT INTO thickness VALUES (0.6, 1.5, 2)')
        cursor.execute('INSERT INTO thickness VALUES (0.6, 2, 3)')
        cursor.execute('INSERT INTO thickness VALUES (0.6, 2.5, 4)')
        cursor.execute('INSERT INTO thickness VALUES (0.6, 3, 5)')
        cursor.execute('INSERT INTO thickness VALUES (0.6, 3.5, 5)')
        cursor.execute('INSERT INTO thickness VALUES (0.6, 4, 6)')
        cursor.execute('INSERT INTO thickness VALUES (0.6, 4.5, 7)')
        cursor.execute('INSERT INTO thickness VALUES (0.6, 5, 8)')
        cursor.execute('INSERT INTO thickness VALUES (0.6, 5.5, 9)')
        cursor.execute('INSERT INTO thickness VALUES (0.6, 6, 10)')
        cursor.execute('INSERT INTO thickness VALUES (0.6, 6.5, 10)')
        cursor.execute('INSERT INTO thickness VALUES (0.6, 7, 11)')
        cursor.execute('INSERT INTO thickness VALUES (0.6, 7.5, 12)')
        cursor.execute('INSERT INTO thickness VALUES (0.6, 8, 13)')
        cursor.execute('INSERT INTO thickness VALUES (0.6, 8.5, 14)')
        cursor.execute('INSERT INTO thickness VALUES (0.6, 9, 15)')
        cursor.execute('INSERT INTO thickness VALUES (0.6, 9.5, 16)')
        cursor.execute('INSERT INTO thickness VALUES (0.6, 10, 16)')
        cursor.execute('INSERT INTO thickness VALUES (0.6, 10.5, 17)')
        cursor.execute('INSERT INTO thickness VALUES (0.6, 11, 18)')
        cursor.execute('INSERT INTO thickness VALUES (0.6, 11.5, 19)')
        cursor.execute('INSERT INTO thickness VALUES (0.6, 12, 20)')
        cursor.execute('INSERT INTO thickness VALUES (0.6, 12.5, 20)')
        cursor.execute('INSERT INTO thickness VALUES (0.6, 13, 21)')
        cursor.execute('INSERT INTO thickness VALUES (0.6, 13.5, 22)')
        cursor.execute('INSERT INTO thickness VALUES (0.6, 14, 23)')
        cursor.execute('INSERT INTO thickness VALUES (0.6, 14.5, 24)')
        cursor.execute('INSERT INTO thickness VALUES (0.6, 15, 24)')
        cursor.execute('INSERT INTO thickness VALUES (0.6, 15.5, 25)')
        cursor.execute('INSERT INTO thickness VALUES (0.6, 16, 25)')
        cursor.execute('INSERT INTO thickness VALUES (0.55, 1, 2)')
        cursor.execute('INSERT INTO thickness VALUES (0.55, 1.5, 3)')
        cursor.execute('INSERT INTO thickness VALUES (0.55, 2, 4)')
        cursor.execute('INSERT INTO thickness VALUES (0.55, 2.5, 5)')
        cursor.execute('INSERT INTO thickness VALUES (0.55, 3, 6)')
        cursor.execute('INSERT INTO thickness VALUES (0.55, 3.5, 7)')
        cursor.execute('INSERT INTO thickness VALUES (0.55, 4, 8)')
        cursor.execute('INSERT INTO thickness VALUES (0.55, 4.5, 9)')
        cursor.execute('INSERT INTO thickness VALUES (0.55, 5, 10)')
        cursor.execute('INSERT INTO thickness VALUES (0.55, 5.5, 11)')
        cursor.execute('INSERT INTO thickness VALUES (0.55, 6, 11)')
        cursor.execute('INSERT INTO thickness VALUES (0.55, 6.5, 12)')
        cursor.execute('INSERT INTO thickness VALUES (0.55, 7, 13)')
        cursor.execute('INSERT INTO thickness VALUES (0.55, 7.5, 14)')
        cursor.execute('INSERT INTO thickness VALUES (0.55, 8, 15)')
        cursor.execute('INSERT INTO thickness VALUES (0.55, 8.5, 16)')
        cursor.execute('INSERT INTO thickness VALUES (0.55, 9, 17)')
        cursor.execute('INSERT INTO thickness VALUES (0.55, 9.5, 18)')
        cursor.execute('INSERT INTO thickness VALUES (0.55, 10, 19)')
        cursor.execute('INSERT INTO thickness VALUES (0.55, 10.5, 20)')
        cursor.execute('INSERT INTO thickness VALUES (0.55, 11, 21)')
        cursor.execute('INSERT INTO thickness VALUES (0.55, 11.5, 22)')
        cursor.execute('INSERT INTO thickness VALUES (0.55, 12, 22)')
        cursor.execute('INSERT INTO thickness VALUES (0.55, 12.5, 23)')
        cursor.execute('INSERT INTO thickness VALUES (0.55, 13, 24)')
        cursor.execute('INSERT INTO thickness VALUES (0.55, 13.5, 25)')
        cursor.execute('INSERT INTO thickness VALUES (0.5, 1, 2)')
        cursor.execute('INSERT INTO thickness VALUES (0.5, 1.5, 3)')
        cursor.execute('INSERT INTO thickness VALUES (0.5, 2, 4)')
        cursor.execute('INSERT INTO thickness VALUES (0.5, 2.5, 5)')
        cursor.execute('INSERT INTO thickness VALUES (0.5, 3, 6)')
        cursor.execute('INSERT INTO thickness VALUES (0.5, 3.5, 7)')
        cursor.execute('INSERT INTO thickness VALUES (0.5, 4, 8)')
        cursor.execute('INSERT INTO thickness VALUES (0.5, 4.5, 9)')
        cursor.execute('INSERT INTO thickness VALUES (0.5, 5, 10)')
        cursor.execute('INSERT INTO thickness VALUES (0.5, 5.5, 11)')
        cursor.execute('INSERT INTO thickness VALUES (0.5, 6, 12)')
        cursor.execute('INSERT INTO thickness VALUES (0.5, 6.5, 13)')
        cursor.execute('INSERT INTO thickness VALUES (0.5, 7, 14)')
        cursor.execute('INSERT INTO thickness VALUES (0.5, 7.5, 15)')
        cursor.execute('INSERT INTO thickness VALUES (0.5, 8, 16)')
        cursor.execute('INSERT INTO thickness VALUES (0.5, 8.5, 17)')
        cursor.execute('INSERT INTO thickness VALUES (0.5, 9, 18)')
        cursor.execute('INSERT INTO thickness VALUES (0.5, 9.5, 19)')
        cursor.execute('INSERT INTO thickness VALUES (0.5, 10, 20)')
        cursor.execute('INSERT INTO thickness VALUES (0.5, 10.5, 21)')
        cursor.execute('INSERT INTO thickness VALUES (0.5, 11, 22)')
        cursor.execute('INSERT INTO thickness VALUES (0.5, 11.5, 23)')
        cursor.execute('INSERT INTO thickness VALUES (0.5, 12, 24)')
        cursor.execute('INSERT INTO thickness VALUES (0.5, 12.5, 25)')
        cursor.execute('INSERT INTO thickness VALUES (0.7, 14, 20)')
        cursor.execute('INSERT INTO thickness VALUES (0.7, 14.5, 20)')
        cursor.execute('INSERT INTO thickness VALUES (0.7, 15, 21)')
        cursor.execute('INSERT INTO thickness VALUES (0.7, 15.5, 22)')
        cursor.execute('INSERT INTO thickness VALUES (0.7, 16, 23)')
        cursor.execute('INSERT INTO thickness VALUES (0.7, 16.5, 24)')
        cursor.execute('INSERT INTO thickness VALUES (0.7, 17, 24)')
        cursor.execute('INSERT INTO thickness VALUES (0.7, 17.5, 25)')

    cursor.execute('''
    create table IF NOT EXISTS machine (
    num serial NOT NULL check (num > 0),
    count integer NOT NULL check (count > 0),
    PRIMARY KEY (num));
    ''')

    cursor.execute('SELECT count(*) FROM machine')

    if cursor.fetchall()[0][0] == 0:
        cursor.execute('INSERT INTO machine VALUES (1, 16)')
        cursor.execute('INSERT INTO machine VALUES (2, 25)')
        cursor.execute('INSERT INTO machine VALUES (3, 13)')

    cursor.execute('''
    create table IF NOT EXISTS cutting_time (
    class text NOT NULL check (class in ('standart', 'econom')),
    type_reel integer NOT NULL check (type_reel in (70, 100, 150, 166)),
    time real check (time > 0),
    PRIMARY KEY (class, type_reel));
    ''')

    cursor.execute('SELECT count(*) FROM cutting_time')

    if cursor.fetchall()[0][0] == 0:
        cursor.execute('INSERT INTO cutting_time VALUES ("econom", 70, 13.2)')
        cursor.execute('INSERT INTO cutting_time VALUES ("econom", 100, 12)')
        cursor.execute('INSERT INTO cutting_time VALUES ("econom", 150, 7.5)')
        cursor.execute('INSERT INTO cutting_time VALUES ("econom", 166, 7.9)')
        cursor.execute('INSERT INTO cutting_time VALUES ("standart", 70, 14.6)')
        cursor.execute('INSERT INTO cutting_time VALUES ("standart", 100, 10.5)')
        cursor.execute('INSERT INTO cutting_time VALUES ("standart", 150, 1)')
        cursor.execute('INSERT INTO cutting_time VALUES ("standart", 166, 1)')

    cursor.execute('''
    create table IF NOT EXISTS retooling (
    type_reel integer NOT NULL check (type_reel in (70, 100, 150, 166)),
    time real check (time > 0),
    PRIMARY KEY (type_reel));
    ''')

    cursor.execute('SELECT count(*) FROM retooling')

    if cursor.fetchall()[0][0] == 0:
        cursor.execute('INSERT INTO retooling VALUES (70, 8)')
        cursor.execute('INSERT INTO retooling VALUES (100, 6.1)')
        cursor.execute('INSERT INTO retooling VALUES (150, 4.5)')
        cursor.execute('INSERT INTO retooling VALUES (166, 4.5)')

    cursor.execute('''
    create table IF NOT EXISTS width (
    class_new text NOT NULL,
    class text NOT NULL check (class in ("standart", "econom")),
    width_1050 int NOT NULL check (width_1050 in (0, 1)),
    width_840 int NOT NULL check (width_840 in (0, 1)));
    ''')

    cursor.execute('SELECT count(*) FROM width')

    if cursor.fetchall()[0][0] == 0:
        cursor.execute('INSERT INTO width VALUES ("Стандарт", "standart", 1, 1)')
        cursor.execute('INSERT INTO width VALUES ("Эконом", "econom", 1, 1)')


    connection.commit()
    connection.close()

def roller(quality):
    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.execute(f'SELECT width_1050, width_840 FROM width WHERE class_new = "{quality}"')
    width = cursor.fetchall()[0]
    if width[0] and width[1]:
        width = 0
    elif width[0]:
        width = 1050
    else:
        width = 840

    connection.commit()
    connection.close()

    return width

def count_reel(width, spool_width):
    connection = sqlite3.connect(path)
    cursor = connection.cursor()

    cursor.execute(f"SELECT count_70, count_100, count_150, count_166 FROM cutting WHERE type_roller = {width} AND type_reel = {spool_width}")
    count_reel = cursor.fetchall()[0]

    connection.commit()
    connection.close()

    return count_reel

def time_cut(spool, width_then):
    cutting_time = 0

    connection = sqlite3.connect(path)
    cursor = connection.cursor()

    cursor.execute(f"SELECT class FROM width WHERE class_new = '{spool.cardboard.quality}'")
    quality = cursor.fetchall()[0][0]

    cursor.execute(f"SELECT time FROM cutting_time WHERE class = '{quality}' AND type_reel = {spool.cardboard.width};")
    cutting_time += cursor.fetchall()[0][0]

    if width_then != spool.cardboard.width:
        cursor.execute(f'SELECT time FROM retooling WHERE type_reel = {spool.cardboard.width}')
        cutting_time += cursor.fetchall()[0][0]

    connection.commit()
    connection.close()

    return cutting_time

def time_wind(spool):
    connection = sqlite3.connect(path)
    cursor = connection.cursor()

    cursor.execute(f"SELECT class FROM width WHERE class_new = '{spool.cardboard.quality}'")
    quality = cursor.fetchall()[0][0]

    cursor.execute(f'SELECT time FROM winding WHERE class = "{quality}" AND type_reel = {spool.cardboard.width} AND thickness >= {spool.thickness}')
    winding_time = cursor.fetchall()[0][0]

    connection.commit()
    connection.close()

    return winding_time

def capacity(index):
    connection = sqlite3.connect(path)
    cursor = connection.cursor()

    cursor.execute(f'SELECT count FROM machine WHERE num = {index};')
    capacity = cursor.fetchall()[0][0]

    connection.commit()
    connection.close()

    return capacity

def count_card(spool):
    connection = sqlite3.connect(path)
    cursor = connection.cursor()

    cursor.execute(f'SELECT count FROM thickness WHERE card = 0.6 AND thickness = {float(spool[1].replace(',', '.'))}')
    count = cursor.fetchall()[0][0]

    connection.commit()
    connection.close()

    return count
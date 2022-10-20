import sqlite3


def main():
    selection = input(
        'SI DESEA INSERTAR UN ALUMNO PULSE 1 \nSI DESEA BUSCAR UN ALUMNO PULSE 2\nSI DESEA MOSTRAR TODOS LOS ALUMNOS PULSE 3\n')
    connection = dbConnect()

    match selection:
        case '1':
            createAlumno(connection)
        case '2':
            readAlumno(connection)
        case '3':
            readAlumnos(connection)
        case _:
            main()

    dbDisconnect(connection)


def dbConnect():
    pathSplit = __file__.split('\\')
    pathSplit.pop()
    path = '\\'.join(pathSplit)
    return sqlite3.connect(path+'\database.db')


def dbDisconnect(conexion):
    conexion.close()


def isNumber(value):
    try:
        return value == int(value) | value == float(value)
    except ValueError:
        return False


def insertQuery(dbName, dataObj):
    keys = ''
    values = ''

    for key in dataObj.keys():
        keys += f'{key}, '

    for value in dataObj.values():
        if isNumber(value):
            values += f"{value}, "
        else:
            values += f"'{value}', "

    dbNameKeys = keys[:-2]
    dbNameValues = values[:-2]
    return f"INSERT INTO {dbName}({dbNameKeys}) VALUES({dbNameValues})"


def readQuery(dbName, param, value):
    return f"SELECT * FROM {dbName} WHERE {param}='{value}'"


def readAllQuery(dbName):
    return f"SELECT * FROM {dbName}"


def createAlumno(conn):
    nombre = input('Ingrese el nombre: ')
    apellidos = input('Ingrese los apellidos: ')
    dataObj = {'nombre': nombre, 'apellidos': apellidos}

    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS alumnos (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT NOT NULL, apellidos TEXT NOT NULL)")
    conn.commit()

    insertQueryStr = insertQuery('alumnos', dataObj)
    cursor.execute(insertQueryStr)
    conn.commit()

    cursor.execute("SELECT LAST_INSERT_ROWID()")
    id = cursor.fetchone()[0]

    print(f'Tu id de usuario es {id}')
    print('')
    cursor.close()


def readAlumno(conn):
    searchName = input('Indica el nombre del usuario que buscas: ')
    cursor = conn.cursor()
    readQueryStr = readQuery('alumnos', 'nombre', searchName)
    cursor.execute(readQueryStr)
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    cursor.close()


def readAlumnos(conn):
    cursor = conn.cursor()
    readAllQueryStr = readAllQuery('alumnos')
    cursor.execute(readAllQueryStr)
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    cursor.close()


if __name__ == '__main__':
    main()

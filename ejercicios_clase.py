#!/usr/bin/env python
'''
SQL Introducción [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import json

import tinymongo as tm
import tinydb

# Bug: https://github.com/schapman1974/tinymongo/issues/58
class TinyMongoClient(tm.TinyMongoClient):
    @property
    def _storage(self):
        return tinydb.storages.JSONStorage

db_name = 'secundaria'


def clear():
    conn = TinyMongoClient()
    db = conn[db_name]

    # Eliminar todos los documentos que existan en la coleccion estudiante
    db.estudiante.remove({})

    # Cerrar la conexión con la base de datos
    conn.close()


def fill():
    print('Completemos esta tablita!')
    # Llenar la coleccion "estudiante" con al menos 5 estudiantes
    # Cada estudiante tiene los posibles campos:
    # id --> este campo es auto completado por mongo
    # name --> El nombre del estudiante (puede ser solo nombre sin apellido)
    # age --> cuantos años tiene el estudiante
    # grade --> en que año de la secundaria se encuentra (1-6)
    # tutor --> nombre de su tutor

    # Se debe utilizar la sentencia insert_one o insert_many.

    conn = TinyMongoClient()
    db = conn[db_name]

    students = [{"name": "Luciana", "age": 17, "grade": 4, "tutor": "Mariela"},
                {"name": "Joaquin", "age": 16, "grade": 3, "tutor": "Mariela"},
                {"name": "Martina", "age": 17, "grade": 4, "tutor": "Candela"},
                {"name": "Carolina", "age": 17, "grade": 4, "tutor": "Candela"},
                {"name": "Jose", "age": 15, "grade": 3, "tutor": "Mariela"},
                {"name": "Ricardo", "age": 16, "grade": 3, "tutor": "Candela"},
                {"name": "Santiago", "age": 17, "grade": 4, "tutor": "Mariela"},
                {"name": "Paola", "age": 16, "grade": 3, "tutor": "Candela"},
                {"name": "Mauro", "age": 15, "grade": 3, "tutor": "Candela"},
                {"name": "Miguel", "age": 13, "grade": 2, "tutor": "Mariela"}]
    
    db.secundaria.insert_many(students)
    conn.close()


def show():
    print('Comprovemos su contenido, ¿qué hay en la tabla?')
    # Utilizar la sentencia find para imprimir en pantalla
    # todos los documentos de la DB
    # Queda a su criterio serializar o no el JSON "dumps"
    #  para imprimirlo en un formato más "agradable"

    conn = TinyMongoClient()
    db = conn[db_name]

    cursor = db.secundaria.find()
    data = list(cursor)
    json_data = json.dumps(data, indent=4)
    print(json_data)

    conn.close()
    
    
def find_by_grade(grade):    # grade 3
    print('Operación búsqueda!')
    # Utilizar la sentencia find para imprimir en pantalla
    # aquellos estudiantes que se encuentra en en año "grade"

    conn = TinyMongoClient()
    db = conn[db_name]

    cursor = db.secundaria.find({"grade": 3})
    data = list(cursor)
    json_data = json.dumps(data, indent=4)
    print(json_data)

    # De la lista de esos estudiantes debe imprimir
    # en pantalla unicamente los siguiente campos por cada uno:
    # id / name / age

    for dato in cursor:
        print('id: {}, name: {}, age: {}'.format(dato["_id"], dato["name"], dato["age"]))

    conn.close()


def insert(student):
    print('Nuevos ingresos!')
    # Utilizar la sentencia insert_one para ingresar nuevos estudiantes
    # a la secundaria

    # El parámetro student deberá ser un JSON el cual se inserta en la db

    conn = TinyMongoClient()
    db = conn[db_name]
    
    # insertar nuevo estudiante
    db.secundaria.insert_one(student)
    
    # Imprimir la base de datos actualizada
    cursor = db.secundaria.find()
    data = list(cursor)
    json_data = json.dumps(data, indent=4)
    print(json_data)
    
    conn.close()


def count(grade):
    print('Contar estudiantes')
    # Utilizar la sentencia find + count para contar
    # cuantos estudiantes pertenecen el grado "grade"

    conn = TinyMongoClient()
    db = conn[db_name]

    filtro_grado = db.secundaria.find({"grade": grade})
    for dato in filtro_grado:
        print(dato)
    
    count = db.secundaria.find({"grade": grade}).count()
    print('La cantidad de estudiantes en', grade, 'grado son', count)
    
    conn.close()


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    # Borrar la db
    # clear()

    # fill()
    # show()

    grade = 3
    # find_by_grade(grade)

    student = {"name": "Mariano", "age": 18, "grade": 6, "tutor": "Mariela"}
    # insert(student)

    count(grade)

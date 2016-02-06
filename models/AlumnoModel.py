# -*- coding: UTF-8 -*-

from SqliteModel import SqliteClass

class Alumno():

	def __init__(self):
	    self.db = SqliteClass()
	    self.db.EjecutarConsulta("CREATE TABLE IF NOT EXISTS alumnos(\
                            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
                            nombre TEXT NOT NULL,\
                            apellido TEXT NOT NULL,\
                            dni INT NOT NULL, \
														turnos TEXT NOT NULL)")

#	def GetName(self, id):
#		nombre = self.db.Consulta("SELECT nombre FROM alumnos WHERE id = " + id)
#		return nombre[0]
#
#	def SetName(self, id, nombre):
#		self.db.EjecutarConsulta("UPDATE alumnos SET nombre = '" + nombre + "' WHERE id = " + id)

	def AddAlumno(self, nombre, apellido, dni):
		self.db.EjecutarConsulta("INSERT INTO alumnos (nombre, apellido, dni) VALUES ('" + nombre + "', '" + apellido + "', " + dni +")")
		
	def DelAlumno(self, id):
		self.db.EjecutarConsulta("DELETE FROM alumnos WHERE id = " + id)
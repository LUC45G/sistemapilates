# -*- coding: UTF-8 -*-

from .SqliteModel import SqliteClass

class AlumnoClass():

	def __init__(self):
	    self.db = SqliteClass()
	    self.db.EjecutarConsulta("CREATE TABLE IF NOT EXISTS alumnos(\
                            id INT PRIMARY KEY NOT NULL,\
                            nombre TEXT NOT NULL,\
                            apellido TEXT NOT NULL,\
                            dni INT NOT NULL, \
                            turnos TEXT NOT NULL)")

	def GetName(self, id):
		nombre = self.db.Consulta("SELECT nombre FROM alumnos WHERE id = " + id)
		return nombre[0]

	def SetName(self, id, nombre):
		self.db.EjecutarConsulta("UPDATE alumnos SET nombre = '" + nombre + "' WHERE id = " + id)
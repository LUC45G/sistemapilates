# -*- coding: UTF-8 -*-

from SqliteModel import SqliteClass

class Profesor():
  
  def __init__(self):
      self.db = SqliteClass()
      self.db.EjecutarConsulta("CREATE TABLE IF NOT EXISTS profesores(\
                                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
                                nombre TEXT NOT NULL, \
                                apellido TEXT NOT NULL, \
                                dni INT NOT NULL, \
                                turnos TEXT NOT NULL)")
      
#  def GetName(self, id):
#    nombre = self.db.Consulta("SELECT nombre FROM profesores WHERE id = " + id )
#    return nombre[0]
#  
#  def SetName(self, id, nombre):
#    self.db.EjecutarConsulta("UPDATE profesores SET nombre = '" + nombre + "' WHERE id = " + id)
    
  def AddProfesor(self, nombre, apellido, dni):
    self.db.EjecutarConsulta("INSERT INTO profesores (nombre, apellido, dni) VALUES ('" + nombre + "', '" + apellido + "', " + dni + ")")
    
  def DelProfesor(self, id):
    self.db.EjecutarConsulta("DELETE FROM profesores WHERE id = " + id)
    
  
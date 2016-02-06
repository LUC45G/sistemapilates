# -*- coding: UTF-8 -*-

import sqlite3
from config import db

class SqliteClass():
  def __init__(self):
    self.con = sqlite3.connect(db)
    self.cursor = self.con.cursor()
    
  def EjecutarConsulta(self, sql):
    self.cursor.execute(sql)
    self.con.commit()
    
  def Consulta(self, sql):
    self.cursor.execute(sql)
    return self.cursor
  
  def Cerrar(self):
    self.con.close()
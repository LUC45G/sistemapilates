from models.SqliteModel import SqliteClass

class MainController():
  
  def __init__(self):
    self.db = SqliteClass()
    self.db.EjecutarConsulta("CREATE TABLE IF NOT EXISTS alumnos(\
                            id INT PRIMARY KEY NOT NULL,\
                            nombre TEXT NOT NULL)")
    self.db.Cerrar()
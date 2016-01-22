# -*- coding: UTF-8 -*-

import sys
from models.SqliteModel import SqliteClass
from models.AlumnoModel import AlumnoClass
from views.Views import ViewsClass
from PyQt5.QtWidgets import QApplication

class MainController():
  
	def __init__(self):
		self.db = SqliteClass()
		self.alumno = AlumnoClass()
		self.run()

	def run(self):
		self.app = QApplication(sys.argv)
		self.window = ViewsClass()
		sys.exit(self.app.exec_())
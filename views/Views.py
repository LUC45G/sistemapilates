# -*- coding:UTF-8 -*-

import sys
from PyQt5.QtWidgets import QWidget

class ViewsClass(QWidget):

	def __init__(self):
		super().__init__()

		self.InitUI()

	def InitUI(self):
		#Tamaños de la ventana
		self.resize(500, 300)
		self.move(300, 250)

		#Titulo
		self.setWindowTitle('Sistema Pilates')

		
		
		self.show()
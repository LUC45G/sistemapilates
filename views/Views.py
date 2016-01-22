# -*- coding:UTF-8 -*-

import sys
from PyQt5.QtWidgets import QWidget

class ViewsClass(QWidget):

	def __init__(self):
		super().__init__()

		self.InitUI()

	def InitUI(self):
		self.resize(500, 300)
		self.move(300, 250)
		self.setWindowTitle('Sistema Pilates')
		self.show()
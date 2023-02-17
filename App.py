from PyQt5.uic import loadUi
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys, sqlite3, random


class Main(QMainWindow):
	def __init__(self):
		super(Main, self).__init__()
		loadUi("Static/ui/UI.ui", self)

		item_text_list = [ 'item1' , 'item2' , 'item3' ]

		for item_text in item_text_list:
		    item = QListWidgetItem(item_text)
		    item.setTextAlignment(Qt.AlignHCenter)
		    self.listWidget.addItem(item)
		    self.listWidget_2.addItem(item)

		self.pushButton_2.clicked.connect(self.teacher)
		self.pushButton.clicked.connect(self.student)
		self.pushButton_12.clicked.connect(self.already_signedin)
		self.pushButton_11.clicked.connect(self.already_signedup)
		self.pushButton_3.clicked.connect(self.signup_check)
		self.pushButton_10.clicked.connect(self.signin_check)
		self.pushButton_13.clicked.connect(self.add_question)
		self.pushButton_5.clicked.connect(self.back_to_teacher)
		self.pushButton_4.clicked.connect(self.save_question)
		self.pushButton_17.clicked.connect(self.back_to_home)
		self.pushButton_16.clicked.connect(self.back_to_home)

	def teacher(self):
		self.stackedWidget.setCurrentIndex(2)
		global teacher
		global student
		student = 0
		teacher = 1

	def student(self):
		self.stackedWidget.setCurrentIndex(2)
		global student
		global teacher
		teacher = 0
		student = 1

	def already_signedup(self):
		self.stackedWidget.setCurrentIndex(1)

	def already_signedin(self):
		self.stackedWidget.setCurrentIndex(2)

	def signin_check(self):
		pass

	def signup_check(self):
		Username = self.lineEdit.text()
		Password = self.lineEdit_2.text()
		Status = ""
		if (teacher == 1): Status = "teacher"
		elif (student == 1): Status = "student"

		if (Username != "" and Password != ""):
			connection = sqlite3.connect("Database/Data.db")
			cursor = connection.cursor()
			cursor.execute('''CREATE TABLE IF NOT EXISTS User(Username text, Password int, Status text)''')
			cursor.execute("INSERT INTO User VALUES(?, ?, ?)", (Username, Password, Status))
			connection.commit()
			connection.close()

			if (Status == "teacher"):
				self.stackedWidget.setCurrentIndex(3)

			if (Status == "student"):
				self.stackedWidget.setCurrentIndex(4)
		else:
			self.label_5.setText("لطفا همه موارد را پر کنید")

	def add_question(self):
		self.stackedWidget.setCurrentIndex(5)

	def back_to_teacher(self):
		self.stackedWidget.setCurrentIndex(3)

	def save_question(self):
		Question = self.lineEdit_4.text()
		Answer = self.lineEdit_3.text()

		if (Question != "" and Answer != ""):
			connection = sqlite3.connect("Database/Questions.db")
			cursor = connection.cursor()
			cursor.execute('''CREATE TABLE IF NOT EXISTS Questions(Question text, Answer text)''')
			cursor.execute("INSERT INTO Questions VALUES(?, ?)", (Question, Answer))
			connection.commit()
			connection.close()
			self.stackedWidget.setCurrentIndex(3)
		else:
			self.label_4.setText("لطفا همه موارد را پر کنید")

	def back_to_home(self):
		self.stackedWidget.setCurrentIndex(0)

main = QApplication(sys.argv)
app = Main()
app.show()
main.exec_()
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

virsh = """Ох,якби те сталось,щоб ви не вертались,Щоб там і здихали,де ви поросли! Не плакали б діти,мати б не ридала,Не чули б у Бога вашої хули.І сонце не гріло б смердячого гною На чистій,широкій,на вольній землі.І люди б не знали,що ви за орли,І не покивали б на вас головою.Схаменіться! будьте люди,Бо лихо вам буде.Розкуються незабаром Заковані люде,Настане суд заговорять.І Дніпро,і гори! І потече сторіками Кров у синє море Дітей ваших і не буде Кому помагати.Одцурається брат брата І дитини мати.І дим хмарою заступить Сонце перед вами,І навіки прокленетесь Своїми синами! Умийтеся! образ Божий Багном не скверніте.Не дуріте дітей ваших,Що вони на світі На те тілько,щоб панувать Бо невчене око Загляне їм в саму душу Глибоко! глибоко! Дознаються небожата,Чия на вас шкура,Та й засядуть,і премудрих Немудрі одурять!"""




class MainGui(QMainWindow):
	def __init__ (self):
		super(MainGui, self).__init__()
		self.passed = True
		self.resize(640,480)
		self.setStyleSheet("background-color:rgb(16,16,14);color:#fff;font-size:50px;")
		self.m = 0
		newest = (virsh.replace(".", "*"))
		
		# newest = (virsh.replace("\n", "*")) # if you have many \n
		
		newest = newest.replace(",", "*")
		newest = newest.replace(" ", "*")
		self.g = newest.split("*")
		self.label = QtWidgets.QLabel(self)
		self.label.setGeometry(0,220,600,50)
		self.label.setText(self.g[self.m])


	def keyPressEvent(self, e):
		if self.passed:
			if e.key() == 45:
				if self.m + 1 != len(self.g):
					self.m += 1
				else:
					self.label.setText("")
					self.passed = False
					return
				if len(self.g[self.m]) >= 3:
					self.label.setText(self.g[self.m])
				else:
					self.label.setText(self.g[self.m] + " " + self.g[self.m+1])
					self.m += 1
				return
		
		if e.key() == 16777216:
			self.close()




def main():
	app = QApplication(sys.argv)
	window = MainGui()
	window.show()
	sys.exit(app.exec())

if __name__ == "__main__":
	main()

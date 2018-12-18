from PySide import QtCore, QtGui, QtUiTools
from calculator import Ui_Calculator
from functools import partial
import sys


class GUI(Ui_Calculator, QtGui.QWidget):

	def __init__(self):
		super(GUI, self).__init__()
		self.setupUi(self)
		for _v in self.children()[0].children():
			if 'val_' in _v.objectName():
				eval("self.%s.clicked.connect(partial(self.Calop, _v))"%_v.objectName())

	def Calop(self, _v):
		_opKey = {
			"add": "+",
			"sub": "-",
			"mul": "*",
			"div": "/",
			"tot": "",
			"dot": "."
		}
		_txt, _newval = self.op_box.toPlainText(), _v.objectName().split('val_')[1]
		_op_txt = "%s%s"%(_txt, _opKey[_newval] if _newval in _opKey.keys() else _newval)
		if _op_txt[-1].isdigit():
			self.op_box.setPlainText("%s"%eval(_op_txt))
		else:
			self.op_box.setPlainText("%s"%_op_txt)

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	a=GUI()
	a.show()
	sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'template2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(865, 455)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(140, 110, 281, 161))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(7)
        self.formLayout.setObjectName("formLayout")
        self.pdsPerYrLabel = QtWidgets.QLabel(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pdsPerYrLabel.sizePolicy().hasHeightForWidth())
        self.pdsPerYrLabel.setSizePolicy(sizePolicy)
        self.pdsPerYrLabel.setMinimumSize(QtCore.QSize(110, 0))
        self.pdsPerYrLabel.setBaseSize(QtCore.QSize(112, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pdsPerYrLabel.setFont(font)
        self.pdsPerYrLabel.setStyleSheet("font: 13pt \"MS Shell Dlg 2\";")
        self.pdsPerYrLabel.setTextFormat(QtCore.Qt.AutoText)
        self.pdsPerYrLabel.setScaledContents(False)
        self.pdsPerYrLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pdsPerYrLabel.setIndent(0)
        self.pdsPerYrLabel.setObjectName("pdsPerYrLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.pdsPerYrLabel)
        self.pdsPerYrInp = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.pdsPerYrInp.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pdsPerYrInp.setPrefix("")
        self.pdsPerYrInp.setSuffix("")
        self.pdsPerYrInp.setMaximum(100000000.0)
        self.pdsPerYrInp.setSingleStep(10.0)
        self.pdsPerYrInp.setObjectName("pdsPerYrInp")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pdsPerYrInp)
        self.startAmountLabel = QtWidgets.QLabel(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startAmountLabel.sizePolicy().hasHeightForWidth())
        self.startAmountLabel.setSizePolicy(sizePolicy)
        self.startAmountLabel.setMinimumSize(QtCore.QSize(110, 0))
        self.startAmountLabel.setBaseSize(QtCore.QSize(112, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.startAmountLabel.setFont(font)
        self.startAmountLabel.setStyleSheet("font: 13pt \"MS Shell Dlg 2\";")
        self.startAmountLabel.setTextFormat(QtCore.Qt.AutoText)
        self.startAmountLabel.setScaledContents(False)
        self.startAmountLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.startAmountLabel.setIndent(0)
        self.startAmountLabel.setObjectName("startAmountLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.startAmountLabel)
        self.fundPctLabel = QtWidgets.QLabel(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fundPctLabel.sizePolicy().hasHeightForWidth())
        self.fundPctLabel.setSizePolicy(sizePolicy)
        self.fundPctLabel.setMinimumSize(QtCore.QSize(110, 0))
        self.fundPctLabel.setBaseSize(QtCore.QSize(112, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.fundPctLabel.setFont(font)
        self.fundPctLabel.setStyleSheet("font: 13pt \"MS Shell Dlg 2\";")
        self.fundPctLabel.setTextFormat(QtCore.Qt.AutoText)
        self.fundPctLabel.setScaledContents(False)
        self.fundPctLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.fundPctLabel.setIndent(0)
        self.fundPctLabel.setObjectName("fundPctLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.fundPctLabel)
        self.fundPctInp = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.fundPctInp.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.fundPctInp.setObjectName("fundPctInp")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.fundPctInp)
        self.funcChrgLabel = QtWidgets.QLabel(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.funcChrgLabel.sizePolicy().hasHeightForWidth())
        self.funcChrgLabel.setSizePolicy(sizePolicy)
        self.funcChrgLabel.setMinimumSize(QtCore.QSize(110, 0))
        self.funcChrgLabel.setBaseSize(QtCore.QSize(112, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.funcChrgLabel.setFont(font)
        self.funcChrgLabel.setStyleSheet("font: 13pt \"MS Shell Dlg 2\";")
        self.funcChrgLabel.setTextFormat(QtCore.Qt.AutoText)
        self.funcChrgLabel.setScaledContents(False)
        self.funcChrgLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.funcChrgLabel.setIndent(0)
        self.funcChrgLabel.setObjectName("funcChrgLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.funcChrgLabel)
        self.fundChrgInp = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.fundChrgInp.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.fundChrgInp.setObjectName("fundChrgInp")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.fundChrgInp)
        self.yrsInvestingLabel = QtWidgets.QLabel(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yrsInvestingLabel.sizePolicy().hasHeightForWidth())
        self.yrsInvestingLabel.setSizePolicy(sizePolicy)
        self.yrsInvestingLabel.setMinimumSize(QtCore.QSize(110, 0))
        self.yrsInvestingLabel.setBaseSize(QtCore.QSize(112, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.yrsInvestingLabel.setFont(font)
        self.yrsInvestingLabel.setStyleSheet("font: 13pt \"MS Shell Dlg 2\";")
        self.yrsInvestingLabel.setTextFormat(QtCore.Qt.AutoText)
        self.yrsInvestingLabel.setScaledContents(False)
        self.yrsInvestingLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.yrsInvestingLabel.setIndent(0)
        self.yrsInvestingLabel.setObjectName("yrsInvestingLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.yrsInvestingLabel)
        self.yrsInvestingInp = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.yrsInvestingInp.setObjectName("yrsInvestingInp")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.yrsInvestingInp)
        self.startAmountInp = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.startAmountInp.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.startAmountInp.setPrefix("")
        self.startAmountInp.setSuffix("")
        self.startAmountInp.setMaximum(100000000.0)
        self.startAmountInp.setSingleStep(10.0)
        self.startAmountInp.setObjectName("startAmountInp")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.startAmountInp)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(445, 110, 241, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.calcButton = QtWidgets.QPushButton(self.centralwidget)
        self.calcButton.setGeometry(QtCore.QRect(220, 280, 101, 31))
        self.calcButton.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.calcButton.setObjectName("calcButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 865, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pdsPerYrInp, self.startAmountInp)
        MainWindow.setTabOrder(self.startAmountInp, self.fundPctInp)
        MainWindow.setTabOrder(self.fundPctInp, self.fundChrgInp)
        MainWindow.setTabOrder(self.fundChrgInp, self.yrsInvestingInp)
        MainWindow.setTabOrder(self.yrsInvestingInp, self.calcButton)
        MainWindow.setTabOrder(self.calcButton, self.textBrowser)

        # My added stuff
        self.calcButton.clicked.connect(self.buttonClick)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Wills Investment Calculator"))
        self.pdsPerYrLabel.setText(_translate("MainWindow", "Yearly Pay in £"))
        self.startAmountLabel.setText(_translate("MainWindow", "Start Amount £"))
        self.fundPctLabel.setText(_translate("MainWindow", "Fund % per year"))
        self.funcChrgLabel.setText(_translate("MainWindow", "Fund % charge"))
        self.yrsInvestingLabel.setText(_translate("MainWindow", "Years investing"))
        self.calcButton.setText(_translate("MainWindow", "Calculate"))

    def setOutput(self, text):
        self.textBrowser.append(str(text))

    def buttonClick(self):
        self.calculate()

    def calculate(self):
        self.textBrowser.clear()

        # Get inputs
        pdsPerYr = self.pdsPerYrInp.value()
        yrsInvesting = self.yrsInvestingInp.value()
        fundPct = self.fundPctInp.value()
        fundChrg = self.fundChrgInp.value()
        startAmount = self.startAmountInp.value()

        pctPerYear = fundPct - fundChrg
        total = startAmount

        # finds the multipler to times the total by 
        pctMultiplier = float('1.0' + (str(pctPerYear)).replace('.',''))

        for i in range(1, yrsInvesting + 1):
            total = pdsPerYr + (total * (pctMultiplier))
            self.setOutput(f'Year{i} £' + str(round(total, 2)))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

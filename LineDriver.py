# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LineDriver.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import xml.etree.ElementTree as ET

class Ui_Dialog(object):

    def __init__(self, TDC_inst):
        self.TDC_inst = TDC_inst
        # self.CSM_inst = CSM_inst

    def setupUi(self, Dialog):

        tree_ePortTX = ET.parse('LpGBT_transfer.xml')
        root = tree_ePortTX.getroot()

        Dialog.setObjectName("Dialog")
        Dialog.resize(420, 620)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 131, 31))
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 40, 381, 161))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 1, 2, 1, 1)

        #Modulation current
        self.horizontalSlider = QtWidgets.QSlider(self.gridLayoutWidget)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setRange(0, 877)
        self.horizontalSlider.setTickInterval(1)
        self.horizontalSlider.valueChanged.connect(self.updateLabel)
        self.gridLayout.addWidget(self.horizontalSlider, 0, 2, 1, 1)

        self.label_slide = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_slide.setText('0.00')
        self.gridLayout.addWidget(self.label_slide, 0, 3, 1, 1)

        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        #PE pulse
        self.horizontalSlider_2 = QtWidgets.QSlider(self.gridLayoutWidget)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalSlider_2.setRange(0, 877)
        self.horizontalSlider_2.setTickInterval(1)
        self.horizontalSlider_2.valueChanged.connect(self.updateLabel_2)
        self.gridLayout.addWidget(self.horizontalSlider_2, 2, 2, 1, 1)

        self.label_slide_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_slide_2.setText('0.00')
        self.gridLayout.addWidget(self.label_slide_2, 2, 3, 1, 1)

        #PE Current
        self.horizontalSlider_3 = QtWidgets.QSlider(self.gridLayoutWidget)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.horizontalSlider_3.setRange(0, 877)
        self.horizontalSlider_3.setTickInterval(1)
        self.horizontalSlider_3.valueChanged.connect(self.updateLabel_3)
        self.gridLayout.addWidget(self.horizontalSlider_3, 3, 2, 1, 1)

        self.label_slide_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_slide_3.setText('0.00')
        self.gridLayout.addWidget(self.label_slide_3, 3, 3, 1, 1)

        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 240, 161, 31))
        self.label_6.setObjectName("label_6")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(19, 280, 361, 131))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 4, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 3, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_2.addWidget(self.checkBox_2, 1, 1, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_3.setText("")
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_2.addWidget(self.checkBox_3, 2, 1, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_4.setText("")
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_2.addWidget(self.checkBox_4, 3, 1, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_5.setText("")
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout_2.addWidget(self.checkBox_5, 4, 1, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 440, 241, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout.addWidget(self.label_11)
        self.checkBox_6 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_6.setText("")
        self.checkBox_6.setObjectName("checkBox_6")
        self.horizontalLayout.addWidget(self.checkBox_6)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(19, 530, 381, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        #Apply
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self.save)

        #Ok
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_2.clicked.connect(self.save)
        self.pushButton_2.clicked.connect(Dialog.reject)

        #cancel
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_3.clicked.connect(Dialog.reject)

        ############ Inserting xml file loading ###############
        # Modulation Current (unsure)
        self.label_slide.setText(root[7][0][1].text)

        # PE Enable
        if root[7][0][0].text == '0x1':
            self.checkBox.setChecked(True)
        else:
            self.checkBox.setChecked(False)

        # PE Pulse (unsure)
        self.label_slide_2.setText(root[7][0][2].text)

        # PE Current (unsure)
        self.label_slide_3.setText(root[7][0][3].text)

        # TEST CLK common mode gen
        if root[7][1][0].text == '0x1':
            self.checkBox_2.setChecked(True)
        else:
            self.checkBox_2.setChecked(False)

        # Reference clock pad (force enable)
        if root[7][1][1].text == '0x1':
            self.checkBox_3.setChecked(True)
        else:
            self.checkBox_3.setChecked(False)

        # REFCLK common mode gen (AcBias)
        if root[7][1][2].text == '0x1':
            self.checkBox_4.setChecked(True)
        else:
            self.checkBox_4.setChecked(False)

        # RECLK input 100 Ohm terminate
        if root[7][1][3].text == '0x1':
            self.checkBox_5.setChecked(True)
        else:
            self.checkBox_5.setChecked(False)

        # Parity check disable
        if root[7][2].text == '0x1':
            self.checkBox_6.setChecked(True)
        else:
            self.checkBox_6.setChecked(False)

        #######################################################
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #testing
        # self.checkBox_6.setChecked(True)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Line Driver: "))
        self.label_3.setText(_translate("Dialog", "Modulation Current (mA): "))
        self.label_2.setText(_translate("Dialog", "PE Enable:"))
        self.label_5.setText(_translate("Dialog", "PE Current (mA):"))
        self.label_4.setText(_translate("Dialog", "PE Pulse: "))
        self.label_6.setText(_translate("Dialog", "Reference Clock Pad: "))
        self.label_10.setText(_translate("Dialog", "REFCLK input 100 Ohm terminate :"))
        self.label_7.setText(_translate("Dialog", "TESTCLK common mode gen. :"))
        self.label_8.setText(_translate("Dialog", "Reference clock pad :"))
        self.label_9.setText(_translate("Dialog", "REFCLK common mode gen. :"))
        self.label_11.setText(_translate("Dialog", "Parity Check Disable :"))
        self.pushButton.setText(_translate("Dialog", "Apply"))
        self.pushButton_2.setText(_translate("Dialog", "OK"))
        self.pushButton_3.setText(_translate("Dialog", "Cancel"))

    def updateLabel(self, value):
        value_scaled = round(value*0.01, 2)
        value_scaled_what = format(value_scaled, '.2f')
        self.label_slide.setText(str(value_scaled_what))

    def updateLabel_2(self, value_2):
        value_2_scaled = round(value_2*0.01, 2)
        value_2_scaled_what = format(value_2_scaled, '.2f')
        self.label_slide_2.setText(str(value_2_scaled_what))

    def updateLabel_3(self, value_3):
        value_3_scaled = round(value_3*0.01, 2)
        value_3_scaled_what = format(value_3_scaled, '.2f')
        self.label_slide_3.setText(str(value_3_scaled_what))

    def save(self):
        print('in progress')
        import xml.etree.ElementTree as ET
        # tree_ePortTX = ET.parse('LpGBT_auto_saved.xml')
        tree_ePortTX = ET.parse('LpGBT_transfer.xml')
        root = tree_ePortTX.getroot()

        #Modulation Current (unsure)
        root[7][0][1].text = self.label_slide.text()

        #PE Enable
        #print(root[7][0][0].label)
        if self.checkBox.isChecked() == True:
            root[7][0][0].text = '0x1'
        else:
            root[7][0][0].text = '0x0'

        #PE Pulse (unsure)
        root[7][0][2].text = self.label_slide_2.text()

        #PE Current (unsure)
        root[7][0][3].text = self.label_slide_3.text()

        #TEST CLK common mode gen
        if self.checkBox_2.isChecked() == True:
            root[7][1][0].text = '0x1'
        else:
            root[7][1][0].text = '0x0'

        # Reference clock pad (force enable)
        if self.checkBox_3.isChecked() == True:
            root[7][1][1].text = '0x1'
        else:
            root[7][1][1].text = '0x0'

        # REFCLK common mode gen (AcBias)
        if self.checkBox_4.isChecked() == True:
            root[7][1][2].text = '0x1'
        else:
            root[7][1][2].text = '0x0'

        #RECLK input 100 Ohm terminate
        if self.checkBox_5.isChecked() == True:
            root[7][1][3].text = '0x1'
        else:
            root[7][1][3].text = '0x0'

        # Parity check disable
        if self.checkBox_6.isChecked() == True:
            root[7][2].text = '0x1'
        else:
            root[7][2].text = '0x0'

        tree_ePortTX.write('LpGBT_auto_saved.xml')
        tree_ePortTX.write('LpGBT_transfer.xml')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from xml.dom import minidom

class Ui_Dialog(QWidget):

    def __init__(self, TDC_inst):
        super().__init__()
        self.TDC_inst = TDC_inst
        self.checkbox_list = []
        self.freq_list = []
        self.ds_list = []
        self.PE_s_list = []
        self.PE_m_list = []
        self.PE_w_list = []
        self.add_and_reg = []

    def setupUi(self, Dialog):

        Dialog.resize(1836, 910)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 1800, 870))
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        # define parameters
        self.clocks = 29
        row = 0
        column = 0
        row_freq = 1
        column_two = 1
        EPCLK_label_width = 110
        EPCLK_label_height = 18

        for i in range(self.clocks):
            if column == 16:
                column = 0
                column_two = 1
                row += 7
                row_freq += 7

            self.label = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label.setText("EPCLK %s" % i)
            self.label.setFont(QtGui.QFont("Calbri", 8))
            self.gridLayout.addWidget(self.label, row, column, 1, 1)

            self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label_3.setText("Invert:")
            self.label_3.setFont(QtGui.QFont("Arial", 7))
            self.label_3.setFixedSize(QtCore.QSize(EPCLK_label_width, EPCLK_label_height))
            self.gridLayout.addWidget(self.label_3, row_freq, column, 1, 1)

            self.checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
            # self.checkBox.setObjectName("inv")
            self.gridLayout.addWidget(self.checkBox, row_freq, column_two, 1, 1)
            self.checkbox_list.append(self.checkBox)
            self.checkBox.address = 108 + 2*i
            self.checkBox.toggled.connect(self.return_byte)
            #self.checkBox.toggled.connect(write(address, self.return_byte))        # write the address and the value here!

            self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label_2.setText("Frequency:")
            self.label_2.setFont(QtGui.QFont("Arial", 7))
            self.label_2.setFixedSize(QtCore.QSize(EPCLK_label_width, EPCLK_label_height))
            self.gridLayout.addWidget(self.label_2, row_freq + 1, column, 1, 1)

            self.freq_box = QtWidgets.QComboBox(self.gridLayoutWidget)
            # self.freq_box.setObjectName("freq")
            self.freq_box.addItem("off")
            self.freq_box.addItem("40")
            self.freq_box.addItem("80")
            self.freq_box.addItem("160")
            self.freq_box.addItem("320")
            self.freq_box.addItem("640")
            self.freq_box.addItem("1280")
            self.freq_box.setFont(QtGui.QFont("Arial", 7))
            self.gridLayout.addWidget(self.freq_box, row_freq + 1, column_two, 1, 1)
            self.freq_list.append(self.freq_box)
            self.freq_box.address = 108 + 2*i
            self.freq_box.currentIndexChanged.connect(self.return_byte)

            self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label_4.setText("Drive Strength:")
            self.label_4.setFont(QtGui.QFont("Arial", 7))
            self.label_4.setFixedSize(QtCore.QSize(EPCLK_label_width, EPCLK_label_height))
            self.gridLayout.addWidget(self.label_4, row_freq + 2, column, 1, 1)

            self.drive_strength = QtWidgets.QComboBox(self.gridLayoutWidget)
            # self.drive_strength.setObjectName("ds")
            self.drive_strength.addItem("0")
            self.drive_strength.addItem("1.0")
            self.drive_strength.addItem("1.5")
            self.drive_strength.addItem("2.0")
            self.drive_strength.addItem("2.5")
            self.drive_strength.addItem("3.0")
            self.drive_strength.addItem("3.5")
            self.drive_strength.addItem("4.0")
            self.drive_strength.setFont(QtGui.QFont("Arial", 7))
            self.gridLayout.addWidget(self.drive_strength, row_freq + 2, column_two, 1, 1)
            self.ds_list.append(self.drive_strength)
            self.drive_strength.address = 108 + 2 * i
            self.drive_strength.currentIndexChanged.connect(self.return_byte)

            self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label_5.setText("PE strength:")
            self.label_5.setFont(QtGui.QFont("Arial", 7))
            self.label_5.setFixedSize(QtCore.QSize(EPCLK_label_width, EPCLK_label_height))
            self.gridLayout.addWidget(self.label_5, row_freq + 3, column, 1, 1)

            self.PE_strength = QtWidgets.QComboBox(self.gridLayoutWidget)
            self.PE_strength.addItem("0")
            self.PE_strength.addItem("1.0")
            self.PE_strength.addItem("1.5")
            self.PE_strength.addItem("2.0")
            self.PE_strength.addItem("2.5")
            self.PE_strength.addItem("3.0")
            self.PE_strength.addItem("3.5")
            self.PE_strength.addItem("4.0")
            self.PE_strength.setFont(QtGui.QFont("Arial", 7))
            self.gridLayout.addWidget(self.PE_strength, row_freq + 3, column_two, 1, 1)
            self.PE_s_list.append(self.PE_strength)
            self.PE_strength.address = 109 + 2*i
            self.PE_strength.currentIndexChanged.connect(self.return_byte_2)

            self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label_6.setText("PE Mode:")
            self.label_6.setFont(QtGui.QFont("Arial", 7))
            self.label_6.setFixedSize(QtCore.QSize(EPCLK_label_width, EPCLK_label_height))
            self.gridLayout.addWidget(self.label_6, row_freq + 4, column, 1, 1)

            self.PE_mode = QtWidgets.QComboBox(self.gridLayoutWidget)
            self.PE_mode.addItem("disabled")
            self.PE_mode.addItem("disabled")
            self.PE_mode.addItem("self timed")
            self.PE_mode.addItem("clock timed")
            self.PE_mode.setFont(QtGui.QFont("Arial", 7))
            self.gridLayout.addWidget(self.PE_mode, row_freq + 4, column_two, 1, 1)
            self.PE_m_list.append(self.PE_mode)
            self.PE_mode.address = 109 + 2*i
            self.PE_mode.currentIndexChanged.connect(self.return_byte_2)

            self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label_7.setText("PE Width:")
            self.label_7.setFont(QtGui.QFont("Arial", 7))
            self.label_7.setFixedSize(QtCore.QSize(EPCLK_label_width, EPCLK_label_height))
            self.gridLayout.addWidget(self.label_7, row_freq + 5, column, 1, 1)

            self.PE_width = QtWidgets.QComboBox(self.gridLayoutWidget)
            self.PE_width.addItem("120")
            self.PE_width.addItem("240")
            self.PE_width.addItem("360")
            self.PE_width.addItem("480")
            self.PE_width.addItem("600")
            self.PE_width.addItem("720")
            self.PE_width.addItem("840")
            self.PE_width.addItem("960")
            self.PE_width.setFont(QtGui.QFont("Arial", 7))
            self.gridLayout.addWidget(self.PE_width, row_freq + 5, column_two, 1, 1)
            self.PE_w_list.append(self.PE_width)
            self.PE_width.currentIndexChanged.connect(self.return_byte_2)
            self.PE_width.address = 109 + 2*i

            column += 2
            column_two += 2

        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(1180, 700, 600, 160))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setText("Apply")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_3.clicked.connect(self.save)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setText("OK")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_2.clicked.connect(self.save)
        self.pushButton_2.clicked.connect(Dialog.reject)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setText("Cancel")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton.clicked.connect(Dialog.reject)

###################################################################################################################
    # for individual changes!

    def return_byte(self):       #This works for all the inv, ds, freq registers
        sender = self.sender()
        address = sender.address
        for inv, ds, freq in zip(self.checkbox_list, self.ds_list, self.freq_list):
            if sender in (inv, ds, freq):
                # get invert binary
                if inv.isChecked():
                    inv_bin = 1
                else:
                    inv_bin = 0
                # get drive strength binary
                ds_bin = bin(ds.currentIndex()).replace("0b", "")
                ds_bin = ds_bin[::-1]
                while len(ds_bin) < 3:
                    ds_bin += '0'
                ds_bin = ds_bin[::-1]
                # get frequency binary
                freq_bin = bin(freq.currentIndex()).replace("0b", "")
                freq_bin = freq_bin[::-1]
                while len(freq_bin) < 3:
                    freq_bin += '0'
                freq_bin = freq_bin[::-1]

                register_bin_value = (str(inv_bin) + ds_bin + freq_bin)
                register_int_value = int(register_bin_value, 2)
                # print(register_bin_value)
                # print(register_int_value)

                print("Address %s : value %s" % (address, register_int_value))
                return address, register_int_value

    def return_byte_2(self):        # This works for all PE_strength, PS_mode, and PE_width registers
        sender = self.sender()
        address = sender.address
        # print(sender)
        # print(address)

        for PE_s, PE_m, PE_w in zip(self.PE_s_list, self.PE_m_list, self.PE_w_list):
            if sender in (PE_s, PE_m, PE_w):
                #get PE_s binary
                PE_s_bin = bin(PE_s.currentIndex()).replace("0b", "")
                PE_s_bin = PE_s_bin[::-1]
                while len(PE_s_bin) < 3:
                    PE_s_bin += '0'
                PE_s_bin = PE_s_bin[::-1]

                # get PE_m binary
                PE_m_bin = bin(PE_m.currentIndex()).replace("0b", "")
                PE_m_bin = PE_m_bin[::-1]
                while len(PE_m_bin) < 2:
                    PE_m_bin += '0'
                PE_m_bin = PE_m_bin[::-1]

                # get PE_w binary
                PE_w_bin = bin(PE_w.currentIndex()).replace("0b", "")
                PE_w_bin = PE_w_bin[::-1]
                while len(PE_w_bin) < 3:
                    PE_w_bin += '0'
                PE_w_bin = PE_w_bin[::-1]

                register_bin_value = (PE_s_bin + PE_m_bin + PE_w_bin)
                register_int_value = int(register_bin_value, 2)
                # print(register_bin_value)
                # print(register_int_value)

                print("Address %s : value %s" % (address, register_int_value))
                return address, register_int_value

##############################################################################################################

    def save(self):         # Save all of the parameters on the page!
        print("Save all page parameters")
        i = 0
        for inv, ds, freq in zip(self.checkbox_list, self.ds_list, self.freq_list):
            address = 108 + 2*i
            # get invert binary
            if inv.isChecked():
                inv_bin = 1
            else:
                inv_bin = 0
            # get drive strength binary
            ds_bin = bin(ds.currentIndex()).replace("0b", "")
            ds_bin = ds_bin[::-1]
            while len(ds_bin) < 3:
                ds_bin += '0'
            ds_bin = ds_bin[::-1]
            # get frequency binary
            freq_bin = bin(freq.currentIndex()).replace("0b", "")
            freq_bin = freq_bin[::-1]
            while len(freq_bin) < 3:
                freq_bin += '0'
            freq_bin = freq_bin[::-1]

            register_bin_value = (str(inv_bin) + ds_bin + freq_bin)
            register_int_value = int(register_bin_value, 2)
            print("Address %s : value %s" % (address, register_int_value))
            self.add_and_reg.append([address, register_int_value])

            # Then here do:
            # write(address, register_int_value)

            i += 1

        i = 0
        for PE_s, PE_m, PE_w in zip(self.PE_s_list, self.PE_m_list, self.PE_w_list):
            address = 109 + 2*i
            PE_s_bin = bin(PE_s.currentIndex()).replace("0b", "")
            PE_s_bin = PE_s_bin[::-1]
            while len(PE_s_bin) < 3:
                PE_s_bin += '0'
            PE_s_bin = PE_s_bin[::-1]

            # get PE_m binary
            PE_m_bin = bin(PE_m.currentIndex()).replace("0b", "")
            PE_m_bin = PE_m_bin[::-1]
            while len(PE_m_bin) < 2:
                PE_m_bin += '0'
            PE_m_bin = PE_m_bin[::-1]

            # get PE_w binary
            PE_w_bin = bin(PE_w.currentIndex()).replace("0b", "")
            PE_w_bin = PE_w_bin[::-1]
            while len(PE_w_bin) < 3:
                PE_w_bin += '0'
            PE_w_bin = PE_w_bin[::-1]

            register_bin_value = (PE_s_bin + PE_m_bin + PE_w_bin)
            register_int_value = int(register_bin_value, 2)
            # print(register_bin_value)
            # print(register_int_value)

            print("Address %s : value %s" % (address, register_int_value))
            self.add_and_reg.append([address, register_int_value])

            # Then here do:
            # write(address, register_int_value)
            i += 1

        list_to_xml = sorted(self.add_and_reg, key=lambda x: (x[0]))
        # print(list_to_xml)

        # getting the xml file
        root = minidom.Document()
        xml = root.createElement('root')
        root.appendChild(xml)

        for user in list_to_xml:
            productChild = root.createElement(str(user[0]))
            productChild.setAttribute('val', str(user[1]))
            xml.appendChild(productChild)

        xml_str = root.toprettyxml(indent="\t")
        save_path_file = "save_lpgbt.xml"
        with open(save_path_file, "w") as f:
            f.write(xml_str)
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Design.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QInputDialog

sys._excepthook = sys.excepthook
def my_exception_hook(exctype, value, traceback):
    # Print the error and traceback
    print(exctype, value, traceback)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)
# Set the exception hook to our wrapping function
sys.excepthook = my_exception_hook

GOAL = None
twelve_hours = int(3600 * 12)
NUMBER_OF_MINIONS = None
HOURLY_PRODUCE = 0
TWELVE_PRODUCE = 0
Hourly_produce_list = None
Twelve_hourly_list = None
MINION_LEVEL = None
FINAL_MINION_STORAGE = None
hour = 3600
OBSIDIAN_MINION_COOLDOWN = {
    1: 90,
    2: 90,
    3: 84,
    4: 84,
    5: 78,
    6: 78,
    7: 70,
    8: 70,
    9: 60,
    10: 60,
    11: 48
}

OBISIDIAN_MINION_STORAGE = {
    1: 64,
    2: 192,
    3: 192,
    4: 384,
    5: 384,
    6: 576,
    7: 576,
    8: 768,
    9: 768,
    10: 960,
    11: 960
}

class Ui_MinionCalculator(QWidget):
    def setupUi(self, MinionCalculator):
        global GOAL
        global NUMBER_OF_MINIONS
        global MINION_LEVEL
        global FINAL_MINION_STORAGE
        global HOURLY_PRODUCE

        MinionCalculator.setObjectName("MinionCalculator")
        MinionCalculator.resize(1061, 615)
        self.centralwidget = QtWidgets.QWidget(MinionCalculator)
        self.centralwidget.setObjectName("centralwidget")
        self.Frame = QtWidgets.QFrame(self.centralwidget)
        self.Frame.setGeometry(QtCore.QRect(0, 0, 1011, 601))
        font = QtGui.QFont()
        font.setFamily("Malgun gothic")
        font.setPointSize(14)
        self.Frame.setFont(font)
        self.Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Frame.setObjectName("Frame")
        self.inputgroupbox = QtWidgets.QGroupBox(self.Frame)
        self.inputgroupbox.setGeometry(QtCore.QRect(10, 10, 490, 580))
        self.inputgroupbox.setStyleSheet("QGroupBox { border: 0.5px solid gray;}")
        self.outputgroupbox = QtWidgets.QGroupBox(self.Frame)
        self.outputgroupbox.setGeometry(QtCore.QRect(521, 10, 490, 580))
        self.outputgroupbox.setStyleSheet("QGroupBox { border: 0.5px solid gray;}")
        self.Selectminiontypelabel = QtWidgets.QLabel(self.Frame)
        self.Selectminiontypelabel.setGeometry(QtCore.QRect(20, 30, 20, 41))
        self.Minionchoosecombo = QtWidgets.QComboBox(self.Frame)
        self.Minionchoosecombo.setGeometry(QtCore.QRect(235, 34, 171, 31))
        self.Minionchoosecombo.setObjectName("Minionchoosecombo")
        self.Minionchoosecombo.addItem("")
        self.SelectMinionamountlabel = QtWidgets.QLabel(self.Frame)
        self.SelectMinionamountlabel.setGeometry(QtCore.QRect(20, 80, 251, 31))
        self.SelectMinionamountlabel.setObjectName("SelectMinionamountlabel")
        self.Minionamountslider = QtWidgets.QSlider(self.Frame)
        self.Minionamountslider.setGeometry(QtCore.QRect(280, 88, 181, 22))
        self.Minionamountslider.setMinimum(1)
        self.Minionamountslider.setMaximum(24)
        self.Minionamountslider.setPageStep(3)
        self.Minionamountslider.setOrientation(QtCore.Qt.Horizontal)
        self.Minionamountslider.setObjectName("Minionamountslider")
        self.Minionamountslider.valueChanged.connect(self.change_slider_label)
        self.Slidervaluelabel = QtWidgets.QLabel(self.Frame)
        self.Slidervaluelabel.setGeometry(QtCore.QRect(470, 90, 101, 21))
        self.Slidervaluelabel.setObjectName("Slidervaluelabel")
        self.ItemgoalLabel = QtWidgets.QLabel(self.Frame)
        self.ItemgoalLabel.setGeometry(QtCore.QRect(30, 330, 111, 31))
        self.ItemgoalLabel.setObjectName("ItemgoalLabel")
        self.ItemgoalLabel.setText("Choose Item Type: ")
        self.itemtypechoosecombo = QtWidgets.QComboBox(self.Frame)
        self.itemtypechoosecombo.setGeometry(QtCore.QRect(150, 328, 150, 41))
        self.itemtypechoosecombo.setObjectName("itemtypechoosecombo")
        self.itemtypechoosecombo.addItem("")
        self.itemtypechoosecombo.addItem("")
        self.submititemtypebutton = QtWidgets.QPushButton(self.Frame)
        self.submititemtypebutton.setGeometry(QtCore.QRect(320, 328, 100, 40))
        self.submititemtypebutton.setObjectName("SubmitItemType")
        self.submititemtypebutton.setText("Submit")
        self.submititemtypebutton.clicked.connect(self.ItemTypeSubmitted)
        MinionCalculator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MinionCalculator)
        self.menubar.setGeometry(QtCore.QRect(20, 30, 1061, 26))
        self.menubar.setObjectName("menubar")
        MinionCalculator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MinionCalculator)
        self.statusbar.setObjectName("statusbar")
        MinionCalculator.setStatusBar(self.statusbar)
        self.Submitbutton = QtWidgets.QPushButton(self.Frame)
        self.Submitbutton.setGeometry(QtCore.QRect(320, 130, 181, 22))
        self.Submitbutton.setObjectName("Submitbutton")
        self.Submitbutton.setText("Submit")
        self.Submitbutton.adjustSize()
        self.Submitbutton.clicked.connect(self.Minionnumbersubmitted)
        self.showminionlevellabel = QtWidgets.QLabel(self.Frame)
        self.showminionlevellabel.setGeometry(QtCore.QRect(21, 200, 1000, 50))
        self.showminionlevellabel.adjustSize()
        self.showminionlevellabel.setWordWrap(True)
        self.redobutton = QtWidgets.QPushButton(self.Frame)
        self.redobutton.setGeometry(QtCore.QRect(50, 520, 150, 60))
        self.redobutton.setText("Redo")
        self.redobutton.clicked.connect(self.redo)
        self.goallistlabel = QtWidgets.QLabel(self.Frame)
        self.goallistlabel.setGeometry(QtCore.QRect(21, 400, 100, 50))
        self.goallistlabel.setWordWrap(True)
        self.houryprodlabel = QtWidgets.QLabel(self.Frame)
        self.houryprodlabel.setGeometry(QtCore.QRect(530, 12, 100, 50))
        self.houryprodlabel.setWordWrap(True)
        self.houryprodlabel.adjustSize()
        self.calculatebutton = QtWidgets.QPushButton(self.Frame)
        self.calculatebutton.setGeometry(QtCore.QRect(300, 520, 150, 60))
        self.calculatebutton.setText("Calculate")
        self.calculatebutton.clicked.connect(self.calculate)
        self.twelveprodlabel = QtWidgets.QLabel(self.Frame)
        self.twelveprodlabel.setGeometry(QtCore.QRect(530, 90, 100, 50))
        self.twelveprodlabel.setWordWrap(True)
        self.twelveprodlabel.adjustSize()
        self.goallabel = QtWidgets.QLabel(self.Frame)
        self.goallabel.setGeometry(QtCore.QRect(530, 180, 100, 50))
        self.goallabel.setWordWrap(True)
        self.hylogo = QtWidgets.QLabel(self.Frame)
        self.hylogo.setGeometry(QtCore.QRect(545, 330, 100, 100))
        pixmap = QPixmap('Hypixel Log.png')
        self.hylogo.setPixmap(pixmap)
        self.hylogo.adjustSize()
        self.hylogo.hide()
        self.retranslateUi(MinionCalculator)
        QtCore.QMetaObject.connectSlotsByName(MinionCalculator)


    def retranslateUi(self, MinionCalculator):
        _translate = QtCore.QCoreApplication.translate
        MinionCalculator.setWindowTitle(_translate("MinionCalculator", "Minion Calculator"))
        self.Selectminiontypelabel.setText(_translate("MinionCalculator", "Select Minion Type: "))
        self.Minionchoosecombo.setItemText(0, _translate("MinionCalculator", "Obsidian"))
        self.SelectMinionamountlabel.setText(_translate("MinionCalculator", "Select Minion Amount: "))
        self.Slidervaluelabel.setText(_translate("MinionCalculator", "1"))
        self.ItemgoalLabel.setText(_translate("MinionCalculator", "Item Goal: "))
        self.itemtypechoosecombo.setItemText(0, _translate("MinionCalculator", "Enchanted"))
        self.itemtypechoosecombo.setItemText(1, _translate("MinionCalculator", "Normal"))
        self.Selectminiontypelabel.adjustSize()

    def change_slider_label(self):
        self.Slidervaluelabel.setText(str(self.Minionamountslider.value()))

    def Minionnumbersubmitted(self):
        global NUMBER_OF_MINIONS
        global MINION_LEVEL
        global FINAL_MINION_STORAGE
        global OBSIDIAN_MINION_COOLDOWN
        global OBISIDIAN_MINION_STORAGE
        self.Minionchoosecombo.setEnabled(False)
        self.Minionamountslider.setEnabled(False)
        self.Submitbutton.setEnabled(False)
        self.Submitbutton.setText("-----")
        self.Submitbutton.adjustSize()
        NUMBER_OF_MINIONS = int(self.Minionamountslider.value())
        MINION_LEVEL = [0] * NUMBER_OF_MINIONS
        FINAL_MINION_STORAGE = [0] * NUMBER_OF_MINIONS

        for minion_level_final in range(NUMBER_OF_MINIONS):
            if minion_level_final + 1 == 1:
                text, ok = QInputDialog.getInt(self, 'Minion Level', 'Type the 1st minion\'s level.' )

                if ok and 0 < text < 12:
                    MINION_LEVEL[minion_level_final] = int(text)

                elif text <= 0 or text >= 12:
                    sys.exit("TYPE A VALID MINION NUMBER")

                else:
                    sys.exit("ERROR")

            elif minion_level_final + 1 == 2:
                text, ok = QInputDialog.getInt(self, 'Minion Level', 'Type the 2nd minion\'s level.')
                if ok and 0 < text < 12:
                    MINION_LEVEL[minion_level_final] = int(text)

                elif text <= 0 or text >= 12:
                    sys.exit("TYPE A VALID MINION NUMBER")

                else:
                    sys.exit("ERROR")

            elif minion_level_final + 1 == 3:
                text, ok = QInputDialog.getInt(self, 'Minion Level', 'Type the 3rd minion\'s level.')
                if ok and 0 < text < 12:
                    MINION_LEVEL[minion_level_final] = int(text)

                elif text <= 0 or text >= 12:
                    sys.exit("TYPE A VALID MINION NUMBER")

                else:
                    sys.exit("ERROR")

            elif minion_level_final + 1 > 3:
                text, ok = QInputDialog.getInt(self, 'Minion Level', 'Type the ' + str(minion_level_final + 1) + 'th minion\'s level.')
                if ok and 0 < text < 12:
                    MINION_LEVEL[minion_level_final] = int(text)

                elif text <= 0 or text >= 12:
                    sys.exit("TYPE A VALID MINION NUMBER")

                else:
                    sys.exit("ERROR")

        for minion_storage_final in range(NUMBER_OF_MINIONS):
            if minion_storage_final + 1 == 1:
                msgbox = QMessageBox()
                msgbox.setWindowTitle("Minion Storage")
                msgbox.setIcon(QMessageBox.Question)
                msgbox.setText("Which extra storage does your 1st minion have?")
                msgbox.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Ignore | QMessageBox.Retry)
                msgbox.setDefaultButton(QMessageBox.Yes)
                buttonX = msgbox.button(QMessageBox.Yes)
                buttonY = msgbox.button(QMessageBox.No)
                buttonZ = msgbox.button(QMessageBox.Ignore)
                buttonA = msgbox.button(QMessageBox.Retry)
                buttonX.setText("None")
                buttonZ.setText("Medium")
                buttonA.setText("Small")
                buttonY.setText("Large")

                result = msgbox.exec_()
                if result == QMessageBox.Yes:
                    FINAL_MINION_STORAGE[minion_storage_final] = OBISIDIAN_MINION_STORAGE[MINION_LEVEL[minion_storage_final]]
                elif result == QMessageBox.Retry:
                    FINAL_MINION_STORAGE[minion_storage_final] = OBISIDIAN_MINION_STORAGE[MINION_LEVEL[minion_storage_final]] + (64 * 3)
                elif result == QMessageBox.Ignore:
                    FINAL_MINION_STORAGE[minion_storage_final] = OBISIDIAN_MINION_STORAGE[MINION_LEVEL[minion_storage_final]] + (64 * 9)
                elif result == QMessageBox.No:
                    FINAL_MINION_STORAGE[minion_storage_final] = OBISIDIAN_MINION_STORAGE[MINION_LEVEL[minion_storage_final]] + (64 * 15)
                else:
                    sys.exit("ERROR")

            elif minion_storage_final + 1 == 2:
                msgbox = QMessageBox()
                msgbox.setWindowTitle("Minion Storage")
                msgbox.setIcon(QMessageBox.Question)
                msgbox.setText("Which extra storage does your 2nd minion have?")
                msgbox.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Ignore | QMessageBox.Retry)
                msgbox.setDefaultButton(QMessageBox.Yes)
                buttonX = msgbox.button(QMessageBox.Yes)
                buttonY = msgbox.button(QMessageBox.No)
                buttonZ = msgbox.button(QMessageBox.Ignore)
                buttonA = msgbox.button(QMessageBox.Retry)
                buttonX.setText("None")
                buttonZ.setText("Medium")
                buttonA.setText("Small")
                buttonY.setText("Large")

                result = msgbox.exec_()
                if result == QMessageBox.Yes:
                    FINAL_MINION_STORAGE[minion_storage_final] = OBISIDIAN_MINION_STORAGE[
                        MINION_LEVEL[minion_storage_final]]
                elif result == QMessageBox.Retry:
                    FINAL_MINION_STORAGE[minion_storage_final] = OBISIDIAN_MINION_STORAGE[
                                                                     MINION_LEVEL[minion_storage_final]] + (64 * 3)
                elif result == QMessageBox.Ignore:
                    FINAL_MINION_STORAGE[minion_storage_final] = OBISIDIAN_MINION_STORAGE[
                                                                     MINION_LEVEL[minion_storage_final]] + (64 * 9)
                elif result == QMessageBox.No:
                    FINAL_MINION_STORAGE[minion_storage_final] = OBISIDIAN_MINION_STORAGE[
                                                                     MINION_LEVEL[minion_storage_final]] + (64 * 15)
                else:
                    sys.exit("ERROR")

            elif minion_storage_final + 1 == 3:
                msgbox = QMessageBox()
                msgbox.setWindowTitle("Minion Storage")
                msgbox.setIcon(QMessageBox.Question)
                msgbox.setText("Which extra storage does your 3rd minion have?")
                msgbox.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Ignore | QMessageBox.Retry)
                msgbox.setDefaultButton(QMessageBox.Yes)
                buttonX = msgbox.button(QMessageBox.Yes)
                buttonY = msgbox.button(QMessageBox.No)
                buttonZ = msgbox.button(QMessageBox.Ignore)
                buttonA = msgbox.button(QMessageBox.Retry)
                buttonX.setText("None")
                buttonZ.setText("Medium")
                buttonA.setText("Small")
                buttonY.setText("Large")

                result = msgbox.exec_()
                if result == QMessageBox.Yes:
                    FINAL_MINION_STORAGE[minion_storage_final] = OBISIDIAN_MINION_STORAGE[
                        MINION_LEVEL[minion_storage_final]]
                elif result == QMessageBox.Retry:
                    FINAL_MINION_STORAGE[minion_storage_final] = OBISIDIAN_MINION_STORAGE[
                                                                     MINION_LEVEL[minion_storage_final]] + (64 * 3)
                elif result == QMessageBox.Ignore:
                    FINAL_MINION_STORAGE[minion_storage_final] = OBISIDIAN_MINION_STORAGE[
                                                                     MINION_LEVEL[minion_storage_final]] + (64 * 9)
                elif result == QMessageBox.No:
                    FINAL_MINION_STORAGE[minion_storage_final] = OBISIDIAN_MINION_STORAGE[
                                                                     MINION_LEVEL[minion_storage_final]] + (64 * 15)
                else:
                    sys.exit("ERROR")

            elif minion_storage_final + 1 > 3:

                msgbox = QMessageBox()
                msgbox.setWindowTitle("Minion Storage")
                msgbox.setIcon(QMessageBox.Question)
                msgbox.setText("Which extra storage does your " + str(minion_storage_final + 1) + "th minion have?")
                msgbox.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Ignore | QMessageBox.Retry)
                msgbox.setDefaultButton(QMessageBox.Yes)
                msgbox.setDefaultButton(QMessageBox.Yes)
                buttonX = msgbox.button(QMessageBox.Yes)
                buttonY = msgbox.button(QMessageBox.No)
                buttonZ = msgbox.button(QMessageBox.Ignore)
                buttonA = msgbox.button(QMessageBox.Retry)
                buttonX.setText("None")
                buttonZ.setText("Medium")
                buttonA.setText("Small")
                buttonY.setText("Large")

                result = msgbox.exec_()
                if result == QMessageBox.Yes:
                    FINAL_MINION_STORAGE[minion_storage_final] = OBISIDIAN_MINION_STORAGE[
                        MINION_LEVEL[minion_storage_final]]
                elif result == QMessageBox.Retry:
                    FINAL_MINION_STORAGE[minion_storage_final] = OBISIDIAN_MINION_STORAGE[
                                                                     MINION_LEVEL[minion_storage_final]] + (64 * 3)
                elif result == QMessageBox.Ignore:
                    FINAL_MINION_STORAGE[minion_storage_final] = OBISIDIAN_MINION_STORAGE[
                                                                     MINION_LEVEL[minion_storage_final]] + (64 * 9)
                elif result == QMessageBox.No:
                    FINAL_MINION_STORAGE[minion_storage_final] = OBISIDIAN_MINION_STORAGE[
                                                                     MINION_LEVEL[minion_storage_final]] + (64 * 15)
                else:
                    sys.exit("ERROR")

            else:
                sys.exit("ERROR")

        minionlevelstring = ', '.join(str(e) for e in MINION_LEVEL)
        self.showminionlevellabel.setText("Your Minion's Levels: " + minionlevelstring)
        self.showminionlevellabel.adjustSize()

    def ItemTypeSubmitted(self):
        global GOAL
        self.itemtypechoosecombo.setEnabled(False)
        self.submititemtypebutton.setEnabled(False)
        self.submititemtypebutton.setText("-----")

        itemtype = self.itemtypechoosecombo.currentText()

        if itemtype == "Normal":
            text1, ok = QInputDialog.getInt(self, 'Item Goal', 'How many normal items do you want?')
            if ok:
                GOAL = int(text1)
                self.goallistlabel.setText("Your goal: " + str(GOAL) + " blocks or " + str(round(GOAL / 160)) + " enchanted blocks")
                self.goallistlabel.adjustSize()
            else:
                sys.exit("ERROR")

        elif itemtype == "Enchanted":
            text2, ok = QInputDialog.getInt(self, 'Item Goal', 'How many enchanted items do you want?')

            if ok:
                GOAL = int(text2) * 160
                self.goallistlabel.setText("Your goal: " + str(GOAL) + " blocks or " + str(round(GOAL / 160)) + " enchanted blocks")
                self.goallistlabel.adjustSize()
            else:
                sys.exit("ERROR")
        else:
            sys.exit("ERROR")

    def redo(self):
        self.Minionchoosecombo.setEnabled(True)
        self.Minionamountslider.setEnabled(True)
        self.Submitbutton.setEnabled(True)
        self.Submitbutton.setText("Submit")
        self.Submitbutton.adjustSize()
        self.itemtypechoosecombo.setEnabled(True)
        self.submititemtypebutton.setEnabled(True)
        self.goallistlabel.setText("")
        self.showminionlevellabel.setText("")
        self.Minionamountslider.setValue(1)
        self.submititemtypebutton.setText("Submit")

    def calculate(self):
        global twelve_hours
        global Twelve_hourly_list
        global HOURLY_PRODUCE
        global Hourly_produce_list
        global NUMBER_OF_MINIONS
        global hour
        global OBISIDIAN_MINION_STORAGE
        global OBSIDIAN_MINION_COOLDOWN
        global FINAL_MINION_STORAGE
        global MINION_LEVEL
        global TWELVE_PRODUCE
        global GOAL

        self.hylogo.show()

        Twelve_hourly_list = [0] * NUMBER_OF_MINIONS

        Hourly_produce_list = [0] * NUMBER_OF_MINIONS

        # Hour_list Fill
        for hourlylist in range(NUMBER_OF_MINIONS):
            Hourly_produce_list[hourlylist] = int(hour / int(OBSIDIAN_MINION_COOLDOWN[MINION_LEVEL[hourlylist]]))
        HOURLY_PRODUCE = round(int(sum(Hourly_produce_list)))

        # Twelve_hour_list fill
        for twelvelist in range(NUMBER_OF_MINIONS):
            if FINAL_MINION_STORAGE[twelvelist] >= int(twelve_hours / OBSIDIAN_MINION_COOLDOWN[MINION_LEVEL[twelvelist]]):
                Twelve_hourly_list[twelvelist] = int(twelve_hours / OBSIDIAN_MINION_COOLDOWN[MINION_LEVEL[twelvelist]])

            elif FINAL_MINION_STORAGE[twelvelist] < int(twelve_hours / OBSIDIAN_MINION_COOLDOWN[MINION_LEVEL[twelvelist]]):
                Twelve_hourly_list[twelvelist] = FINAL_MINION_STORAGE[twelvelist]

            else:
                sys.exit("ERROR")

        for calcgoal in range(NUMBER_OF_MINIONS):
            self.goaltimehour = GOAL / HOURLY_PRODUCE

        #Output Labels
        TWELVE_PRODUCE = int(sum(Twelve_hourly_list))
        self.twelveprodlabel.setText("Twelve Hour Production: " + str(TWELVE_PRODUCE) + " obsidians or " + str(round((TWELVE_PRODUCE / 160), 2)) + " enchanted obsidians")
        self.twelveprodlabel.adjustSize()

        self.houryprodlabel.setText("Hourly Production:  " + str(HOURLY_PRODUCE) + " Obsidian or " + str(
            round(HOURLY_PRODUCE / 160, 2)) + " Enchanted Obsidian.")
        self.houryprodlabel.setWordWrap(True)
        self.houryprodlabel.adjustSize()
        self.goallabel.setText("It takes " + str(self.goaltimehour) + " hours or " + str(round(self.goaltimehour / 24, 2)) + " days to reach your goal without considering the minion storage.")
        self.goallabel.adjustSize()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MinionCalculator = QtWidgets.QMainWindow()
    ui = Ui_MinionCalculator()
    ui.setupUi(MinionCalculator)
    MinionCalculator.show()
    sys.exit(app.exec_())


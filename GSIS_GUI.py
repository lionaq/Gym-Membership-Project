# Form implementation generated from reading ui file 'ArellanoAclo_GSIS.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtWidgets, QtGui
from PyQt6.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QComboBox, QDialog, QMessageBox, QDateEdit, QPushButton
from PyQt6.QtGui import QIntValidator, QDoubleValidator
from PyQt6.QtCore import QDate


def show_error_message(message):
    error_box = QMessageBox()
    error_box.setIcon(QMessageBox.Icon.Critical)
    error_box.setWindowTitle("Error")
    error_box.setText("An error occurred.")
    error_box.setInformativeText(message)
    error_box.exec()

class Ui_GSIS(object):
    def setupUi(self, GSIS):
        GSIS.setObjectName("GSIS")
        GSIS.setEnabled(True)
        GSIS.resize(1200, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GSIS.sizePolicy().hasHeightForWidth())
        GSIS.setSizePolicy(sizePolicy)
        GSIS.setMinimumSize(QtCore.QSize(1200, 800))
        GSIS.setMaximumSize(QtCore.QSize(1200, 800))
        GSIS.setMouseTracking(False)
        GSIS.setStyleSheet("background-color:rgb(34, 40, 49)")
        GSIS.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.centralwidget = QtWidgets.QWidget(parent=GSIS)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1181, 780))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMaximumSize(QtCore.QSize(1181, 780))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.tabWidget.setFont(font)
        self.tabWidget.setStatusTip("")
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("background-color:rgb(34, 40, 49)")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.TextElideMode.ElideNone)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.customerTab = QtWidgets.QWidget()
        self.customerTab.setEnabled(True)
        self.customerTab.setObjectName("customerTab")
        self.customerTable = QtWidgets.QTableView(parent=self.customerTab)
        self.customerTable.setEnabled(True)
        self.customerTable.setGeometry(QtCore.QRect(20, 120, 1141, 621))
        self.customerTable.setAutoFillBackground(False)
        self.customerTable.setStyleSheet("background-color: rgb(238, 238, 238)")
        self.customerTable.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.customerTable.setObjectName("customerTable")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.customerTab)
        self.horizontalLayoutWidget.setEnabled(True)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 71, 1141, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.hboxlayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.hboxlayout.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout.setSpacing(7)
        self.hboxlayout.setObjectName("hboxlayout")
        self.customerLineEdit = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget)
        self.customerLineEdit.setEnabled(True)
        self.customerLineEdit.setStyleSheet("background-color: rgb(238, 238, 238)")
        self.customerLineEdit.setText("")
        self.customerLineEdit.setMaxLength(250)
        self.customerLineEdit.setObjectName("customerLineEdit")
        self.hboxlayout.addWidget(self.customerLineEdit)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(parent=self.customerTab)
        self.horizontalLayoutWidget_3.setEnabled(True)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 10, 1141, 61))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 6, 0, 6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.addButtonCustomer = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_3)
        self.addButtonCustomer.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addButtonCustomer.sizePolicy().hasHeightForWidth())
        self.addButtonCustomer.setSizePolicy(sizePolicy)
        self.addButtonCustomer.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.addButtonCustomer.setMouseTracking(False)
        self.addButtonCustomer.setStyleSheet("background-color:rgb(0, 173, 181);\n"
"font: 87 8pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.addButtonCustomer.setObjectName("addButtonCustomer")
        self.horizontalLayout_3.addWidget(self.addButtonCustomer)
        self.deleteButtonStudent = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_3)
        self.deleteButtonStudent.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteButtonStudent.sizePolicy().hasHeightForWidth())
        self.deleteButtonStudent.setSizePolicy(sizePolicy)
        self.deleteButtonStudent.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.deleteButtonStudent.setStyleSheet("background-color:rgb(0, 173, 181);\n"
"font: 87 8pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.deleteButtonStudent.setObjectName("deleteButtonStudent")
        self.horizontalLayout_3.addWidget(self.deleteButtonStudent)
        self.tabWidget.addTab(self.customerTab, "")
        self.gymmembership_detaitsTab = QtWidgets.QWidget()
        self.gymmembership_detaitsTab.setObjectName("gymmembership_detaitsTab")
        self.tabWidget_2 = QtWidgets.QTabWidget(parent=self.gymmembership_detaitsTab)
        self.tabWidget_2.setEnabled(True)
        self.tabWidget_2.setGeometry(QtCore.QRect(10, 10, 1151, 721))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget_2.sizePolicy().hasHeightForWidth())
        self.tabWidget_2.setSizePolicy(sizePolicy)
        self.tabWidget_2.setUsesScrollButtons(False)
        self.tabWidget_2.setDocumentMode(False)
        self.tabWidget_2.setTabsClosable(False)
        self.tabWidget_2.setTabBarAutoHide(False)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.plansTab = QtWidgets.QWidget()
        self.plansTab.setEnabled(True)
        self.plansTab.setObjectName("plansTab")
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(parent=self.plansTab)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(0, 60, 631, 41))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.plansTab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 591, 641))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.addPlansButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.addPlansButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addPlansButton.sizePolicy().hasHeightForWidth())
        self.addPlansButton.setSizePolicy(sizePolicy)
        self.addPlansButton.setStyleSheet("background-color:rgb(0, 173, 181);\n"
"font: 87 8pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.addPlansButton.setObjectName("addPlansButton")
        self.horizontalLayout_5.addWidget(self.addPlansButton)
        self.deletePlansButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deletePlansButton.sizePolicy().hasHeightForWidth())
        self.deletePlansButton.setSizePolicy(sizePolicy)
        self.deletePlansButton.setStyleSheet("background-color:rgb(0, 173, 181);\n"
"font: 87 8pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.deletePlansButton.setObjectName("deletePlansButton")
        self.horizontalLayout_5.addWidget(self.deletePlansButton)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.PlansLineEdit_3 = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.PlansLineEdit_3.setStyleSheet("background-color: rgb(238, 238, 238)")
        self.PlansLineEdit_3.setText("")
        self.PlansLineEdit_3.setMaxLength(500)
        self.PlansLineEdit_3.setObjectName("PlansLineEdit_3")
        self.verticalLayout.addWidget(self.PlansLineEdit_3)
        self.plansTable = QtWidgets.QTableView(parent=self.verticalLayoutWidget)
        self.plansTable.setAutoFillBackground(False)
        self.plansTable.setStyleSheet("background-color: rgb(238, 238, 238)")
        self.plansTable.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.plansTable.setObjectName("plansTable")
        self.verticalLayout.addWidget(self.plansTable)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.plansTab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(660, 40, 448, 611))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.availableAmenitiesLabel = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.availableAmenitiesLabel.setStyleSheet("\n"
"font: 87 8pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.availableAmenitiesLabel.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.availableAmenitiesLabel.setLineWidth(0)
        self.availableAmenitiesLabel.setObjectName("availableAmenitiesLabel")
        self.verticalLayout_2.addWidget(self.availableAmenitiesLabel, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.addAvailableAmenities = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.addAvailableAmenities.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addAvailableAmenities.sizePolicy().hasHeightForWidth())
        self.addAvailableAmenities.setSizePolicy(sizePolicy)
        self.addAvailableAmenities.setStyleSheet("background-color:rgb(0, 173, 181);\n"
"font: 87 8pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.addAvailableAmenities.setObjectName("addAvailableAmenities")
        self.horizontalLayout_7.addWidget(self.addAvailableAmenities)
        self.deleteAvailableAmenities = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteAvailableAmenities.sizePolicy().hasHeightForWidth())
        self.deleteAvailableAmenities.setSizePolicy(sizePolicy)
        self.deleteAvailableAmenities.setStyleSheet("background-color:rgb(0, 173, 181);\n"
"font: 87 8pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.deleteAvailableAmenities.setObjectName("deleteAvailableAmenities")
        self.horizontalLayout_7.addWidget(self.deleteAvailableAmenities)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.availableAmenitiesSearch = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_2)
        self.availableAmenitiesSearch.setStyleSheet("background-color: rgb(238, 238, 238)")
        self.availableAmenitiesSearch.setText("")
        self.availableAmenitiesSearch.setMaxLength(500)
        self.availableAmenitiesSearch.setObjectName("availableAmenitiesSearch")
        self.verticalLayout_2.addWidget(self.availableAmenitiesSearch)
        self.listView = QtWidgets.QListView(parent=self.verticalLayoutWidget_2)
        self.listView.setStyleSheet("background-color: rgb(238, 238, 238)")
        self.listView.setObjectName("listView")
        self.verticalLayout_2.addWidget(self.listView)
        self.tabWidget_2.addTab(self.plansTab, "")
        self.trainerTab = QtWidgets.QWidget()
        self.trainerTab.setEnabled(True)
        self.trainerTab.setObjectName("trainerTab")
        self.trainerTable = QtWidgets.QTableView(parent=self.trainerTab)
        self.trainerTable.setGeometry(QtCore.QRect(0, 110, 1161, 601))
        self.trainerTable.setAutoFillBackground(False)
        self.trainerTable.setStyleSheet("background-color: rgb(238, 238, 238)")
        self.trainerTable.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.trainerTable.setObjectName("trainerTable")
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(parent=self.trainerTab)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(-10, 10, 1171, 41))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.addButtonTrainer_2 = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_7)
        self.addButtonTrainer_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addButtonTrainer_2.sizePolicy().hasHeightForWidth())
        self.addButtonTrainer_2.setSizePolicy(sizePolicy)
        self.addButtonTrainer_2.setStyleSheet("background-color:rgb(0, 173, 181);\n"
"font: 87 8pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.addButtonTrainer_2.setObjectName("addButtonTrainer_2")
        self.horizontalLayout_8.addWidget(self.addButtonTrainer_2)
        self.deleteButtonTrainer_2 = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteButtonTrainer_2.sizePolicy().hasHeightForWidth())
        self.deleteButtonTrainer_2.setSizePolicy(sizePolicy)
        self.deleteButtonTrainer_2.setStyleSheet("background-color:rgb(0, 173, 181);\n"
"font: 87 8pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.deleteButtonTrainer_2.setObjectName("deleteButtonTrainer_2")
        self.horizontalLayout_8.addWidget(self.deleteButtonTrainer_2)
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(parent=self.trainerTab)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(0, 60, 1161, 41))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.trainertLineEdit_2 = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_8)
        self.trainertLineEdit_2.setEnabled(True)
        self.trainertLineEdit_2.setStyleSheet("background-color: rgb(238, 238, 238)")
        self.trainertLineEdit_2.setText("")
        self.trainertLineEdit_2.setMaxLength(500)
        self.trainertLineEdit_2.setObjectName("trainertLineEdit_2")
        self.horizontalLayout_9.addWidget(self.trainertLineEdit_2)
        self.tabWidget_2.addTab(self.trainerTab, "")
        self.amenitiesTab = QtWidgets.QWidget()
        self.amenitiesTab.setObjectName("amenitiesTab")
        self.amenitiesTable = QtWidgets.QTableView(parent=self.amenitiesTab)
        self.amenitiesTable.setEnabled(True)
        self.amenitiesTable.setGeometry(QtCore.QRect(0, 110, 1161, 601))
        self.amenitiesTable.setAutoFillBackground(False)
        self.amenitiesTable.setStyleSheet("background-color: rgb(238, 238, 238)")
        self.amenitiesTable.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.amenitiesTable.setObjectName("amenitiesTable")
        self.horizontalLayoutWidget_15 = QtWidgets.QWidget(parent=self.amenitiesTab)
        self.horizontalLayoutWidget_15.setEnabled(True)
        self.horizontalLayoutWidget_15.setGeometry(QtCore.QRect(0, 60, 1161, 41))
        self.horizontalLayoutWidget_15.setObjectName("horizontalLayoutWidget_15")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_15)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.amenitiesButtonLineEdit = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_15)
        self.amenitiesButtonLineEdit.setEnabled(True)
        self.amenitiesButtonLineEdit.setStyleSheet("background-color: rgb(238, 238, 238)")
        self.amenitiesButtonLineEdit.setText("")
        self.amenitiesButtonLineEdit.setMaxLength(500)
        self.amenitiesButtonLineEdit.setObjectName("amenitiesButtonLineEdit")
        self.horizontalLayout_16.addWidget(self.amenitiesButtonLineEdit)
        self.horizontalLayoutWidget_16 = QtWidgets.QWidget(parent=self.amenitiesTab)
        self.horizontalLayoutWidget_16.setEnabled(True)
        self.horizontalLayoutWidget_16.setGeometry(QtCore.QRect(0, 10, 1161, 41))
        self.horizontalLayoutWidget_16.setObjectName("horizontalLayoutWidget_16")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_16)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.addAmenitiesButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_16)
        self.addAmenitiesButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addAmenitiesButton.sizePolicy().hasHeightForWidth())
        self.addAmenitiesButton.setSizePolicy(sizePolicy)
        self.addAmenitiesButton.setStyleSheet("background-color:rgb(0, 173, 181);\n"
"font: 87 8pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.addAmenitiesButton.setObjectName("addAmenitiesButton")
        self.horizontalLayout_17.addWidget(self.addAmenitiesButton)
        self.deleteAmenitiesButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_16)
        self.deleteAmenitiesButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteAmenitiesButton.sizePolicy().hasHeightForWidth())
        self.deleteAmenitiesButton.setSizePolicy(sizePolicy)
        self.deleteAmenitiesButton.setStyleSheet("background-color:rgb(0, 173, 181);\n"
"font: 87 8pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.deleteAmenitiesButton.setObjectName("deleteAmenitiesButton")
        self.horizontalLayout_17.addWidget(self.deleteAmenitiesButton)
        self.tabWidget_2.addTab(self.amenitiesTab, "")
        self.tabWidget.addTab(self.gymmembership_detaitsTab, "")
        GSIS.setCentralWidget(self.centralwidget)

        self.retranslateUi(GSIS)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(GSIS)

    def retranslateUi(self, GSIS):
        _translate = QtCore.QCoreApplication.translate
        GSIS.setWindowTitle(_translate("GSIS", "MainWindow"))
        self.customerLineEdit.setPlaceholderText(_translate("GSIS", "Customers Search"))
        self.addButtonCustomer.setText(_translate("GSIS", "ADD GYM MEMBER"))
        self.deleteButtonStudent.setText(_translate("GSIS", "DELETE INFORMATION"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.customerTab), _translate("GSIS", "CUSTOMER"))
        self.addPlansButton.setText(_translate("GSIS", "ADD PLANS"))
        self.deletePlansButton.setText(_translate("GSIS", "DELETE INFORMATION"))
        self.PlansLineEdit_3.setPlaceholderText(_translate("GSIS", "Plans Search"))
        self.availableAmenitiesLabel.setText(_translate("GSIS", "PLAN"))
        self.addAvailableAmenities.setText(_translate("GSIS", "ADD AMENITIES FOR"))
        self.deleteAvailableAmenities.setText(_translate("GSIS", "DELETE AMENITIES FOR"))
        self.availableAmenitiesSearch.setPlaceholderText(_translate("GSIS", "Available Amenities Search"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.plansTab), _translate("GSIS", "PLANS"))
        self.addButtonTrainer_2.setText(_translate("GSIS", "ADD TRAINER"))
        self.deleteButtonTrainer_2.setText(_translate("GSIS", "DELETE INFORMATION"))
        self.trainertLineEdit_2.setPlaceholderText(_translate("GSIS", "Trainers Search"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.trainerTab), _translate("GSIS", "TRAINERS"))
        self.amenitiesButtonLineEdit.setPlaceholderText(_translate("GSIS", "Amenities Search"))
        self.addAmenitiesButton.setText(_translate("GSIS", "ADD AMENITIES"))
        self.deleteAmenitiesButton.setText(_translate("GSIS", "DELETE INFORMATION"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.amenitiesTab), _translate("GSIS", "AMENITIES"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.gymmembership_detaitsTab), _translate("GSIS", "GYM MEMBERSHIP DETAILS"))

class customerAddWindow(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Customer Form")

        # Create labels
        customerID_label = QLabel("Customer ID:")
        customerName_label = QLabel("Name:")
        gender_label = QLabel("Gender:")
        weight_label = QLabel("Weight (kg):")
        height_label = QLabel("Height (cm):")
        PlanName_label = QLabel("Plan Name:")
        startDate_label = QLabel("Start Date:")
        endDate_label = QLabel("End Date:")
        contactNo_label = QLabel("Contact Number:")
        birthDate_label = QLabel("Birth Date:")

        # Create line edits
        self.customerID_lineEdit = QLineEdit()
        self.customerID_lineEdit.setValidator(QIntValidator())
        self.customerID_lineEdit.setMaxLength(6)
        self.customerName_lineEdit = QLineEdit()
        self.customerName_lineEdit.setMaxLength(100)
        self.weight_lineEdit = QLineEdit()
        self.weight_lineEdit.setValidator(QDoubleValidator())
        self.weight_lineEdit.setMaxLength(6)
        self.height_lineEdit = QLineEdit()
        self.height_lineEdit.setValidator(QIntValidator())
        self.height_lineEdit.setMaxLength(3)
        self.contactNo_lineEdit = QLineEdit()
        self.contactNo_lineEdit.setValidator(QIntValidator())
        self.contactNo_lineEdit.setMaxLength(11)

        self.weight_lineEdit.textEdited.connect(self.removeE)

        # Create date edits
        self.startDate_edit = QDateEdit()
        self.startDate_edit.setDisplayFormat("yyyy-MM-dd")
        self.startDate_edit.setDate(QDate.currentDate())
        self.endDate_edit = QDateEdit()
        self.endDate_edit.setDisplayFormat("yyyy-MM-dd")
        self.endDate_edit.setDate(QDate.currentDate())
        self.birthDate_edit = QDateEdit()
        self.birthDate_edit.setDisplayFormat("yyyy-MM-dd")
        self.birthDate_edit.setDate(QDate.currentDate())


        # creat combo box
        self.gender_combo_box = QComboBox()
        self.gender_combo_box.addItems(["Male", "Female", "Other"])
        self.confirm_button = QtWidgets.QPushButton("Confirm")
        self.confirm_button.clicked.connect(self.accept)

        self.PlanName_combo_box = QComboBox()
        self.confirm_button = QtWidgets.QPushButton("Confirm")
        self.confirm_button.clicked.connect(self.accept)

        # Create a layout for the input window
        layout = QVBoxLayout()
        self.setLayout(layout)
    
        # Add the labels, line edits, and combo boxes to the layout
        layout.addWidget(customerID_label)
        layout.addWidget(self.customerID_lineEdit)
        layout.addWidget(customerName_label)
        layout.addWidget(self.customerName_lineEdit)
        layout.addWidget(gender_label)
        layout.addWidget(self.gender_combo_box)
        layout.addWidget(weight_label )
        layout.addWidget(self.weight_lineEdit)
        layout.addWidget(height_label)
        layout.addWidget(self.height_lineEdit)
        layout.addWidget(PlanName_label)
        layout.addWidget(self.PlanName_combo_box)
        layout.addWidget(startDate_label)
        layout.addWidget(self.startDate_edit)
        layout.addWidget(endDate_label)
        layout.addWidget(self.endDate_edit)
        layout.addWidget(contactNo_label)
        layout.addWidget(self.contactNo_lineEdit)
        layout.addWidget(birthDate_label)
        layout.addWidget(self.birthDate_edit)
        layout.addWidget(self.confirm_button)
        layout.addWidget(self.confirm_button)
        self.setLayout(layout)

    def removeE(self, text):
        # Remove any existing dashes from the text
        text = text.replace("e", "")
        self.weight_lineEdit.setText(text)

    def return_info(self):
        if len(self.weight_lineEdit.text()) < 1 or len(self.height_lineEdit.text()) < 1:
            show_error_message("BLANK FIELDS, TRY AGAIN")
            return 0
        
        list = [self.customerID_lineEdit.text(),
                self.customerName_lineEdit.text().title(),
                self.gender_combo_box.currentText(),
                float(self.weight_lineEdit.text()),
                int(self.height_lineEdit.text()),
                self.PlanName_combo_box.currentText(),
                self.startDate_edit.text(),
                self.endDate_edit.text(),
                self.contactNo_lineEdit.text(),
                self.birthDate_edit.text()]
        print(list)
        if len(list[5]) < 1:
            show_error_message("NO PlanName AVAILABLE, PLEASE ADD A COURSE")
            return 0
        
        if len(list[0]) >= 1 and len(list[1]) >= 1 and len(list[8]) >= 1  and not list[1].isspace():
            return list
        else:
            show_error_message("BLANK FIELDS, TRY AGAIN")
            return 0
        


class trainerAddWindow(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Trainer Window")

        # Create labels
        trainerID_label = QLabel("Trainer ID:")
        trainerName_label = QLabel("Name:")
        PlanName_label = QLabel("Plan Name:")

        # Create line edits
        self.trainerID_lineEdit = QLineEdit()
        self.trainerID_lineEdit.setValidator(QIntValidator())
        self.trainerID_lineEdit.setMaxLength(7)
        self.trainerName_lineEdit = QLineEdit()
        self.trainerName_lineEdit.setMaxLength(100)

        # creat combo box
        self.PlanName_combo_box = QComboBox()

        self.confirm_button = QtWidgets.QPushButton("Confirm")
        self.confirm_button.clicked.connect(self.accept)

        # Create a layout for the input window
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Add the labels, line edits, and combo boxes to the layout
        layout.addWidget(trainerID_label)
        layout.addWidget(self.trainerID_lineEdit)
        layout.addWidget(trainerName_label)
        layout.addWidget(self.trainerName_lineEdit)
        layout.addWidget(PlanName_label)
        layout.addWidget(self.PlanName_combo_box)
        layout.addWidget(self.confirm_button)
        self.setLayout(layout)
        
    def return_info(self):
        data = [
            self.trainerID_lineEdit.text(),
            self.trainerName_lineEdit.text().title(),
            self.PlanName_combo_box.currentText()
        ]
        
        if len(data[0]) >= 1 and len(data[1]) >= 1 and not data[1].isspace() and not data[0].isspace():
            return data
        else:
            show_error_message("BLANK FIELDS, TRY AGAIN")
            return 0

# amenities

class amenityAddWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Amenity Window")

        # Create labels
        amenity_label = QLabel("Amenity:")

        # Create line edit
        self.amenity_lineEdit = QLineEdit()

        # Create a confirm button
        self.confirm_button = QPushButton("Confirm")
        self.confirm_button.clicked.connect(self.accept)

        # Create a layout for the input window
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Add the labels, line edit, and confirm button to the layout
        layout.addWidget(amenity_label)
        layout.addWidget(self.amenity_lineEdit)
        layout.addWidget(self.confirm_button)
        self.setLayout(layout)

    def return_info(self):
        amenityType = self.amenity_lineEdit.text().title()

        if len(amenityType.strip()) >= 1:
            return [amenityType]
        else:
            show_error_message("BLANK FIELDS, TRY AGAIN")
            return 0

class planAddWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Plan Window")

        # Create labels
        PlanName_label = QLabel("Plan Name:")
        pricing_label = QLabel("Pricing:")

        # Create line edits
        self.planName_lineEdit = QLineEdit()
        self.pricing_lineEdit = QLineEdit()
        self.pricing_lineEdit.setValidator(QIntValidator())
        self.pricing_lineEdit.setMaxLength(5)
        # Create a confirm button
        self.confirm_button = QPushButton("Confirm")
        self.confirm_button.clicked.connect(self.accept)

        # Create a layout for the input window
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Add the labels, line edits, and confirm button to the layout
        layout.addWidget(PlanName_label)
        layout.addWidget(self.planName_lineEdit)
        layout.addWidget(pricing_label)
        layout.addWidget(self.pricing_lineEdit)
        layout.addWidget(self.confirm_button)
        self.setLayout(layout)

    def return_info(self):
        planName = self.planName_lineEdit.text().title()
        pricing = self.pricing_lineEdit.text()

        if len(planName.strip()) >= 1 and len(pricing.strip()) >= 1:
            return [planName, pricing]
        else:
            show_error_message("BLANK FIELDS, TRY AGAIN")
            return 0

class deletePopUp(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Delete")

        self.deleteLabel = QLabel("Confirm Deletion?")
        
        self.confirm_button = QtWidgets.QPushButton("Confirm")
        self.confirm_button.clicked.connect(self.accept)

        layout = QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(self.deleteLabel)
        layout.addWidget(self.confirm_button)
        self.setLayout(layout)

        
class availableAmenitiesPopUp(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Amenities")

        # Create labels
        self.amenities_label = QLabel("Amenities:")
        self.amenitiesComboBox = QComboBox()

        self.confirm_button = QPushButton("Confirm")
        self.confirm_button.clicked.connect(self.accept)

        # Create a layout for the input window
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Add the labels, line edits, and confirm button to the layout
        layout.addWidget(self.amenities_label)
        layout.addWidget(self.amenitiesComboBox)
        layout.addWidget(self.confirm_button)
        self.setLayout(layout)

    def return_info(self):
        if len(self.amenitiesComboBox.currentText()) >= 1:
            return self.amenitiesComboBox.currentText()
        else:
            return 0
            
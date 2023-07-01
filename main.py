from GSIS_GUI import Ui_GSIS, customerAddWindow,  show_error_message, trainerAddWindow, amenityAddWindow, planAddWindow, availableAmenitiesPopUp, deletePopUp
from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt, QDate, QSortFilterProxyModel, QStringListModel
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from datetime import date
import mySQLconnection as mysql


class function(Ui_GSIS):
    def __init__ (self, GSIS):
        Ui_GSIS.setupUi(self, GSIS)
        self.customerPK = []
        self.plansPK = []
        self.trainerPK = []
        self.amenitiesPK = []
        self.modelCustomer = QStandardItemModel()
        self.modelPlans = QStandardItemModel()
        self.modelTrainers = QStandardItemModel()
        self.modelAmenities = QStandardItemModel()
        self.availableAmenitiesModel = QStringListModel()
        self.searchLineInit()
        self.updateCustomerTable()
        self.updatePlansTable()
        self.updateTrainersTable()
        self.updateAmenitiesTable()
        self.customerTable.selectionModel().selectionChanged.connect(self.cellSelectedCustomer)
        self.trainerTable.selectionModel().selectionChanged.connect(self.cellSelectedTrainer)
        self.plansTable.selectionModel().selectionChanged.connect(self.cellSelectedPlan)
        self.amenitiesTable.selectionModel().selectionChanged.connect(self.cellSelectedAmenity)
        self.addButtonCustomer.clicked.connect(self.addCustomerPopUp)
        self.deleteButtonStudent.clicked.connect(self.deleteRowCustomer)
        self.addButtonTrainer_2.clicked.connect(self.addTrainerPopUp)
        self.deleteButtonTrainer_2.clicked.connect(self.deleteRowTrainer)
        self.addAmenitiesButton.clicked.connect(self.addAmenityPopUp)
        self.deleteAmenitiesButton.clicked.connect(self.deleteRowAmenities)
        self.addPlansButton.clicked.connect(self.addPlansPopUp)
        self.deletePlansButton.clicked.connect(self.deleteRowPlans)
        self.customerTable.doubleClicked.connect(self.editCustomerPopUp)
        self.trainerTable.doubleClicked.connect(self.editTrainerPopUp)
        self.plansTable.doubleClicked.connect(self.editPlanPopUp)
        self.amenitiesTable.doubleClicked.connect(self.editAmenityPopUp)
        self.addAvailableAmenities.clicked.connect(self.addAvailableAmenitiesPopUp)
        self.deleteAvailableAmenities.clicked.connect(self.deleteRowAvailableAmenities)


    # Cell Section

    def cellSelectedCustomer(self):
        selected_indexes = self.customerTable.selectedIndexes()
        if not selected_indexes:  # Check if the list is empty
            return
        
        row = selected_indexes[0].row()  # Assume all selected indexes are from the same row
        row_data = []

        for column in range(self.customerTable.model().columnCount()):
            index = self.customerTable.model().index(row, column)
            item = index.data()
            row_data.append(item)

        self.customerPK = row_data
        print(self.customerPK)

    def cellSelectedTrainer(self):
        selected_indexes = self.trainerTable.selectedIndexes()
        if not selected_indexes:
            return
        
        row = selected_indexes[0].row()
        row_data = []

        for column in range(self.trainerTable.model().columnCount()):
            index = self.trainerTable.model().index(row, column)
            item = index.data()
            row_data.append(item)

        self.trainerPK = row_data

    def cellSelectedPlan(self):
        selected_indexes = self.plansTable.selectedIndexes()
        if not selected_indexes:
            return
        
        row = selected_indexes[0].row()
        row_data = []

        for column in range(self.plansTable.model().columnCount()):
            index = self.plansTable.model().index(row, column)
            item = index.data()
            row_data.append(item)

        self.plansPK = row_data
        self.availableAmenitiesLabel.setText(self.plansPK[0].upper())
        data = [item[0] for item in mysql.queryAvailableAmenitiesTable([self.plansPK[0]])]
        print(data)
        self.availableAmenitiesModel.setStringList(data)
        self.listView.setModel(self.filterAvailableAmenitiesModel)

    def cellSelectedAmenity(self):
        selected_indexes = self.amenitiesTable.selectedIndexes()
        if not selected_indexes:
            return
        
        row = selected_indexes[0].row()
        row_data = []

        for column in range(self.amenitiesTable.model().columnCount()):
            index = self.amenitiesTable.model().index(row, column)
            item = index.data()
            row_data.append(item)

        self.amenitiesPK = row_data

    # DUPLICATE CHECKER

    def duplicateCustomerChecker(self, stringVal):
        list = [item[0] for item in mysql.queryCustomerTable()]
        for row in list:
            #print(row)
            if row == stringVal:
                show_error_message("CUSTOMER ID ALREADY EXISTS")
                return True
            
        return False
    
    def duplicateContactNoChecker(self, stringVal):
        list = [item[8] for item in mysql.queryCustomerTable()]
        for row in list:
            #print(row)
            if row == stringVal:
                show_error_message("CONTACT NUMBER ALREADY EXISTS")
                return True
            
        return False


    
    def duplicateTrainerChecker(self, stringVal):
        list = [item[0] for item in mysql.queryTrainersTable()]
        for row in list:
            #print(row, stringVal)
            if stringVal == str(row):
                show_error_message("TRAINER ID ALREADY EXISTS")
                return True
            
        return False

    def duplicateAmenitiesChecker(self, stringVal):
        list = [item[0] for item in mysql.queryAmenitiesTable()]
        for row in list:
            #print(row)
            if row == stringVal:
                show_error_message("AMENITY ALREADY EXISTS")
                return True
            
        return False

    def duplicatePlansChecker(self, stringVal):
        list = [item[0] for item in mysql.queryPlansTable()]
        for row in list:
            #print(row)
            if row == stringVal:
                show_error_message("PLAN ALREADY EXISTS")
                return True
            
        return False

    # Delete function

    def deleteRowCustomer(self):
        if self.customerPK != []:
            popUp = deletePopUp()
            if popUp.exec() == 1:
                mysql.deleteCustomerTableRow(self.customerPK[0])
                self.updateCustomerTable()


    def deleteRowTrainer(self):
        if self.trainerPK != []:
            popUp = deletePopUp()
            if popUp.exec() == 1:
                mysql.deleteTrainersTableRow(self.trainerPK[0])
                self.updateTrainersTable()


    def deleteRowAmenities(self):
        if self.amenitiesPK != []:
            popUp = deletePopUp()
            if popUp.exec() == 1:
                mysql.deleteAmenityTableRow(self.amenitiesPK[0])
                self.updateAmenitiesTable()
                if self.plansPK != []:
                    self.availableAmenitiesLabel.setText(self.plansPK[0].upper())
                    data = [item[0] for item in mysql.queryAvailableAmenitiesTable([self.plansPK[0]])]
                    print(data)
                    self.availableAmenitiesModel.setStringList(data)
                    self.listView.setModel(self.filterAvailableAmenitiesModel)

    def deleteRowPlans(self):

        if self.plansPK != []:
            popUp = deletePopUp()
            if popUp.exec() == 1:
                mysql.deletePlansTableRow(self.plansPK[0])
                self.updatePlansTable()
                self.updateCustomerTable()
                self.updateTrainersTable()
    
    def deleteRowAvailableAmenities(self):

        if self.amenitiesPK != []:
            popUp = deletePopUp()
            if popUp.exec() == 1:
                selected_index = self.listView.currentIndex()
                
                if selected_index.isValid():
                    row = selected_index.row()
                    item_text = self.availableAmenitiesModel.data(self.availableAmenitiesModel.index(row), role= Qt.ItemDataRole.DisplayRole)
                    self.availableAmenitiesModel.removeRow(row)
                    mysql.deleteAvailableAmenities([self.plansPK[0], item_text])
                    self.listView.update()

    # EDIT
    def editCustomerPopUp(self):
        inputWindow = customerAddWindow()
        boolPK = False
        boolContactNo = False

        items = [item[0] for item in mysql.queryPlansTable()]
        for item in items:
            inputWindow.PlanName_combo_box.addItem(item)

        inputWindow.setWindowTitle("Edit Customer Form")
        inputWindow.customerID_lineEdit.setText(self.customerPK[0])
        inputWindow.customerName_lineEdit.setText(self.customerPK[1])
        inputWindow.gender_combo_box.setCurrentText(self.customerPK[2])
        inputWindow.weight_lineEdit.setText(self.customerPK[3])
        inputWindow.height_lineEdit.setText(self.customerPK[4])
        inputWindow.PlanName_combo_box.setCurrentText(self.customerPK[5])
        date_string = self.customerPK[6]  # Example date string
        date = QDate.fromString(date_string, "yyyy-MM-dd") 
        inputWindow.startDate_edit.setDate(date)
        date_string = self.customerPK[7]  # Example date string
        date = QDate.fromString(date_string, "yyyy-MM-dd") 
        inputWindow.endDate_edit.setDate(date)
        inputWindow.contactNo_lineEdit.setText(self.customerPK[8])
        date_string = self.customerPK[9]
        date = QDate.fromString(date_string, "yyyy-MM-dd") 
        inputWindow.birthDate_edit.setDate(date)

        if inputWindow.exec() == 1:
            data = inputWindow.return_info()

            if data == 0:
                return
            data.append(self.customerPK[0])
            print(data)

            if data[0] != self.customerPK[0]:
                #print("SAME CUSTOMER ID")
                boolPK = self.duplicateCustomerChecker(data[0])

            if data[8] != self.customerPK[8]:
                #print("SAME CUSTOMER ID")
                boolContactNo = self.duplicateContactNoChecker(data[8])

            if boolPK != True and boolContactNo != True and data!= 0:
                mysql.updateCustomerTable(data)
                self.updateCustomerTable()

    def editTrainerPopUp(self):
        inputWindow = trainerAddWindow()
        bool = False

        items = [item[0] for item in mysql.queryPlansTable()]
        for item in items:
            inputWindow.PlanName_combo_box.addItem(item)

        inputWindow.setWindowTitle("Edit Trainer Form")
        inputWindow.trainerID_lineEdit.setText(self.trainerPK[0])
        inputWindow.trainerName_lineEdit.setText(self.trainerPK[1])
        inputWindow.PlanName_combo_box.setCurrentText(self.trainerPK[2])

        if inputWindow.exec() == 1:
            data = inputWindow.return_info()

            if data == 0:
                return
            data.append(self.trainerPK[0])
            print(data)

            if data[0] != self.trainerPK[0]:
                #print("SAME TRAINER ID")
                bool = self.duplicateTrainerChecker(data[0])

            if bool != True and data!= 0:
                mysql.updateTrainerTable(data)
                self.updateTrainersTable()

    def editPlanPopUp(self):
        inputWindow = planAddWindow()
        bool = False

        items = [item[0] for item in mysql.queryPlansTable()]

        inputWindow.setWindowTitle("Edit Plan Form")
        inputWindow.planName_lineEdit.setText(self.plansPK[0])
        inputWindow.pricing_lineEdit.setText(self.plansPK[1])

        if inputWindow.exec() == 1:
            data = inputWindow.return_info()

            if data == 0:
                return
            data.append(self.plansPK[0])
            print(data)

            if data[0] != self.plansPK[0]:
                #print("SAME TRAINER ID")
                bool = self.duplicatePlansChecker(data[0])

            if bool != True and data!= 0:
                mysql.updatePlanTable(data)
                self.updatePlansTable()
                self.updateTrainersTable()
                self.updateCustomerTable()
                self.plansPK[0] = data[0]
                self.availableAmenitiesLabel.setText(self.plansPK[0].upper())
   
    
    def editAmenityPopUp(self):
        inputWindow = amenityAddWindow()
        bool = False

        inputWindow.setWindowTitle("Edit Plan Form")
        inputWindow.amenity_lineEdit.setText(self.amenitiesPK[0])
        
        if inputWindow.exec() == 1:
            data = inputWindow.return_info()

            if data == 0:
                return
            data.append(self.amenitiesPK[0])
            print(data)

            if data[0] != self.amenitiesPK[0]:
                #print("SAME TRAINER ID")
                bool = self.duplicateAmenitiesChecker(data[0])

            if bool != True and data!= 0:
                mysql.updateAmenitiesTable(data)
                self.updateAmenitiesTable()
                self.updateAvailableAmenitiesList()
   
    # ADD  

    def addCustomerPopUp(self):
        inputWindow = customerAddWindow()
        items = [item[0] for item in mysql.queryPlansTable()]
        for item in items:
            inputWindow.PlanName_combo_box.addItem(item)


        if inputWindow.exec() == 1:
            data = inputWindow.return_info()
            if data == 0:
                return
            if self.duplicateCustomerChecker(data[0]) != True and data != 0 and self.duplicateContactNoChecker(data[8]) != True:
                mysql.insertCustomerTable(data)
                self.updateCustomerTable()

    def addTrainerPopUp(self):
        inputWindow = trainerAddWindow()

        #Add items to the PlanName combo box
        items = [item[0] for item in mysql.queryPlansTable()]
        inputWindow.PlanName_combo_box.addItems(items)

        if inputWindow.exec() == 1:
            data = inputWindow.return_info()
            print(data)
            if data == 0:
                return
            if self.duplicateTrainerChecker(data[0]) != True and data != 0:
                mysql.insertTrainerTable(data)
                self.updateTrainersTable()

    def addAmenityPopUp(self):
        inputWindow = amenityAddWindow()
        print("PRESSED")

        if inputWindow.exec() == 1:
            data = inputWindow.return_info()
            print(data)
            if data == 0:
                return
            if self.duplicateAmenitiesChecker(data[0]) != True and data != 0:
                mysql.insertAmenitiesTable(data)
                self.updateAmenitiesTable()


    def addPlansPopUp(self):
        inputWindow = planAddWindow()

        if inputWindow.exec() == 1:
            data = inputWindow.return_info()
            print(data)
            if data == 0:
                return
            if self.duplicatePlansChecker(data[0]) != True and data != 0:
                mysql.insertPlanTable(data)
                self.updatePlansTable()

    def addAvailableAmenitiesPopUp(self):

        if not self.plansPK:
            show_error_message("No Plans Selected")
            return 0
        
        inputWindow = availableAmenitiesPopUp()

        items = [item[0] for item in mysql.queryAmenitiesTable()]
        for item in items:
            if item not in self.availableAmenitiesModel.stringList():
                inputWindow.amenitiesComboBox.addItem(item)

        if inputWindow.exec() == 1:
            data = [self.plansPK[0]]
            data.append(inputWindow.return_info())
            print(data)
            if inputWindow.amenitiesComboBox.count() != 0:
                mysql.insertAvailableAmenitiesTable(data)
                self.updateAvailableAmenitiesList()
    
    #UPDATE TABLE

    def updateCustomerTable(self):
            self.modelCustomer.clear()
            self.displayCustomerTable(mysql.queryCustomerTable())
            self.customerTable.setModel(self.filterCustomerModel)

    def updatePlansTable(self):
            self.modelPlans.clear()
            self.displayPlansTable(mysql.queryPlansTable())
            self.plansTable.setModel(self.filterPlansModel)

    def updateTrainersTable(self):
            self.modelTrainers.clear()
            self.displayTrainersTable(mysql.queryTrainersTable())
            self.trainerTable.setModel(self.filterTrainersModel)

    def updateAmenitiesTable(self):
            self.modelAmenities.clear()
            self.displayAmenitiesTable(mysql.queryAmenitiesTable())
            self.amenitiesTable.setModel(self.filterAmenitiesModel)

    def updateAvailableAmenitiesList(self):
            if self.plansPK != []:
                data = [item[0] for item in mysql.queryAvailableAmenitiesTable([self.plansPK[0]])]
                print(data)
                self.availableAmenitiesModel.setStringList(data)

    # DISPLAY TABLE

    def displayCustomerTable(self, rows):
        # Set the column headers
        headers = ["CustomerID", "Name", "Gender", "Weight (kg)", "Height (cm)", "PlanName", "StartDate", "EndDate", "ContactNo", "BirthDate", "Age"]
        self.modelCustomer.setHorizontalHeaderLabels(headers)
        self.customerTable.setColumnWidth(1,300)
        for row in rows:
            #print(row)
            item_row = []
            for value in row:
                item = QStandardItem(str(value))
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                item_row.append(item)
            self.modelCustomer.appendRow(item_row)
        return self.modelCustomer
    
    def displayPlansTable(self, rows):
        # Set the column headers
        headers = ["PlanName", "Pricing"]
        self.modelPlans.setHorizontalHeaderLabels(headers)
        self.plansTable.setColumnWidth(1,474)
        for row in rows:
            print(row)
            item_row = []
            for value in row:
                item = QStandardItem(str(value))
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                item_row.append(item)
            self.modelPlans.appendRow(item_row)
        return self.modelPlans

    def displayTrainersTable(self, rows):
        # Set the column headers
        headers = ["TrainerID", "Name", "PlanName"]
        self.modelTrainers.setHorizontalHeaderLabels(headers)
        self.trainerTable.setColumnWidth(1,932)
        for row in rows:
            #print(row)
            item_row = []
            for value in row:
                item = QStandardItem(str(value))
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                item_row.append(item)
            self.modelTrainers.appendRow(item_row)
        return self.modelTrainers
    
    def displayAmenitiesTable(self, rows):
        # Set the column headers
        headers = ["Amenity"]
        self.modelAmenities.setHorizontalHeaderLabels(headers)
        self.amenitiesTable.setColumnWidth(0,1200)
        for row in rows:
            print(row)
            item_row = []
            for value in row:
                item = QStandardItem(str(value))
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                item_row.append(item)
            self.modelAmenities.appendRow(item_row)
        return self.modelCustomer

    # SEARCH

    def searchLineInit(self):
        self.filterCustomerModel = MultiColumnFilterProxyModel()
        self.filterCustomerModel.setSourceModel(self.modelCustomer)
        self.customerTable.setModel(self.filterCustomerModel)
        self.customerLineEdit.textChanged.connect(self.filterCustomerModel.setSearchText)

        self.filterPlansModel = MultiColumnFilterProxyModel()
        self.filterPlansModel.setSourceModel(self.modelPlans)
        self.plansTable.setModel(self.filterPlansModel)
        self.PlansLineEdit_3.textChanged.connect(self.filterPlansModel.setSearchText)

        self.filterTrainersModel = MultiColumnFilterProxyModel()
        self.filterTrainersModel.setSourceModel(self.modelTrainers)
        self.trainerTable.setModel(self.filterTrainersModel)
        self.trainertLineEdit_2.textChanged.connect(self.filterTrainersModel.setSearchText)

        self.filterAmenitiesModel = MultiColumnFilterProxyModel()
        self.filterAmenitiesModel.setSourceModel(self.modelAmenities)
        self.amenitiesTable.setModel(self.filterAmenitiesModel)
        self.amenitiesButtonLineEdit.textChanged.connect(self.filterAmenitiesModel.setSearchText)

        self.filterAvailableAmenitiesModel = QSortFilterProxyModel()
        self.filterAvailableAmenitiesModel.setSourceModel(self.availableAmenitiesModel)
        self.filterAmenitiesModel.setFilterKeyColumn(0)
        self.availableAmenitiesSearch.textChanged.connect(self.filterAvailableAmenitiesModel.setFilterRegularExpression)

#MISC
    
class MultiColumnFilterProxyModel(QSortFilterProxyModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.searchText = ""

    def setSearchText(self, searchText):
        self.searchText = searchText
        self.invalidateFilter()

    def filterAcceptsRow(self, sourceRow, sourceParent):
        if not self.searchText:
            return True

        model = self.sourceModel()
        rowCount = model.columnCount()
        for column in range(rowCount):
            text = model.data(model.index(sourceRow, column), Qt.ItemDataRole.DisplayRole)
            if self.searchText.lower() in text.lower():
                return True

        return False

def calculate_age(date_string):
    # Convert the date string to a date object
    birth_date = date.fromisoformat(date_string)

    # Get the current date
    current_date = date.today()

    # Calculate the age
    age = current_date.year - birth_date.year

    # Adjust the age if the current date hasn't reached the birth month and day yet
    if current_date.month < birth_date.month or (current_date.month == birth_date.month and current_date.day < birth_date.day):
        age -= 1

    return age

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GSIS = QtWidgets.QMainWindow()
    ui = function(GSIS)
    app.aboutToQuit.connect(mysql.closeConnection)
    GSIS.show()
    sys.exit(app.exec())


from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector


class Ui_GSIS(object):
    def __init__(self):
        # Existing code for UI setup

        self.addButtonmember.clicked.connect(self.add_member)
        self.addButtonmember_2.clicked.connect(self.edit_member)
        self.deleteButtonmember.clicked.connect(self.delete_member)

        # Establish MySQL connection
        self.connection = mysql.connector.connect(
            host='localhost',
            user='your_username',
            password='your_password',
            database='your_database'
        )
        self.cursor = self.connection.cursor()

    def add_member(self):
        member_id = self.memberLineEdit.text()
        member_name = self.memberLineEdit_2.text()
        member_age = self.memberLineEdit_3.text()

        # Perform database operation to add member
        query = "INSERT INTO members (id, name, age) VALUES (%s, %s, %s)"
        values = (member_id, member_name, member_age)
        self.cursor.execute(query, values)
        self.connection.commit()

        # Refresh the table view to reflect changes
        self.refresh_member_table()

    def edit_member(self):
        selected_row = self.memberTable.selectionModel().selectedRows()
        if selected_row:
            member_id = self.memberTable.model().index(selected_row[0].row(), 0).data()
            member_name = self.memberLineEdit_2.text()
            member_age = self.memberLineEdit_3.text()

            # Perform database operation to update member
            query = "UPDATE members SET name = %s, age = %s WHERE id = %s"
            values = (member_name, member_age, member_id)
            self.cursor.execute(query, values)
            self.connection.commit()

            # Refresh the table view to reflect changes
            self.refresh_member_table()

    def delete_member(self):
        selected_row = self.memberTable.selectionModel().selectedRows()
        if selected_row:
            member_id = self.memberTable.model().index(selected_row[0].row(), 0).data()

            # Perform database operation to delete member
            query = "DELETE FROM members WHERE id = %s"
            values = (member_id,)
            self.cursor.execute(query, values)
            self.connection.commit()

            # Refresh the table view to reflect changes
            self.refresh_member_table()

    def refresh_member_table(self):
        # Retrieve member data from the database
        query = "SELECT * FROM members"
        self.cursor.execute(query)
        member_data = self.cursor.fetchall()

        # Update the table view with the retrieved data
        model = QtGui.QStandardItemModel()
        model.setColumnCount(3)
        model.setHorizontalHeaderLabels(["ID", "Name", "Age"])
        for row, data in enumerate(member_data):
            for column, item in enumerate(data):
                model.setItem(row, column, QtGui.QStandardItem(str(item)))

        self.memberTable.setModel(model)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GSIS = QtWidgets.QMainWindow()
    ui = Ui_GSIS()
    ui.setupUi(GSIS)
    GSIS.show()
    sys.exit(app.exec())

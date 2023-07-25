import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QLineEdit, QHBoxLayout, QCheckBox
from PyQt6.QtCore import Qt
from typing import List
import json
from agreement import Agreement
import time


class MyApp(QMainWindow):
    def __init__(self, path):
        super().__init__()

        self.setWindowTitle("Agreement Editor")
        self.setGeometry(100, 100, 2500, 600)
        self.agreement_list = []
        with open(path, 'r') as f:
            contents = json.loads(f.read())
        for content in contents:
            self.agreement_list.append(Agreement(**content))


        self.init_ui()

    def init_ui(self):
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()
        self.filter_layout = QHBoxLayout()

        self.filter_box = QLineEdit(self)
        self.filter_box.setPlaceholderText("Filter")
        self.filter_box.textChanged.connect(self.filter_table)
        self.filter_layout.addWidget(self.filter_box)

        self.table_widget = QTableWidget(self.central_widget)
        layout.addLayout(self.filter_layout)
        layout.addWidget(self.table_widget)

        header_labels = list(vars(self.agreement_list[0]).keys())
        self.table_widget.setColumnCount(len(header_labels))
        self.table_widget.setHorizontalHeaderLabels(header_labels)

        self.load_data()

        self.central_widget.setLayout(layout)
        self.table_widget.cellChanged.connect(self.update_data)


    def load_data(self):
        self.table_widget.setRowCount(len(self.agreement_list))

        for row, agreement_instance in enumerate(self.agreement_list):
            for col, (attr_name, attr_value) in enumerate(vars(agreement_instance).items()):
                if isinstance(attr_value, bool):
                    checkbox = QCheckBox()
                    checkbox.setChecked(attr_value)
                    checkbox.stateChanged.connect(lambda state, row=row, col=col: self.update_data(row, col))
                    self.table_widget.setCellWidget(row, col, checkbox)
                else:
                    item = QTableWidgetItem(str(attr_value)) if attr_value is not None else QTableWidgetItem("")
                    self.table_widget.setItem(row, col, item)

    def update_data(self, row, column):
        if isinstance(self.table_widget.cellWidget(row, column), QCheckBox):
            checkbox = self.table_widget.cellWidget(row, column)
            new_value = checkbox.isChecked()
        else:
            item = self.table_widget.item(row, column)
            new_value = item.text()

        setattr(self.agreement_list[row], list(vars(self.agreement_list[0]).keys())[column], new_value)

        #TODO: more efficient!
        agreements = []
        for agreement in self.agreement_list:
            agreements.append(agreement.__dict__)
        with open('edgg_loas', 'w') as fout:
            json.dump(agreements, fout, indent=0)

    def filter_table(self):
        filter_text = self.filter_box.text().strip().lower()

        for row in range(self.table_widget.rowCount()):
            row_data = [self.table_widget.item(row, col).text().lower() if not isinstance(self.table_widget.cellWidget(row, col), QCheckBox)
                        else str(self.table_widget.cellWidget(row, col).isChecked()) for col in range(self.table_widget.columnCount())]

            show_row = any(filter_text in data for data in row_data)
            self.table_widget.setRowHidden(row, not show_row)

def main():
    app = QApplication(sys.argv)
    window = MyApp('edgg_loas')
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

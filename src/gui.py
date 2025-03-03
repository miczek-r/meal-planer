from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt
from schedule_utils import load_groups, load_data, generate_schedule
from pdf_generator import save_as_pdf
from datetime import datetime
import sys
import os
import subprocess

def generate_button_click(month_combobox, year_entry):
    try:
        data = load_data("data.json")

        month = month_combobox.currentText()
        year = int(year_entry.text())
        month_num = list(data["months"].values()).index(month) + 1

        groups = load_groups('groups.json')["groups"]
        days, month_name, html_content = generate_schedule(month_num, year, groups, data)

        output_pdf = f'schedule_{month_num}_{year}.pdf'
        save_as_pdf(html_content, output_pdf)

        QMessageBox.information(None, "Sukces", f"Harmonogram został zapisany jako {output_pdf}")
        
        if sys.platform == "win32":
            os.startfile(output_pdf)  # For Windows
        elif sys.platform == "darwin":
            subprocess.run(["open", output_pdf])  # For macOS
        else:
            subprocess.run(["xdg-open", output_pdf])  # For Linux

    except Exception as e:
        QMessageBox.critical(None, "Błąd", f"Wystąpił błąd: {str(e)}")


def run_gui():
    data = load_data("data.json")

    current_year = datetime.now().year
    current_month = datetime.now().strftime('%B')

    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("Meal Planner")
    window.setFixedSize(300, 100)

    layout = QVBoxLayout()

    year_layout = QHBoxLayout()
    year_label = QLabel("Wybierz rok:")
    year_layout.addWidget(year_label)
    year_entry = QLineEdit(str(current_year))
    year_layout.addWidget(year_entry)
    layout.addLayout(year_layout)

    month_layout = QHBoxLayout()
    month_label = QLabel("Wybierz miesiąc:")
    month_layout.addWidget(month_label)
    month_combobox = QComboBox()
    month_combobox.addItems(list(data["months"].values()))
    month_combobox.setCurrentText(current_month)
    month_layout.addWidget(month_combobox)
    layout.addLayout(month_layout)

    generate_button = QPushButton("Generuj Harmonogram")
    generate_button.clicked.connect(lambda: generate_button_click(month_combobox, year_entry))
    layout.addWidget(generate_button)

    window.setLayout(layout)
    
    window.show()

    sys.exit(app.exec_())

import pdfkit
import os
import sys

def save_as_pdf(html_content, output_file):
    if getattr(sys, 'frozen', False):
        application_path = sys._MEIPASS
    else:
        application_path = os.path.abspath("")

    wkhtmltopdf_path = os.path.join(application_path, 'assets', "wkhtmltox", "bin", "wkhtmltopdf.exe")
    config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)
    pdfkit.from_string(html_content, output_file, configuration=config, options={"orientation": "Landscape", "page-size": "A4"})

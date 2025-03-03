import json
import os
import sys
import calendar
from datetime import datetime
from jinja2 import Template

def load_data(data_file="data.json"):
    if getattr(sys, 'frozen', False):
        application_path = sys._MEIPASS
    else:
        application_path = os.path.abspath("")

    data_path = os.path.join(application_path, 'data', data_file)
    
    with open(data_path, "r", encoding="utf-8") as file:
        return json.load(file)

def load_groups(json_file="groups.json"):
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    else:
        application_path = os.path.abspath(".")

    json_path = os.path.join(application_path, json_file)
    
    if os.path.exists(json_path):
        with open(json_path, "r", encoding="utf-8") as file:
            return json.load(file)
    else:
        raise FileNotFoundError(f"{json_file} not found.")


def generate_schedule(month, year, groups, data):
    months = data["months"]
    weekdays = data["weekdays"]

    days = [(datetime(year, month, d).strftime("%A"), d) for d in range(1, calendar.monthrange(year, month)[1] + 1)]
    days = [(weekdays[day_name], day) for day_name, day in days]

    month_name = months.get(str(month), datetime(year, month, 1).strftime("%B"))

    if getattr(sys, 'frozen', False):
        application_path = sys._MEIPASS
    else:
        application_path = os.path.abspath(".")

    template_path = os.path.join(application_path, 'assets', 'template.html')

    with open(template_path, 'r', encoding='utf-8') as file:
        template = Template(file.read())

    html_content = template.render(days=days, groups=groups, month_name=month_name, year=year)

    return days, month_name, html_content


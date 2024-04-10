import csv
from flask import Flask, url_for, render_template, request, session, redirect, flash
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = '123456789'

class TripInfo:
    def __init__(self, trip_name, email, description, completness, contact_ok):
        self.trip_name = trip_name
        self.email = email
        self.description = description
        self.completness = completness
        self.contact_ok = contact_ok

class SaveData:
    def read_csv_data(self):
        full_file_path = os.path.join(app.static_folder, 'trips.txt')
        fieldnames = ['trip_name', 'email', 'description', 'completness', 'contact_ok']
        entries = []
        with open(full_file_path, mode='r', encoding='utf-8') as f:
            csv_reader = csv.DictReader(f, fieldnames=fieldnames)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    entries.append(row)
                line_count += 1
        return entries

    def append_csv_data(self):
        full_file_path = os.path.join(app.static_folder, 'trips.txt')
        fieldnames = ['trip_name', 'email', 'description', 'completness', 'contact_ok']

        if not os.path.exists(full_file_path):
            with open(full_file_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)

            with open(full_file_path, 'a', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writerow(data)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_new_trip', methods = ['GET', 'POST'])
def add_new_trip():
    if request.method == 'GET':
        return render_template('add_new_trip.html')
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
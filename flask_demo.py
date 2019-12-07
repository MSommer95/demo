from __future__ import division
from datetime import datetime
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


def get_calendar_week(date):
    return date.isocalendar()[1]


def get_day(day_number):
    days = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag']
    return days[day_number]


@app.route('/')
def home():
    current_date = datetime.now()
    return render_template('index.html', current_calendar_week=get_calendar_week(current_date),
                           current_date=current_date.strftime('%d.%m.%Y') + ' %s' % get_day(current_date.weekday()))


@app.route('/my_week/', methods=['POST'])
def my_week():
    date_to_check = request.form['date_to_check']
    if not date_to_check:
        return redirect('/')
    date_obj = datetime.strptime(date_to_check, '%Y-%m-%d')
    return render_template('index.html', current_calendar_week=get_calendar_week(date_obj),
                           current_date=date_obj.strftime('%d.%m.%Y') + ' %s' % get_day(date_obj.weekday()))


if __name__ == "__main__":
    app.run()

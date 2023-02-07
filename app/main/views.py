import json
import flask
from app import app
from flask import render_template
from public_method.date_calculator import DateCalculator


# 时间计算接口
@app.route('/application/dateCalculator', methods=['GET'])
def person_add():
    # 1. 获取时间参数
    param_dic = flask.request.args
    start_date = param_dic["start_date"]
    end_date = param_dic["end_date"]
    interval_date = DateCalculator.calculate_date(start_date=start_date, end_date=end_date)
    return json.dumps(interval_date)


@app.route('/bootstrap/<name>')
def flask_bootstrap_test(name):
    return render_template('login_bootstrap.html', name=name)

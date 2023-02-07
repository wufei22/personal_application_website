# from config import Config
from flask import Flask
# from .models import db
from flask_bootstrap import Bootstrap
import urllib3

app = Flask(__name__)

bootstrap = Bootstrap(app)

# 引入配置信息
# try:
# app.config.from_object(Config)

# db绑定app
# db.init_app(app)
# db.app = app
# db.create_all()

# except Exception as e:
#     print(e)
# db.make_connector()
urllib3.disable_warnings()
from .main import views




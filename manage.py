#!/usr/bin/env python
from app import app
# from flask_script import Manager, Server
# from flask_migrate import Migrate, MigrateCommand
# from app.models import db
# import logging
# from logging.handlers import TimedRotatingFileHandler


# 定义开启服务的主函数
def live_main():
    app.debug = False
    app.config["JSON_AS_ASCII"] = False
    # formatter = logging.Formatter(
    #     "[%(asctime)s][%(filename)s:%(lineno)d][%(levelname)s][%(thread)d] - %(message)s")
    # handler = TimedRotatingFileHandler(
    #     "flask.log", when="D", interval=1, backupCount=5,
    #     encoding="UTF-8", delay=False, utc=True)
    # app.logger.addHandler(handler)
    # handler.setFormatter(formatter)
    # manager = Manager(app)
    # Migrate(app=app, db=db)
    # manager.add_command('db', MigrateCommand)  # 创建数据库映射命令
    # manager.add_command('start', Server(port=5080, threaded=True))  # 创建启动命令
    app.run(host='0.0.0.0', port=5080, threaded=True)


if __name__ == '__main__':
    live_main()


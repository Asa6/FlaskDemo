import os
from flask import Flask
from flask_migrate import Migrate


from .models import db
# 需要将model导入，否则flask db xxxx 无法使用
from .models import user, cmdb

migrate = Migrate()


def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('settings.Config')


    # if config is None:
    #     # load the instance config, if it exists, when not testing
    #     app.config.from_pyfile('settings.py', silent=True)
    # else:
    #     # load the test config if passed in
    #     app.config.from_mapping(config)
    #
    # # ensure the instance folder exists
    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass

    db.init_app(app)
    migrate.init_app(app, db)


    # 注册蓝图
    from .views import (
        cmdb, user
    )
    app.register_blueprint(cmdb.bp)
    app.register_blueprint(user.bp)


    return app

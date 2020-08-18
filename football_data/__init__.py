import os

import click
from flask import Flask

from football_data.blueprints.auth import auth_bp
from football_data.blueprints.football_data import football_data_bp
from football_data.extensions import db, migrate
from football_data.setting import config
from football_data.models import User

def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')
    
    app = Flask('football_data')
    app.config.from_object(config[config_name])

    register_extensions(app)
    register_blueprints(app)
    register_shell_context(app) 
    register_commands(app)
    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)



def register_blueprints(app):
    app.register_blueprint(football_data_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')


def register_shell_context(app):
    """注册 shell 上下文对象

    使用 make_shell_context 函数注册上下文对象

    Args:
        app: Flask 对象

    """
    @app.shell_context_processor
    def make_shell_context():
        """向 shell 中传入数据库对象

        使用 shell_context_processor 装饰器传入数据库对象

        Returns:
            以{ 'db': db }传回数据库对象db
        """
        return dict(db=db)


def register_commands(app):
    @app.cli.command()
    @click.option('--drop', is_flag=True, help='Create after drop')
    def initdb(drop):
        """Initialize the database.

        Args:
            drop: 可选参数，如果为True,则删除数据库中的数据
        """
        if drop:
            click.confirm(
                'This operation will delete the database, '
                'do you want to continue?',
                abort=True
            )
            db.drop_all()
            click.echo('Drop tables.')
        db.create_all()
        click.echo('Initialized database.')

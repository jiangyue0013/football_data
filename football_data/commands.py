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



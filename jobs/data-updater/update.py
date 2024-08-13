"""Data importer job"""
import asyncio

from data_updater.worker import create_app, run

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        asyncio.run(run(app))

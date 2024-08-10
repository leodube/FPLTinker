"""Data importer job"""
import asyncio

from data_updater.worker import create_app, run

if __name__ == '__main__':
    app = create_app()
    try:
        event_loop = asyncio.get_event_loop()
        event_loop.run_until_complete(run(app))
    except Exception as err:
        raise err
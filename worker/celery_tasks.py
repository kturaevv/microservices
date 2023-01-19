from .celery_worker import app

from celery import Task

import time, logging, requests, sys

FORMAT = '%(asctime)s - %(levelname)s: %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO, handlers=[logging.StreamHandler(sys.stdout)])


class BaseTask(Task):
    """ Genereric base task for all tasks. """
    ...

class CustombaseTask(Task):
    """ Base tasks for use inside of tasks. """
    _custom = None

    @property
    def custom(self):
        if self._custom is None:
            self._custom = "This is custom property."
        return self._custom


@app.task(base=CustombaseTask)
def custom_base():
    return custom_base.custom

@app.task(name='test')
def test_task(complexity):
    time.sleep(int(complexity))
    return {"Success":complexity}

@app.task
def process_img(image_path):
    logging.info("[celery] Received %r" % image_path)
    requests.get("http://app:8000/")
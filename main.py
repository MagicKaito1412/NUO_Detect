import os
import multiprocessing as mp
import time


def start_flask(cmd):
    os.system("python " + cmd)


if __name__ == '__main__':
    flask_apps = [
        'backend/db_module/run.py runserver',
        'backend/model_training/run.py',
        'backend/nuo_prediction/run.py'
    ]
    queues = []
    processes = []
    for app in flask_apps:
        p = mp.Process(target=start_flask, args=(app,))
        processes.append(p)
        p.start()

    while True:
        try:
            pass
        except KeyboardInterrupt:
            for p in processes:
                p.terminate()
                p.join()
            raise KeyboardInterrupt

import sys
import os
sys.path.append(os.path.sep.join(sys.path[0].split(sep=os.path.sep)[:-2]))

from backend.model_training import app

if __name__ == '__main__':
    app.run('127.0.0.1', '5010')

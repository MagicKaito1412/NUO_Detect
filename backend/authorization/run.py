import sys
import os
sys.path.append(os.path.sep.join(sys.path[0].split(sep=os.path.sep)[:-2]))

from backend.authorization import app

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5005')

from . import service
from run import app


@app.route('/train', methods=['GET'])
def train():
    service.train()


from . import service
from app import app


@app.route('/train', methods=['GET'])
def train():
    service.train()


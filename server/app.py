from flask import Flask
from flask_cors import CORS
from router import use_router
# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

use_router(app)

if __name__ == '__main__':
    app.run()
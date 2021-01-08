from xls2db import xls2db

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base


def create_app() -> Flask:
    
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.url_map.strict_slashes = False
    
    # load_dotenv(find_dotenv())
    
    from app.database.sqlalchemy_extension import db
    db.init_app(app)
    
    from app.apis import api
    api.init_app(app)
    
    return app

application = create_app()

if __name__ == "__main__":
    application.run(port=5000)
from flask import request, Response
import requests
import json
from flask_restplus import Api, Resource, Namespace, fields, Model
from app.database.sqlalchemy_extension import db

study_ns = Namespace('study', description='Functions related to learning content')

@study_ns.route('/')
class FetchContent(Resource):
    
    def get(self):    
        learn = db.Table('Learn', db.metadata, autoload=True, autoload_with=db.engine)
        study_data = db.session.query(learn).all()

        data = list()
        for content in study_data:
            json_data = {
                "id": content.Sno,
                "grade": content.Grade,
                "subject": content.Subject,
                "topic": content.Topic
            }
            data.append(json_data)
            
            # print(type(author.__dict__))
        return {"content":data}, 200
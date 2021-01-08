from flask_restplus import Api

from .study import study_ns as ns1

api = Api(
    title='Educational-App',
    version='0.1.0',
    description='Study from home',
)

api.add_namespace(ns1)

from flask import Flask
from flask_restful import Resource,Api

app=Flask(__name__)
api=Api(app)

class Student(Resource):#inheriting the base class Resource
    def get(self,name):
        return {'Student':name}

api.add_resource(Student,'/student/<string:name>')

app.run()
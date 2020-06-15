from flask import Flask,request
from flask_restful import Resource,Api
from flask_jwt import JWT,jwt_required

from security import authenticate,identity

app=Flask(__name__)
app.secret_key='sk'
api=Api(app)

items=[]

jwt=JWT(app,authenticate,identity)

class Store(Resource):
    @jwt_required()
    def get(self,name):
        item=next(filter(lambda x: x['item_name']==name,items),None)
        return {'item':item}, 200 if item else 404 #ternary operator 

    def post(self,name):
        if next(filter(lambda x: x['item_name']==name,items),None):#checking 
            return {"message":f'item with name {name} exists'},400 #not the problem of application but client to send same name item hence 400 error code (bad request)


        request_data=request.get_json()
        item={'item_name':name,'price':request_data['price']}
        items.append(item)
        return item,201 #201 status code for creation (202 accepted delayed creation) 

    def delete(self,name):
        global items
        items=list(filter(lambda x: x['item_name']!=name,items))
        return {"message":"item deleted!"}


class ItemList(Resource):
    def get(self):
        return {'Items':items},200

api.add_resource(Store,'/item/<string:name>')#on the same resource we are creating several endpoints on the same url
api.add_resource(ItemList,'/items')

app.run(debug=True)


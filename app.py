from flask import Flask,jsonify,request,render_template

#sets a unique name to the page
app=Flask(__name__)


stores=[
    {'storeName':'seven 11',
    
    'items':[
        {
            'item_name':'chair',
            'quantity':40,
            'price':44.0
        }
    ]

    }

]

#exposing endpoints of the website / ie homepage
@app.route('/')
def homepage():
    return render_template('index.html')


#endpoint to return the list of all stores present
@app.route('/stores')
def get_stores():
    return jsonify({'stores':stores})

#endpoint to add a new store 
@app.route('/addstore',methods=['POST'])
def add_store():
    request_data=request.get_json()#the request.get_json() will convert the json string to a python dictionary
    new_store={
        'storeName':request_data['storeName'],
        'items':[]
    }
    stores.append(new_store)
    return jsonify({'stores':stores})

#endpoint to get store details after iterating through all the stores
@app.route('/store/<string:storename>')
def get_store_details(storename):
    for i in stores:
        if i['storeName']==storename:
            return jsonify(i)#can directly return i as i is a dictionary itself.
    return jsonify({'message':'Error store not found!!!!!'})

#endpoint to get specific item from store
@app.route('/store/<string:storename>/<string:itemname>')
def get_store_item(storename,itemname):
    for store in stores:
        if store['storeName']==storename:
            for item in store['items']:
                if item['item_name']==itemname:
                    return jsonify(item)
            return jsonify({'message':'Item not present in store'})
    return jsonify({'message':'Store not found!'})

#endpoint to get all the items from a particular store
@app.route('/store/<string:storename>/item')
def get_store_items(storename):
    for store in stores:
        if store['storeName']==storename:
            return jsonify({'item_list':store['items']})
    return jsonify({'message':'store not found!'})


#endpoint to add a new item to the store
@app.route('/store/<string:storename>/additem',methods=['POST'])
def add_items_to_store(storename):
    request_data=request.get_json()
    for store in stores:
        if store['storeName']==storename:
           new_item={
               'item_name':request_data['item_name'],
                'quantity':request_data['quantity'],
                 'price':request_data['price']
           }
           store['items'].append(new_item)
           return jsonify(store)
    return jsonify({'message':'Store not found!'})
app.run(port=4000,debug=True)



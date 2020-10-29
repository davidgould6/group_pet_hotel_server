# Where our server requests will be

#flask imports
from flask import Flask, request, jsonify
#import con from connectionFunction.py
from connFunction import con
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello World'


@app.route('/pets', methods=['GET', 'POST'])
def get_pets():
  if (request.method == 'GET'):
    querytext = 'SELECT "pets"."id", "pets"."petName", "pets"."breed", "pets"."color", "pets"."isCheckedIn", "owners"."name" AS "ownerName" FROM "pets" JOIN "owners" ON "pets"."owner_id" = "owners"."id";'
    cur = con.cursor()
    cur.execute(querytext)
    rows = cur.fetchall()
    print(rows)
    return jsonify(rows), 201

  elif (request.method == 'POST'):
    content = request.json
    print('hopefully this is content?', content)
    print('is this our pet info', content["owner_id"], content["petName"], content["breed"], content["color"],)
    querytext = 'INSERT INTO "pets" ("owner_id", "petName", "breed", "color") VALUES (%s, %s, %s, %s);'
    cur = con.cursor()
    # executes query with sanitization
    cur.execute(querytext, (content["owner_id"], content["petName"], content["breed"], content["color"],))
    # commits changes to the table in the db
    con.commit()
    # closes connection. 
    cur.close()
    # returns 'created' and 201 status code
    return 'created', 201

@app.route('/pets/<id>', methods=['DELETE', 'PUT'])
def pets_delete_put(id):
  if (request.method == 'DELETE'):
    petId = id
    querytext = 'DELETE FROM "pets" WHERE "id" = %s;'
    cur = con.cursor()
    cur.execute(querytext, (petId))
    con.commit()
    cur.close()
    return 'Deleted', 201
  elif (request.method == 'PUT'):
    cur = con.cursor()
    petId = id
    content = request.json["checkedStatus"]
    if (content == "in"):
      querytext = 'UPDATE "pets" SET "isCheckedIn" = TRUE WHERE "id" = %s;'
      cur.execute(querytext, (petId))
      con.commit()
      cur.close()
      return 'updated', 201
    elif (content == "out"):
      querytext = 'UPDATE "pets" SET "isCheckedIn" = FALSE WHERE "id" = %s;'
      cur.execute(querytext, (petId))
      con.commit()
      cur.close()
      return 'updated', 201



@app.route('/owners', methods=['GET', 'POST'])
def get_owners():
  #if request from client is 'GET' run this code block
  if (request.method == 'GET'):
    # querytext to execute
    querytext = 'SELECT "owners"."id", "owners"."name", COUNT("pets"."owner_id") FROM "pets" JOIN "owners" ON "owners"."id" = "pets"."owner_id" GROUP BY "owners"."id";'
    # creating cursor
    cur = con.cursor()
    # executing query
    cur.execute(querytext)
    # fetching all data from db and declaring as rows
    rows = cur.fetchall()
    # print rows to make sure this data is correct
    print(rows)
    # using flask built in jsonify to send data via json data type and 201 code.
    return jsonify(rows), 201

    # if request from client is 'POST' run this code block
  elif (request.method == 'POST'):
    # declares content to be the data from client that is sent over
    content = request.json
    # print testing that this is our data/content
    print('hopefully this is content?', content)
    print('is this our name?', content["name"])
    # querytext to execute
    querytext = 'INSERT INTO "owners" ("name") VALUES (%s);'
    # creates a new cursor
    cur = con.cursor()
    # executes query with sanitization
    cur.execute(querytext, (content["name"],))
    # commits changes to the table in the db
    con.commit()
    # closes connection. 
    cur.close()
    # returns 'created' and 201 status code
    return 'created', 201
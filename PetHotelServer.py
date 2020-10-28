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
  if request.method == 'GET':
    querytext = 'SELECT "pets"."id", "pets"."petName", "pets"."breed", "pets"."color", "pets"."isCheckedIn", "owners"."name" AS "ownerName" FROM "pets" JOIN "owners" ON "pets"."owner_id" = "owners"."id";'
    cur = con.cursor()
    cur.execute(querytext)
    rows = cur.fetchall()
    print(rows)
  return 'Pets'
import psycopg2
import psycopg2.extras

# Connect to db. line 8 allows data to come back as an array with objects inside
# Found from https://www.psycopg.org/docs/extras.html
con = psycopg2.connect(
  "dbname=pet_hotel user=davidgould host=localhost", 
  cursor_factory=psycopg2.extras.RealDictCursor)
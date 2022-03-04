#Web Service XML/JSON
import json
data = '''
  [
    { "id" : "001",
      "x" : "2",
     "name" : "Quincy"
    } ,
    { "id" : "009",
      "x" : "7",
      "name" : "Mrugesh"
    }
  ]
'''
info = json.loads(data)
for item in info:
  print('id:', item["id"])
  print('X:', item["x"])
  print('Name:', item["name"])
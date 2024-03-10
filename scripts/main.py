from flask import Flask, request, jsonify,render_template
import json
import db_helper
app = Flask(__name__)



@app.route("/", methods=["POST"])
# def index():
#    if request.method == "POST":
#       return render_template("index.html")
      

def handle_request():
    # Get payload
    payload = request.json
 

    # Get info from payload
    
    intent = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']
    print(intent)

    if intent == "Get.water":
        return jsonify({
  "fulfillmentMessages": [
    {
      "text": {
        "text": [
          "Sure here is some water for you "
        ]
      }
      }
  ]
})
    
    if intent == "get-doctor":
        return get_doctor()
    if intent == "get-nurse":
        return get_nurse()
    # if intent == "Nurse_complete":
    #    return nurse_done()
    # if intent == "doctor_done":
    #    parameters['ID']
    #    return doctor_done()


def get_doctor():
      
  doc_name = db_helper.fetch_doctor()

  if doc_name:
      db_helper.update_doctor_status(doc_name[0])
      return jsonify({
  "fulfillmentMessages": [
      {
        "text": {
          "text": [
            f"Sure, I'll get Doctor {doc_name[0]}"
          ]
        }
      }
    ]
})
    
  else:
      return jsonify({
  "fulfillmentMessages": [
      {
        "text": {
          "text": [
            f"Sorry could not find any doctor at this moment"
          ]
        }
      }
    ]
})
  
def get_nurse():
    nurse_name = db_helper.fetch_nurse()
    if nurse_name:
      db_helper.update_nurse_status(nurse_name[0])
      return jsonify({
  "fulfillmentMessages": [
      {
        "text": {
          "text": [
            f"Sure, I'll get nurse {nurse_name[0]}"
          ]
        }
      }
    ]
})
    
    else:
      return jsonify({
  "fulfillmentMessages": [
      {
        "text": {
          "text": [
            f"Sorry could not find any nurse at this moment"
          ]
        }
      }
    ]
})
    
# def nurse_done(nurse_name,nurse_id):
#   db_helper.complete_nurse(nurse_id)
#   return jsonify({
#   "fulfillmentMessages": [
#       {
#         "text": {
#           "text": [
#             f"{nurse_name} status updated"
#           ]
#         }
#       }
#     ]
# })

def doctor_done(doc_id):
  db_helper.complete_doctor(doc_id)
  return jsonify({
  "fulfillmentMessages": [
      {
        "text": {
          "text": [
            "status updated"
          ]
        }
      }
    ]
})
         


if __name__ == "__main__":
    app.run(debug =True)

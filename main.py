from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/api/days/<int:num_days>", methods=['GET'])
def get_days(num_days: int):
    user_data_file = open("user_data.txt", "r")
    lines = user_data_file.readlines()
    user_data_file.close()
    user_info = lines[0]

    if len(lines) == 0:
        return jsonify({"error": "No user created"})

    if len(lines) == 1:
        return jsonify({})

    lines = lines[1:][-5:]
    lines.reverse() # We want the most recent lines first.

    user_data = {}

    for idx, line in enumerate(lines):
        fields = [int(i) for i in line.split(" ")]
        day_name = f"day{idx+1}"
        day_data = {"carbohydrate": fields[0], "protein": fields[1], "fat": fields[2], "calories": fields[3]}
        user_data[day_name] = day_data
     
    return jsonify(user_data)

@app.route("/api/user_info", methods=['GET'])
def get_user_info():
    user_data_file = open("user_data.txt", "r")
    lines = user_data_file.readlines()
   
    if len(lines) == 0:
        return jsonify({"error": "No user created"})
  
    data_line = lines[0]
    fields = data_line.strip().split(" ")
     
    user_data = {"username": fields[0], "height": fields[1], "weight": fields[2], "sex": fields[3]}

    return jsonify(user_data)

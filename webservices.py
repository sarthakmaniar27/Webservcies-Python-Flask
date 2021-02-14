"""REST Methods i have used:
1.) GET -> to retrieve data
2.) PUT -> to update existing data
3.) POST -> to store data
4.) DELETE -> to delete record
"""

from flask import Flask, jsonify, request
import json

app = Flask(__name__)

with open('stud_data.json') as f:
    studDB = json.load(f)
print(studDB)


# this method is just for checking whether route is working properly or not
@app.route("/", methods=['GET'])
def welcome():
    return "Welcome alien"


# Getting all the student data
@app.route("/student/getStudents", methods=['GET'])
def getStudents():
    return jsonify({"stud": studDB})


# Fetching student details by name
@app.route("/student/getStudentDetails/<Name>", methods=['GET'])
def getStudentDetails(Name):
    student = [stud for stud in studDB if (stud["Name"] == Name)]
    print(student)
    return jsonify({"stud": student})


#  updating student name
@app.route("/student/updateStudentDetails/<ID>", methods=['PUT'])
def updateStudentDetails(ID):
    student = [stud for stud in studDB if (stud["ID"] == ID)]
    if 'ID' in request.json:
        print("Student Available")
    if 'Name' in request.json:
        student[0]['Name'] = request.json['Name']
    return jsonify({"stud": student[0]})


#  adding student details
@app.route("/student/addStudent", methods=['POST'])
def addStudent():
    student = {
        "ID": request.json["ID"],
        "Name": request.json["Name"],
        "Gender": request.json["Gender"],
        "Class": request.json["Class"],
        "Club": request.json["Club"],
        "Persona": request.json["Persona"],
        "Crush": request.json["Crush"],
        "BreastSize": request.json["BreastSize"],
        "Strength": request.json["Strength"],
        "marks": request.json["marks"],
        "Hairstyle": request.json["Hairstyle"],
        "Color": request.json["Color"],
        "Stockings": request.json["Stockings"],
        "Accessory": request.json["Accessory"],
        "ScheduleTime": request.json["ScheduleTime"],
        "ScheduleDestination": request.json["ScheduleDestination"],
        "ScheduleAction": request.json["ScheduleAction"],
    }
    studDB.append(student)
    return jsonify({"stud": studDB})


#  deleting student details
@app.route("/student/removeStudent/<ID>", methods=['DELETE'])
def removeStudent(ID):
    student = [stud for stud in studDB if (stud['ID'] == ID)]
    if len(student) > 0:
        studDB.remove(student[0])
    return jsonify({"stud": student})


@app.route("/student/countStudents", methods=['GET'])
def countStudents():
    c = len(studDB)

    return "Total records in student data is " + str(c)


if __name__ == "__main__":
    app.run()

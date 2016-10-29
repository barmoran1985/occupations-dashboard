from flask import Flask
from flask import render_template
from pymongo import MongoClient
import json

app = Flask(__name__)

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DBS_NAME = 'occupations2011'
COLLECTION_NAME = 'projects'
FIELDS = {'_id': False, 'Town': True, 'County': True, 'Region': True, 'Males_Managers_Directors_Senior_Officials': True,
          'Males_Professional': True, 'Males_Associate_Professional_And_Technical': True,
          'Males_Administrative_Secretarial': True, 'Males_Skilled_Trade': True,
          'Males_Caring_Leisure_And_Other_Service': True, 'Males_Sales_Customer_Service': True,
          'Males_Process_Plant_Machine': True, 'Males_Elementary_Occupations': True, 'Males_Not_Stated': True,
          'Males_Total': True, 'Females_Managers_Directors_Senior_Officials': True, 'Females_Professional': True,
          'Females_Associate_Professional_And_Technical': True, 'Females_Administrative_Secretarial': True,
          'Females_Skilled_Trade': True, 'Females_Caring_Leisure_And_Other_Service': True,
          'Females_Sales_Customer_Service': True, 'Females_Process_Plant_Machine': True,
          'Females_Occupation_Elementary': True, 'Females_Not_Stated': True, 'Females_Total': True}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/occupations2011/projects")
def jobs_projects():
    connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    collection = connection[DBS_NAME][COLLECTION_NAME]
    projects = collection.find(projection=FIELDS, limit=55000)
    json_projects = []
    for project in projects:
        json_projects.append(project)
    json_projects = json.dumps(json_projects)
    connection.close()
    return json_projects


if __name__ == "__main__":
    app.run(debug=True)
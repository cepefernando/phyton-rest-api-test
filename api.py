from flask import Flask
from flask_restful import Resource, Api, reqparse, abort, marshal, fields
import re

# Initialize Flask
app = Flask(__name__)
api = Api(app)


@app.route("/")
def service_status():
    infile = r"log.txt"
    pattern = re.compile("error")
    service_name = ["api-gateway"]
    instance_id = ["ffd3082fe09d"]

    with open(infile) as f:
        f = f.readlines()

    count = 0
    for line in f:
        for match in re.finditer(pattern, line):
            count += 1
    # print(service_name[0] + " " + str(count))
    # print(instance_id[0] + " " + str(count))

    html = ''

    html += '<h2>Service: ' + service_name[0] + " " + str(count) + " errors "+ '</br>'

    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

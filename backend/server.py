from flask_restful import Resource, Api
from flask import Flask, request

app = Flask(__name__)
api = Api(app)
app.config["testcase"] = []


@app.route("/")
def hello_world():
    return "Hello world!"


class TestCaseServer(Resource):
    def get(self):
        if "id" in request.args:
            for i in app.config["testcase"]:
                if i["id"] == int(request.args["id"]):
                    return i
        else:
            return app.config["testcase"]

    def post(self):
        if "id" not in request.json:
            return {"fail": "error", "errcode": 404}
        app.config["testcase"].append(request.json)
        return {"success": "ok", "errcode": 0}


api.add_resource(TestCaseServer, "/testcase")

if __name__ == '__main__':
    app.run(debug=True)

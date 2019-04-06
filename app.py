from flask import Flask, request
from flask_restful import Resource, Api
import datetime
app = Flask(__name__)
api = Api(app)

motor_data = {}

class MotorData(Resource):
    def get(self):
        return motor_data

    def post(self):
        motor_data[get_max_id(commands)+1] = request.form['data']
        return {id: motor_data[id]}

commands = {}

class Command(Resource):
    def get(self):
        return commands

    def post(self):
        i = get_max_id(commands)+1
        nd = {'ts': request.form['ts'], 'command': request.form['command']}
        commands.update({i: nd})
        return {i: commands[i]}

def get_max_id(dict):
    if len(dict) > 0:
        return max(dict.keys())
    return 0


api.add_resource(Command, '/Commands')

if __name__ == '__main__':
    app.run(debug=True)
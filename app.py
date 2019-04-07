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
        i = get_max_id(motor_data)+1
        nd = {'ts': request.form['ts'], 'current': request.form['current'], 'voltage': request.form['voltage']}
        motor_data.update({i: nd})
        return {i: motor_data[i]}

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
api.add_resource(MotorData, '/MotorData')

if __name__ == '__main__':
    app.run(debug=True)
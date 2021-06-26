from flask import Flask

app = Flask(__name__)
@app.route('/', methods=['GET'])
def home():
    return 'This is my L4 SCA DevOps Assignment'


if __name__ == '__main__':
    app.run(debug=True)

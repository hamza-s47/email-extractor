from flask import Flask, jsonify, request, render_template
from modules.regex import email_extract

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root_route():
    return render_template('index.html')

# print(email_extract('dfdfnd hamza@gmial.ds'))

if __name__ == '__main__':
    app.run(debug=True)
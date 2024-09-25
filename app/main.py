from flask import Flask, jsonify, request, render_template
from modules.regex import email_extract
import modules.extractors as extractor


app = Flask(__name__)

@app.route('/', methods=['GET'])
def root_route():
    return render_template('index.html')

@app.route('/api/extract', methods=['POST'])
def extract_route():
    data = request.get_json()
    print("My Data", data)

    response = {"message":"success!"}
    return jsonify(response), 200
# print(len( extract_text_from_url('https://hamzasiddiqui.netlify.app/')))
# print(email_extract(extract_text_from_url('https://hamzasiddiqui.netlify.app/')))

if __name__ == '__main__':
    app.run(debug=True)
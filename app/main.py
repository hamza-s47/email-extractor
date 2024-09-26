from flask import Flask, jsonify, request, render_template
from modules.regex import email_extract
import modules.extractors as extractor


app = Flask(__name__)

@app.route('/', methods=['GET'])
def root_route():
    return render_template('index.html')

@app.route('/api/extract', methods=['POST'])
def extract_route():
    mainData = ''
    
    if request.files:
        mainData = request.files['file']
        extractedEmails = email_extract(extractor.extract_text_from_file(mainData))
        response = {
            "message":"Successfully Extracted",
            "emails":extractedEmails,
            "emailCount":len(extractedEmails)
        }
        return jsonify(response), 200

    else:
        mainData = request.get_json()
        if mainData['type'] == 'url':
            extractedEmails = email_extract(extractor.extract_url(mainData['content']))
            response = {
                "message":"Successfully Extracted",
                "emails":extractedEmails,
                "emailCount":len(extractedEmails)
            }
            return jsonify(response), 200
        else:
            extractedEmails = email_extract(mainData['content'])
            response = {
                "message":"Successfully Extracted",
                "emails":extractedEmails,
                "emailCount":len(extractedEmails),
                "textCount":len(mainData['content'])
            }
            return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
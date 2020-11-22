from flask import Flask, request
import re, os


app = Flask(__name__)


def sanitize_string(filename):
    ## any character (at the beginning) from a to Z, 0 to 9, the “-“ character, and the dot (.)
    valid_pattern = r'^[\.]?[a-zA-Z\-]+' # my solution.
    valid_pattern2 = r'^[\w\-\.]+$'  # lab solution does not accept any '/'
                                     # but sub-directories could be fine

    if re.search(valid_pattern, filename):
        return filename
    else:
        raise ValueError('Cannot use special characters')

def  cat(filename):
    try:
        sanitize_string(filename)
        with open(filename, 'r') as file:
            data = file.read()
            return data
    except ValueError:
        return 'invalid filename'

@app.route('/get_file', methods=['GET'])
def get_file():
    filename = request.args['filename']
    return '''Content of the file {} is...\n\n {}'''.format(filename, cat(filename))


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=int("8080"), debug=True)
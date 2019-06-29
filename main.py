from flask import Flask
from caesar import rotate_string
from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<! DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form method="POST">
            <label>Rotate by:</label>
            <input type="text" name="rot" value="0"></input>
            <br>
            <textarea name="textarea"></textarea>
            <br>
            <input type="submit">
        </form>
    </body>
</html>"""


@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt(rot, text):
    encypted_string = text(rotate_string)
    return """<h1>encrypted_string</h1>"""


app.run()
import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    password = "admin123"   # hardcoded secret
    os.system("ls")         # dangerous command
    return "Hello SecureFlow"
    
app.run(debug=True)
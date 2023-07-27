#!/usr/bin/env python3

import cgi
import os

# Set the upload directory to the cgi-bin folder
UPLOAD_DIR = os.getcwd()

# Function to handle file upload
def handle_upload():
    form = cgi.FieldStorage()
    if 'csvFile' not in form:
        return "Error: No file received."

    fileitem = form['csvFile']
    if fileitem.filename == '':
        return "Error: Empty file name."

    # Store the file in the upload directory
    filename = os.path.join(UPLOAD_DIR, "ravi.csv")
    with open(filename, 'wb') as f:
        f.write(fileitem.file.read())

    # Set read-write permissions for the uploaded file
    os.chmod(filename, 0o666)

    return f"File '{fileitem.filename}' uploaded and saved as '{filename}'."

# Main CGI script
print("Content-type: text/plain\n")

try:
    message = handle_upload()
    print(message)
except Exception as e:
    print("Error:", str(e))
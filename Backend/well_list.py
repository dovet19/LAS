import os
from flask import Blueprint, jsonify


# Create a blueprint for the LAS file API
list_api = Blueprint('list_api', __name__)

@list_api.route('/list', methods=['GET'])
def view_list():
    directory_path = '/data'  # Specify the directory path on the server

    # Check if the directory exists
    if not os.path.isdir(directory_path):
        return jsonify({'error': 'Directory not found'}), 500

    well_list = []

    # Iterate over the LAS files in the directory
    for filename in os.listdir(directory_path):
        # Make sure the file is a LAS file
        if filename.endswith('.las'):
            well_list.append(filename)

    return jsonify(well_list), 200
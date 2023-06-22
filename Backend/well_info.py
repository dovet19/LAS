import os
from flask import Blueprint, jsonify
from welly import Well


# Create a blueprint for the LAS file API
info_api = Blueprint('info_api', __name__)

@info_api.route('/list/<file>', methods=['GET'])
def view_data():
    directory_path = '/data'  # Specify the directory path on the server

    # Check if the directory exists
    if not os.path.isdir(directory_path):
        return jsonify({'error': 'Directory not found'}), 500

    well_list = []

    # Iterate over the LAS files in the directory
    for filename in os.listdir(directory_path):
        # Make sure the file is a LAS file
        if filename.endswith('.las'):
            file_path = os.path.join(directory_path, filename)

            # Load the LAS file
            try:
                # Load the first well from the file using comma
                # Do we account for files with multiple wells?
                well = Well.from_las(file_path)
            except Exception as e:
                well_list.append({'filename': filename, 'error': str(e)})
                continue

            # Extract information from the LAS file
            well_info = {
                'filename': filename,
                'well_name': well.name,
                'well_location': well.location,
                'well_headers': well.headers,
                'curve_names': [curve.mnemonic for curve in well.curves],
                'well_data': well.data,
                'well_metadata': well.params
            }

            well_list.append(well_info)

    return jsonify(well_list), 200
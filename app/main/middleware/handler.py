from flask import jsonify  # Not being framework agnostic (tied to Flask)


def handle_not_found_error(error):
    response = jsonify({"message": str(error)})
    response.status_code = 400
    return response

import json

def format_data(data):
    """Formats JSON data for better readability."""
    return json.dumps(data, indent=2)

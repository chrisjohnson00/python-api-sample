import json


def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    print(json.dumps([{'id': 1234, 'text': 'Foo the bar'}, {'id': 12345, 'text': 'Bar the foo'}]))

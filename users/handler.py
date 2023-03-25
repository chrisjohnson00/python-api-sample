import json


def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    print(json.dumps([{'firstname': 'Sam', 'lastname': 'Ample', 'id': 12345},
                      {'firstname': 'Ample', 'lastname': 'Sam', 'id': 54321}]))

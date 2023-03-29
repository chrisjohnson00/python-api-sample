import json
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET",
    }

    if req.method == "OPTIONS":
        return func.HttpResponse("", headers=headers, status_code=204)

    headers["Content-Type"] = "application/json"
    return func.HttpResponse(
        json.dumps([{'firstname': 'Sam', 'lastname': 'Ample', 'id': 12345},
                    {'firstname': 'Ample', 'lastname': 'Sam', 'id': 54321}]), headers=headers, status_code=200
    )

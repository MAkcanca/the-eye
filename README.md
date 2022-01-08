# The Eye
The Eye acts as a data aggregation/collection platform for all the application needs.


## Installation
### With Docker
After cloning the repository, review the `core/settings.py` and replace the Sentry SDK DSN URL.
```
docker-compose up -d --build
```
## Features

- The Eye handles the event log create requests asynchronously by offloading the database transactions to the Celery & Redis.
- The Eye keeps it simple and stores Session ID, Category, Name and, Timestamp along with a data json payload.
- You can query the logs with a Session ID, Category and/or Name.
- All the queries are ordered by Timestamp data (descending).
- It can process more than ~100 events/second but can be further improved by switching to a Non-relational database system (such as MongoDB).
- This project uses Sentry for collecting basic logs and exceptions. However, for errors happening inside containers (such as Redis, Celery etc.) and more fine-grained tuning, please see [this](https://jmaitrehenry.ca/how-to-catch-your-application-errors-easily-with-sentry-and-docker/).
- For more performance, consider using a cache layer such as Aerospike Cache in front of DB.

## Usage

To create an event log, simply call the `/api/event/` [*POST*] endpoint with proper body like below:
```
{
  "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
  "category": "page interaction",
  "name": "cta click",
  "data": {
    "host": "www.consumeraffairs.com",
    "path": "/",
    "element": "chat bubble"
  },
  "timestamp": "2021-01-01 09:15:27.243860"
}
```
If it succeeds it will return `{success: True}` else, it will return `{success: False}` .

To query event logs, simply call the `/api/event/` [*GET*] endpoint with query parameters:
- *timestamp_start*
- *timestamp_end*
- *session_id*
- *category*
- *name*

Example Request
```
Request
GET /api/event/?timestamp_after=2021-01-01&timestamp_before=2021-01-02&session_id=e2085be5-9137-4e4e-80b5-f1ffddc25423
---
Response
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
            "timestamp": "2021-01-01T09:15:27.243860Z",
            "category": "page interaction",
            "name": "cta click",
            "data": {
                "host": "www.consumeraffairs.com",
                "path": "/",
                "element": "chat bubble"
            }
        }
    ]
}
```

# Flask Full CRUD API Lab

## Description

A simple RESTful API built with Python and Flask to manage events. It uses an in-memory list to simulate a database.

## Setup

Install the dependencies:

```bash
python -m pip install flask pytest
```

Run the application:

```bash
python app.py
```

The API runs at `http://127.0.0.1:5000`.

## API Routes

| Method | Endpoint | Description | Success status |
|---|---|---|---|
| GET | `/` | Display a welcome message | 200 |
| GET | `/events` | Retrieve all events | 200 |
| POST | `/events` | Create an event | 201 |
| PATCH | `/events/<id>` | Update an event's title | 200 |
| DELETE | `/events/<id>` | Delete an event | 204 |

Invalid input returns `400 Bad Request`. Requests for nonexistent events return `404 Not Found`.

## Example Requests

### Create an event

```bash
curl -X POST http://127.0.0.1:5000/events \
  -H "Content-Type: application/json" \
  -d '{"title":"Hackathon"}'
```

Example response (`201 Created`):

```json
{"id": 3, "title": "Hackathon"}
```

### Update an event

```bash
curl -X PATCH http://127.0.0.1:5000/events/1 \
  -H "Content-Type: application/json" \
  -d '{"title":"Hackathon 2025"}'
```

### Delete an event

```bash
curl -X DELETE http://127.0.0.1:5000/events/2
```

A successful deletion returns `204 No Content`.

## Run Tests

```bash
python -m pytest -v
```

The API stores data in memory, so changes are not persisted after the application restarts.

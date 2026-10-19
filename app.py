
from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}


# In-memory "database"
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]


# Welcome route
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Events API"}), 200


# Get all events
@app.route("/events", methods=["GET"])
def get_events():
    return jsonify([event.to_dict() for event in events]), 200


# Create a new event
@app.route("/events", methods=["POST"])
def create_event():
    data = request.get_json(silent=True)

    # Validate the incoming JSON and required title
    if not isinstance(data, dict) or not isinstance(data.get("title"), str) or not data["title"].strip():
        return jsonify({"error": "A valid title is required"}), 400

    # Generate the next available ID
    new_id = max((event.id for event in events), default=0) + 1

    # Create and save the event
    new_event = Event(new_id, data["title"].strip())
    events.append(new_event)

    return jsonify(new_event.to_dict()), 201


# Update the title of an existing event
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    data = request.get_json(silent=True)

    # Validate the incoming JSON and required title
    if not isinstance(data, dict) or not isinstance(data.get("title"), str) or not data["title"].strip():
        return jsonify({"error": "A valid title is required"}), 400

    # Find the event by ID
    for event in events:
        if event.id == event_id:
            event.title = data["title"].strip()
            return jsonify(event.to_dict()), 200

    return jsonify({"error": "Event not found"}), 404


# Remove an event from the list
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    # Find the event by ID
    for event in events:
        if event.id == event_id:
            events.remove(event)
            return "", 204

    return jsonify({"error": "Event not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)

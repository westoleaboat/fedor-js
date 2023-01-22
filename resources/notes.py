# BLueprint
import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import notes


blp = Blueprint("notes", __name__, description="Operations on notes")


@blp.route('/mynotes')
class NoteList(MethodView):
    def get(self):
        return{"notes": list(notes.values())}

    def post(self):
        note_data = request.get_json()

        if (
            "name" not in note_data
            or "note" not in note_data

        ):
            abort(
                400, message="Bad request, Ensure 'name', and 'note' are included in the JSON payload.",
            )
        # check for duplicate.
        # for note in notes.values():
        #     if (
        #         note_data["name"] == note['name']
        #     ):
        #         abort(400, message='Already exists.')

        note_id = uuid.uuid4().hex
        note = {**note_data, "id": note_id}
        # names = {**note_data["names"]}
        notes[note_id] = note
        return note

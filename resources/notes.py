# BLueprint
import json
import uuid
from flask import request, render_template
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import notes
from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm
from datetime import datetime


blp = Blueprint("notes", __name__, description="Operations on notes")
notesList = 0


class NameForm(FlaskForm):
    name = StringField('author')
    note = StringField('note')  # , validators=[DataRequired()])
    submit = SubmitField('Submit')


@blp.route('/mynotes')
class NoteList(MethodView):
    def get(self):
        if notes == {}:
            empty = True
            author = 'No author'
            note = 'No note'
            data = 'no data'
            i = 'no data'
            ia = 'no data'
        else:
            empty = False

            # print(notes.values())
            # print(dict(notes['name']))
            data = list(notes.values())
            print(f'database lenght = {len(data)}')
            # for i in data:
            for item in data:
                # print(i['name'])
                # author = i['name']
                author = item['name']
                # note = i['note']
                # i = note['note']
                print(item['name'])
            # for i in data:
            # print(list([dict(name=result['name']) for result in data]))
        return render_template('notes.html', empty=empty,
                               jsonfile=notes, amount=len(notes), author=author, data=data, form=NameForm())  # , note=i)  # ,  # ,

        # return{"notes": list(notes.values())}
        # the JSON is a list
        # data = list(notes.values())

        # if notes == {}:
        #     empty = True
        #     # data1 = 'no data'
        # else:
        #     empty = False
        #     # data1 = data[0]['name']
        # if empty == False:
        #     try:
        #         print(f'first note: {data[0]}')

        #         data2 = list([dict(name=result['name']) for result in data])
        #         # print(data2) prints [{'name': 'Name Title2'}]
        #         try:
        #             print(f'first item of first note: {data2[0]}')

        #         except IndexError:
        #             pass

        #         try:
        #             data3 = list([dict(name=result['name'])
        #                           for result in data2])
        #         # for i in dict(data3):
        #             print(data3[0]['name'])
        #         except IndexError:
        #             pass

        #     except UnboundLocalError:
        #         pass

        # # form = NameForm
        # return render_template('notes.html',  # ,
        #                        jsonfile=json.dumps(data),
        #                        empty=empty)  # , name=data2)  # , title=data1)  # , info=info)  # ,
        # #                        form=form,
        # #                        current_time=datetime.utcnow())

    def post(self):
        global notesList
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

        # note_id = uuid.uuid4().hex
        # notesList = 1
        note_id = notesList + 1
        notesList += 1
        note = {**note_data, "id": note_id}
        # names = {**note_data["names"]}
        notes[note_id] = note
        # print(len(notes))
        return note

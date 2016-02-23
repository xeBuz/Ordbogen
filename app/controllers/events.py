from .base import BaseController
from app.models.events import Event, EventCategory
from app.models.countries import Country
from flask import Blueprint, request
from flask.views import MethodView

events = Blueprint('events', __name__, url_prefix='/api/events')


class EventAPI(MethodView, BaseController):

    def get(self, event_id):
        if event_id:
            query_events = Event.query.filter_by(id=event_id).first()
            if query_events is None:
                return self.response(404)

        else:
            query_events = Event.query.all()

            if len(query_events) == 0:
                return self.response(404)

        return self.response(200, query_events)

    def post(self):
        try:
            self.validate_fields(Event.required_fields(), request.form.keys())
        except ValueError:
            return self.response(400, 'Required fields: ' + ' '.join(Event.required_fields()))

        params = self.get_form_values(Event.get_columns(), request.form)

        country = Country.query.filter_by(id=params['country_id']).first()
        if country:
            self.response(400, "The country_id doesn't exists")

        if params['category_id']:
            category = EventCategory.query.filter_by(id=params['category_id']).first()
            if category:
                self.response(400, "The category_id doesn't exists")

        new_event = Event(
            title=params['title'],
            description=params['description'],
            datetime=params['datetime'],
            category_id=params['category_id'],
            country_id=params['country_id'],
        )
        new_event.save()

        return self.response(201)

    def delete(self, event_id):
        event = Event.query.filter_by(id=event_id).first()
        if event is None:
            return self.response(404)

        event.delete()
        return self.response(200)

    def put(self, event_id):
        event = Event.query.filter_by(id=event_id).first()
        if event is None:
            return self.response(404)

        params = self.get_form_values(Country.get_columns(), request.form)

        if params['title']:
            event.title = params['title']
        if params['description']:
            event.description = params['description']
        if params['datetime']:
            event.datetime = params['datetime']
        if params['category_id']:
            event.category_id = params['category_id']
        if params['country_id']:
            event.country_id = params['country_id']

        event.save()

        return self.response(200)

event_view = EventAPI.as_view('event_api')
events.add_url_rule('/', defaults={'event_id': None}, view_func=event_view, methods=['GET'])
events.add_url_rule('/', view_func=event_view, methods=['POST'])
events.add_url_rule('/<int:event_id>', view_func=event_view, methods=['GET', 'PUT', 'DELETE'])
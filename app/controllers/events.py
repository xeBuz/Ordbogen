from .base import BaseController
from app.models.events import Event, EventCategory
from app.models.countries import Country
from flask import Blueprint, request
from flask.views import MethodView

events = Blueprint('events', __name__, url_prefix='/api/events')


class EventAPI(MethodView, BaseController):

    def get(self, event_id):
        if event_id:
            pagination = None
            query_events = Event.query.filter_by(id=event_id).first()
            if query_events is None:
                return self.response(404)

        else:
            allowed_sort = ['title', 'datetime', 'id']

            page = int(request.args.get('page', '1'))
            count = int(request.args.get('count', '5'))
            sort = request.args.get('sort', 'id')
            country_code = request.args.get('country_id')

            if sort not in allowed_sort:
                return self.response(400, 'Invalid sort field')

            if country_code:
                country = Country.query.filter_by(iso_code=country_code).first()
                if country is None:
                    return self.response(404)

                pagination = Event.query.filter_by(country_id=country.id).order_by(sort).paginate(page, count, False)
            else:
                pagination = Event.query.order_by(sort).paginate(page, count, False)

            query_events = pagination.items

            if len(query_events) == 0:
                return self.response(404)

        return self.response(200, query_events, pagination)

    def post(self):
        try:
            self.validate_fields(Event.required_fields(), request.form.keys())
        except ValueError:
            return self.response(400, 'Required fields: ' + ' '.join(Event.required_fields()))

        params = self.get_form_values(Event.get_columns(), request.form)

        country = Country.query.filter_by(iso_code=str(params['country_id'].upper())).first()
        if country is None:
            return self.response(400, "The country_id doesn't exists")

        if params['category_id']:
            category = EventCategory.query.filter_by(id=params['category_id']).first()
            if category is None:
                return self.response(400, "The category_id doesn't exists")

        new_event = Event(
            title=params['title'],
            description=params['description'],
            category_id=params['category_id'],
            country_id=country.id,
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

        params = self.get_form_values(Event.get_columns(), request.form)

        country = Country.query.filter_by(iso_code=str(params['country_id'].upper())).first()
        if country is None:
            return self.response(400, "The country_id doesn't exists")

        if params['title']:
            event.title = params['title']
        if params['description']:
            event.description = params['description']
        if params['category_id']:
            event.category_id = params['category_id']
        if params['country_id']:
            event.country_id = country.id

        event.save()

        return self.response(200)

event_view = EventAPI.as_view('event_api')
events.add_url_rule('/', defaults={'event_id': None}, view_func=event_view, methods=['GET'])
events.add_url_rule('/', view_func=event_view, methods=['POST'])
events.add_url_rule('/<int:event_id>', view_func=event_view, methods=['GET', 'PUT', 'DELETE'])
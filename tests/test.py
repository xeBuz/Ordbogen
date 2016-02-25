import os
import unittest
from app import app
from app.models.continents import Continent
from app.models.countries import Country
from app.models.events import Event
from app.models.users import Users
from app.models.tokens import Tokens
from flask import json


basedir = os.path.abspath(os.path.dirname(__file__))
database_path = basedir + "/../database/"


class OrdbogenTestCase(unittest.TestCase):

    country = {}
    continent = {}

    event_id = None
    country_id = None
    token = None
    header = {}

    def setUp(self):
        self.app = app.test_client()
        self.continent_index = 5

        self.continent = {
            'code': 666,
            'name': 'Middle-earth'
        }

        self.country = {
            'iso_code': 'GO',
            'iso_code_long': 'GON',
            'short_name': 'Gondor',
            'formal_name': 'Reunited Kingdom of Gondor and Arnor',
            'demonym': 'Gondorian',
            'country_code': 42,
            'continental_code': 666,
            'coordinates': '12.3,-32.2',
            'elevation': 1200,
            'elevation_low': 0,
            'area': 54422,
            'land': 51241,
            'fertility': 46,
            'population': 423151,
            'population_urban': 62334,
            'birth': 12,
            'death': 34.1,
            'itu': 'http://tolkiengateway.net/wiki/Gondor',
            'web': 'https://www.google.com.ar/search?q=gondor',
            'gis': 'http://lotr.wikia.com/wiki/Gondor',
            'statistics': 'https://en.wikipedia.org/wiki/Gondor',
            'flag': 'http://vignette1.wikia.nocookie.net/cybernations/images/3/3a/GondorFlag.png',
            'government': 'Kingdom',
            'boundary_box': None,
            'currency': 'gold'
        }

        self.event = {
            'title': 'Attack',
            'description': 'Minas Tirith is under attack',
            'category_id': 1,
            'country_id': 'GO',
        }

        self.user = {
            'name': 'Isildur',
            'email': 'isildur@ring.com',
            'password': 'Valandil123'
        }

    def tearDown(self):
        pass

    def test_00_token_new(self):
        token = Tokens(user_id=1)
        token.save()

        OrdbogenTestCase.token = token.key
        OrdbogenTestCase.header['Authorization'] = token.key

        self.assertIsNotNone(token.key)

    def test_01_contintent_new(self):
        new_continent = Continent(code=self.continent['code'], name=self.continent['name'])
        new_continent.save()

        self.assertEqual(new_continent.code, self.continent['code'], "New Continent code")
        self.assertEqual(new_continent.name, self.continent['name'], "New Contientnt name")

    def test_02_continent_query(self):
        continent = Continent.query.filter_by(code=self.continent['code']).first()

        self.assertIsNotNone(continent, 'Empty Continent Query')
        self.assertEqual(continent.name, self.continent['name'], "Query Continent")

    def test_03_continent_delete(self):
        continent = Continent.query.filter_by(code=self.continent['code']).first()
        continent.delete()
        continent = Continent.query.filter_by(code=self.continent['code']).first()
        self.assertIsNone(continent)

    def test_04_continent_post(self):
        response = self.app.post('/api/continents/', data=self.continent, headers=self.header)
        data = json.loads(response.data)
        self.assertEqual(data['status']['code'], 201)

    def test_05_continent_get_all(self):
        response = self.app.get('/api/continents/')
        data = json.loads(response.data)

        self.assertEqual(data['status']['code'], 200)
        self.assertEqual(data['status']['message'], 'OK')

        self.assertEqual(data['data'][self.continent_index]['name'], self.continent['name'])
        self.assertEqual(data['data'][self.continent_index]['code'], self.continent['code'])

    def test_06_continent_get_one(self):
        response = self.app.get('/api/continents/' + str(self.continent['code']))
        data = json.loads(response.data)

        self.assertEqual(data['status']['code'], 200)
        self.assertEqual(data['status']['message'], 'OK')

        self.assertEqual(data['data']['name'], self.continent['name'])
        self.assertEqual(data['data']['code'], self.continent['code'])

    def test_07_continent_get_one_invalid(self):
        response = self.app.get('/api/continents/6661')
        data = json.loads(response.data)
        self.assertEqual(data['status']['code'], 404)

    def test_08_continent_put(self):
        fake = {'name': 'Mordor'}
        original = {'name': self.continent['name']}
        response = self.app.put('/api/continents/' + str(self.continent['code']), data=fake, headers=self.header)
        data = json.loads(response.data)
        self.assertEqual(data['status']['code'], 200)

        response = self.app.get('/api/continents/' + str(self.continent['code']))
        data = json.loads(response.data)
        self.assertEqual(data['data']['name'], fake['name'])

        response = self.app.put('/api/continents/' + str(self.continent['code']), data=original, headers=self.header)
        data = json.loads(response.data)
        self.assertEqual(data['status']['code'], 200)

    def test_09_country_new(self):
        new_country = Country(
            iso_code=self.country['iso_code'],
            iso_code_long=self.country['iso_code_long'],
            short_name=self.country['short_name'],
            formal_name=self.country['formal_name'],
            demonym=self.country['demonym'],
            country_code=self.country['country_code'],
            continental_code=self.country['continental_code'],
            coordinates=self.country['coordinates'],
            elevation=self.country['elevation'],
            elevation_low=self.country['elevation_low'],
            area=self.country['area'],
            land=self.country['land'],
            fertility=self.country['fertility'],
            population=self.country['population'],
            population_urban=self.country['population_urban'],
            birth=self.country['birth'],
            death=self.country['death'],
            itu=self.country['itu'],
            web=self.country['web'],
            gis=self.country['gis'],
            statistics=self.country['statistics'],
            flag=self.country['flag'],
            government=self.country['government'],
            boundary_box=self.country['boundary_box'],
            currency=self.country['currency']
        )
        new_country.save()
        self.assertEqual(new_country.iso_code, self.country['iso_code'], "New Countru ISO Code")

    def test_10_country_query(self):
        country = Country.query.filter_by(iso_code=self.country['iso_code']).first()
        self.assertIsNotNone(country, 'Empty Country Query')
        self.assertEqual(country.iso_code, self.country['iso_code'])
        self.assertEqual(country.iso_code_long, self.country['iso_code_long'])
        self.assertEqual(country.short_name, self.country['short_name'])
        self.assertEqual(country.formal_name, self.country['formal_name'])
        self.assertEqual(country.demonym, self.country['demonym'])
        self.assertEqual(country.country_code, self.country['country_code'])
        self.assertEqual(country.continental_code, self.country['continental_code'])
        self.assertEqual(country.coordinates, self.country['coordinates'])
        self.assertEqual(country.elevation, self.country['elevation'])
        self.assertEqual(country.elevation_low, self.country['elevation_low'])
        self.assertEqual(country.area, self.country['area'])
        self.assertEqual(country.land, self.country['land'])
        self.assertEqual(country.fertility, self.country['fertility'])
        self.assertEqual(country.population, self.country['population'])
        self.assertEqual(country.population_urban, self.country['population_urban'])
        self.assertEqual(country.birth, self.country['birth'])
        self.assertEqual(country.death, self.country['death'])
        self.assertEqual(country.itu, self.country['itu'])
        self.assertEqual(country.web, self.country['web'])
        self.assertEqual(country.gis, self.country['gis'])
        self.assertEqual(country.statistics, self.country['statistics'])
        self.assertEqual(country.flag, self.country['flag'])
        self.assertEqual(country.government, self.country['government'])
        self.assertEqual(country.boundary_box, self.country['boundary_box'])
        self.assertEqual(country.currency, self.country['currency'])

    def test_11_country_delete(self):
        country = Country.query.filter_by(iso_code=self.country['iso_code']).first()
        country.delete()
        country = Country.query.filter_by(iso_code=self.country['iso_code']).first()
        self.assertIsNone(country)

    def test_12_country_post(self):
        response = self.app.post('/api/countries/', data=self.country, headers=self.header)
        data = json.loads(response.data)
        self.assertEqual(data['status']['code'], 201)

    def test_13_country_get_all(self):
        response = self.app.get('/api/countries/')
        data = json.loads(response.data)

        self.assertEqual(data['status']['code'], 200)
        self.assertEqual(data['status']['message'], 'OK')

    def test_14_country_get_one(self):
        response = self.app.get('/api/countries/' + str(self.country['iso_code']))
        data = json.loads(response.data)

        self.assertEqual(data['status']['code'], 200)
        self.assertEqual(data['status']['message'], 'OK')

        self.assertEqual(data['data']['iso_code_long'], self.country['iso_code_long'])
        self.assertEqual(data['data']['short_name'], self.country['short_name'])
        self.assertEqual(data['data']['formal_name'], self.country['formal_name'])
        self.assertEqual(data['data']['demonym'], self.country['demonym'])
        self.assertEqual(data['data']['country_code'], self.country['country_code'])
        self.assertEqual(data['data']['continental_code'], self.country['continental_code'])
        self.assertEqual(data['data']['coordinates'], self.country['coordinates'])
        self.assertEqual(data['data']['elevation'], self.country['elevation'])
        self.assertEqual(data['data']['elevation_low'], self.country['elevation_low'])
        self.assertEqual(data['data']['area'], self.country['area'])
        self.assertEqual(data['data']['land'], self.country['land'])
        self.assertEqual(data['data']['fertility'], self.country['fertility'])
        self.assertEqual(data['data']['population'], self.country['population'])
        self.assertEqual(data['data']['population_urban'], self.country['population_urban'])
        self.assertEqual(data['data']['birth'], self.country['birth'])
        self.assertEqual(data['data']['death'], self.country['death'])
        self.assertEqual(data['data']['ITU'], self.country['itu'])
        self.assertEqual(data['data']['web'], self.country['web'])
        self.assertEqual(data['data']['GIS'], self.country['gis'])
        self.assertEqual(data['data']['statistics'], self.country['statistics'])
        self.assertEqual(data['data']['flag'], self.country['flag'])
        self.assertEqual(data['data']['government'], self.country['government'])
        self.assertEqual(data['data']['boundary_box'], self.country['boundary_box'])
        self.assertEqual(data['data']['currency'], self.country['currency'])

    def test_15_country_put(self):
        fake = {
            'formal_name': 'Hyaralondie',
            'area': 10000000
        }
        original = {
            'formal_name': self.country['formal_name'],
            'area': self.country['area']
        }

        response = self.app.put('/api/countries/' + str(self.country['iso_code']), data=fake, headers=self.header)
        data = json.loads(response.data)
        self.assertEqual(data['status']['code'], 200)

        response = self.app.get('/api/countries/' + str(self.country['iso_code']))
        data = json.loads(response.data)
        self.assertEqual(data['data']['formal_name'], fake['formal_name'])
        self.assertEqual(data['data']['area'], fake['area'])

        response = self.app.put('/api/countries/' + str(self.country['iso_code']), data=original, headers=self.header)
        data = json.loads(response.data)
        self.assertEqual(data['status']['code'], 200)

    def test_16_event_post(self):
        response = self.app.post('/api/events/', data=self.event, headers=self.header)
        data = json.loads(response.data)
        self.assertEqual(data['status']['code'], 201)

    def test_17_event_get_all(self):
        response = self.app.get('/api/countries/', headers=self.header)
        data = json.loads(response.data)
        self.assertEqual(data['status']['code'], 200)
        self.assertEqual(data['status']['message'], 'OK')

    def test_18_user_add(self):
        response = self.app.post('/api/users/', data=self.user, headers=self.header)
        data = json.loads(response.data)
        self.assertEqual(data['status']['code'], 201)

    def test_96_user_delete(self):
        user = Users.query.filter_by(name=self.user['name']).first()
        response = self.app.delete('/api/users/' + str(user.id), headers=self.header)
        data = json.loads(response.data)
        self.assertEqual(data['status']['code'], 200)

    def test_97_event_delete(self):
        event = Event.query.filter_by(title=self.event['title']).first()
        response = self.app.delete('/api/events/' + str(event.id), headers=self.header)
        data = json.loads(response.data)
        self.assertEqual(data['status']['code'], 200)

    def test_98_country_delete(self):
        response = self.app.delete('/api/countries/' + str(self.country['iso_code']), headers=self.header)
        data = json.loads(response.data)
        self.assertEqual(data['status']['code'], 200)

    def test_99_continent_api_delete(self):
        response = self.app.delete('/api/continents/' + str(self.continent['code']), headers=self.header)
        data = json.loads(response.data)
        self.assertEqual(data['status']['code'], 200)

    def test_99_remove_toke(self):
        token = Tokens.query.filter_by(user_id=1).first()
        if token:
            token.delete()

if __name__ == '__main__':
    unittest.main()

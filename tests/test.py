import os
import unittest
from app import app
from app.models.continents import Continent
from app.models.countries import Country
from flask import json


basedir = os.path.abspath(os.path.dirname(__file__))
database_path = basedir + "/../database/"


class OrdbogenTestCase(unittest.TestCase):

    country = {}
    continent = {}

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

    def tearDown(self):
        pass

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
        response = self.app.post('/api/continents/', data=self.continent)
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

    def test_08s_continent_put(self):
        fake = {'name': 'Mordor'}
        original = {'name': self.continent['name']}

        response = self.app.put('/api/continents/' + str(self.continent['code']), data=fake)
        data = json.loads(response.data)
        self.assertEqual(data['status']['code'], 200)

        response = self.app.get('/api/continents/' + str(self.continent['code']))
        data = json.loads(response.data)
        self.assertEqual(data['data']['name'], fake['name'])

        response = self.app.put('/api/continents/' + str(self.continent['code']), data=original)
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
        pass

    def test_12_country_post(self):
        pass

    def test_13_country_get_all(self):
        pass

    def test_14_country_get_one(self):
        pass

    def test_15_country_put(self):
        pass

    def test_98_country_delete(self):
        pass

    def test_99_continent_api_delete(self):
        response = self.app.delete('/api/continents/' + str(self.continent['code']))
        data = json.loads(response.data)
        self.assertEqual(data['status']['code'], 200)


if __name__ == '__main__':
    unittest.main()
# API Endpoints

## Summary

We have five important Entities/Models, each one with the proper endpoint:

- [Continents](#continents-item)
- [Countries](#countries-item)
- [Events](#events-item)
- [Users](#users-item)
- [Tokens](#tokens-item)
    

### Continents

| Method  | Endpoint               | Usage                  | 
| :-----: |  --------------------- | ---------------------- |
| `GET`   | `/api/continents/`     | Get all Continents     | 
| `GET`   | `/api/continents/<id>` | Get one Continent      | 
| `POST`  | `/api/continents/`     | Create a new Continent |
| `PUT`   | `/api/continents/<id>` | Edit a Continent       |
| `DELETE`| `/api/continents/<id>` | Delete a Continent     |


### Countries

| Method  | Endpoint                    | Usage                                                                                   | 
| :-----: |  ---------------------------| --------------------------------------------------------------------------------------- |
| `GET`   | `/api/countries/`           | Get all Countries                                                                       |
| `GET`   | `/api/countries/<iso_code>` | Get a Country using [ISO_3166-1 Alpha-2 Code](https://en.wikipedia.org/wiki/ISO_3166-1) | 
| `GET`   | `/api/countries/?name=<XX>` | Get a Countries list filtering by name                                                  |
| `POST`  | `/api/countries/`           | Create a new Country                                                                    |
| `PUT`   | `/api/countries/<id>`       | Edit a Country                                                                          |
| `DELETE`| `/api/countries/<id>`       | Delete a Country                                                                        |


### Events

| Method  | Endpoint                       | Usage                                              | 
| :-----: |  ----------------------------- | -------------------------------------------------- |
| `GET`   | `/api/events/`                 | Get all Events                                     | 
| `GET`   | `/api/events/<id>`             | Get one Event                                      | 
| `GET`   | `/api/events/?country_id=<XX>` | Get a Events list filtering by Country ISO Code    |
| `POST`  | `/api/events/`                 | Create a new Event                                 |
| `PUT`   | `/api/events/<id>`             | Edit an Event                                      |
| `DELETE`| `/api/events/<id>`             | Delete an Event                                    |



### Users

| Method  | Endpoint          | Usage             | 
| :-----: |  ---------------- | ----------------- |
| `GET`   | `/api/users/`     | Get all Users     | 
| `GET`   | `/api/users/<id>` | Get one User      | 
| `POST`  | `/api/users/`     | Create a new User |
| `DELETE`| `/api/users/<id>` | Delete a User     |



### Tokens

| Method   | Endpoint         | Usage               | 
| :-----:  | ---------------- | ------------------- |
| `POST`   | `/api/login/`    | Create a new Token  |
| `DELETE` | `/api/login/`    | Delete a Token      | 


## Responses

The Endpoint responses are very similar to each others.

### Success

These responses have 4 properties:

- `data`: Specific endpoint data.
- `links`: Pagination links (if apply), `first`, `prev`, `next` and `last`.
- `status`: HTTP code and message.
- `success`: Boolean, provide a easy handler to validate if the response is valid or not.

```json
{
  "data": [
      ...
  ],
  "links": {
    "first": "http://127.0.0.1:5000/api/countries/?count=5&page=1",
    "last": "http://127.0.0.1:5000/api/countries/?count=5&page=43",
    "next": "http://127.0.0.1:5000/api/countries/?count=5&page=2"
  },
  "status": {
    "code": 200,
    "message": "OK"
  },
  "success": true
}
```


### Error

These responses have 3 properties:

- `error`: One or more messages provided by the application
- `status`: HTTP code and message.
- `success`: Boolean, provide a easy handler to validate if the response is valid or not.

```json
{
  "error": {
    "message": "Invalid user"
  },
  "status": {
    "code": 400,
    "message": "Bad Request"
  },
  "success": false
}
```

## Authentication

The endpoint POST `/api/login/` grant temporal access to a user, using the e-mail and the password.
This access is provided by a Token system, much simpler than a oAuth server, but quite strong.

When the User generate a valid token, this token has 24 hours to expire, after this time the token will be deleted. Also, if the User try to generate a new Token, the old Token is deleted.

After the creation, the Token must be provided to the app using `HTTP Headers`, name `Authorization`

Every method with the decorator `@login_required` will check the Headers, an continue only if the token and expiration date are valid.  
With this method we also could know who user is executing the operation.

**Local User**
- e-mail: admin@ordbogen.com
- password: wordbook


Example with `cURL`:


```bash
curl -X "POST" "http://127.0.0.1:5000/api/continents/" \
	-H "Authorization: xYwLUkgDJ0NippmNMGk25fQoVwzC39vo5sQ0LNhFBEpzAUffh1bNZS55opvE "

```

Example with `HTTPie`:

```bash
http POST http://127.0.0.1:5000/api/continents/ \
    'Authorization':'xYwLUkgDJ0NippmNMGk25fQoVwzC39vo5sQ0LNhFBEpzAUffh1bNZS55opvE '
```




## <a name="continents-item"></a>Continents


### Model

- code
- name


### Allowed Methods
 - GET
 - POST
 - PUT
 - DELETE


### GET

#### Successful Responses

- Get all Continents 

```
GET /api/continents/ HTTP/1.1
```

```json
{
    "data": [
        {
            "code": 2,
            "name": "Africa"
        },
        {
            "code": 19,
            "name": "America"
        },
        {
            "code": 142,
            "name": "Asia"
        },
        {
            "code": 150,
            "name": "Europa"
        },
        {
            "code": 9,
            "name": "Oceania"
        }
    ],
    "status": {
        "code": 200,
        "message": "OK"
    },
    "success": true
}

```


- Get one Continent

```
GET /api/continents/142 HTTP/1.1
```


```json
{
  "data": {
    "code": 142,
    "name": "Asia"
  },
  "status": {
    "code": 200,
    "message": "OK"
  },
  "success": true
}
```
- Get a invalid Continent

```
GET /api/continents/111111 HTTP/1.1
```

```json
{
  "status": {
    "code": 404,
    "message": "Not Found"
  },
  "success": false
}
```


### PUT

You can modify just the `name` field.  **Login required.**



```
PUT /api/continents/9 HTTP/1.1
Authorization: xyzxyzxyzxyzxyzxyzxyzxyz

name=Continent+Name
```


```json
{
  "status": {
    "code": 200,
    "message": "OK"
  },
  "success": true
}
```

### POST 
You must provide the `name`. **Login required.**

```
POST /api/continents/ HTTP/1.1
Authorization: xyzxyzxyzxyzxyzxyzxyzxyz

name=Continent+Name
```

```json
{
  "status": {
    "code": 201,
    "message": "Created"
  },
  "success": true
}
```


### DELETE
**Login required.**

```
DELETE /api/continents/9 HTTP/1.1
Authorization: xyzxyzxyzxyzxyzxyzxyzxyz
```

```json
{
  "status": {
    "code": 200,
    "message": "OK"
  },
  "success": true
}
```



## <a name="countries-item"></a>Countries


### Model:

- iso_code
- iso\_code\_long
- short_name
- formal_name
- demonym
- country_code
- continental_code
- coordinates
- elevation
- elevation_low
- area
- land
- fertility
- population
- population_urban
- birth
- death
- ITU
- web
- GIS
- statistics
- flag
- government
- boundary_box
- currency

### GET


- Get all Countries

```
GET /api/countries/ HTTP/1.1
```

```json
{
  "data": [
    {
      "GIS": "estadistica.ad",
      "ITU": "govern.ad",
      "area": 468,
      "birth": 8.48,
      "boundary_box": "euro",
      "continental_code": 150,
      "coordinates": "42.5,1.5",
      "country_code": 20,
      "currency": "€",
      "death": 6.82,
      "demonym": "Andorran",
      "elevation": 2946,
      "elevation_low": 840,
      "fertility": 5.32,
      "flag": "https://www.cia.gov/library/publications/the-world-factbook/graphics/flags/large/an-lgflag.gif",
      "formal_name": "Principality of Andorra",
      "government": "parliamentary democracy (since March 1993) that retains as its chiefs of state a co-principa",
      "iso_code": "AD",
      "iso_code_long": "AND",
      "land": 468,
      "population": 79218,
      "population_urban": 68258,
      "short_name": "Andorra",
      "statistics": "laposte.fr",
      "web": "iea.ad"
    },
    ...
  ],
  "links": {
    "first": "http://127.0.0.1:5000/api/countries/?count=5&page=1",
    "last": "http://127.0.0.1:5000/api/countries/?count=5&page=43",
    "next": "http://127.0.0.1:5000/api/countries/?count=5&page=2"
  },
  "status": {
    "code": 200,
    "message": "OK"
  },
  "success": true
}
```


- Get one Countries by ISO code

```
GET /api/countries/DK HTTP/1.1
GET /api/countries/dk HTTP/1.1
```


```json
{
  "data": {
    "GIS": "dst.dk",
    "ITU": "denmark.dk",
    "area": 43094,
    "birth": 10.22,
    "boundary_box": "couronne",
    "continental_code": 150,
    "coordinates": "56,10",
    "country_code": 208,
    "currency": "DKr",
    "death": 10.23,
    "demonym": "Danish",
    "elevation": 171,
    "elevation_low": null,
    "fertility": 57.99,
    "flag": "https://www.cia.gov/library/publications/the-world-factbook/graphics/flags/large/da-lgflag.gif",
    "formal_name": "Kingdom of Denmark",
    "government": "constitutional monarchy",
    "iso_code": "DK",
    "iso_code_long": "DNK",
    "land": 42434,
    "population": 5613706,
    "population_urban": 4902113,
    "short_name": "Denmark",
    "statistics": "postdanmark.dk",
    "web": "geus.dk"
  },
  "status": {
    "code": 200,
    "message": "OK"
  },
  "success": true
}
```


- Filtering using the Name, with the querystring `?name=XX`. Minimum two characters.

```
GET /api/countries/?name=arg HTTP/1.1
```

```json
{
  "data": [
    {
      "GIS": "indec.mecon.ar",
      "ITU": "argentina.gov.ar",
      "area": 2780400,
      "birth": 16.88,
      "boundary_box": "比 索",
      "continental_code": 19,
      "coordinates": "-34,-64",
      "country_code": 32,
      "currency": "$Arg",
      "death": 7.34,
      "demonym": "Argentine",
      "elevation": 6960,
      "elevation_low": null,
      "fertility": 13.68,
      "flag": "https://www.cia.gov/library/publications/the-world-factbook/graphics/flags/large/ar-lgflag.gif",
      "formal_name": "Argentine Republic",
      "government": "republic",
      "iso_code": "AR",
      "iso_code_long": "ARG",
      "land": 2736690,
      "population": 41446246,
      "population_urban": 37903421,
      "short_name": "Argentina",
      "statistics": "correoargentino.com.ar",
      "web": "ign.gob.ar"
    }
  ],
  "links": {
    "first": "http://127.0.0.1:5000/api/countries/?count=1&page=1",
    "last": "http://127.0.0.1:5000/api/countries/?count=1&page=1"
  },
  "status": {
    "code": 200,
    "message": "OK"
  },
  "success": true
}
```

#### Extra parametrization
You can use a few extra parametrization via query string:

 - `page`: Number of page
 - `count`: Items per page
 - `sort`: Sort field, allowed: `iso_code`, `short_name` and `country_code`


### POST 
You must provide valid `iso_code`, `iso_code_long`, `short_name`, `continental_code` and `country_code`.  The other fields are optional

**Login required.**

```
POST /api/countries/ HTTP/1.1
Authorization: xyzxyzxyzxyzxyzxyzxyzxyz

key=values
```

```json
{
  "status": {
    "code": 201,
    "message": "Created"
  },
  "success": true
}
```


### PUT 
**Login required.**

```
PUT /api/countries/<iso_code> HTTP/1.1
Authorization: xyzxyzxyzxyzxyzxyzxyzxyz
```

Fields allowed listed on top

```json
{
  "status": {
    "code": 200,
    "message": "OK"
  },
  "success": true
}
```


### DELETE
**Login required.**

```
DELETE  /api/countries/<iso_code>  HTTP/1.1
Authorization: xyzxyzxyzxyzxyzxyzxyzxyz
```

```json
{
  "status": {
    "code": 200,
    "message": "OK"
  },
  "success": true
}
```



## <a name="events-item"></a>Events

### Model

- title 
- description 
- datetime 
- category_id 
- country_id 


#### Categories

- 1. Alert
- 2. News
- 3. Warnings


### GET
**Login required.**


- Get all the events

```
GET /api/events/ HTTP/1.1
```

```json
{
  "data": [
    {
      "category": "News",
      "country": {
        "iso_code": "AS",
        "name": "American Samoa"
      },
      "datetime": "2016-02-23 15:47:36",
      "description": "Here goes the description",
      "id": 1,
      "title": "Event Test"
    }
    ...
  ],
  "links": {
    "first": "http://127.0.0.1:5000/api/events/?count=1&page=1",
    "last": "http://127.0.0.1:5000/api/events/?count=1&page=1"
  },
  "status": {
    "code": 200,
    "message": "OK"
  },
  "success": true
}
```

- Get Event by ID

```
GET /api/events/1 HTTP/1.1
```


```json
{
  "data": {
    "category": "News",
    "country": {
      "iso_code": "AS",
      "name": "American Samoa"
    },
    "datetime": "2016-02-23 15:47:36",
    "description": "Here goes the description",
    "id": 1,
    "title": "Event Test"
  },
  "status": {
    "code": 200,
    "message": "OK"
  },
  "success": true
}
```

- Get Events by `country_id` (ISO code)

```
GET /api/events/?country_id=AS HTTP/1.1
```

```json
{
  "data": [
    {
      "category": "News",
      "country": {
        "iso_code": "AS",
        "name": "American Samoa"
      },
      "datetime": "2016-02-23 15:47:36",
      "description": "Here goes the description",
      "id": 1,
      "title": "Event Test"
    }
  ],
  "links": {
    "first": "http://127.0.0.1:5000/api/events/?count=1&page=1",
    "last": "http://127.0.0.1:5000/api/events/?count=1&page=1"
  },
  "status": {
    "code": 200,
    "message": "OK"
  },
  "success": true
}
```

#### Extra parametrization
You can use a few extra parametrization via query string:

 - `page`: Number of page
 - `count`: Items per page
 - `sort`: Sort field, allowed: `title`, `datetime` and `id`



### POST 
You must provide valid `title`, `country_id`.  The other fields are optional

**Login required.**

```
POST /api/event/ HTTP/1.1
Authorization: xyzxyzxyzxyzxyzxyzxyzxyz

key=values
```

```json
{
  "status": {
    "code": 201,
    "message": "Created"
  },
  "success": true
}
```


### PUT 
**Login required.**

```
PUT /api/event/<id> HTTP/1.1
Authorization: xyzxyzxyzxyzxyzxyzxyzxyz
```

Fields allowed listed on top

```json
{
  "status": {
    "code": 200,
    "message": "OK"
  },
  "success": true
}
```



### DELETE
**Login required.**

```
DELETE  /api/events/<id>  HTTP/1.1
Authorization: xyzxyzxyzxyzxyzxyzxyzxyz
```

```json
{
  "status": {
    "code": 200,
    "message": "OK"
  },
  "success": true
}
```


## <a name="users-item"></a>User

#### Model

 - name
 - email
 - password


### GET 

- Get all Users

```
GET /api/users/ HTTP/1.1
```


```json
{
  "data": [
    {
      "e-mail": "fakeemail1@gmail.com",
      "id": 1,
      "name": "User"
    },
    {
      "e-mail": "fakeemail2@gmail.com",
      "id": 2,
      "name": "Lando"
    },
    {
      "e-mail": "fakeemail5@gmail.com",
      "id": 5,
      "name": "Pepe"
    }
  ],
  "links": {
    "first": "http://127.0.0.1:5000/api/users/?count=3&page=1",
    "last": "http://127.0.0.1:5000/api/users/?count=3&page=1"
  },
  "status": {
    "code": 200,
    "message": "OK"
  },
  "success": true
}
```

- Get one User

```
GET /api/users/1 HTTP/1.1
```

```json
{
  "data": {
    "e-mail": "fakeemail@gmail.com",
    "id": 1,
    "name": "User"
  },
  "status": {
    "code": 200,
    "message": "OK"
  },
  "success": true
}
```




### POST 
You must provide valid `title`, `country_id`.  The other fields are optional

**Login required.**

```
POST /api/users/ HTTP/1.1
Authorization: xyzxyzxyzxyzxyzxyzxyzxyz

key=values
```

```json
{
  "status": {
    "code": 201,
    "message": "Created"
  },
  "success": true
}
```



### DELETE
**Login required.**

```
DELETE  /api/users/<id>  HTTP/1.1
Authorization: xyzxyzxyzxyzxyzxyzxyzxyz
```

```json
{
  "status": {
    "code": 200,
    "message": "OK"
  },
  "success": true
}
```



## <a name="tokens-item"></a>Login

### Authorize a User / Create a Token

```
POST /api/login/ HTTP/1.1

email=fakeemail%40gmail.com&password=password
```

```json
{
  "data": {
    "access_key": "xYwLUkgDJ0NippmNMGk25fQoVwzC39vo5sQ0LNhFBEpzAUffh1bNZS55opvE",
    "expiration": "2016-02-26 01:18:17",
    "user": {
      "e-mail": "fakeemail@gmail.com",
      "name": "User Name"
    }
  },
  "status": {
    "code": 200,
    "message": "OK"
  },
  "success": true
}
```


- Invalid authentication

```
{
  "error": {
    "message": "Invalid user"
  },
  "status": {
    "code": 400,
    "message": "Bad Request"
  },
  "success": false
}
```


- Invalid Operation over a Endpoint with login required

```json
{
  "status": {
    "code": 401,
    "message": "Unauthorized Access"
  },
  "success": false
}
```



- Invalid Operation, Token expired

```json
{
  "status": {
    "code": 401,
    "message": "Login Expired"
  },
  "success": false
}
```

# Local Environment

## Clone this repository

```bash
git clone git@github.com:xeBuz/Ordbogen.git
```

## Activate virtualenv

For a better usage activate `virtualenv`, if you don't have `virtualenv` installed follow [this](http://virtualenv.readthedocs.org/en/latest/installation.html) steps.

```bash
cd Ordbogen;
source venv/bin/activate
```

## Install Python requirements

Based on a suggestion, this project doesn't have many external library, this app only requires `Flask` and `Flask-SQLAlchemy`.

```bash
pip install -r requirements.txt
```

An extra library is required for a easier method to run the tests, install `nose` in this case.

## Run the Server

The project is Python 2.7 and Python 3.5 compatible. To run the server you must execute the following command


```bash
python server.py

 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 
```


## Run tests

```bash
python2 venv/bin/nosetests;
........................
----------------------------------------------------------------------
Ran 24 tests in 0.715s

OK
```

```
python3 venv/bin/nosetests;
........................
----------------------------------------------------------------------
Ran 24 tests in 0.866s

OK
```

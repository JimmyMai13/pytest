# pytest

### Setup

1. Install [python3](https://www.python.org/downloads/)

2. ```$ python3 -m pip install virtualenv``` in project root

3. Create a new virtual environment ```$ python3 -m venv env```

4. Activate environment ```$ source env/bin/activate```

5. Install dependencies ```(env)$ python3 -m pip install -r requirements.txt```

6. Install [chrome](https://www.google.com/chrome/?brand=CHBD&brand=FKPE&gclid=CjwKCAiAwrf-BRA9EiwAUWwKXoA4ry4QOhBBpEOGtjVMMQWSM32df6UIZ8oGiF3brFjQDeH-fSli1RoCgbIQAvD_BwE&gclsrc=aw.ds)

7. Download [chrome driver](https://chromedriver.chromium.org/downloads) for chrome version installed and place in `pytest/drivers/`

8. ```$ export PATH=$PATH:/path/to/chromedriver```

9. ```cd drivers/```

10. ```xattr -d com.apple.quarantine <name-of-chromedriver-executable>```

### Set environment configs in `config.ini`

1. ```apikey=<YOUR_CALLRAIL_API_KEY>```
2. ```baseurl=<CALLRAIL_API_HOST>```
 
### Usage

[pytest docs](https://docs.pytest.org/en/stable/contents.html)

[useful command-line options](https://docs.pytest.org/en/reorganize-docs/new-docs/user/commandlineuseful.html)

To run api tests:

- ```(env)$ python3 -m pytest apitests/test-accounts.py```

To run ui tests:

- ```(env)$ python3 -m pytest uitests/test-careers-page.py```
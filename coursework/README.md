![Wahoot Logo](wahoot_web/static/wahoot_logo.svg)

## Setup Instructions

> 1. First, install the `pipenv` package, by using this command in the terminal:

```sh 
pip install pipenv
```

> 2. Then, we use `pipenv` to read the contents of the Pipfile and install all the necessary packages that make the Wahoot frontend work. This can be accompished with:
```sh
pipenv install
```
(Make sure the terminal is opened within the correct folder!)


> 3. From here on out, you only need to type this command in the terminal to run Wahoot:
```sh
pipenv run flask --app wahoot_web --debug run
```
The 'website' will then be running locally at `localhost:5000`, and you can access it as a url in your preferred web browser.

You can stop Wahoot at any time by pressing **CTRL+C** in the terminal.
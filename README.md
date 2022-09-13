## Listings service

# Dependencies
To run this service you must have [Python3](https://www.python.org/downloads/) and [pip](https://pypi.org/project/pip/) to install dependencies. After installing Python and pip, depending on its version you should install project dependencies running the following command `pip install -r requirements.txt`

# Running the project

Running the project is done by running the following command: `python3 -m uvicorn src.main:app --reload`

# Testing

Running project tests is done by running the following command: `pytest src/tests/`

# URLs

- Project will be running on port 8000.
- Listing API: api/v1/listings
- Docs endpoint: /docs
- OpenAPI endpint /redoc

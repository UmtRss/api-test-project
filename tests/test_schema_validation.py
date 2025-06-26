import pytest
import requests
import json
import os
from jsonschema import validate, ValidationError

def test_get_post_schema_validation():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    assert response.status_code == 200


    response_json = response.json()


    schema_path = os.path.join(os.path.dirname(__file__), '../schemas/post_schema.json')
    with open(schema_path, 'r') as file:
        schema = json.load(file)


    try:
        validate(instance=response_json, schema=schema)
    except ValidationError as e:
        pytest.fail(f"Schema validation failed: {e.message}")

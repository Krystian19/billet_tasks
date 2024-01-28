import json
from datetime import datetime as dt
from faker import Faker

fake = Faker()

def test_create_user(test_app):
    test_create_user_payload = {
        "username": fake.user_name()
    }

    response = test_app.post("/v1/users", data=json.dumps(test_create_user_payload))
    assert response.status_code == 201

    res = response.json()
    assert res['success'] is True
    assert 'payload' in res

    payload = res['payload']
    assert 'id' in payload 
    assert payload['username'] == test_create_user_payload['username']
    assert 'created_at' in payload 

def test_get_user(test_app):
    test_create_user_payload = {
        "username": fake.user_name()
    }

    creation_response = test_app.post("/v1/users", data=json.dumps(test_create_user_payload))
    assert creation_response.status_code == 201

    created_user_res = creation_response.json()
    assert created_user_res['success'] is True
    created_user = created_user_res['payload']

    found_user_response = test_app.get("/v1/users/{}".format(created_user["id"]))
    found_user = found_user_response.json()

    assert found_user is not None
    assert created_user["id"] is not None

    assert test_create_user_payload["username"] == found_user["username"]
    assert found_user["created_at"] == created_user["created_at"]

def test_destroy_user(test_app):
    test_create_user_payload = {
        "username": fake.user_name()
    }

    creation_response = test_app.post("/v1/users", data=json.dumps(test_create_user_payload))
    assert creation_response.status_code == 201

    created_user_res = creation_response.json()
    assert created_user_res['success'] is True
    created_user = created_user_res['payload']

    deletion_response = test_app.delete("/v1/users/{}".format(created_user["id"]))
    deleted_user_res = deletion_response.json()

    assert deleted_user_res is not None
    assert deleted_user_res["success"] is True

    found_deleted_user_response = test_app.get("/v1/users/{}".format(created_user["id"]))
    found_deleted_user = found_deleted_user_response.json()

    # make sure the user record was actually deleted
    assert found_deleted_user is None

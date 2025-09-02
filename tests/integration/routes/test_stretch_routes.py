import pytest

def test_create_stretch(test_client, test_database):
    res = test_client.post(
        "/exercises",
        json = {
            "name": "test",
            "description": "test",
            "repetitions": 1,
            "duration_seconds": 1,
            "muscle_group": "test"
        }
    )

    assert res.status_code == 401 and res.json() == {

    }

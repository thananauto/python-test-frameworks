import pytest
import requests
import json
from conf.conftest import api_url

@pytest.mark.parametrize("user_id, first_name",[(1, 'George'), (2, 'Janet')])
@pytest.mark.user
def test_valid_user(api_url, user_id, first_name):
    url = api_url + '/users/'+ str(user_id)
    resp = requests.get(url)
    j = json.loads(resp.text)
    assert resp.status_code == 200, resp.text
    j = json.loads(resp.text)
    assert resp.status_code == 200, resp.text
    assert j['data']['id'] == user_id, resp.text
    assert j['data']['first_name'] == first_name, resp.text


@pytest.mark.user
def test_list_invaliduser(api_url):
    url = api_url + "/users/50"
    resp = requests.get(url)
    assert resp.status_code == 404, resp.text
import pytest
import requests
import json
from conf.conftest import api_url

@pytest.mark.xfail
@pytest.mark.login
def test_login_valid(api_url):
    url = api_url + "/login/"
    data = {'email':'test@test.com','password':'something'}
    resp = requests.post(url, data=data)
    j = json.loads(resp.text)
    assert resp.status_code == 200, resp.text
    assert j['token'] == "QpwL5tke4Pnpja7X", resp.text

@pytest.mark.login
def test_login_no_password(api_url):
    url = api_url + "/login/"
    data = {'email':'test@test.com'}
    resp = requests.post(url, data=data)
    j = json.loads(resp.text)
    assert resp.status_code == 400, resp.text
    assert j['error'] == "Missing password", resp.text

def test_login_no_email(api_url):
    url = api_url + "/login/"
    data = {}
    resp = requests.post(url, data=data)
    j = json.loads(resp.text)
    assert resp.status_code == 400, resp.text
    assert j['error'] == "Missing email or username", resp.text
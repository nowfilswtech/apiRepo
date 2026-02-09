import pytest
import requests

# ==================== GLOBAL CONFIGURATION ====================
BASE_URL = "https://devsfit.vvdntech.com/api-node/testcases"

COMMON_HEADERS = {}

# ==================== TEST FUNCTIONS ====================
def test_tc001_get_testcases_based_on_project():
    """Test ID: TC001, Name: unnamed, Expected: 200 status code"""
    url = "/testcases/getTestCasesBasedOnProject"
    headers = {
    }
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    assert 'success' in response.text
    assert 'message' in response.text
    assert 'data' in response.text

def test_tc002_get_testcases_based_on_project():
    """Test ID: TC002, Name: unnamed, Expected: 200 status code"""
    url = "/testcases/getTestCasesBasedOnProject"
    headers = {
        **COMMON_HEADERS,
    }
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    assert 'success' in response.text
    assert 'message' in response.text

def test_tc003_get_test_cases_based_on_project():
    """Test ID: TC003, Name: unnamed, Expected: 200 status code"""
    url = "/testcases/getTestCasesBasedOnProject"
    headers = {
    }
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    assert 'success' in response.text
    assert 'message' in response.text

def test_tc004_get_testcases_based_on_project():
    """Test ID: TC004, Name: unnamed, Expected: 200 status code"""
    url = "/testcases/getTestCasesBasedOnProject"
    headers = {
    }
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    assert 'success' in response.text
    assert 'message' in response.text

def test_tc005_get_testcases_based_on_project():
    """Test ID: TC005, Name: unnamed, Expected: 200 status code"""
    url = "/testcases/getTestCasesBasedOnProject"
    headers = {
    }
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    assert 'success' in response.text
    assert 'message' in response.text
import pytest
import requests
from requests.auth import HTTPBasicAuth

def test_basiAuth():
    res = requests.get("https://api.github.com/user", auth=HTTPBasicAuth('krishnagajjela@gmail.com', 'Gkrish@2020'))
    print(res.text)
    print("Test Kgajjela1 branch")
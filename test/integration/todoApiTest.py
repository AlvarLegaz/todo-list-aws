import http.client
import os
import unittest
from urllib.request import urlopen
import requests
import json

import pytest

#Load enviroment variable defined in /home/username/.bashrc
BASE_URL = os.environ.get("BASE_URL_PROD")
DEFAULT_TIMEOUT = 2  # in secs

# Production database has the following: [{"checked": false, "createdAt": "1718559552.1348243", "text": "Aprender git y aws", "id": "57cef4f7-2c07-11ef-becf-a3092365244b", "updatedAt": "1718559552.1348243"}]

@pytest.mark.api
class TestApi(unittest.TestCase):

    self.
    
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_listtodos(self):
        print('---------------------------------------')
        print('Starting - integration test List TODO')
        #List
        url = BASE_URL+"/todos"
        response = requests.get(url)
        print('Response List Todo:' + str(response.json()))
        self.assertEqual(
            response.status_code, 200, "Error en la petición API a {url}"
        )
        self.assertTrue(response.json())
        
        print('End - integration test List TODO')
        
    def test_api_gettodo(self):
        print('---------------------------------------')
        print('Starting - integration test Get TODO')
        #Test GET TODO
        ID_TODO="57cef4f7-2c07-11ef-becf-a3092365244b"
        url = BASE_URL+"/todos/"+ID_TODO
        response = requests.get(url)
        json_response = response.json()
        print('Response Get Todo: '+ str(json_response))
        self.assertEqual(
            response.status_code, 200, "Error en la petición API a {url}"
        )
        self.assertEqual(
            json_response['text'], "Aprender git y aws", "Error en la petición API a {url}"
        )
        print('End - integration test Get TODO')
    

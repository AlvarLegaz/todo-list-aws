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

#Prod database has the following entry: [{"checked": false, "createdAt": "1718558081.332397", "text": "Aprender git y aws", "id": "eb2450fd-2c03-11ef-a81e-c9cc90002600", "updatedAt": "1718558081.332397"}]

@pytest.mark.api
class TestApi(unittest.TestCase):
    
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_listtodos(self):
        print('---------------------------------------')
        print('Starting - integration test List TODO')
        #Add TODO
        url = BASE_URL+"/todos"
        data = {
         "text": "Aprender git y aws"
        }
        response = requests.post(url, data=json.dumps(data))
        json_response = response.json()
        print('Response Add Todo: '+ str(json_response))
        jsonbody= json.loads(json_response['body'])
        self.ID_TODO = jsonbody['id']
        print ('ID todo:'+ID_TODO)
        self.assertEqual(
            response.status_code, 200, "Error en la petición API a {url}"
        )
        self.assertEqual(
            jsonbody['text'], "Aprender git y aws", "Error en la petición API a {url}"
        )
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
        url = BASE_URL+"/todos/"+self.ID_TODO
        response = requests.get(url)
        json_response = response.json()
        print('Response Get Todo: '+ str(json_response))
        self.assertEqual(
            response.status_code, 200, "Error en la petición API a {url}"
        )
        self.assertEqual(
            json_response['text'], "Aprender git y aws", "Error en la petición API a {url}"
        )
        #Delete TODO to restore state
        response = requests.delete(url)
        self.assertEqual(
            response.status_code, 200, "Error en la petición API a {url}"
        )
        print('End - integration test Get TODO')
    

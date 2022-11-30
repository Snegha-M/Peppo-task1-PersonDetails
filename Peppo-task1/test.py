import json
from app import app
import unittest
import pytest



class FlaskTest(unittest.TestCase):

    pytest.token=""

    #check for authentication
    def test_authentication(self):
        tester = app.test_client(self)
        data1 = {"username":"snegha","password":"snegha123"}
        response = tester.post("/auth", content_type='application/json', data=json.dumps(data1))
        result = response.data.decode('utf-8')
        js = json.loads(result)
        pytest.token=js["access_token"]
        # print("Start Display Token")
        # print(pytest.token)
        # print("End Display Token")
        self.assertTrue(True)

    # check for post
    def test_post(self):
        data = [{
            "PersonName": "Rashmi-new",
            "PersonAge": 25,
            "PersonAddress": "Bangalore"
        }]
        tester = app.test_client(self)
        str = "JWT "
        authToken = {"Content-Type": "application/json", "Authorization": (str + (pytest.token))}
        # print(json.dumps(data))
        # print(authToken)
        response = tester.post("/person", headers=authToken, data=json.dumps(data))
        # print(response.data)
        self.assertEqual(response.status_code, 201)

    # check for get valid id
    def test_get_validId(self):
        tester = app.test_client(self)
        str = "JWT "
        authToken = {"Content-Type": "application/json", "Authorization": (str + (pytest.token))}
        response = tester.get("/person/124", headers=authToken)
        expValue = b'{"PersonId": 124, "PersonName": "Rayan", "PersonAge": 32, "PersonAddress": "Erode"}\n'
        self.assertEqual(response.data.decode("utf-8"), expValue.decode("utf-8"))

    #check for get invalid id
    def test_get_invalidId(self):
        tester = app.test_client(self)
        str = "JWT "
        authToken = {"Content-Type": "application/json", "Authorization": (str + (pytest.token))}
        response = tester.get("/person/1203", headers=authToken)
        self.assertEqual(response.data, b'{"message": "Person id is not available"}\n')

    #check for put_id_available
    def test_put_id_available(self):
        data = {
            "PersonName":"Reshma"
        }
        tester = app.test_client(self)
        str = "JWT "
        authToken = {"Content-Type": "application/json", "Authorization": (str + (pytest.token))}
        response = tester.put("/person/127", headers=authToken, data=json.dumps(data))
        expValue = b'{"PersonId": 127, "PersonName": "Reshma", "PersonAge": 25, "PersonAddress": "Bangalore"}\n'
        self.assertEqual(response.data.decode("utf-8"), expValue.decode("utf-8"))

    #check for put_id_not_available
    def test_put_id_not_available(self):
        data = {
            "PersonName":"Reshma"
        }
        tester = app.test_client(self)
        str = "JWT "
        authToken = {"Content-Type": "application/json", "Authorization": (str + (pytest.token))}
        response = tester.put("/person/1270", headers=authToken, data=json.dumps(data))
        #print(response.data)
        self.assertEqual(response.data, b'{"message": "Person id is not available"}\n')

    #check for delete_id_available
    # def test_delete_id_available(self):
    #     tester = app.test_client(self)
    #     str = "JWT "
    #     authToken = {"Content-Type": "application/json", "Authorization": (str + (pytest.token))}
    #     response = tester.delete("/person/133", headers=authToken)
    #     statuscode = response.status_code
    #     #print(statuscode)
    #     self.assertEqual(statuscode,200)

    #check for delete_id_not_available
    def test_delete_id_not_available(self):
        tester = app.test_client(self)
        str = "JWT "
        authToken = {"Content-Type": "application/json", "Authorization": (str + (pytest.token))}
        response = tester.delete("/person/128", headers=authToken)
        #print(response.data)
        self.assertEqual(response.data, b'{"message": "Person id is not available"}\n')




if __name__ =='__main__':
        unittest.main()


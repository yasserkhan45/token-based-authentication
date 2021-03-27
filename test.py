try:
    import unittest
    from app import app

except Exception as e:
    print ("Some Modules are missing {} ".format(e))

class FlaskTest(unittest.TestCase):
    
    def test_authors(self):
        tester = app.test_client(self)
        response = tester.get("/authors")
        statuscode = response.status_code
        self.assertEqual(response.content_type, "application/json")
    
    def test_author(self):
        tester = app.test_client(self)
        response = tester.get("/author")
        statuscode = response.status_code
        self.assertEqual(response.content_type, "application/json")

if __name__ == "__main__":
    unittest.main()
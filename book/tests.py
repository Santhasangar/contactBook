from django.test import TestCase
from rest_framework.test import APITestCase
from book.models import contactBook

# Create your tests here.
class contactBookAPITestCase(APITestCase):
    def setUp(self):
        contactBook.objects.create(firstName="Mehr",lastName="Sachdeva",userName="MehrSachdeva",phone="9876543210",email="mehr@gmail.com",address="horamavu,prestige",city="Bangalore", state="Karnataka",country="India",zipCode="560043") 

    def test_get_method(self):
        url = 'http://127.0.0.1:8000/book/create-contact/' 
        response = self.client.get(url) 
        self.assertEqual(response.status_code,200)
        contact=contactBook.objects.filter(userName='MehrSachdeva')  
        self.assertEqual(contact.count(),1)

    def test_post_method_success(self):
        url = 'http://127.0.0.1:8000/book/create-contact/'
        data= {
            'firstName':"tang",
            'lastName':"dev",
            'userName':"tangdev",
            'phone':"9876542310",
            'email':"tang@gmail.com",
            'address':"horamavu,prestige",
            'city':"Bangalore", 
            'state':"Karnataka",
            'country':"India",
            'zipCode':"560016"
        }
        response=self.client.post(url,data,format='json')
        print(response.status_code)
        self.assertEqual(response.status_code,201)

    def test_delete_method_success(self):
        url = 'http://127.0.0.1:8000/book/contact-detail/1/'
        response = self.client.delete(url)
        print("Delete Success",response.status_code)
        self.assertEqual(response.status_code,204)

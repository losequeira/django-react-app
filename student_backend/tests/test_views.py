from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from ..models import Address, Student

class StudentViewTestCase(TestCase):
    @classmethod
    def setUpTestData(self):
        number_of_students = 13
        saved_address = Address.objects.create(
            state="san jose",
            city="san pedro",
            zipcode="110202"
        )

        for student_id in range(number_of_students):
            Student.objects.create(
                name=f'Student {student_id}',
                lastname=f'Surname {student_id}',
                birthdate=timezone.now(),
                address=saved_address
            )
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/api/students/')
        self.assertEqual(response.status_code, 200)
    
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('student-list'))
        self.assertEqual(response.status_code, 200)
    
    def test_list_all_students(self):
        number_of_students = 13
        response = self.client.get(reverse('student-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(number_of_students, len(response.data))
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Address, Student

class StudentTestCase(TestCase):
    @classmethod
    def setUpTestData(self):
        saved_address = Address.objects.create(
            state="san jose",
            city="san pedro",
            zipcode="110202"
        )
        self.student = Student.objects.create(
            name="Loe",
            lastname="Sequeira",
            birthdate=timezone.now(),
            address=saved_address)

    def test_first_name_label(self):
        field_label = self.student._meta.get_field('name').verbose_name
        self.assertEqual('student first name', field_label)
    
    def test_last_name_label(self):
        field_label = self.student._meta.get_field('lastname').verbose_name
        self.assertEqual('student last name', field_label)
    
    def test_object_name_is_first_name_blank_last_name(self):
        expected_object_name = f'{self.student.name} {self.student.lastname}'
        self.assertEquals(expected_object_name, str(self.student))

    def test_student_created_successfully(self):
        self.assertEqual(self.student.name, 'Loe')
        self.assertEqual(self.student.lastname, 'Sequeira')

class AddressTestCase(TestCase):
    def setUp(self):
        saved_address = Address.objects.create(
            state="san jose",
            city="san pedro",
            zipcode="110202"
        )
    
    def test_address_created_successfully(self):
        address = Address.objects.get(id="1")
        
        self.assertEqual(address.__str__(), "san jose, san pedro, 110202")
        self.assertEqual(address.state, "san jose")
        self.assertEqual(address.city, "san pedro")
        self.assertEqual(address.zipcode, "110202")

class StudentViewTestCase(TestCase):
    @classmethod
    def setUpTestData(self):
        # Create 13 students for pagination tests
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
        response = self.client.get(reverse('student-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(13, len(response.data))
from django.test import TestCase

from tracking.models import Project, User, Client


class ProjectModelTest(TestCase):
    def setUp(self):
        self.client_instance = Client.objects.create(name="Test Client")
        self.creator = User.objects.create_user(username='Test', password='te8904!sting')
        self.project = Project.objects.create(
            creator=self.creator,
            name="Test Project",
            client=self.client_instance,
            amount=10000,
            start_date='2023-01-01',
            end_date='2023-12-31',
            additional_costs=2000
        )

    def test_calculate_profit_or_loss(self):
        self.assertEqual(self.project.calculate_profit_or_loss(), 8000)

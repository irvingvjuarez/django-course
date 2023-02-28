from django.utils import timezone
from django.test import TestCase
import datetime

from .models import Question

# Create your tests here.
class QuestionModelTests(TestCase):
    def test_was_published_recently_future_dates(self):
        '''
        Method was_published_recently must return False when the pub_date is in the future
        '''

        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(content="Who is the best teacher in platzi?", pub_date=time)

        self.assertIs(future_question.was_published_recently(), False)

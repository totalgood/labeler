import os
import datetime

from django.test import TestCase
from django.utils import timezone
# from django.core.urlresolvers import reverse

from settings import MEDIA_ROOT
from .models import Image
# from .forms import FileUploadForm


class ImageModelTest(TestCase):
    fixtures = ['labeler_test_data.json']
    caption = "This is only a test ... image take 2.5 years ago."

    def create_image(self, caption=caption):
        return Image.objects.create(caption=caption,
                                    taken_date=timezone.now() - datetime.timedelta(365.25 * 2.5),
                                    file=open(os.path.join(MEDIA_ROOT, 'test_image.jpg', 'rb')),
                                    uploaded_date=timezone.now(),
                                    created_date=timezone.now())

    def test_image_creation(self):
        image = self.create_image()
        self.assertTrue(isinstance(image, Image))
        # self.assertEqual(image.__unicode__(), image.caption)
        self.assertEqual(self.caption, image.caption)

from django.test import TestCase
from django.urls import reverse
from .models import Note


class NoteTests(TestCase):
    def setUp(self):
        self.note = Note.objects.create(
            title="Test Note",
            content="Test Content"
        )

    def test_note_list_view(self):
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Note")

    def test_note_detail_view(self):
        response = self.client.get(reverse('note_detail', args=[self.note.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Content")

    def test_note_create_view(self):
        response = self.client.post(reverse('note_create'), {
            'title': 'New Note',
            'content': 'New Content'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after creation
        self.assertTrue(Note.objects.filter(title='New Note').exists())

    def test_note_update_view(self):
        response = self.client.post(
            reverse('note_update', args=[self.note.id]),
            {
                'title': 'Updated Note',
                'content': 'Updated Content'
            }
        )
        self.assertEqual(response.status_code, 302)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'Updated Note')

    def test_note_delete_view(self):
        response = self.client.post(
            reverse('note_delete', args=[self.note.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Note.objects.filter(id=self.note.id).exists())

    def test_create_note_with_empty_title(self):
        response = self.client.post(reverse('note_create'), {
            'title': '',
            'content': 'Some content'
        })
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertTrue(form.errors)
        self.assertIn('title', form.errors)
        self.assertIn('This field is required.', form.errors['title'])

    def test_create_note_with_empty_content(self):
        response = self.client.post(reverse('note_create'), {
            'title': 'Title Only',
            'content': ''
        })
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertTrue(form.errors)
        self.assertIn('content', form.errors)
        self.assertIn('This field is required.', form.errors['content'])

    def test_update_note_with_empty_title(self):
        response = self.client.post(
            reverse('note_update', args=[self.note.id]),
            {
                'title': '',
                'content': 'Updated Content'
            }
        )
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertTrue(form.errors)
        self.assertIn('title', form.errors)
        self.assertIn('This field is required.', form.errors['title'])

    def test_update_note_with_empty_content(self):
        response = self.client.post(
            reverse('note_update', args=[self.note.id]),
            {
                'title': 'Updated Title',
                'content': ''
            }
        )
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertTrue(form.errors)
        self.assertIn('content', form.errors)
        self.assertIn('This field is required.', form.errors['content'])

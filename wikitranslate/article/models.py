from django.db import models

LANG_CHOICES = (
    ('hi','Hindi'),
    ('bn', 'Bengali'),
    ('pa','Punjabi'),
    ('te','Telugu'),
    ('ta','Tamil'),
)

# Create your models here.
class Project(models.Model):
    wiki_title = models.CharField(max_length=200)
    target_lang = models.CharField(max_length=7, choices=LANG_CHOICES, default='hi')

    def __str__(self):
        return self.wiki_title

class Sentence(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    original_sentence = models.TextField(blank = True, null = True)
    translated_sentence = models.TextField(blank = True, null =True)
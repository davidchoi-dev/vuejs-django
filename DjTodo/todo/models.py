from django.db import models

class Todo(models.Model):
    name = models.CharField('NAME', max_length=5, blank=True)
    todo = models.CharField('TODO', max_length=50)

    def __str__(self):
        return self.todo

    def save(self, force_insert=False, force_update=False, using=None, update_field=None):
        if not self.name:
            self.name = '홍길동'

        super().save()

from django.db import models
from model_utils.models import TimeStampedModel


class User(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    password = models.TextField(null=True, blank=True)
    about = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Blog(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = ('Post/Blog')

    def __str__(self):
        return f'{self.title}'


class Like(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)



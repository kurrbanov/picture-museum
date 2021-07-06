from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    img = models.ImageField()
    born = models.IntegerField()
    die = models.IntegerField()
    bio = models.TextField()

    def __str__(self):
        return f"{self.name} {self.surname}"


class Picture(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField()
    year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

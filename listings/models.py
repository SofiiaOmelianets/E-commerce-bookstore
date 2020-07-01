import datetime

from django.db import models

from owners.models import Owner


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['title']
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.title = self.title.capitalize()
        return super().save(*args, **kwargs)


YEAR_CHOICES = [(r, r) for r in range(1984, datetime.date.today().year + 1)]
CURRENT_YEAR = datetime.date.today().year

RATE_CHOICE = [(r, r) for r in range(1, 6)]
COVER_CHOICES = [
    ('М\'ягка', 'Softcover'),
    ('Тверда', 'Hardcover'),
]
LANGUAGE_CHOICES = [
    ('Українська', 'UA'),
    ('Російська', 'RU'),
    ('Англійська', 'EN'),
]


class Book(models.Model):
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    # is_new = models.BooleanField(default=True)
    author = models.CharField(max_length=250)
    category = models.ManyToManyField('Category')
    # price = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    # owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='owner_books')
    publisher = models.CharField(max_length=250)
    language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES)
    year_of_publishing = models.IntegerField(choices=YEAR_CHOICES, default=CURRENT_YEAR)
    number_of_pages = models.IntegerField()
    translator = models.CharField(max_length=50, null=True, blank=True)
    book_cover = models.CharField(max_length=9, choices=COVER_CHOICES)
    # annotation = models.TextField(blank=True)
    rate = models.IntegerField(choices=RATE_CHOICE)

    image_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    image_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.slug

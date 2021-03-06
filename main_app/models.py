from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)


class FavoriteTreat(models.Model):
    name = models.CharField(max_length=50)
    flavor = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('treats_detail', kwargs={'pk': self.id})

## THE NEXT SECTION IS HERE:
# https://seir-222-sasquatch.netlify.app/second-language/week-21/day-3/lecture-materials/intro-to-django-authentication-and-authorization#update-the-cat-model:~:text=in%20Cat%20Collector.-,Update%20the%20CatModel,-Adding%20the%20relationship
## AUTHENTICATION AND AUTHORIZATION
class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    treats = models.ManyToManyField(FavoriteTreat)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def fed_for_today(self):
        return self.meal_set.filter(date=date.today()).count() >= len(MEALS)

    def get_absolute_url(self):
        return reverse("detail", kwargs={"dog_id": self.id})


class Meal(models.Model):
    date = models.DateField('Feeding Date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )

    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"

    class Meta:
        ordering = ['-date']


class Photo(models.Model):
    url = models.CharField(max_length=200)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for dog_id: {self.dog_id} @ {self.url}"

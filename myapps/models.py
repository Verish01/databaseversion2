from django.db import models

# Create your models here.
class Inventory(models.Model):
    product_name=models.CharField(max_length=30,null=False,blank=False)
    cost_per_item=models.DecimalField(max_digits=12,decimal_places=2,null=False,blank=False)
    quantity_in_stock=models.IntegerField(null=False,blank=False)
    quantity_sold=models.IntegerField(null=False,blank=False)
    sales=models.DecimalField(max_digits=12,decimal_places=2,null=False,blank=False)
    stock_date=models.DateField()
    photos=models.ImageField(upload_to="Inventph/")

    def __str__(self):
        return self.product_name

class Weather(models.Model):
    formatted_date = models.DateTimeField()
    summary = models.CharField(max_length=200)
    precip_type = models.CharField(max_length=50, null=True, blank=True)
    temperature_c = models.FloatField()
    apparent_temperature_c = models.FloatField()
    humidity = models.FloatField()
    wind_speed_kmh = models.FloatField()
    wind_bearing_degrees = models.IntegerField()
    visibility_km = models.FloatField()
    loud_cover = models.FloatField()
    pressure_millibars = models.FloatField()
    daily_summary = models.TextField()

    def __str__(self):
        return self.precip_type
    
from django.db import models

class Movie(models.Model):
    poster_link = models.URLField()
    series_title = models.CharField(max_length=255)
    released_year = models.CharField(max_length=10)
    certificate = models.CharField(max_length=10)
    runtime = models.CharField(max_length=50)
    genre = models.CharField(max_length=255)
    imdb_rating = models.FloatField()
    overview = models.TextField()
    meta_score = models.CharField(max_length=10, null=True)
    director = models.CharField(max_length=255)
    star1 = models.CharField(max_length=255)
    star2 = models.CharField(max_length=255)
    star3 = models.CharField(max_length=255)
    star4 = models.CharField(max_length=255)
    no_of_votes = models.IntegerField()
    gross = models.CharField(max_length=255)  # Gross is a string due to commas and other characters

    def __str__(self):
        return self.series_title


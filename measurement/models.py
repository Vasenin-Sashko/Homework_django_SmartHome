from django.db import models

# Модель сенсоров
class Sensor(models.Model):
    name_sensor = models.CharField(max_length=50)
    description_sensor = models.TextField(max_length=200)
# Модель измерений
class Measurement(models.Model):
    id_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temp_measurement = models.DecimalField(max_digits=5, decimal_places=2)
    date_measurement = models.DateTimeField(auto_now_add=True)


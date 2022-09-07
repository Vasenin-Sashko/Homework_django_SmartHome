from dataclasses import field
from pyexpat import model
from rest_framework import serializers

from measurement.models import Measurement, Sensor

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['id_sensor','temp_measurement', 'date_measurement']

class SensorSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name_sensor', 'description_sensor', 'measurements']


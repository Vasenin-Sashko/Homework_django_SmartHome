from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from measurement.models import Sensor
from measurement.serializers import MeasurementSerializer, SensorSerializer

# Получение списка датчиков и создание датчиков
class SensorView(ListCreateAPIView):
    serializer_class = SensorSerializer

    def get_queryset(self):
        queryset = Sensor.objects.all()
        return queryset

    def perform_create(self, serializer):
        serializer.save()

# Обновление датчиков
class UpdateSensorView(RetrieveUpdateAPIView):
    serializer_class = SensorSerializer

    def get_queryset(self):
        queryset = Sensor.objects.all()
        return queryset

    def perform_update(self, serializer):
        serializer.save()

# Создание измерений
class MeasurementView(CreateAPIView):
    serializer_class = MeasurementSerializer

    def perform_update(self, serializer):
        serializer.save()
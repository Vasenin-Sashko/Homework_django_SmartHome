from django.urls import path

from measurement.views import SensorView, UpdateSensorView, MeasurementView

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', UpdateSensorView.as_view()),
    path('measurements/', MeasurementView.as_view())
]

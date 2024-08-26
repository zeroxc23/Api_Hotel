from rest_framework import serializers
from .models import Habitaciones, TipoHabitaciones

class TipoHabitacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoHabitaciones
        fields = '__all__'

class HabitacionesSerializer(serializers.ModelSerializer):
    id_tipo_hab = TipoHabitacionesSerializer()

    class Meta:
        model = Habitaciones
        fields = '__all__'

    def create(self, validated_data):
        id_tipo_hab_data = validated_data.pop('id_tipo_hab')
        id_tipo_hab = TipoHabitaciones.objects.create(**id_tipo_hab_data)
        habitacion = Habitaciones.objects.create(id_tipo_hab=id_tipo_hab, **validated_data)
        return habitacion

    def update(self, instance, validated_data):
        id_tipo_hab_data = validated_data.pop('id_tipo_hab', None)
        if id_tipo_hab_data:
            id_tipo_hab_serializer = self.fields['id_tipo_hab']
            instance_id_tipo_hab = instance.id_tipo_hab
            id_tipo_hab_serializer.update(instance_id_tipo_hab, id_tipo_hab_data)
        
        return super().update(instance, validated_data)
    
    

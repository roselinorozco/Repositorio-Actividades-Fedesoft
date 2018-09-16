from rest_framework import serializers
from appSoyEco.models import Usuario 

class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = ('id_user','nombre','apellido','correo','name_user','password')
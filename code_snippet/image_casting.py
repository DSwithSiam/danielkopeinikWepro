import base64
import uuid
from django.core.files.base import ContentFile
from rest_framework import serializers

class Base64ImageField(serializers.ImageField):
    """
    A DRF ImageField for handling base64-encoded images (all extensions supported).
    """

    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            try:
                format, imgstr = data.split(';base64,')
                ext = format.split('/')[-1]
            except ValueError:
                raise serializers.ValidationError("Invalid image data format.")

            file_name = f"{uuid.uuid4()}.{ext}"

            try:
                decoded_file = base64.b64decode(imgstr)
            except (base64.binascii.Error, ValueError):
                raise serializers.ValidationError("Invalid base64 image data.")

            data = ContentFile(decoded_file, name=file_name)

        return super().to_internal_value(data)

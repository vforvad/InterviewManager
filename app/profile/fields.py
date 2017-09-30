from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers
from attachments.serializers import AttachmentBaseSerializer
import ipdb

class AttachmentField(serializers.Field):
    """ Custom field for 'attachment' attribute in request """

    def get_attribute(self, obj):
        return AttachmentBaseSerializer(obj.attachments.last()).data

    def to_representation(self, obj):
        return obj

    def to_internal_value(self, data):
        return data

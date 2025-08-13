from urllib.parse import urlparse

from rest_framework.serializers import ValidationError


def validate_url(url_on_video):
    """ Проверка YouTube-ссылок """

    allowed = ["youtube.com", "www.youtube.com", "youtu.be"]
    domain = urlparse(url_on_video.lower()).netloc  # Извлечение домена netloc

    if domain not in allowed: # проверка, если домена нет в списке
        raise ValidationError("Требуются только ссылки на YouTube")

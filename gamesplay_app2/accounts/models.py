
from django.contrib.auth import models as auth_models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Profile(auth_models.AbstractUser):
    AGE_MIN = 12
    PASSWORD_MAX_LEN = 30
    FIRST_NAME_MAX_LEN = 30
    LAST_NAME_MAX_LEN = 30

    email = models.EmailField()

    age = models.IntegerField(
        validators=(
            MinValueValidator(AGE_MIN),
        )
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

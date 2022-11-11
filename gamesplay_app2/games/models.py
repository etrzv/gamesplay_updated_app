from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify

UserModel = get_user_model()


class Game(models.Model):
    ACTION = 'Action'
    ADVENTURE = 'Adventure'
    PUZZLE = 'Puzzle'
    STRATEGY = 'Strategy'
    SPORTS = 'Sports'
    BOARD_CARD_GAME = 'Board/Card Game'
    OTHER = 'Other'

    CHOICES = [(x, x) for x in (ACTION, ADVENTURE, PUZZLE, STRATEGY, SPORTS, BOARD_CARD_GAME, OTHER)]

    TITLE_MAX_LEN = 30
    CATEGORY_MAX_LEN = 15
    RATING_MIN = 0.1
    RATING_MAX = 5.0
    MAX_LEVEL_MIN = 1

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
        unique=True,
    )

    category = models.CharField(
        max_length=CATEGORY_MAX_LEN,
        choices=CHOICES,
    )

    rating = models.FloatField(
        validators=(
            MinValueValidator(RATING_MIN),
            MaxValueValidator(RATING_MAX),
        )

    )

    max_level = models.IntegerField(
        validators=(
            MinValueValidator(MAX_LEVEL_MIN),
        )
    )

    image_url = models.URLField()

    summary = models.TextField(
        null=True,
        blank=True,
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )

    def save(self, *args, **kwargs):
        # Create/Update
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.id}-{self.name}')

        # Without the `if` the following scenario might happen:
        # The url is `/pets/4-stamat`
        # Rename `stamat` to `stamata`
        # The new url is `/pets/4-stamata`, but `/pets/4-stamat` does not work

        # Update
        return super().save(*args, **kwargs)

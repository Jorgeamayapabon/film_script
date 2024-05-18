from django.db import models
from apps.user.models import AccountModel, UserModel


# Create your models here.
class FilmScriptModel(models.Model):
    """
    """
    class ACTORGESTURE(models.TextChoices):
        # Positive Emotions
        HAPPY = "Happy/Smiling"
        ENTHUSIASTIC = "Enthusiastic"
        RELIEVED = "Relieved"
        PROUD = "Proud"

        # Negative Emotions
        SAD = "Sad/Depressed"
        ANGRY = "Angry"
        WORRIED = "Worried"
        FRUSTRATED = "Frustrated"

        # Interaction
        LISTENING_ATTENTIVELY = "Listening Attentively"
        ARGUING = "Arguing"
        HUGGING = "Hugging"
        COMFORTING = "Comforting"

        # Action
        RUNNING = "Running"
        JUMPING = "Jumping"
        FIGHTING = "Fighting"
        HIDING = "Hiding"

        # Resting
        SITTING_RELAXED = "Sitting Relaxed"
        SLEEPING = "Sleeping"
        MEDITATING = "Meditating"
        WAITING = "Waiting"

        # Dramatic
        FAINTING = "Fainting"
        EXTREME_SURPRISE = "Extreme Surprise"
        LOVE_DECLARATION = "Love Declaration"
        SAD_FAREWELL = "Sad Farewell"

        # Specific Context
        ON_PHONE = "On the Phone"
        READING_BOOK = "Reading a Book"
        WRITING = "Writing"
        COOKING = "Cooking"
    
    class ACTORLOCATION(models.TextChoices):
        # Predefined Locations
        LOCATION_1 = "0,0,0,0,0,0", "Location 1: (x=0, y=0, z=0, rx=0, ry=0, rz=0)"
        LOCATION_2 = "1,1,1,10,10,10", "Location 2: (x=1, y=1, z=1, rx=10, ry=10, rz=10)"
        LOCATION_3 = "2,2,2,20,20,20", "Location 3: (x=2, y=2, z=2, rx=20, ry=20, rz=20)"
        LOCATION_4 = "3,3,3,30,30,30", "Location 4: (x=3, y=3, z=3, rx=30, ry=30, rz=30)"
        LOCATION_5 = "4,4,4,40,40,40", "Location 5: (x=4, y=4, z=4, rx=40, ry=40, rz=40)"
        LOCATION_6 = "5,5,5,50,50,50", "Location 6: (x=5, y=5, z=5, rx=50, ry=50, rz=50)"

    author = models.ForeignKey(
        UserModel,
        verbose_name="author",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        help_text="Script author",
    )
    
    account = models.ForeignKey(
        AccountModel,
        verbose_name="account",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        help_text="Script account",
    )
    
    title = models.CharField(
        "Title",
        max_length=45,
        null=False,
        blank=False,
    )
    
    genre = models.CharField(
        "Genre",
        max_length=45,
        null=False,
        blank=False,
    )
    
    uuid = models.CharField(
        "uuid",
        max_length=45,
        null=False,
        blank=False,
    )
    
    actor_location = models.CharField(
        "Actor location",
        max_length=60,
        choices=ACTORLOCATION.choices,
    )
    
    actor_gesture = models.CharField(
        "Actor gesture",
        max_length=60,
        choices=ACTORGESTURE.choices,
    )
    
    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        db_table = "film_script"
        verbose_name = "filmscript"
        verbose_name_plural = "film scripts"
        ordering = ["id"]

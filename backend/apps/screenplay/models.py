from django.db import models

from backend.apps.user.models import User, AccountModel


class FilmScriptModel(models.Model):
    """
    A model representing a film script in the system.

    Attributes:
        owner (UserModel): The author of the script.
        account (AccountModel): The account associated with the script.
        title (str): The title of the film script.
        genre (str): The genre of the film script.
    """
    owner = models.ForeignKey(
        User,
        verbose_name="Owner",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        help_text="Script owner",
        related_name="filmscript_user_owner",
    )
    
    account = models.ForeignKey(
        AccountModel,
        verbose_name="account",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        help_text="Script account",
        related_name="filmscript_account"
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
    
    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        db_table = "film_script"
        verbose_name = "filmscript"
        verbose_name_plural = "filmscripts"
        ordering = ["id"]


class SceneModel(models.Model):
    """
    A model representing a Scene in the system.

    Attributes:
        film_script (FilmScriptModel): The film script of the scene.
        name (str): The name of the scene.
        actor_name (str): The actor's name of the scene.
        actor_location (str): The location of the actor in the scene.
        actor_gesture (str): The gesture or action of the actor in the scene.
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

    film_script = models.ForeignKey(
        FilmScriptModel,
        verbose_name="film_script",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        help_text="Film script",        
    )
    
    name = models.CharField(
        "name",
        max_length=45,
        null=False,
        blank=False,
    )
    
    actor_name = models.CharField(
        "Actor name",
        max_length=45,
        null=False,
        blank=False,
    )
    
    actor_location = models.CharField(
        "Actor location",
        max_length=60,
        null=False,
        blank=False,
        choices=ACTORLOCATION.choices,
    )
    
    actor_gesture = models.CharField(
        "Actor gesture",
        max_length=60,
        null=False,
        blank=False,
        choices=ACTORGESTURE.choices,
    )
    
    dialogue = models.TextField(
        "Actor dialogue",
        blank=True,
    )
    
    created_by = models.ForeignKey(
        User,
        verbose_name="Created by",
        on_delete=models.DO_NOTHING,
        null=False,
        blank=False,
        help_text="Scene creator",
        related_name="scene_user_creator",
    )
    
    updated_by = models.ForeignKey(
        User,
        verbose_name="Updated by",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Scene updater",
        related_name="scene_user_updater",
    )
    
    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        db_table = "scene"
        verbose_name = "Scene"
        verbose_name_plural = "Scenes"
        ordering = ["id"]


class HistoricSceneModel(models.Model):
    """
    A model representing a historic scene in the system.

    Attributes:
        scene (SceneModel): The scene of the historic.
        updated_by (UserModel): The user updater of the scene.
        update_at (DateTimeField): The update datetime of the scene.
    """
    scene = models.ForeignKey(
        SceneModel,
        verbose_name="Scene",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        help_text="Historic scene",
    )

    updated_by = models.ForeignKey(
        User,
        verbose_name="Updated by",
        on_delete=models.DO_NOTHING,
        null=False,
        blank=False,
        help_text="Scener updater",
        related_name="historic_user_updater",
    )

    update_at = models.DateTimeField(
        "Updated at",
        auto_now=True,
    )

    class Meta:
        db_table = "historic_scene"
        verbose_name = "HistoricScene"
        verbose_name_plural = "HistoricScenes"
        ordering = ["id"]

from django.db.models.signals import post_save
from django.dispatch import receiver

from backend.apps.screenplay.models import SceneModel, HistoricSceneModel


@receiver(post_save, sender=SceneModel)
def create_historic_scene(sender, instance: SceneModel, created, **kwargs):
    """
    Signal receiver that creates a HistoricSceneModel entry whenever a SceneModel instance is saved.

    This function is triggered after a SceneModel instance is saved. It creates a corresponding
    HistoricSceneModel entry, capturing the current state of the SceneModel instance for historical purposes.
    The user who performed the last update (or the creator if no update user is specified) is recorded.

    Args:
        sender (Type[SceneModel]): The model class that sent the signal.
        instance (SceneModel): The instance of SceneModel that was saved.
        created (bool): A boolean indicating whether a new record was created.
        **kwargs: Additional keyword arguments.

    Attributes:
        updated_by (User): The user who performed the last update on the SceneModel instance.
                           Defaults to the creator if no update user is specified.

    Models:
        HistoricSceneModel: The model used to store historical data for SceneModel instances.
    """
    updated_by = instance.updated_by if instance.updated_by else instance.created_by
    HistoricSceneModel.objects.create(
        scene=instance,
        updated_by=updated_by
    )

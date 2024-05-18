from django.db import models


# Create your models here.
class UserModel(models.Model):
    """
    """
    fullname = models.CharField(
        "Fullname",
        max_length=60,
        null=False,
        blank=False,
    )
    
    email = models.CharField(
        "Email",
        max_length=60,
        null=False,
        blank=False,
    )
    
    def __str__(self) -> str:
        return f"{self.fullname}"

    class Meta:
        db_table = "user"
        verbose_name = "user"
        verbose_name_plural = "users"
        ordering = ["id"]


class AccountModel(models.Model):
    """
    """
    uuid = models.CharField(
        "uuid",
        max_length=45,
        null=False,
        blank=False,
    )
    
    name = models.CharField(
        "Name",
        max_length=45,
        null=False,
        blank=False,
    )
    
    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        db_table = "account"
        verbose_name = "Account"
        verbose_name_plural = "Accounts"
        ordering = ["id"]


class UserAccountRel(models.Model):
    """
    """
    class USERTYPE(models.TextChoices):
        OWNER = "Owner"
        SCREENWRITER = "Screenwriter"
        VIEWER = "Viewer"
    
    user_id = models.ForeignKey(
        UserModel,
        verbose_name="author",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        help_text="Script author",
    )
    
    account_id = models.ForeignKey(
        AccountModel,
        verbose_name="account",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        help_text="Script account",
    )
    
    user_type = models.CharField(
        "User type",
        max_length=45,
        choices=USERTYPE.choices,
    )

from django.db import models


class UserModel(models.Model):
    """
    A model representing a user in the system.

    Attributes:
        fullname (str): The full name of the user.
        email (str): The email address of the user.
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
    A model representing an account in the system.

    Attributes:
        uuid (str): Unique identifier for the account (up to 45 characters).
        name (str): The name of the account (up to 45 characters).
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
    A model representing the relationship between users and accounts in the system.

    Attributes:
        user_id (UserModel): The user associated with the account.
        account_id (AccountModel): The account associated with the user.
        user_type (str): The role of the user in the account. Choices are 'Owner', 'Screenwriter', or 'Viewer'.
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

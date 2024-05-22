import uuid
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)


class UserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError("Miss email")

        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password)
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    
    objects = UserManager()
    
    USERNAME_FIELD = "email"

    def __str__(self) -> str:
        return f"{self.name}"
    

class AccountModel(models.Model):
    """
    A model representing an account in the system.

    Attributes:
        uuid (str): Unique identifier for the account (up to 45 characters).
        name (str): The name of the account (up to 45 characters).
    """
    uuid = models.UUIDField(
        "uuid",
        auto_created=True,
        editable=False,
        default=uuid.uuid4()
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
        user (UserModel): The user associated with the account.
        account (AccountModel): The account associated with the user.
        user_type (str): The role of the user in the account. Choices are 'Owner', 'Screenwriter', or 'Viewer'.
    """
    class USERTYPE(models.TextChoices):
        OWNER = "Owner"
        SCREENWRITER = "Screenwriter"
        VIEWER = "Viewer"

    user = models.ForeignKey(
        User,
        verbose_name="author",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        help_text="Script author",
        related_name="user_account_rel"
    )

    account = models.ForeignKey(
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
        default=USERTYPE.VIEWER
    )

from django.db import models
from django.contrib.auth.models import {
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
}

class Usuario(AbstractBaseUser, PermissionsMixin):
        
        email=models.EmailField(
            verbose_name="E-mail do usuário",
            max_length=194,
            unique=True
        )

        is_active = models.BooleanField(
                verbose_name="Usuário esta ativo"
                default=True
        )

        is_staf = models.BooleanField(
                verbose_name="Usuário é da equipe de desenvolvimento"
                default=False
        )

        is_superuser = models.BooleanField(
                verbose_name="Usuário é superusuário"
                default=False
        )

        USERNAME_FIELD = "email"

        class Meta:
                verbose_name="Usuário"
                verbose_name_plural="Usuários"
                db_table="usuario"

        def __str__(self) -> str:
                return self.email
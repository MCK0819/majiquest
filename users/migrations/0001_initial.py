# Generated by Django 4.2.11 on 2024-04-05 02:33

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Specifies automatic assignment of all permissions.",
                        verbose_name="superuser status",
                    ),
                ),
                ("ID", models.CharField(max_length=150, unique=True)),
                ("nickname", models.CharField(max_length=150)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("last_login", models.DateTimeField(blank=True, null=True)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                ("rank", models.CharField(blank=True, max_length=50, null=True)),
                ("rating", models.FloatField(default=0)),
                (
                    "groups",
                    models.ManyToManyField(
                        related_name="custom_users", to="auth.group"
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True, related_name="custom_users", to="auth.permission"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
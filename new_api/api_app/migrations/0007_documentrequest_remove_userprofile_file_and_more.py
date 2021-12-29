# Generated by Django 4.0 on 2021-12-23 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api_app", "0006_userwantrequest_status_request_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="DocumentRequest",
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
                ("time", models.DateTimeField(auto_now_add=True)),
                (
                    "status_request",
                    models.CharField(
                        choices=[
                            ("INITIATED_STATUS", "initiated"),
                            ("RECEIVED_STATUS", "received"),
                        ],
                        default=1,
                        max_length=50,
                    ),
                ),
                ("file", models.FileField(blank=True, null=True, upload_to="media/")),
                (
                    "from_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="from_user_received",
                        to="api_app.user",
                    ),
                ),
                (
                    "to_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="to_user_sent",
                        to="api_app.user",
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="file",
        ),
        migrations.DeleteModel(
            name="UserWantRequest",
        ),
    ]

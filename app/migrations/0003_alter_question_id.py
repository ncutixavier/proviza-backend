# Generated by Django 4.1.5 on 2023-01-05 21:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_question_created_at_question_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
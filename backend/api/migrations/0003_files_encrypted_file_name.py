# Generated by Django 4.2.5 on 2023-10-22 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_files_encryptedfilename'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='encrypted_file_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
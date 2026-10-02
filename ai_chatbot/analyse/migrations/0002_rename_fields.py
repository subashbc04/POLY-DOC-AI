from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyse', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='analyse',
            old_name='description',
            new_name='queries',
        ),
        migrations.RenameField(
            model_name='analyse',
            old_name='resume',
            new_name='document',
        ),
        migrations.AlterField(
            model_name='analyse',
            name='document',
            field=models.FileField(upload_to='doc/'),
        ),
    ]
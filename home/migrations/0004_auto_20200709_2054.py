
from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('home', '0003_auto_20200709_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='slug',
            field=models.CharField(default='', max_length=1000),
      
        ),
    ]


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200709_2054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=50000)),
                ('name', models.CharField(max_length=900)),
                ('email', models.CharField(max_length=1101)),
                ('address', models.CharField(max_length=1101)),
                ('city', models.CharField(max_length=1101)),
                ('state', models.CharField(max_length=1101)),
                ('zip_code', models.CharField(max_length=1011)),
                ('phone', models.CharField(default='', max_length=1011)),
      
      
            ],
        ),
    ]

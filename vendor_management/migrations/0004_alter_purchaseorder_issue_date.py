# Generated by Django 5.0.4 on 2024-05-06 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_management', '0003_alter_purchaseorder_issue_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='issue_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

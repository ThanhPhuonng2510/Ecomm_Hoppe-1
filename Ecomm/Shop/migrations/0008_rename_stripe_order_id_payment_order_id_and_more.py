# Generated by Django 4.1.5 on 2023-02-08 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0007_alter_orderplaced_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='stripe_order_id',
            new_name='order_id',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='stripe_payment_id',
            new_name='payment_options',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='stripe_payment_status',
            new_name='payment_status',
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Packed', 'Packed'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel'), ('Pending', 'Pending'), ('On The Way', 'On The Way'), ('Accepted', 'Accepted')], default='Pending', max_length=50),
        ),
    ]

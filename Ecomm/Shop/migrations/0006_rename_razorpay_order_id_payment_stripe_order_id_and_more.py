# Generated by Django 4.1.5 on 2023-02-06 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0005_alter_cart_quantity_alter_orderplaced_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='razorpay_order_id',
            new_name='stripe_order_id',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='razorpay_payment_id',
            new_name='stripe_payment_id',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='razorpay_payment_status',
            new_name='stripe_payment_status',
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('On The Way', 'On The Way'), ('Packed', 'Packed'), ('Accepted', 'Accepted'), ('Cancel', 'Cancel'), ('Pending', 'Pending'), ('Delivered', 'Delivered')], default='Pending', max_length=50),
        ),
    ]
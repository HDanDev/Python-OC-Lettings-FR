from django.db import migrations

def copy_lettings_data(apps, schema_editor):
    """
    Copies data from the 'oc_lettings_site' app's Address and Letting models
    to the corresponding models in the 'lettings' app.

    This function retrieves all records from the old Address and Letting models,
    and creates equivalent entries in the new models, preserving IDs and field values.

    Args:
        apps: An instance of the Django application registry used to get historical models.
        schema_editor: A database schema editor for executing SQL commands if needed.

    Notes:
        - This is intended to be used as a data migration step.
        - Assumes that the schemas for both the old and new models are compatible.
    """

    OldAddress = apps.get_model('oc_lettings_site', 'Address')
    OldLetting = apps.get_model('oc_lettings_site', 'Letting')
    NewAddress = apps.get_model('lettings', 'Address')
    NewLetting = apps.get_model('lettings', 'Letting')

    for old_address in OldAddress.objects.all():
        NewAddress.objects.create(
            id=old_address.id,
            number=old_address.number,
            street=old_address.street,
            city=old_address.city,
            state=old_address.state,
            zip_code=old_address.zip_code,
            country_iso_code=old_address.country_iso_code
        )

    for old_letting in OldLetting.objects.all():
        NewLetting.objects.create(
            id=old_letting.id,
            title=old_letting.title,
            address=NewAddress.objects.get(id=old_letting.address.id)
        )

class Migration(migrations.Migration):
    """
    Migration class to copy data from the 'oc_lettings_site' app
    to the new 'lettings' app as part of the migration process.

    This ensures that all existing letting and address data is
    preserved during the app refactoring or restructuring.
    """

    dependencies = [
        ('lettings', '0001_initial'),
        ('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(copy_lettings_data),
    ]

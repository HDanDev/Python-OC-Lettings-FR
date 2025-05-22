from django.db import migrations

def copy_profiles_data(apps, schema_editor):
    """
    Copies Profile data from the 'oc_lettings_site' app to the 'profiles' app.

    This function migrates all Profile entries from the old app by creating
    corresponding entries in the new 'profiles' app. It ensures that user 
    relationships and profile details such as 'favorite_city' are preserved.

    Args:
        apps: Django app registry used to retrieve historical versions of models.
        schema_editor: Schema editor for executing SQL or schema-level operations.

    Notes:
        - This migration assumes that the related User entries already exist and 
          have the same IDs.
        - It preserves primary keys to maintain relationships and data integrity.
    """

    OldProfile = apps.get_model('oc_lettings_site', 'Profile')
    NewProfile = apps.get_model('profiles', 'Profile')
    User = apps.get_model('auth', 'User')

    for old_profile in OldProfile.objects.all():
        NewProfile.objects.create(
            id=old_profile.id,
            user=User.objects.get(id=old_profile.user.id),
            favorite_city=old_profile.favorite_city
        )

class Migration(migrations.Migration):
    """
    Data migration that transfers Profile records from the 'oc_lettings_site' app
    to the new 'profiles' app.

    This migration is part of a broader app restructuring process aimed at modularizing
    the application. It ensures that all user profile data is successfully moved to 
    the new app namespace while maintaining existing user associations.
    """

    dependencies = [
        ('profiles', '0001_initial'),
        ('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(copy_profiles_data),
    ]

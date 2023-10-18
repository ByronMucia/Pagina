# autenticacion/signals.py
'''
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Group

@receiver(post_save, sender=User)
def asignar_grupo_estudiantes(sender, instance, created, **kwargs):
    if created:
        estudiantes_group = Group.objects.get(name='estudiantes')
        instance.groups.add(estudiantes_group)'''
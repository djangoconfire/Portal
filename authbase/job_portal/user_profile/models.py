from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User 



class UserProfile( models.Model ):
    
    user        = models.OneToOneField( User)
    # is_applied  = models.NullBooleanField(blank=True,null=True)

    def __str__( self ):
        return str( self.user.username)


    class Meta :
        ordering = ['user']


   


from django.db import models
from profiles.models import Profile

# Create your models here.
class FriendRequest(models.Model):
    from_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='friend_request_from_profile'
    )
    to_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='friend_request_to_profile'
    )
    
    accepted = models.BooleanField(default=False)
    declined = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.from_profile} to {self.to_profile}'
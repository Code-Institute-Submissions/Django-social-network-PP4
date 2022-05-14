from django.shortcuts import render
from django.views import View
from django.db.models import Q
from .models import (
    PostEvent,
    CommentEvent,
    LikeDislikeEvent,
    FriendRequestEvent,
    FriendEvent,
    RemoveFriendEvent,
    CommunityJoinEvent,
    CommunityLeaveEvent,
    CommunityCreateEvent,
    CommunityDeleteEvent
)

# Create your views here.
class FeedView(View):
    def get(self, request, *args, **kwargs):
        # get all post events for the user where the initiator is the user or a friend of the user
        post_events = PostEvent.objects.filter(
            Q(initiator=request.user) |
            Q(initiator__profile__in=request.user.profile.friends.all())
        )
        comment_events = CommentEvent.objects.filter(
            Q(initiator=request.user) |
            Q(initiator__profile__in=request.user.profile.friends.all())
        )
        like_dislike_events = LikeDislikeEvent.objects.filter(
            Q(initiator=request.user) |
            Q(initiator__profile__in=request.user.profile.friends.all()) |
            Q(post__author=request.user) |
            Q(comment__author=request.user)
        )
        friend_request_events = FriendRequestEvent.objects.filter(
            Q(initiator=request.user) |
            Q(target=request.user) |
            Q(initiator__profile__in=request.user.profile.friends.all())
        )
        friend_events = FriendEvent.objects.filter(
            Q(initiator=request.user) |
            Q(target=request.user) |
            Q(initiator__profile__in=request.user.profile.friends.all()) |
            Q(target__profile__in=request.user.profile.friends.all())
        )
        remove_friend_events = RemoveFriendEvent.objects.filter(
            Q(initiator=request.user) |
            Q(target=request.user) |
            Q(initiator__profile__in=request.user.profile.friends.all()) |
            Q(target__profile__in=request.user.profile.friends.all())
        )
        community_join_events = CommunityJoinEvent.objects.filter(
            Q(initiator=request.user) |
            Q(initiator__profile__in=request.user.profile.friends.all())
        )
        community_leave_events = CommunityLeaveEvent.objects.filter(
            Q(initiator=request.user) |
            Q(initiator__profile__in=request.user.profile.friends.all())
        )
        community_create_events = CommunityCreateEvent.objects.filter(
            Q(initiator=request.user) |
            Q(initiator__profile__in=request.user.profile.friends.all())
        )
        community_delete_events = CommunityDeleteEvent.objects.filter(
            Q(initiator=request.user) |
            Q(initiator__profile__in=request.user.profile.friends.all()) |
            Q(community__members=request.user)
        )
        # now we need to merge all the events into one list and sort them by -timestamp
        all_events = []
        all_events.extend(post_events)
        all_events.extend(comment_events)
        all_events.extend(like_dislike_events)
        all_events.extend(friend_request_events)
        all_events.extend(friend_events)
        all_events.extend(remove_friend_events)
        all_events.extend(community_join_events)
        all_events.extend(community_leave_events)
        all_events.extend(community_create_events)
        all_events.extend(community_delete_events)
        # sort the events
        all_events.sort(key=lambda x: x.timestamp, reverse=True)
        return render(request, 'feed/feed.html', {'events': all_events})

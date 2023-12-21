from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from server.user.interface import User
from server.context import Context


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin, form=None):
        super().save_user(request, sociallogin, form)
        user = sociallogin.user
        User.create(
            Context(elevated=True),
            group='other',
            user=user,
            email=user.email,
        )
        return user

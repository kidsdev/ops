from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied


def permission_required(perm, login_url=None, raise_exception=False):
    # ref: https://docs.djangoproject.com/en/2.0/_modules/django/contrib/auth/decorators/#permission_required
    def check_perms(user):
        if isinstance(perm, str):
            perms = (perm,)
        else:
            perms = perm

        for _ in perms:
            if user.has_perm(_):
                return True
        # First check if the user has the permission (even anon users)
        # if user.has_perms(perms):
        #     return True
        # In case the 403 handler should be called raise the exception
        if raise_exception:
            raise PermissionDenied
        # As the last resort, show the login form
        return False

    return user_passes_test(check_perms, login_url=login_url)

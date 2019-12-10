"""
URL conf for user activation, using the ng-utils invite registration backend.

If the default behavior of these views is acceptable to you, simply use a line like this
in your root URLconf to set up the default URLs for registration::

    (r'^', include('itng.registration.backends.invite.urls.activation')),

If you'd like to customize registration behavior, feel free to set up
your own URL patterns for these views instead.

"""

from django.urls import re_path, path

from itng.registration.backends.invite import views


urlpatterns = [
    path('activate/complete/', views.ActivationCompleteView.as_view(), name='activation_complete'),
    # Activation keys get matched by \w+ instead of the more specific
    # [a-fA-F0-9]{40} because a bad activation key should still get to the view;
    # that way it can return a sensible "invalid key" message instead of a
    # confusing 404.
    # The activation key can make use of any character from the
    # URL-safe base64 alphabet, plus the colon as a separator.
    path('activate/(?P<activation_key>[-:\w]+)/', views.ActivationView.as_view(), name='activate'),
]

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # disable x/ path during deployment
    path('x', admin.site.urls),
    path('', views.FrontPage, name="main-frontpage-url"),
    path('auth/', include('authentication.urls')),
    path('dashboard/', views.Dashboard, name="main-dashboard-url"),
]

handler404 = 'utilities.views.handle_404'
handler500 = 'utilities.views.handle_500'

# links
# .../auth/ = authentication
# .../c/ = candidate (view profile)
# .../e/ = election (management)
# .../public-election/ = public election
# .../private-election/ = private election

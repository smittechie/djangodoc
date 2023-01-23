from django.urls import path

from . import views

app_name = 'm2m'

urlpatterns=[
    path('pgmmember/', views.PGM_Group.as_view(), name='pgmmember'),  ## Member form
    path('pgmpersonresult/', views.PGMPersonresult.as_view(), name='pgmpersonresult'),
    path('pgmgroupresult/', views.PGMGroupresult.as_view(), name='pgmgroupresult'),
    # path('pgmoptions/', views.PGMOptions.as_view(), name='pgmoptions'),  ## options to select
]
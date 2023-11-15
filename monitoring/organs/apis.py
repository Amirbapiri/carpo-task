from rest_framework.views import APIView

from django.contrib.auth import get_user_model



# Now I want to create an instance of Organ only if user was role of SYSADMIN
User = get_user_model()


class OrganAPI(APIView):
    pass

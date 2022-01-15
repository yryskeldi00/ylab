from rest_framework.generics import (
    CreateAPIView, UpdateAPIView, RetrieveAPIView,
)
from rest_framework.response import Response

from main.models import BankAccount
from main.serializers import (
    BankAccountCreateSerializer, BankAccountRetrieveSerializer,
    BankAccountUpdateSerializer
)


class BankAccountCreateAPIView(CreateAPIView):
    """
    Endpoint for creating Bank Account
    """
    serializer_class = BankAccountCreateSerializer


class BankAccountUpdateAPIView(UpdateAPIView):
    """
    Endpoint for updating Bank Account
    """
    serializer_class = BankAccountUpdateSerializer
    queryset = BankAccount.objects.all()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response({'money': request.data.get('money')})


class BankAccountRetrieveAPIViewAPIView(RetrieveAPIView):
    """
    Endpoint for detail Bank Account
    """
    serializer_class = BankAccountRetrieveSerializer
    queryset = BankAccount.objects.all()

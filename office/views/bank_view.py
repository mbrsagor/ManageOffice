from rest_framework.response import Response
from django_filters import rest_framework as filters
from rest_framework import viewsets, permissions, views

from office.models import Bank
from office.serializers.bank_serailizer import BankSerializer
from office.pagination import StandardResultsSetPagination
from office.filter import BankFilter


class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    permission_classes = [permissions.IsAdminUser]
    pagination_class = StandardResultsSetPagination
    filterset_class = BankFilter
    filter_backends = (filters.DjangoFilterBackend,)

    # API URL: /api/v1/bank/
    """
        {
            "name": "Bank Name",
            "is_active": true
        }
    """


# class OfferCrateView(views.View):
#     def post(self, request, *args, **kwargs):
#         access = self.request.user.role
#         if access == enum_utils.allow_access_consumer:
#             try:
#                 serializer = offer_serializer.OfferRatingSerializer(data=request.data)
#                 if serializer.is_valid(raise_exception=True):
#                     serializer.save(consumer=self.request.user)
#                     # Rating added point will add to consumer account
#                     consumer = User.objects.get(id=self.request.user.id)
#                     points = 5.00
#                     consumer.points = F('points') + points
#                     consumer.save()
#                     return Response(response.prepare_success_response(messages.OFFER_SAVE), status=status.HTTP_200_OK)
#                 return Response(response.prepare_error_response(serializer.errors), status=status.HTTP_404_NOT_FOUND)
#             except Exception as ex:
#                 return Response(response.prepare_error_response(str(ex)), status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response(response.prepare_error_response(messages.PERMISSION_MSG))

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


"""
class RemoveMemberAPIView(views.APIView):

    def delete(self, reqeust, pk):
        try:
            access = self.request.user.role
            action = reqeust.data.get('action')  # Action get from reqeust
            if access == enum_utils.allow_access_consumer or access == self.request.user.is_superuser:
                member = Member.objects.get(id=pk)
                if member is not None:
                    if action == 1:
                        member.delete()
                        return Response(response.prepare_success_response(messages.REMOVE_MERCHANT),
                                        status=status.HTTP_200_OK)
                    if action == 2:
                        member.delete()
                        return Response(response.prepare_success_response(messages.REQUEST_CANCEL_MERCHANT),
                                        status=status.HTTP_200_OK)
                return Response(response.prepare_error_response(messages.NO_CONTENT_FOUND), status=status.HTTP_200_OK)
            else:
                return Response(response.prepare_error_response(messages.PERMISSION_MSG), status=status.HTTP_200_OK)
        except Member.DoesNotExist:
            return Response(response.prepare_error_response(messages.ERROR_COMMON))
"""

from rest_framework import views, status
from rest_framework.response import Response

from utils.response import prepare_success_response


class CrewOrderSearchByCalender(views.APIView):
    """
    Name: Crew order/issue search by calendar
    Desc: Worker/Crew can search all of complete or incomplete works/issues using calendar widget.
    """
    queryset = AssignIssue.objects.all()
    serializer_class = serializers.AssignIssueListSerializer

    def get(self, request, *args, **kwargs):
        get_data = request.query_params  # or request.GET check both
        assign_issue = AssignIssue.objects.filter(crew=self.request.user, date=get_data['date'])
        serializer = serializers.AssignIssueListSerializer(assign_issue, many=True)
        issues = []
        for obj in serializer.data:
            data = {
                'id': obj['id'],
                'issue': obj['issue'],
                'issue_name': obj['issue_name'],
                'date': obj['date'],
                'status': obj['status'],
                'duration': obj['duration'],
            }
            issues.append(data)
        return Response(prepare_success_response(issues), status=status.HTTP_200_OK)


class OfferListFilterAPIView(generics.ListAPIView):
    queryset = Offer.objects.all()
    serializer_class = offer_serializer.OfferSerializer
    pagination_class = OfferPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ['is_publish']

    def get_queryset(self):
        queryset = Offer.objects.all()
        is_save = self.request.query_params.get("is_save")
        if is_save is not None:
            queryset = queryset.filter(offers__isnull=False)
        return queryset

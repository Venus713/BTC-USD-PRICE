from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Quote
from .pagenation import BasicPagination, PaginationHandlerMixin
from .permissions import ApiKeyAuth
from .serializers import QuoteSerializer
from .utils import get_exchange_data, save_exchange_data


class QuoteView(APIView, PaginationHandlerMixin):
    permission_classes = (ApiKeyAuth,)
    pagination_class = BasicPagination
    serializer_class = QuoteSerializer

    def get(self, request, format=None, *args, **kwargs):
        instance = Quote.objects.all()
        page = self.paginate_queryset(instance)
        if page is not None:
            serializer = self.get_paginated_response(
                self.serializer_class(page, many=True).data
            )
        else:
            serializer = self.serializer_class(instance, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        exchange_data = get_exchange_data()
        res, data = save_exchange_data(exchange_data)
        if res:
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

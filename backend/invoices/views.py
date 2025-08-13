from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Invoice
from .serializers import InvoiceSerializer

class InvoiceViewSet(ReadOnlyModelViewSet):
    queryset = Invoice.objects.select_related('order', 'order__customer', 'order__service').all()
    serializer_class = InvoiceSerializer

    @action(detail=False, methods=['get'])
    def by_order(self, request):
        order_id = request.query_params.get('order_id')
        if not order_id:
            return Response({"error": "order_id is required"}, status=400)
        try:
            invoice = Invoice.objects.select_related('order').get(order_id=order_id)
            serializer = self.get_serializer(invoice)
            return Response(serializer.data)
        except Invoice.DoesNotExist:
            return Response({"error": "Invoice not found"}, status=404)

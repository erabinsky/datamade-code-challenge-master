import usaddress
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.exceptions import ParseError


class Home(TemplateView):
    template_name = 'parserator_web/index.html'


class AddressParse(APIView):
    renderer_classes = [JSONRenderer]
    def post(self, request):
        # TODO: Flesh out this method to parse an address string using the
        # parse() method and return the parsed components to the frontend. 

        return Response(self.parse(request.data))

    def parse(self, address):
        # TODO: Implement this method to return the parsed components of a
        # given address using usaddress: https://github.com/datamade/usaddress

        try:
            address = usaddress.tag(address)
            address_components = []
            address_type = ''
            for i in address:
                address_components = dict(address[0])
                address_type = address[1]
            return address_components, address_type
        except usaddress.RepeatedLabelError:
            return 'Unable to parse this value due to repeated labels. Our team has been notified of the error.'
        
        

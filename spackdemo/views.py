
from pyspkac import SPKAC
from M2Crypto import EVP, X509
from pyramid.response import Response
from pyramid.view import view_config

@view_config(route_name='home', renderer='templates/home.jinja2')
def home(request):
    return {'account': {'username': request.headers.get('X-ssl-client-s-dn')}}



@view_config(route_name='create_account',
             renderer='templates/create_account.jinja2')
def create_account(request):

    if request.method == 'POST':

        with open('certs/cert-admin.pem', 'r') as pem:
            ca_crt = pem.read()
        cert = X509.load_cert_string(ca_crt)

        with open('certs/key-admin.pem', 'r') as pem:
            ca_pkey = pem.read()
        pkey  = EVP.load_key_string(ca_pkey)

        # ne = X509.new_extension
        email = request.params['email']
        username = request.params['username']
        spkac = SPKAC(request.params['spkac'],
                      None,
                      # ne,
                      CN=username,
                      Email=email
                      )
        serial = 1000  # XXX must be incremented
        try:
            crt = spkac.gen_crt(pkey, cert, serial, hash_algo='sha512')
        except TypeError:
            crt = spkac.gen_crt(pkey, cert, serial)
        response = Response(body=crt.as_pem(),
                            headers={'Accept-Ranges': 'bytes',
                                     'Content-Type': 'application/x-x509-user-cert'
                                     },
                            content_type='application/x-x509-user-cert')
        return response
    return {}

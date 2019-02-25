"""Auth decorator."""

import logging
from flask import request
from flask_restful import abort
import jwt


def authenticate_client(client_entity):
    """Decorator to verify requests from web clients."""
    def func(origin):
        """Inner."""
        def inner(self, *args, **kwargs):
            """Inner."""
            headers = request.headers
            authorization = headers.get('Authorization')

            if not authorization:
                abort(403, message='Unauthorized')

            auth_type, token = authorization.split()

            if auth_type == 'Bearer':
                # Getting secret from model
                client_secret = client_entity.get('secret')
                payload_decoded = None

                try:
                    payload_decoded = jwt.decode(
                        token, client_secret, algorithms=['HS256'])
                    setattr(self, "client", payload_decoded)
                except jwt.ExpiredSignatureError:
                    logging.error("Signature has expired")
                    abort(403, "Signature has expired")

            return origin(self, *args, **args)

        inner.__name__ = origin.__name__
        inner.__doc__ = origin.__doc__
        inner.__dict__.update(origin.__dict__)

        return inner

    return func
import datetime
from functools import wraps
from flask import Response, request
from app.auth.utils import TokenManagement, Message
from app.auth.controllers import UserController
def authorized(f):
    """
    The authorized function will check for the presence of a valid JWT in the request header.
    If it is present, it will decode and verify that token. If not, an unauthorized response
    will be returned.

    Args:
        f: Pass the function to be decorated

    Returns:
        A function that is then called by the route
    """

    @wraps(f)
    def decorated(*args, **kwargs):
        """
        The decorated function will check for the presence of a valid JWT in the request header.
        If it is present, it will decode and verify that token. If not, an unauthorized response
        will be returned.

        Args:
            *args: Send a non-keyworded variable length argument list to the function
            **kwargs: Pass a keyworded, variable-length argument list

        Returns:
            A function

        """
        auth_type = None

        auth_token = request.headers.get("Authorization")
        if auth_token:
            auth_type = auth_token.split(" ")[0]

        # Check if token is present in request header
        if auth_token and auth_type == "Bearer":
            token = request.headers.get("Authorization").split(" ")[1]
        else:
            return {
                "error": Message.MISSING_TOKEN,
                "status": 401
            }

        # Check for validity of token
        try:
            decoded_token = TokenManagement.decode_token(token)

            if decoded_token is None:
                return {
                    "error": Message.TOKEN_INVALID,
                    "status": 401
                }

            current_time = datetime.datetime.now()
            expiry_time = datetime.datetime.utcfromtimestamp(decoded_token["exp"])

            if current_time > expiry_time:
                return {
                    "error": Message.TOKEN_EXPIRED,
                    "status": 401
                }

            logged_in_user = UserController.get_current_user(token)

            if not logged_in_user:
                return {
                    "error": Message.USER_UNAUTHENTICATED,
                    "status": 401
                }

        except Exception as e:
            return {
                "error": str(e),
                "status": 500
            }
        return f(logged_in_user, *args, **kwargs)

    return decorated


def anonymous(f):
    """
    The anonymous function will check for the presence of a valid JWT in the request header.
    If present, it will decode and verify it, then pass along the decoded payload to your function.
    If not present or invalid, None is passed instead.

    Args:
        f: Pass the function to be decorated

    Returns:
        A function that returns a function
    """

    @wraps(f)
    def decorated(*args, **kwargs):
        """
        The decorated function will check for the presence of a valid JWT in the request header.
        If present, it will decode and verify it, then pass along the decoded payload to your function.
        If not present or invalid, None is passed instead.

        Args:
            *args: Send a non-keyworded variable length argument list to the function
            **kwargs: Pass a keyworded, variable-length argument list

        Returns:
            The result of the decorated function

        """
        auth_type = None

        auth_token = request.headers.get("Authorization")
        if auth_token:
            auth_type = auth_token.split(" ")[0]

        # Check if token is present in request header
        if auth_token and auth_type == "Bearer":
            token = request.headers.get("Authorization").split(" ")[1]
        else:
            return f(None, *args, **kwargs)

        logged_in_user = None
        # Check for validity of token
        try:
            decoded_token = TokenManagement.decode_token(token)

            if decoded_token is None:
                return f(None, *args, **kwargs)

            current_time = datetime.datetime.now()
            expiry_time = datetime.datetime.utcfromtimestamp(decoded_token["exp"])

            if current_time > expiry_time:
                return f(None, *args, **kwargs)

            logged_in_user = UserController.get_current_user(token)

        except Exception as e:
            return {
                "error": str(e),
                "status": 500
            }

        finally:
            return f(logged_in_user, *args, **kwargs)

    return decorated
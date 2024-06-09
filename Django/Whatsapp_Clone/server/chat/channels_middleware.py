from channels.middleware import BaseMiddleware
from rest_framework.exceptions import AuthenticationFailed
from django.db import close_old_connections
from base.auth import UserAuthentication


class JWTWebsocketMiddleware(BaseMiddleware):
    """handle authentication for websockets"""

    async def __call__(self, scope, receive, send):
        """get query"""

        close_old_connections()

        query_string = scope.get("query_string", b"").decode("utf-8")
        query_params = dict(qp.split('=') for qp in query_string.split('&'))
        token = query_params.get("token", None)
        if token is None:
            await send({
                "type": "websocket.close",
                "code": 4000
            })
        
        authentication = UserAuthentication()
        try:
            user = await authentication.authenticate_websocket(token)
            if user is not None:
                scope['user'] = user
            else:
                await send({
                    "type": "websocket.close",
                    "code": 4000
                })
            await super().__call__(scope, receive, send)
        except AuthenticationFailed:
            await send({
                "type": "websocket.close",
                "code": 4002
            })

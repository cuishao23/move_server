import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from move_server.dao import user

logger = logging.getLogger('nms.' + __name__)


class MoveUser(APIView):
    def get(self, request, *args, **kwargs):
        user_list, user_total_num = user.get_user_info()

        logger.info('[MoveUser] user_list:%s' % user_list)
        logger.info('[MoveUser] user_total_num:%s' % user_total_num)

        response = {'success': 1}
        response['data'] = user_list
        response['total_num'] = user_total_num
        return Response(response)

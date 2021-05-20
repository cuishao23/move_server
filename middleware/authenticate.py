import logging
from os import PRIO_PGRP
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.core.cache import cache

logger = logging.getLogger('nms.' + __name__)


def authenticateMiddleware(get_response):
    def middleware(request):
        try:
            login_token = cache.get('login_token', None)
            print('login_token=%s'%login_token)
            
            if login_token is None:
                return JsonResponse({'success': 0}, status=401)
        except Exception as e:
            logger.error(e)
            print("e1=%s"%e)
            return JsonResponse({'success': 0}, status=401)
        # 在每一个响应前执行
        response = get_response(request)
        # 在每一个响应后执行
        return response
    return middleware
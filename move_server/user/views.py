import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import FileResponse
from move_server.dao import user

logger = logging.getLogger('nms.' + __name__)


class MoveUser(APIView):
    def get(self, request, *args, **kwargs):
        page = request.GET.get('newPageNum')
        address = request.GET.get('address')
        gender = request.GET.get('genderType')
        logger.info('[MoveUser] address:%s' % address)
        logger.info('[MoveUser] gender:%s' % gender)
        
        user_list, user_total_num = user.get_user_info(page, gender, address)
        logger.info('[MoveUser] user_list:%s' % user_list)
        logger.info('[MoveUser] user_total_num:%s' % user_total_num)

        response = {'success': 1}
        response['data'] = user_list
        response['total_num'] = user_total_num
        return Response(response)

class DownloadUser(APIView):
    def get(self, request, *args, **kwargs):
        address = request.GET.get('address')
        gender = request.GET.get('genderType')
        logger.info('[DownloadUser] address:%s' % address)
        logger.info('[DownloadUser] gender:%s' % gender)

        user.export_user_info_list(address, gender)
        f = open('/opt/data/users.xlsx', 'rb')
        response = FileResponse(f)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename=users.xlsx'
        return response

class MobileUser(APIView):
    def get(self, request, *args, **kwargs):
        page = request.GET.get('newPageNum')

        user_list, user_total_num = user.get_mobile_user_info(page)
        logger.info('[MobileUser] user_list:%s' % user_list)
        logger.info('[MobileUser] user_total_num:%s' % user_total_num)

        response = {'success': 1}
        response['data'] = user_list
        response['total_num'] = user_total_num
        return Response(response)

class DownloadMobileUser(APIView):
    def get(self, request, *args, **kwargs):
        user.export_mobile_user_info_list()
        f = open('/opt/data/users.xlsx', 'rb')
        response = FileResponse(f)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename=users.xlsx'
        return response

class BasicUser(APIView):
    def get(self, request, *args, **kwargs):
        page = request.GET.get('newPageNum')
        address = request.GET.get('address')
        gender = request.GET.get('genderType')
        appType = request.GET.get('appType')
        logger.info('[BasicUser] address:%s' % address)
        logger.info('[BasicUser] gender:%s' % gender)
        logger.info('[BasicUser] appType:%s' % appType)
        print(address)
        print(gender)
        print(appType)
        
        user_list, user_total_num = user.get_basic_user_info(page, gender, address, appType)
        logger.info('[BasicUser] user_list:%s' % user_list)
        logger.info('[BasicUser] user_total_num:%s' % user_total_num)

        response = {'success': 1}
        response['data'] = user_list
        response['total_num'] = user_total_num
        return Response(response)

class DownloadBasicUser(APIView):
    def get(self, request, *args, **kwargs):
        address = request.GET.get('address')
        gender = request.GET.get('genderType')
        appType = request.GET.get('appType')
        logger.info('[DownloadBasicUser] address:%s' % address)
        logger.info('[DownloadBasicUser] gender:%s' % gender)
        logger.info('[DownloadBasicUser] appType:%s' % appType)

        user.export_basic_user_info_list(address, gender, appType)
        f = open('/opt/data/users.xlsx', 'rb')
        response = FileResponse(f)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename=users.xlsx'
        return response
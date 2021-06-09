import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import FileResponse
from django.contrib.auth import authenticate, login,logout, update_session_auth_hash
from django.core.cache import cache
from move_server.dao import user


logger = logging.getLogger('nms.' + __name__)


class MoveUser(APIView):
    def get(self, request, *args, **kwargs):
        login_token = cache.get('login_token', None)
        if login_token is None:
            response = {'success': 0, 'message':'未登陆用户','status': 401}
            return Response(response)

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
        login_token = cache.get('login_token', None)
        if login_token is None:
            response = {'success': 0, 'message':'未登陆用户','status': 401}
            return Response(response)

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
        login_token = cache.get('login_token', None)
        if login_token is None:
            response = {'success': 0, 'message':'未登陆用户','status': 401}
            return Response(response)

        page = request.GET.get('newPageNum')
        address = request.GET.get('address')
        gender = request.GET.get('genderType')
        appType = request.GET.get('appType')
        logger.info('[BasicUser] address:%s' % address)
        logger.info('[BasicUser] gender:%s' % gender)
        logger.info('[BasicUser] appType:%s' % appType)

        user_list = user.get_basic_user_info(page, gender, address, appType)
        logger.info('[BasicUser] user_list:%s' % user_list)

        response = {'success': 1}
        response['data'] = user_list
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

class TotalPageNum(APIView):
    def get(self, request, *args, **kwargs):
        address = request.GET.get('address')
        gender = request.GET.get('genderType')
        appType = request.GET.get('appType')
        logger.info('[TotalPageNum] address:%s' % address)
        logger.info('[TotalPageNum] gender:%s' % gender)
        logger.info('[TotalPageNum] appType:%s' % appType)

        user_total_num = user.get_total_page_num(gender, address, appType)
        logger.info('[TotalPageNum] user_total_num:%s' % user_total_num)

        response = {'success': 1}
        response['total_num'] = user_total_num
        return Response(response)

class LoginView(APIView):
    def post(self,request):

        # 获取属性
        username = request.data.get('username')
        password = request.data.get('passwd')
        logger.info('[LoginView] username:%s' % username)
        logger.info('[LoginView] password:%s' % password)

        # 进行校验
        if username == '' or password == '':
            return Response({'success': 0, 'msg': '数据不完整'})
        # 查询
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # 保存登陆信息
            login(request, user)
            # 设置登陆有效时长login_token
            cache.set('login_token', user.username, 30*60)
            response = {'success': 1, 'msg': '登陆成功','username': user.username}
            return Response(response)
        else:
            response = {'success': 0, 'msg': '登陆失败'}
            return Response(response)

class LoginOutView(APIView):
    def post(self,request):
        # 清除登陆信息
        logout(request)
        # 清除login_token
        cache.clear()
        response = {'success': 1, 'msg': '退出登陆'}
        return Response(response)

class GraphView(APIView):
    def get(self,request, *args, **kwargs):
        login_token = cache.get('login_token', None)
        if login_token is None:
            response = {'success': 0, 'message':'未登陆用户','status': 401}
            return Response(response)

        tab = request.GET.get('tab')
        logger.info('\n[GraphTab] tab:%s' % tab)
        # 模拟数据库数据，之后修改
        response = {'success': 1}
        if tab=='governmentticket':
            response ['data'] = {'mock_active_user':33333, 'mock_total_user':111111, 'mock_coupon_user':5000,
            'mock_use_coupon_user':2222, 'mock_use_coupon_total':88888, 'mock_coupon_total':1500000}
        elif tab=='businessticket':
            response ['data'] = {'mock_active_user':23333, 'mock_total_user':311111, 'mock_coupon_user':4000,
            'mock_use_coupon_user':3333, 'mock_use_coupon_total':66666, 'mock_coupon_total':1333333}
        elif tab=='analyseticket':
            response ['data'] = {'yAxis':['23周','24周','25周','26周'],'bus':[1.1,1.2,1.3,1.4], 
            'gov':[1.2,1.3,1.4,1.5], 'active':[1.4,1.5,1.6,1.7],
            'pct_data':{'mock_gov_given_coupon': 333,'mock_gov_prepared_coupon':9222,'mock_bus_given_coupon': 111,'mock_bus_prepared_coupon':6888}}
        else:
            response ['data'] = {'mock_gov_coupon':1111,'mock_bus_coupon':2222,'mock_site_cost':8888,'mock_bus_cost':4567,'roi':'60%'}
        # logger.info('\n\n[GraphTab] response:%s' % response)
        return Response(response)
import logging
import pandas as pd
from django.db.models import Q
from django.db import connection
from move_server.dao.mysql.user import *
from move_server.utils.globalfun import get_time


logger = logging.getLogger('nms.'+__name__)

def getPage(page):
    if not page:
        page = 1
    else:
        page = int(page)

    start = (page - 1) * 15
    end = page * 15

    return start, end


# 用户身份信息接口
def get_user_info(page, gender, address):

    # 获取查询页码
    start,end = getPage(page)
    logger.info("start:%s, end:%s"%(start,end))

    if gender == 'all':
        if address == '':
            result = list(MoveMember.objects.filter(id__gt=start, id__lt=end+1))
            #result = MoveMember.objects.all()[start:end]
            total_num = MoveMember.objects.all().count()
        else:
            result = MoveMember.objects.filter(Q(province__icontains=address)|Q(city__icontains=address)|Q(county__icontains=address))[start:end]
            total_num = MoveMember.objects.filter(Q(province__icontains=address)|Q(city__icontains=address)|Q(county__icontains=address)).count()
    else:
        if address == '':
            result = MoveMember.objects.filter(gender=gender)[start:end]
            total_num = MoveMember.objects.filter(gender=gender).count()
        else:
            result = MoveMember.objects.filter(Q(province__icontains=address)|Q(city__icontains=address)|Q(county__icontains=address), gender=gender)[start:end]
            total_num = MoveMember.objects.filter(Q(province__icontains=address)|Q(city__icontains=address)|Q(county__icontains=address), gender=gender).count()

    user_list = []
    for user in result:
        user_list.append({'name': user.name,
                          'id_type': user.id_type,
                          'id_number': user.id_number,
                          'birth': user.birth,
                          'gender': user.gender,
                          'province': user.province,
                          'city': user.city,
                          'county': user.county,
                          'state': user.state,
                          'status': user.status,
                          'create_time': get_time(user.create_time)})

    return user_list, total_num

# 导出数据
def export_user_info_list(address, gender):
    try:
        user_list = get_user_info_list(address, gender)

        df = pd.DataFrame(user_list)
        df = df.set_index('id')
        writer = pd.ExcelWriter(r'/opt/data/users.xlsx', engine='xlsxwriter')
        df.to_excel(writer)
        writer.close()
        print('export ok！')
    except Exception as e:
        print(e)
        logger.error(e)

def get_user_info_list(address, gender):
    if gender == 'all':
        if address == '':
            result = MoveMember.objects.all()
        else:
            result = MoveMember.objects.filter(Q(province__icontains=address)|Q(city__icontains=address)|Q(county__icontains=address))
    else:
        if address == '':
            result = MoveMember.objects.filter(gender=gender)
        else:
            result = MoveMember.objects.filter(Q(province__icontains=address)|Q(city__icontains=address)|Q(county__icontains=address), gender=gender)
    user_list = []
    for user in result:
        user_list.append({'id': user.id,
                          'name': user.name,
                          'id_type': user.id_type,
                          'id_number': user.id_number,
                          'birth': user.birth,
                          'gender': user.gender,
                          'province': user.province,
                          'city': user.city,
                          'county': user.county,
                          'state': user.state,
                          'status': user.status,
                          'create_time': get_time(user.create_time)})

    return user_list


# 用户手机信息接口
def get_mobile_user_info(page):

    # 获取查询页码
    start,end = getPage(page)
    logger.info("start:%s, end:%s"%(start,end))

    result = MoveMobileMember.objects.all()[start:end]
    total_num = MoveMobileMember.objects.all().count()

    user_list = []
    for user in result:
        user_list.append({'unionid': user.unionid,
                          'mobile': user.mobile,
                          'id_number': user.id_number})

    return user_list, total_num

def export_mobile_user_info_list():
    try:
        user_list = get_mobile_user_info_list()

        df = pd.DataFrame(user_list)
        df = df.set_index('id')
        writer = pd.ExcelWriter(r'/opt/data/users.xlsx', engine='xlsxwriter')
        df.to_excel(writer)
        writer.close()
        print('export ok！')
    except Exception as e:
        print(e)
        logger.error(e)

def get_mobile_user_info_list():
    result = MoveMobileMember.objects.all()
    user_list = []
    for user in result:
        user_list.append({'id': user.id,
                          'unionid': user.unionid,
                          'mobile': user.mobile,
                          'id_number': user.id_number})

    return user_list


# 用户基本信息接口
def get_basic_user_info(page, gender, address, appType):

    # 获取查询页码
    start,end = getPage(page)
    logger.info("start:%s, end:%s"%(start,end))

    cursor = connection.cursor()
    if gender == 'all':
        if appType == 'all':
            if address == '':
                # 分页差的数据
                sql1 = '''
                    SELECT
                            move_user.name,
                            move_user.mobile,
                            FROM_UNIXTIME( move_user.create_time ),
                            move_user_channel.openid,
                            move_user_channel.app,
                            move_user_channel.session_key,
                            move_user_channel.gid,
                            move_user_channel.extappid,
                            move_user_channel.dist,
                            move_user_channel.point,
                            move_user_channel.total_point,
                            move_user_info.uid,
                            move_user_info.role,
                            move_user_info.status,
                            move_user_info.nickname,
                            move_user_info.avatarurl,
                            move_user_info.gender,
                            move_user_info.country,
                            move_user_info.province,
                            move_user_info.city,
                            move_user_info.id_type,
                            move_user_info.id_number,
                            move_user_info.address,
                            move_user_info.reg_user_id,
                            move_user_info.jdid,
                            move_user_info.verifytime,
                            move_user_info.phone_token,
                            move_user_info.token_time,
                            move_user_info.validity,
                            move_user_info.logindays,
                            move_user_info.email,
                            move_user_info.birth,
                            move_user_info.appid,
                            move_user_info.login_type,
                            move_user_info.login_id,
                            move_user_info.district,
                            move_user_info.street
                    FROM
                            move_user
                            LEFT JOIN move_user_channel ON move_user.unionid = move_user_channel.unionid
                            LEFT JOIN move_user_info ON move_user.id = move_user_info.uid
                    LIMIT %s,%s
                '''
                
                cursor.execute(sql1, [start, 15])
                result = cursor.fetchall()
            else:
                sql1 = '''
                    SELECT
                            move_user.name,
                            move_user.mobile,
                            FROM_UNIXTIME( move_user.create_time ),
                            move_user_channel.openid,
                            move_user_channel.app,
                            move_user_channel.session_key,
                            move_user_channel.gid,
                            move_user_channel.extappid,
                            move_user_channel.dist,
                            move_user_channel.point,
                            move_user_channel.total_point,
                            move_user_info.uid,
                            move_user_info.role,
                            move_user_info.status,
                            move_user_info.nickname,
                            move_user_info.avatarurl,
                            move_user_info.gender,
                            move_user_info.country,
                            move_user_info.province,
                            move_user_info.city,
                            move_user_info.id_type,
                            move_user_info.id_number,
                            move_user_info.address,
                            move_user_info.reg_user_id,
                            move_user_info.jdid,
                            move_user_info.verifytime,
                            move_user_info.phone_token,
                            move_user_info.token_time,
                            move_user_info.validity,
                            move_user_info.logindays,
                            move_user_info.email,
                            move_user_info.birth,
                            move_user_info.appid,
                            move_user_info.login_type,
                            move_user_info.login_id,
                            move_user_info.district,
                            move_user_info.street
                    FROM
                            move_user
                            LEFT JOIN move_user_channel ON move_user.unionid = move_user_channel.unionid
                            LEFT JOIN move_user_info ON move_user.id = move_user_info.uid
                    WHERE
                            move_user_info.province = %s
                    LIMIT %s,%s
                '''
                cursor.execute(sql1, [address, start, 15])
                result = cursor.fetchall()
        else:
            if address == '':
                sql1 = '''
                    SELECT
                            move_user.name,
                            move_user.mobile,
                            FROM_UNIXTIME( move_user.create_time ),
                            move_user_channel.openid,
                            move_user_channel.app,
                            move_user_channel.session_key,
                            move_user_channel.gid,
                            move_user_channel.extappid,
                            move_user_channel.dist,
                            move_user_channel.point,
                            move_user_channel.total_point,
                            move_user_info.uid,
                            move_user_info.role,
                            move_user_info.status,
                            move_user_info.nickname,
                            move_user_info.avatarurl,
                            move_user_info.gender,
                            move_user_info.country,
                            move_user_info.province,
                            move_user_info.city,
                            move_user_info.id_type,
                            move_user_info.id_number,
                            move_user_info.address,
                            move_user_info.reg_user_id,
                            move_user_info.jdid,
                            move_user_info.verifytime,
                            move_user_info.phone_token,
                            move_user_info.token_time,
                            move_user_info.validity,
                            move_user_info.logindays,
                            move_user_info.email,
                            move_user_info.birth,
                            move_user_info.appid,
                            move_user_info.login_type,
                            move_user_info.login_id,
                            move_user_info.district,
                            move_user_info.street
                    FROM
                            move_user
                            LEFT JOIN move_user_channel ON move_user.unionid = move_user_channel.unionid
                            LEFT JOIN move_user_info ON move_user.id = move_user_info.uid
                    WHERE
                            move_user_channel.app = %s
                    LIMIT %s,%s
                '''
                cursor.execute(sql1, [appType, start, 15])
                result = cursor.fetchall()
            else:
                sql1 = '''
                    SELECT
                            move_user.name,
                            move_user.mobile,
                            FROM_UNIXTIME( move_user.create_time ),
                            move_user_channel.openid,
                            move_user_channel.app,
                            move_user_channel.session_key,
                            move_user_channel.gid,
                            move_user_channel.extappid,
                            move_user_channel.dist,
                            move_user_channel.point,
                            move_user_channel.total_point,
                            move_user_info.uid,
                            move_user_info.role,
                            move_user_info.status,
                            move_user_info.nickname,
                            move_user_info.avatarurl,
                            move_user_info.gender,
                            move_user_info.country,
                            move_user_info.province,
                            move_user_info.city,
                            move_user_info.id_type,
                            move_user_info.id_number,
                            move_user_info.address,
                            move_user_info.reg_user_id,
                            move_user_info.jdid,
                            move_user_info.verifytime,
                            move_user_info.phone_token,
                            move_user_info.token_time,
                            move_user_info.validity,
                            move_user_info.logindays,
                            move_user_info.email,
                            move_user_info.birth,
                            move_user_info.appid,
                            move_user_info.login_type,
                            move_user_info.login_id,
                            move_user_info.district,
                            move_user_info.street
                    FROM
                            move_user
                            LEFT JOIN move_user_channel ON move_user.unionid = move_user_channel.unionid
                            LEFT JOIN move_user_info ON move_user.id = move_user_info.uid
                    WHERE
                            move_user_channel.app = %s and move_user_info.province = %s
                    LIMIT %s,%s
                '''
                cursor.execute(sql1, [appType, address, start, 15])
                result = cursor.fetchall()
    else:
        if appType == 'all':
            if address == '':
                sql1 = '''
                    SELECT
                            move_user.name,
                            move_user.mobile,
                            FROM_UNIXTIME( move_user.create_time ),
                            move_user_channel.openid,
                            move_user_channel.app,
                            move_user_channel.session_key,
                            move_user_channel.gid,
                            move_user_channel.extappid,
                            move_user_channel.dist,
                            move_user_channel.point,
                            move_user_channel.total_point,
                            move_user_info.uid,
                            move_user_info.role,
                            move_user_info.status,
                            move_user_info.nickname,
                            move_user_info.avatarurl,
                            move_user_info.gender,
                            move_user_info.country,
                            move_user_info.province,
                            move_user_info.city,
                            move_user_info.id_type,
                            move_user_info.id_number,
                            move_user_info.address,
                            move_user_info.reg_user_id,
                            move_user_info.jdid,
                            move_user_info.verifytime,
                            move_user_info.phone_token,
                            move_user_info.token_time,
                            move_user_info.validity,
                            move_user_info.logindays,
                            move_user_info.email,
                            move_user_info.birth,
                            move_user_info.appid,
                            move_user_info.login_type,
                            move_user_info.login_id,
                            move_user_info.district,
                            move_user_info.street
                    FROM
                            move_user
                            LEFT JOIN move_user_channel ON move_user.unionid = move_user_channel.unionid
                            LEFT JOIN move_user_info ON move_user.id = move_user_info.uid
                    WHERE
                            move_user_info.gender = %s
                    LIMIT %s,%s
                '''
                cursor.execute(sql1, [gender, start, 15])
                result = cursor.fetchall()
            else:
                sql1 = '''
                    SELECT
                            move_user.name,
                            move_user.mobile,
                            FROM_UNIXTIME( move_user.create_time ),
                            move_user_channel.openid,
                            move_user_channel.app,
                            move_user_channel.session_key,
                            move_user_channel.gid,
                            move_user_channel.extappid,
                            move_user_channel.dist,
                            move_user_channel.point,
                            move_user_channel.total_point,
                            move_user_info.uid,
                            move_user_info.role,
                            move_user_info.status,
                            move_user_info.nickname,
                            move_user_info.avatarurl,
                            move_user_info.gender,
                            move_user_info.country,
                            move_user_info.province,
                            move_user_info.city,
                            move_user_info.id_type,
                            move_user_info.id_number,
                            move_user_info.address,
                            move_user_info.reg_user_id,
                            move_user_info.jdid,
                            move_user_info.verifytime,
                            move_user_info.phone_token,
                            move_user_info.token_time,
                            move_user_info.validity,
                            move_user_info.logindays,
                            move_user_info.email,
                            move_user_info.birth,
                            move_user_info.appid,
                            move_user_info.login_type,
                            move_user_info.login_id,
                            move_user_info.district,
                            move_user_info.street
                    FROM
                            move_user
                            LEFT JOIN move_user_channel ON move_user.unionid = move_user_channel.unionid
                            LEFT JOIN move_user_info ON move_user.id = move_user_info.uid
                    WHERE
                            move_user_info.gender = %s and move_user_info.province = %s
                    LIMIT %s,%s
                '''
                cursor.execute(sql1, [gender, address, start, 15])
                result = cursor.fetchall()
        else:
            if address == '':
                sql1 = '''
                    SELECT
                            move_user.name,
                            move_user.mobile,
                            FROM_UNIXTIME( move_user.create_time ),
                            move_user_channel.openid,
                            move_user_channel.app,
                            move_user_channel.session_key,
                            move_user_channel.gid,
                            move_user_channel.extappid,
                            move_user_channel.dist,
                            move_user_channel.point,
                            move_user_channel.total_point,
                            move_user_info.uid,
                            move_user_info.role,
                            move_user_info.status,
                            move_user_info.nickname,
                            move_user_info.avatarurl,
                            move_user_info.gender,
                            move_user_info.country,
                            move_user_info.province,
                            move_user_info.city,
                            move_user_info.id_type,
                            move_user_info.id_number,
                            move_user_info.address,
                            move_user_info.reg_user_id,
                            move_user_info.jdid,
                            move_user_info.verifytime,
                            move_user_info.phone_token,
                            move_user_info.token_time,
                            move_user_info.validity,
                            move_user_info.logindays,
                            move_user_info.email,
                            move_user_info.birth,
                            move_user_info.appid,
                            move_user_info.login_type,
                            move_user_info.login_id,
                            move_user_info.district,
                            move_user_info.street
                    FROM
                            move_user
                            LEFT JOIN move_user_channel ON move_user.unionid = move_user_channel.unionid
                            LEFT JOIN move_user_info ON move_user.id = move_user_info.uid
                    WHERE
                            move_user_info.gender = %s and move_user_channel.app = %s
                    LIMIT %s,%s
                '''
                cursor.execute(sql1, [gender, appType, start, 15])
                result = cursor.fetchall()
            else:
                sql1 = '''
                    SELECT
                            move_user.name,
                            move_user.mobile,
                            FROM_UNIXTIME( move_user.create_time ),
                            move_user_channel.openid,
                            move_user_channel.app,
                            move_user_channel.session_key,
                            move_user_channel.gid,
                            move_user_channel.extappid,
                            move_user_channel.dist,
                            move_user_channel.point,
                            move_user_channel.total_point,
                            move_user_info.uid,
                            move_user_info.role,
                            move_user_info.status,
                            move_user_info.nickname,
                            move_user_info.avatarurl,
                            move_user_info.gender,
                            move_user_info.country,
                            move_user_info.province,
                            move_user_info.city,
                            move_user_info.id_type,
                            move_user_info.id_number,
                            move_user_info.address,
                            move_user_info.reg_user_id,
                            move_user_info.jdid,
                            move_user_info.verifytime,
                            move_user_info.phone_token,
                            move_user_info.token_time,
                            move_user_info.validity,
                            move_user_info.logindays,
                            move_user_info.email,
                            move_user_info.birth,
                            move_user_info.appid,
                            move_user_info.login_type,
                            move_user_info.login_id,
                            move_user_info.district,
                            move_user_info.street
                    FROM
                            move_user
                            LEFT JOIN move_user_channel ON move_user.unionid = move_user_channel.unionid
                            LEFT JOIN move_user_info ON move_user.id = move_user_info.uid
                    WHERE
                            move_user_info.gender = %s and move_user_channel.app = %s and move_user_info.province = %s
                    LIMIT %s,%s
                '''
                cursor.execute(sql1, [gender, appType, address, start, 15])
                result = cursor.fetchall()

    user_list = []
    for info in result:
        user_list.append({'name': info[0], 'mobile': info[1], 'create_time': info[2],
                            'openid': info[3], 'app': info[4], 'session_key': info[5], 'gid': info[6],
                            'extappid': info[7], 'dist': info[8], 'point': info[9], 'total_point': info[10],
                            'uid': info[11], 'role': info[12], 'status': info[13], 'nickname': info[14],
                            'avatarurl': info[15], 'gender': info[16], 'country': info[17],
                            'province': info[18], 'city': info[19], 'id_type': info[20],
                            'id_number': info[21], 'address': info[22], 'reg_user_id': info[23], 'jdid': info[24],
                            'verifytime': info[25], 'phone_token': info[26], 'token_time': info[27],
                            'validity': info[28], 'logindays': info[29], 'email': info[30], 'birth': info[31],
                            'appid': info[32], 'login_type': info[33], 'login_id': info[34],
                            'district': info[35], 'street': info[36]})

    return user_list

# 导出数据
def export_basic_user_info_list(address, gender, appType):
    try:
        print('export start')
        user_list = get_basic_user_info_list(address, gender, appType)
        print('user_list=%s'%user_list)

        df = pd.DataFrame(user_list)
        # df = df.set_index('id')
        writer = pd.ExcelWriter(r'/opt/data/users.xlsx', engine='xlsxwriter', options={'strings_to_urls': False}) # 不将字符串转换为URL的选项创建ExcelWriter对象
        df.to_excel(writer)
        writer.close()
        print('export ok！')
    except Exception as e:
        print(e)
        logger.error(e)

def get_basic_user_info_list(address, gender, appType):
    print(address)
    print(gender)
    print(appType)
    cursor = connection.cursor()
    if gender == 'all':
        if appType == 'all':
            if address == '':
                print(111111111)
                sql1 = '''
                    SELECT
                            move_user.name,
                            move_user.mobile,
                            FROM_UNIXTIME( move_user.create_time ),
                            move_user_channel.openid,
                            move_user_channel.app,
                            move_user_channel.session_key,
                            move_user_channel.gid,
                            move_user_channel.extappid,
                            move_user_channel.dist,
                            move_user_channel.point,
                            move_user_channel.total_point,
                            move_user_info.uid,
                            move_user_info.role,
                            move_user_info.status,
                            move_user_info.nickname,
                            move_user_info.avatarurl,
                            move_user_info.gender,
                            move_user_info.country,
                            move_user_info.province,
                            move_user_info.city,
                            move_user_info.id_type,
                            move_user_info.id_number,
                            move_user_info.address,
                            move_user_info.reg_user_id,
                            move_user_info.jdid,
                            move_user_info.verifytime,
                            move_user_info.phone_token,
                            move_user_info.token_time,
                            move_user_info.validity,
                            move_user_info.logindays,
                            move_user_info.email,
                            move_user_info.birth,
                            move_user_info.appid,
                            move_user_info.login_type,
                            move_user_info.login_id,
                            move_user_info.district,
                            move_user_info.street
                    FROM
                            move_user
                            LEFT JOIN move_user_channel ON move_user.unionid = move_user_channel.unionid
                            LEFT JOIN move_user_info ON move_user.id = move_user_info.uid
                    LIMIT %s,%s
                '''
                cursor.execute(sql1, [0, 500000])
                result = cursor.fetchall()
            else:
                sql1 = '''
                    SELECT
                            move_user.name,
                            move_user.mobile,
                            FROM_UNIXTIME( move_user.create_time ),
                            move_user_channel.openid,
                            move_user_channel.app,
                            move_user_channel.session_key,
                            move_user_channel.gid,
                            move_user_channel.extappid,
                            move_user_channel.dist,
                            move_user_channel.point,
                            move_user_channel.total_point,
                            move_user_info.uid,
                            move_user_info.role,
                            move_user_info.status,
                            move_user_info.nickname,
                            move_user_info.avatarurl,
                            move_user_info.gender,
                            move_user_info.country,
                            move_user_info.province,
                            move_user_info.city,
                            move_user_info.id_type,
                            move_user_info.id_number,
                            move_user_info.address,
                            move_user_info.reg_user_id,
                            move_user_info.jdid,
                            move_user_info.verifytime,
                            move_user_info.phone_token,
                            move_user_info.token_time,
                            move_user_info.validity,
                            move_user_info.logindays,
                            move_user_info.email,
                            move_user_info.birth,
                            move_user_info.appid,
                            move_user_info.login_type,
                            move_user_info.login_id,
                            move_user_info.district,
                            move_user_info.street
                    FROM
                            move_user
                            LEFT JOIN move_user_channel ON move_user.unionid = move_user_channel.unionid
                            LEFT JOIN move_user_info ON move_user.id = move_user_info.uid
                    WHERE
                            move_user_info.province = %s
                    LIMIT %s,%s
                '''
                cursor.execute(sql1, [address, 0, 500000])
                result = cursor.fetchall()
        else:
            if address == '':
                sql1 = '''
                    SELECT
                            move_user.name,
                            move_user.mobile,
                            FROM_UNIXTIME( move_user.create_time ),
                            move_user_channel.openid,
                            move_user_channel.app,
                            move_user_channel.session_key,
                            move_user_channel.gid,
                            move_user_channel.extappid,
                            move_user_channel.dist,
                            move_user_channel.point,
                            move_user_channel.total_point,
                            move_user_info.uid,
                            move_user_info.role,
                            move_user_info.status,
                            move_user_info.nickname,
                            move_user_info.avatarurl,
                            move_user_info.gender,
                            move_user_info.country,
                            move_user_info.province,
                            move_user_info.city,
                            move_user_info.id_type,
                            move_user_info.id_number,
                            move_user_info.address,
                            move_user_info.reg_user_id,
                            move_user_info.jdid,
                            move_user_info.verifytime,
                            move_user_info.phone_token,
                            move_user_info.token_time,
                            move_user_info.validity,
                            move_user_info.logindays,
                            move_user_info.email,
                            move_user_info.birth,
                            move_user_info.appid,
                            move_user_info.login_type,
                            move_user_info.login_id,
                            move_user_info.district,
                            move_user_info.street
                    FROM
                            move_user
                            LEFT JOIN move_user_channel ON move_user.unionid = move_user_channel.unionid
                            LEFT JOIN move_user_info ON move_user.id = move_user_info.uid
                    WHERE
                            move_user_channel.app = %s
                    LIMIT %s,%s
                '''
                cursor.execute(sql1, [appType, 0, 500000])
                result = cursor.fetchall()
            else:
                sql1 = '''
                    SELECT
                            move_user.name,
                            move_user.mobile,
                            FROM_UNIXTIME( move_user.create_time ),
                            move_user_channel.openid,
                            move_user_channel.app,
                            move_user_channel.session_key,
                            move_user_channel.gid,
                            move_user_channel.extappid,
                            move_user_channel.dist,
                            move_user_channel.point,
                            move_user_channel.total_point,
                            move_user_info.uid,
                            move_user_info.role,
                            move_user_info.status,
                            move_user_info.nickname,
                            move_user_info.avatarurl,
                            move_user_info.gender,
                            move_user_info.country,
                            move_user_info.province,
                            move_user_info.city,
                            move_user_info.id_type,
                            move_user_info.id_number,
                            move_user_info.address,
                            move_user_info.reg_user_id,
                            move_user_info.jdid,
                            move_user_info.verifytime,
                            move_user_info.phone_token,
                            move_user_info.token_time,
                            move_user_info.validity,
                            move_user_info.logindays,
                            move_user_info.email,
                            move_user_info.birth,
                            move_user_info.appid,
                            move_user_info.login_type,
                            move_user_info.login_id,
                            move_user_info.district,
                            move_user_info.street
                    FROM
                            move_user
                            LEFT JOIN move_user_channel ON move_user.unionid = move_user_channel.unionid
                            LEFT JOIN move_user_info ON move_user.id = move_user_info.uid
                    WHERE
                            move_user_channel.app = %s and move_user_info.province = %s
                    LIMIT %s,%s
                '''
                cursor.execute(sql1, [appType, address, 0, 500000])
                result = cursor.fetchall()
    else:
        if appType == 'all':
            if address == '':
                sql1 = '''
                    SELECT
                            move_user.name,
                            move_user.mobile,
                            FROM_UNIXTIME( move_user.create_time ),
                            move_user_channel.openid,
                            move_user_channel.app,
                            move_user_channel.session_key,
                            move_user_channel.gid,
                            move_user_channel.extappid,
                            move_user_channel.dist,
                            move_user_channel.point,
                            move_user_channel.total_point,
                            move_user_info.uid,
                            move_user_info.role,
                            move_user_info.status,
                            move_user_info.nickname,
                            move_user_info.avatarurl,
                            move_user_info.gender,
                            move_user_info.country,
                            move_user_info.province,
                            move_user_info.city,
                            move_user_info.id_type,
                            move_user_info.id_number,
                            move_user_info.address,
                            move_user_info.reg_user_id,
                            move_user_info.jdid,
                            move_user_info.verifytime,
                            move_user_info.phone_token,
                            move_user_info.token_time,
                            move_user_info.validity,
                            move_user_info.logindays,
                            move_user_info.email,
                            move_user_info.birth,
                            move_user_info.appid,
                            move_user_info.login_type,
                            move_user_info.login_id,
                            move_user_info.district,
                            move_user_info.street
                    FROM
                            move_user
                            LEFT JOIN move_user_channel ON move_user.unionid = move_user_channel.unionid
                            LEFT JOIN move_user_info ON move_user.id = move_user_info.uid
                    WHERE
                            move_user_info.gender = %s
                    LIMIT %s,%s
                '''
                cursor.execute(sql1, [gender, 0, 500000])
                result = cursor.fetchall()
            else:
                sql1 = '''
                    SELECT
                            move_user.name,
                            move_user.mobile,
                            FROM_UNIXTIME( move_user.create_time ),
                            move_user_channel.openid,
                            move_user_channel.app,
                            move_user_channel.session_key,
                            move_user_channel.gid,
                            move_user_channel.extappid,
                            move_user_channel.dist,
                            move_user_channel.point,
                            move_user_channel.total_point,
                            move_user_info.uid,
                            move_user_info.role,
                            move_user_info.status,
                            move_user_info.nickname,
                            move_user_info.avatarurl,
                            move_user_info.gender,
                            move_user_info.country,
                            move_user_info.province,
                            move_user_info.city,
                            move_user_info.id_type,
                            move_user_info.id_number,
                            move_user_info.address,
                            move_user_info.reg_user_id,
                            move_user_info.jdid,
                            move_user_info.verifytime,
                            move_user_info.phone_token,
                            move_user_info.token_time,
                            move_user_info.validity,
                            move_user_info.logindays,
                            move_user_info.email,
                            move_user_info.birth,
                            move_user_info.appid,
                            move_user_info.login_type,
                            move_user_info.login_id,
                            move_user_info.district,
                            move_user_info.street
                    FROM
                            move_user
                            LEFT JOIN move_user_channel ON move_user.unionid = move_user_channel.unionid
                            LEFT JOIN move_user_info ON move_user.id = move_user_info.uid
                    WHERE
                            move_user_info.gender = %s and move_user_info.province = %s
                    LIMIT %s,%s
                '''
                cursor.execute(sql1, [gender, address, 0, 500000])
                result = cursor.fetchall()
        else:
            if address == '':
                sql1 = '''
                    SELECT
                            move_user.name,
                            move_user.mobile,
                            FROM_UNIXTIME( move_user.create_time ),
                            move_user_channel.openid,
                            move_user_channel.app,
                            move_user_channel.session_key,
                            move_user_channel.gid,
                            move_user_channel.extappid,
                            move_user_channel.dist,
                            move_user_channel.point,
                            move_user_channel.total_point,
                            move_user_info.uid,
                            move_user_info.role,
                            move_user_info.status,
                            move_user_info.nickname,
                            move_user_info.avatarurl,
                            move_user_info.gender,
                            move_user_info.country,
                            move_user_info.province,
                            move_user_info.city,
                            move_user_info.id_type,
                            move_user_info.id_number,
                            move_user_info.address,
                            move_user_info.reg_user_id,
                            move_user_info.jdid,
                            move_user_info.verifytime,
                            move_user_info.phone_token,
                            move_user_info.token_time,
                            move_user_info.validity,
                            move_user_info.logindays,
                            move_user_info.email,
                            move_user_info.birth,
                            move_user_info.appid,
                            move_user_info.login_type,
                            move_user_info.login_id,
                            move_user_info.district,
                            move_user_info.street
                    FROM
                            move_user
                            LEFT JOIN move_user_channel ON move_user.unionid = move_user_channel.unionid
                            LEFT JOIN move_user_info ON move_user.id = move_user_info.uid
                    WHERE
                            move_user_info.gender = %s and move_user_channel.app = %s
                    LIMIT %s,%s
                '''
                cursor.execute(sql1, [gender, appType, 0, 500000])
                result = cursor.fetchall()
            else:
                sql1 = '''
                    SELECT
                            move_user.name,
                            move_user.mobile,
                            FROM_UNIXTIME( move_user.create_time ),
                            move_user_channel.openid,
                            move_user_channel.app,
                            move_user_channel.session_key,
                            move_user_channel.gid,
                            move_user_channel.extappid,
                            move_user_channel.dist,
                            move_user_channel.point,
                            move_user_channel.total_point,
                            move_user_info.uid,
                            move_user_info.role,
                            move_user_info.status,
                            move_user_info.nickname,
                            move_user_info.avatarurl,
                            move_user_info.gender,
                            move_user_info.country,
                            move_user_info.province,
                            move_user_info.city,
                            move_user_info.id_type,
                            move_user_info.id_number,
                            move_user_info.address,
                            move_user_info.reg_user_id,
                            move_user_info.jdid,
                            move_user_info.verifytime,
                            move_user_info.phone_token,
                            move_user_info.token_time,
                            move_user_info.validity,
                            move_user_info.logindays,
                            move_user_info.email,
                            move_user_info.birth,
                            move_user_info.appid,
                            move_user_info.login_type,
                            move_user_info.login_id,
                            move_user_info.district,
                            move_user_info.street
                    FROM
                            move_user
                            LEFT JOIN move_user_channel ON move_user.unionid = move_user_channel.unionid
                            LEFT JOIN move_user_info ON move_user.id = move_user_info.uid
                    WHERE
                            move_user_info.gender = %s and move_user_channel.app = %s and move_user_info.province = %s
                    LIMIT %s,%s
                '''
                cursor.execute(sql1, [gender, appType, address, 0, 500000])
                result = cursor.fetchall()

                # 总数量
                sql2 = '''
                    SELECT
                            count(1)
                    FROM
                            move_user
                            left JOIN move_user_channel ON move_user.unionid = move_user_channel.unionid
                            left JOIN move_user_info ON move_user.id = move_user_info.uid
                    WHERE   move_user_info.gender = %s and move_user_channel.app = %s and move_user_info.province = %s
                '''
                cursor.execute(sql2, [gender, appType, address])
                num = cursor.fetchone()

    user_list = []
    for info in result:
        user_list.append({'name': info[0], 'mobile': info[1], 'create_time': info[2],
                            'openid': info[3], 'app': info[4], 'session_key': info[5], 'gid': info[6],
                            'extappid': info[7], 'dist': info[8], 'point': info[9], 'total_point': info[10],
                            'uid': info[11], 'role': info[12], 'status': info[13], 'nickname': info[14],
                            'avatarurl': info[15], 'gender': '男' if info[16] == 1 else '女', 'country': info[17],
                            'province': info[18], 'city': info[19], 'id_type': info[20],
                            'id_number': info[21], 'address': info[22], 'reg_user_id': info[23], 'jdid': info[24],
                            'verifytime': info[25], 'phone_token': info[26], 'token_time': info[27],
                            'validity': info[28], 'logindays': info[29], 'email': info[30], 'birth': info[31],
                            'appid': info[32], 'login_type': info[33], 'login_id': info[34],
                            'district': info[35], 'street': info[36]})

    return user_list

def get_total_page_num(gender, address, appType):
    cursor = connection.cursor()
    if gender == 'all':
        if appType == 'all':
            if address == '':
                # 总数量
                sql2 = '''
                    select a.dd-c.ff+b.ee from 
                        (select count(unionid) dd from move_user ) a,
                        (select count(unionid) ee from move_user_channel) b,
                        (select count(distinct unionid) ff from move_user_channel) c
                '''
                cursor.execute(sql2)
                num = cursor.fetchone()
            else:
                # 总数量
                sql2 = '''
                    SELECT
                            count(1)
                    FROM
                            move_user
                            left JOIN move_user_channel ON move_user.unionid = move_user_channel.unionid
                            left JOIN move_user_info ON move_user.id = move_user_info.uid
                    WHERE   move_user_info.province = %s
                '''
                cursor.execute(sql2, [address,])
                num = cursor.fetchone()
        else:
            if address == '':
                # 总数量
                sql2 = '''
                    SELECT
                            count(1)
                    FROM
                            move_user
                            left JOIN move_user_channel ON move_user.unionid = move_user_channel.unionid
                            left JOIN move_user_info ON move_user.id = move_user_info.uid
                    WHERE   move_user_channel.app = %s
                '''
                cursor.execute(sql2, [appType,])
                num = cursor.fetchone()
            else:
                # 总数量
                sql2 = '''
                    SELECT
                            count(1)
                    FROM
                            move_user
                            left JOIN move_user_channel ON move_user.unionid = move_user_channel.unionid
                            left JOIN move_user_info ON move_user.id = move_user_info.uid
                    WHERE   move_user_channel.app = %s and move_user_info.province = %s
                '''
                cursor.execute(sql2, [appType, address])
                num = cursor.fetchone()
    else:
        if appType == 'all':
            if address == '':
                # 总数量
                sql2 = '''
                    SELECT
                            count(1)
                    FROM
                            move_user
                            left JOIN move_user_channel ON move_user.unionid = move_user_channel.unionid
                            left JOIN move_user_info ON move_user.id = move_user_info.uid
                    WHERE   move_user_info.gender = %s
                '''
                cursor.execute(sql2, [gender,])
                num = cursor.fetchone()
            else:
                # 总数量
                sql2 = '''
                    SELECT
                            count(1)
                    FROM
                            move_user
                            left JOIN move_user_channel ON move_user.unionid = move_user_channel.unionid
                            left JOIN move_user_info ON move_user.id = move_user_info.uid
                    WHERE   move_user_info.gender = %s and move_user_info.province = %s
                '''
                cursor.execute(sql2, [gender, address])
                num = cursor.fetchone()
        else:
            if address == '':
                # 总数量
                sql2 = '''
                    SELECT
                            count(1)
                    FROM
                            move_user
                            left JOIN move_user_channel ON move_user.unionid = move_user_channel.unionid
                            left JOIN move_user_info ON move_user.id = move_user_info.uid
                    WHERE   move_user_info.gender = %s and move_user_channel.app = %s
                '''
                cursor.execute(sql2, [gender, appType])
                num = cursor.fetchone()
            else:
                # 总数量
                sql2 = '''
                    SELECT
                            count(1)
                    FROM
                            move_user
                            left JOIN move_user_channel ON move_user.unionid = move_user_channel.unionid
                            left JOIN move_user_info ON move_user.id = move_user_info.uid
                    WHERE   move_user_info.gender = %s and move_user_channel.app = %s and move_user_info.province = %s
                '''
                cursor.execute(sql2, [gender, appType, address])
                num = cursor.fetchone()

    total_num = 0
    if num:
        total_num = num[0]

    return total_num
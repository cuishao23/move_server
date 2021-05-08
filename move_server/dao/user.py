import logging
from django.db.models import Q
from move_server.dao.mysql.user import *
from move_server.utils.globalfun import get_time


logger = logging.getLogger('nms.'+__name__)

def getPage(page):
    if not page:
        page = 1
    else:
        page = int(page)

    start = (page - 1) * 10
    end = page * 10

    return start, end
    
def get_user_info(page, gender, address):

    # 获取查询页码
    start,end = getPage(page)
    logger.info("start:%s, end:%s"%(start,end))

    if gender == 'all':
        if address == '':
            result = MoveMember.objects.all()[start:end]
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

import logging
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
    
def get_user_info(page):

    # 获取查询页码
    start,end = getPage(page)
    logger.info("start:%s, end:%s"%(start,end))

    result = MoveMember.objects.all()[start:end]
    total_num = MoveMember.objects.all().count()

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

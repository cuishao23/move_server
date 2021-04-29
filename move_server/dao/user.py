from move_server.dao.mysql.user import *


def get_user_info():
    result = MoveMember.objects.all()[0:10]
    total_num = MoveMember.objects.all()[0:10].count()

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
                          'create_time': user.create_time})

    return user_list, total_num

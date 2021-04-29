from django.db import models


class MoveUser(models.Model):
    unionid = models.CharField(unique=True, max_length=128)
    name = models.CharField(max_length=28, blank=True, null=True)
    mobile = models.CharField(max_length=200, blank=True, null=True)
    mobileid = models.CharField(max_length=200, blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    id_type = models.IntegerField(blank=True, null=True)
    id_number = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        db_table = 'move_user'
        app_label = 'user'
        unique_together = (('id', 'unionid'), ('unionid', 'mobileid'), ('id_type', 'id_number'),)
        verbose_name = '用户基本表'


class MoveUserChannel(models.Model):
    uid = models.IntegerField()
    unionid = models.CharField(max_length=128)
    openid = models.CharField(max_length=200, blank=True, null=True)
    app = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    session_key = models.CharField(max_length=255, blank=True, null=True)
    token = models.CharField(max_length=255, blank=True, null=True)
    gid = models.IntegerField(blank=True, null=True)
    extappid = models.CharField(max_length=64, blank=True, null=True)
    dist = models.IntegerField(blank=True, null=True)
    point = models.IntegerField(blank=True, null=True)
    total_point = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'move_user_channel'
        app_label = 'user'
        verbose_name = '用户channel表'


class MoveUserInfo(models.Model):
    uid = models.IntegerField(unique=True, blank=True, null=True)
    role = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    create_time = models.IntegerField(blank=True, null=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    avatarurl = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    province = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    language = models.CharField(max_length=255, blank=True, null=True)
    id_type = models.IntegerField(blank=True, null=True)
    id_number = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    reg_user_id = models.IntegerField(blank=True, null=True)
    jdid = models.CharField(max_length=32, blank=True, null=True)
    verifytime = models.DateTimeField(blank=True, null=True)
    real_name = models.IntegerField(blank=True, null=True)
    real_idcard = models.CharField(max_length=128, blank=True, null=True)
    conflict_idcard = models.CharField(max_length=128, blank=True, null=True)
    phone_token = models.CharField(max_length=255, blank=True, null=True)
    token_time = models.DateTimeField(blank=True, null=True)
    validity = models.DateTimeField(blank=True, null=True)
    logindays = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    birth = models.DateField(blank=True, null=True)
    appid = models.IntegerField(blank=True, null=True)
    login_type = models.CharField(max_length=64, blank=True, null=True)
    login_id = models.CharField(max_length=64, blank=True, null=True)
    district = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'move_user_info'
        app_label = 'user'
        verbose_name = '用户详细表'


class MoveMember(models.Model):
    name = models.CharField(max_length=64)
    id_type = models.IntegerField(blank=True, null=True)
    id_number = models.CharField(unique=True, max_length=128)
    birth = models.DateField(blank=True, null=True)
    gender = models.PositiveIntegerField(blank=True, null=True)
    province = models.CharField(max_length=128, blank=True, null=True)
    city = models.CharField(max_length=128, blank=True, null=True)
    county = models.CharField(max_length=128, blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'move_member'
        app_label = 'user'
        verbose_name = '用户实名认证表'


class MoveMobileMember(models.Model):
    unionid = models.CharField(unique=True, max_length=128, blank=True, null=True)
    mobile = models.CharField(max_length=200)
    id_number = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        db_table = 'move_mobile_member'
        app_label = 'user'
        verbose_name = '用户member表'

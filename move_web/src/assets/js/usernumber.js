 /*
 * 用户身份表表格属性
 * @param 
 * @returns {*[]}
 */
 export function getUserInfoFields() {
    return [
      {
        prop: 'name',
        label: '姓名'
      },
      {
        prop: 'id_type',
        label: '证件类型'
      },
      {
        prop: 'id_number',
        label: '证件号'
      },
      {
        prop: 'birth',
        label: '生日'
      },
      {
        prop: 'gender',
        label: '性别'
      },
      {
        prop: 'province',
        label: '省'
      },
      {
        prop: 'city',
        label: '市'
      },
      {
        prop: 'county',
        label: '县/区'
      },
      {
        prop: 'state',
        label: '是否认证'
      },
      {
        prop: 'status',
        label: '状态'
      },
      {
        prop: 'create_time',
        label: '创建时间'
      }
    ]
  }

  export const genderTypes = [
    {
      text: '性别',
      value: 'all'
    },
    {
      text: '男',
      value: '1'
    },
    {
      text: '女',
      value: '2'
    }
  ];

 /*
 * 用户手机表表格属性
 * @param 
 * @returns {*[]}
 */
 export function getUserMobileInfoFields() {
  return [
    {
      prop: 'unionid',
      label: 'unionid'
    },
    {
      prop: 'mobile',
      label: '手机号'
    },
    {
      prop: 'id_number',
      label: '证件号'
    }
  ]
}

export const appTypes = [
  {
    text: '赛事',
    value: 'all'
  },
  {
    text: '每步赛事',
    value: '1'
  },
  {
    text: '赛易云',
    value: '12'
  },
  {
    text: '迈麦体育产业',
    value: '7'
  },
  {
    text: 'RunBike儿童平衡车',
    value: '10'
  },
  {
    text: 'PTSA+',
    value: '8'
  },
  {
    text: '奔跑吧少东家',
    value: '6'
  },
  {
    text: '每步+',
    value: '3'
  },
  {
    text: 'Campusrun跑步训练营',
    value: '2'
  },
  {
    text: 'mpms',
    value: '4'
  },
  {
    text: '每步运动会H5',
    value: '101'
  },
  {
    text: '五星运动汇小程序',
    value: '16'
  },
  {
    text: '慕道无极',
    value: '18'
  },
  {
    text: '黄浦我来赛',
    value: '17'
  },
  {
    text: '体育锻炼达标赛',
    value: '21'
  },
  {
    text: '赛易云h5',
    value: '11'
  },
  {
    text: '上海市青少年体育协会',
    value: '108'
  },
  {
    text: '第三届市民运动会配送服务平台',
    value: '109'
  },
  {
    text: '嘉定体育',
    value: '110'
  },
  {
    text: '全嘉运动会',
    value: '111'
  },
  {
    text: '上海市武术世锦赛',
    value: '112'
  },
  {
    text: 'Campusrun跑步训练营',
    value: '113'
  },
  {
    text: '松江健步走',
    value: '114'
  },
  {
    text: '虹口 谁是联赛王',
    value: '115'
  },
  {
    text: '汇体育',
    value: '116'
  },
  {
    text: '泳乐趣',
    value: '117'
  },
  {
    text: '黄浦区体育指导员',
    value: '118'
  },
  {
    text: '高校百英里',
    value: '119'
  },
  {
    text: '爱在每步',
    value: '19'
  },
  {
    text: '动驿动',
    value: '20'
  },
  {
    text: '精英挑战赛',
    value: '122'
  },
  {
    text: '嘉定云配送',
    value: '123'
  },
  {
    text: '上海市线上运动会',
    value: '124'
  },
  {
    text: '翔动宝',
    value: '125'
  },
  {
    text: '健康浦东行',
    value: '126'
  },
  {
    text: '健身地图',
    value: '127'
  },
  {
    text: '江湾体育场',
    value: '128'
  },
  {
    text: '华新镇',
    value: '129'
  },
  {
    text: '长宁小程序',
    value: '130'
  },
  {
    text: '上海市社体 (竞赛) 中心内部管理系统',
    value: '131'
  },
  {
    text: '普陀线上运动会',
    value: '132'
  },
  {
    text: '云动斜土',
    value: '133'
  },
  {
    text: '质在青浦',
    value: '134'
  },
  {
    text: '厦门线上运动会小程序',
    value: '135'
  },
  {
    text: '长宁区社区公共运动场',
    value: '136'
  },
  {
    text: '培训会员h5',
    value: '137'
  },
  {
    text: '日照体育小程序',
    value: '138'
  },
  {
    text: '崇明休闲体育',
    value: '139'
  },
  {
    text: '圣步',
    value: '140'
  },
  {
    text: '漂移赛事服务系统',
    value: '141'
  },
  {
    text: '健步赛事服务系统',
    value: '142'
  },
  {
    text: '兰菁智慧赛事服务系统',
    value: '143'
  }
];


 /*
 * 用户基本信息表表格属性
 * @param 
 * @returns {*[]}
 */
 export function getUserBasicFields() {
  return [
    {
      prop: 'name',
      label: '姓名'
    },
    {
      prop: 'mobile',
      label: '手机号'
    },
    {
      prop: 'create_time',
      label: '创建时间'
    },
    {
      prop: 'openid',
      label: '微信登陆id'
    },
    {
      prop: 'app',
      label: '活动',
      flag: 'app_type'
    },
    {
      prop: 'id_type',
      label: '证件类型'
    },
    {
      prop: 'id_number',
      label: '证件号码'
    },
    {
      prop: 'uid',
      label: '用户uid'
    },
    {
      prop: 'role',
      label: '角色'
    },
    {
      prop: 'status',
      label: '状态'
    },
    {
      prop: 'nickname',
      label: '昵称'
    },
    {
      prop: 'avatarurl',
      label: '照片'
    },
    {
      prop: 'session_key',
      label: '登陆session'
    },
    {
      prop: 'gid',
      label: '企业id'
    },
    {
      prop: 'extappid',
      label: 'appid'
    },
    {
      prop: 'dist',
      label: '渠道号'
    },
    {
      prop: 'point',
      label: '当前剩余积分'
    },
    {
      prop: 'total_point',
      label: '总积分'
    },
    {
      prop: 'gender',
      label: '性别'
    },
    {
      prop: 'country',
      label: '国家'
    },
    {
      prop: 'province',
      label: '省份'
    },
    {
      prop: 'city',
      label: '城市'
    },
    {
      prop: 'district',
      label: '县（区）'
    },
    {
      prop: 'street',
      label: '街道'
    },
    {
      prop: 'address',
      label: '详细地址'
    },
    {
      prop: 'reg_user_id',
      label: '用户关联id'
    },
    {
      prop: 'jdid',
      label: 'jd号'
    },
    {
      prop: 'verifytime',
      label: 'verifytime'
    },
    {
      prop: 'phone_token',
      label: '手机token'
    },
    {
      prop: 'token_time',
      label: '在线时间'
    },
    {
      prop: 'validity',
      label: 'validity'
    },
    {
      prop: 'logindays',
      label: 'logindays'
    },
    {
      prop: 'email',
      label: '邮箱'
    },
    {
      prop: 'birth',
      label: '生日'
    },
    {
      prop: 'appid',
      label: 'appid'
    },
    {
      prop: 'login_type',
      label: '登陆类型'
    },
    {
      prop: 'login_id',
      label: '登陆id'
    }
  ]
}
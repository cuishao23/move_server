/**
 * 用户表表格属性
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
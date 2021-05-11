import axios from 'axios'
import cookie from 'cookie'

if (process.env.API_ROOT === '' && process.env.NODE_ENV === 'development') {
  alert('请配置 API_ROOT, 路径:config/dev.env.js')
  console.log("请配置")
}
console.log("API " + process.env.API_ROOT)
axios.defaults.baseURL = process.env.API_ROOT;
axios.defaults.headers.post['Content-Type'] = 'application/x-www-fromurlencodeed';
axios.defaults.withCredentials = false;
axios.interceptors.request.use((config) => {
  config.headers['X-Requested-With'] = 'XMLHttpRequest';
  config.headers['X-CSRFToken'] = cookie.parse(document.cookie).csrftoken;
  return config
});


export default axios;

// 查询用户实名登记信息
export const getUserInfoList = params => {
    return axios.get('/move/user', params).then(res => res.data)
};
// 导出用户实名登记信息
export const getUserDownLoad = params => {
  return axios.get('/move/download', params).then(res => res.data)
};
// 查询用户号码信息
export const getUserMobileInfoList = params => {
  return axios.get('/move/mobile', params).then(res => res.data)
};
// 导出用户号码信息
export const getUserMobileDownLoad = params => {
return axios.get('/move/mobiledownload', params).then(res => res.data)
};
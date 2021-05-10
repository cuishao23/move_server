/**
 * vue从后台获取数据，并导出EXCEL文件
 * @param value
 * @returns {*}
 * @constructor james 2021.5.8
 */

 export function Upexcele(value, name) {
    const url = window.URL.createObjectURL(value)
    const a = document.createElement('a')
    a.href = url
    a.download = name
    document.body.appendChild(a)
    a.click()
    window.URL.revokeObjectURL(url)
    document.body.removeChild(a)
  }
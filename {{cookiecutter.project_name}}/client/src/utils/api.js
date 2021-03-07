function encodeQueryParams(params) {
  console.log('params', params)
  return Object.keys(params)
    .map(key => {
      return `${encodeURIComponent(key)}=${encodeURIComponent(params[key])}`
    })
    .join('&')
}

export default encodeQueryParams

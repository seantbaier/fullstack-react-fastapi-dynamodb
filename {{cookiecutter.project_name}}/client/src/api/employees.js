import axios from 'axios'
import encodeQueryParams from '../utils/api'

const employees = (endpointUrl, entityPath) => ({
  find: params => {
    console.log('params', params)
    const queryString = encodeQueryParams(params)

    return axios
      .get(endpointUrl(`${entityPath}?${queryString}`))
      .then(response => response)
  },
  findById: id =>
    axios
      .get(endpointUrl(`${entityPath}/${id}`))
      .then(response => response.data),
  create: params =>
    axios.post(endpointUrl(entityPath), params).then(response => response.data),
  update: (id, params) =>
    axios
      .put(endpointUrl(`${entityPath}/${id}`), params)
      .then(response => response.data),
  delete: id =>
    axios
      .patch(endpointUrl(`${entityPath}/${id}`))
      .then(response => response.data),
})

export default employees

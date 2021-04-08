import axios from 'axios'

const projects = endpointUrl => ({
  find: params =>
    axios.get(`${endpointUrl}/projects`).then(response => response),
  findById: id =>
    axios.get(`${endpointUrl}/projects/${id}`).then(response => response.data),
  create: params =>
    axios
      .post(`${endpointUrl}/projects`, params)
      .then(response => response.data),
  update: (id, params) =>
    axios
      .put(`${endpointUrl}/projects/${id}`, params)
      .then(response => response.data),
  delete: id =>
    axios
      .patch(`${endpointUrl}/projects/${id}`)
      .then(response => response.data),
})

export default projects

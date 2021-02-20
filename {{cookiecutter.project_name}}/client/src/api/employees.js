import axios from 'axios'
const employeeResponse = {
  uid: 'd6c039d9-bf27-4735-be62-8187b3211718',
  first_name: 'leslie',
  last_name: 'knope',
  position: 'deputy assistant',
}

const employeeList = [
  employeeResponse,
  {
    uid: 'd6c039d9-bf27-1234-be62-8187b3211718',
    first_name: 'andy',
    last_name: 'dwyer',
    position: 'shoe shiner',
  },
  {
    uid: 'd6c039d9-4069-1234-be62-8187b3211718',
    first_name: 'apri',
    last_name: 'ludgate',
    position: 'assistant',
  },
  {
    uid: '456739d9-bf27-1234-be62-8187b3211718',
    first_name: 'anne',
    last_name: 'perkins',
    position: 'nurse',
  },
  {
    uid: 'd6c039d9-bf27-1234-be62-8187b3210h58',
    first_name: 'chris',
    last_name: 'traeger',
    position: 'city manager',
  },
]

const employeesResponse = {
  data: {
    employees: employeeList,
  },
}

const employees = (endpointUrl, entityPath) => ({
  find: params => employeesResponse,
  // axios.get(endpointUrl(`${entityPath}`)).then(response => response),
  findById: id => employeeResponse,
  // axios
  // .get(endpointUrl(`${entityPath}/${id}`))
  // .then(response => response.data),
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

import { useQuery } from 'react-query'
import api from '../api'

// Constants
import { SKIP, LIMIT } from '../constants/queryParams'

const getEmployees = async params => {
  const { skip = SKIP, limit = LIMIT } = params

  const employees = await api('employees').find({ skip, limit })
  return employees
}

export default function useTab() {
  return useQuery('employees', getEmployees)
}

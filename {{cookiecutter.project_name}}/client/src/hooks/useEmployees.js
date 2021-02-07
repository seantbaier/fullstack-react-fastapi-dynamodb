import { useQuery } from 'react-query'
import api from '../api'

const getEmployees = async () => {
  const employees = await api('employees').find()
  return employees
}

export default function useTab() {
  return useQuery('employees', getEmployees)
}

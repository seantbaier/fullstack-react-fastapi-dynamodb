import { useQuery } from 'react-query'
import api from '../api'

const getProjects = async () => {
  const projects = await api('projects').find()
  return projects
}

export default function useProjects() {
  return useQuery('projects', getProjects)
}

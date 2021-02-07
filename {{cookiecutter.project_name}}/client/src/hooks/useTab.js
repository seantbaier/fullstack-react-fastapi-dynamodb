import { useQuery } from 'react-query'

const getTab = async () => {
  const data = 'github'
  return data
}

export default function useTab() {
  return useQuery('tab', getTab)
}

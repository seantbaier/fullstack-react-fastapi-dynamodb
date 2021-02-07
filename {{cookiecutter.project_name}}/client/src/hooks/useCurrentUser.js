import { useQuery } from 'react-query'

const getCurrentUser = async () => {
  const data = {
    user: {
      email: 'sean.t.baier@gmail.com',
      first_name: 'sean',
      last_name: 'baier',
    },
  }
  return data
}

export default function useCurrentUser() {
  return useQuery('currentUser', getCurrentUser)
}

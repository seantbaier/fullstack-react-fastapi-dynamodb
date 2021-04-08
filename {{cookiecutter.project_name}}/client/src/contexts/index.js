import * as React from 'react'
import { BrowserRouter as Router } from 'react-router-dom'
import { QueryClient, QueryClientProvider, useIsFetching } from 'react-query'
import { ReactQueryDevtools } from 'react-query/devtools'
import { AuthProvider } from './auth'

const queryClient = new QueryClient()

function GlobalLoadingIndicator() {
  const isFetching = useIsFetching()

  return isFetching ? (
    <div>Queries are fetching in the background...</div>
  ) : null
}

function AppProviders({ children }) {
  return (
    <QueryClientProvider client={queryClient}>
      <Router>
        <AuthProvider>{children}</AuthProvider>
      </Router>
      <ReactQueryDevtools initialIsOpen={false} />
      <GlobalLoadingIndicator />
    </QueryClientProvider>
  )
}

export default AppProviders

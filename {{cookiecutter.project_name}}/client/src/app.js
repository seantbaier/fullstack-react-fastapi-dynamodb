/** @jsx jsx */
import React from 'react'
import { jsx } from '@emotion/react'
import { useAuth } from './contexts/auth'

// components
import FullPageSpinner from './components/spinner'

const AuthenticatedApp = React.lazy(() =>
  import(/* webpackPrefetch: true */ './authenticated-app'),
)
const UnauthenticatedApp = React.lazy(() => import('./unauthenticated-app'))

function App() {
  const { user } = useAuth()

  console.log('url', process.env.REACT_APP_CLIENT_URL)

  return (
    <React.Suspense fallback={<FullPageSpinner />}>
      {user ? <AuthenticatedApp /> : <UnauthenticatedApp />}
    </React.Suspense>
  )
}

export default App

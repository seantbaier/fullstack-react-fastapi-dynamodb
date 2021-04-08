/** @jsx jsx */
import React from 'react'
import { jsx } from '@emotion/react'
import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom'
import { useAuth } from './contexts/auth'

// Constants
import { LOGIN_URL, REGISTER_URL } from './utils/constants'

// Components
const Signup = React.lazy(() => import('./views/signup/signup'))
const Login = React.lazy(() => import('./views/login/login'))

function UnauthenticatedApp() {
  const { login, register } = useAuth()

  return (
    <Router>
      <Switch>
        <Route path={LOGIN_URL}>
          <Login onSubmit={login} />
        </Route>
        <Route path={REGISTER_URL}>
          <Signup onSubmit={register} />
        </Route>
        <Route path="/">
          <Signup onSubmit={login} />
        </Route>
        <Route path="*">
          <Link to={LOGIN_URL}>404 Not Found</Link>
        </Route>
      </Switch>
    </Router>
  )
}

export default UnauthenticatedApp

/** @jsx jsx */
import { jsx } from '@emotion/react'
import {
  BrowserRouter as Router,
  Redirect,
  Switch,
  Route,
  Link,
} from 'react-router-dom'

import Projects from './views/projects'
import Project from './views/project'
import Dashboard from './components/dashboard/dashboard'

function AuthenticatedApp() {
  return <AppRoutes />
}

function AppRoutes() {
  return (
    <Router>
      <Switch>
        <Route exact path="/project/:project_id">
          <Dashboard>
            <Project />
          </Dashboard>
        </Route>
        <Route exact path="/projects">
          <Dashboard>
            <Projects />
          </Dashboard>
        </Route>
        <Route exact path="/">
          <Redirect to="/projects" />
        </Route>
        <Route path="*">
          <Dashboard>
            <Link to="/projects">404 Not Found</Link>
          </Dashboard>
        </Route>
      </Switch>
    </Router>
  )
}

export default AuthenticatedApp

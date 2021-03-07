/** @jsx jsx */
import { jsx } from '@emotion/react'
import { ReactQueryDevtools } from 'react-query/devtools'
import { QueryClient, QueryClientProvider } from 'react-query'
import {
  BrowserRouter as Router,
  Redirect,
  Switch,
  Route,
  Link,
} from 'react-router-dom'

import Employees from './screens/employees'
import Employee from './screens/employee'
import Dashboard from './components/dashboard/dashboard'

const queryClient = new QueryClient()

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <AppRoutes />
      <ReactQueryDevtools initialIsOpen={false} />
    </QueryClientProvider>
  )
}

function AppRoutes() {
  return (
    <Router>
      <Switch>
        <Route exact path="/employee/:employee_id">
          <Dashboard>
            <Employee />
          </Dashboard>
        </Route>
        <Route exact path="/employees">
          <Dashboard>
            <Employees />
          </Dashboard>
        </Route>
        <Route exact path="/">
          <Redirect to="/employees" />
        </Route>
        <Route path="*">
          <Dashboard>
            <Link to="/employees">404 Not Found</Link>
          </Dashboard>
        </Route>
      </Switch>
    </Router>
  )
}

export default App

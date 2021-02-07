/** @jsx jsx */
import { jsx } from '@emotion/react'
import { ReactQueryDevtools } from 'react-query/devtools'
import { QueryClient, QueryClientProvider } from 'react-query'
import {
  HashRouter as Router,
  Redirect,
  Switch,
  Route,
  Link,
} from 'react-router-dom'

import Items from './screens/items'
import Item from './screens/item'
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
        <Route exact path="/items/:item">
          <Dashboard>
            <Item />
          </Dashboard>
        </Route>
        <Route exact path="/items">
          <Dashboard>
            <Items />
          </Dashboard>
        </Route>
        <Route exact path="/">
          <Redirect to="/items" />
        </Route>
        <Route path="*">
          <Dashboard>
            <Link to="/configs/github">404 Not Found</Link>
          </Dashboard>
        </Route>
      </Switch>
    </Router>
  )
}

export default App

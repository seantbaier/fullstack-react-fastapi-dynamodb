/** @jsx jsx */
import { jsx } from '@emotion/react'
import PropTypes from 'prop-types'

// Hooks
import useEmployees from '../hooks/useEmployees'

// Components
import Employee from './employee'

// Styles
import * as styles from './styles'

function Employees(props) {
  const { status, data, error, isFetching } = useEmployees()

  if (isFetching) {
    return <span>Loading...</span>
  }

  if (error) {
    return <div>{error}</div>
  }

  const { employees } = data.data || {}

  return (
    <main css={styles.employees}>
      {isFetching
        ? 'loading...'
        : employees.map(employee => (
            <Employee key={employee.last_name} employee={employee} />
          ))}
    </main>
  )
}

Employees.defaultProps = {
  children: null,
}

Employees.propTypes = {
  children: PropTypes.element,
}

export default Employees

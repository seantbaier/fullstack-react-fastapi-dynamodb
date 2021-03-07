/** @jsx jsx */
import { jsx } from '@emotion/react'
import PropTypes from 'prop-types'

// Hooks
import useEmployees from '../hooks/useEmployees'

// Components
import Table from '../components/table/table'

// Styles
import * as styles from './styles'

// Constants
import { SKIP, LIMIT } from '../constants/queryParams'

function Employees(props) {
  const { status, data, error, isFetching } = useEmployees({
    skip: SKIP,
    limit: LIMIT,
  })

  if (isFetching) {
    return <span>Loading...</span>
  }

  if (error) {
    return <div>{error}</div>
  }

  const { employees } = data.data || {}
  console.log('employees', employees)

  return (
    <div css={styles.employees}>
      {isFetching ? 'loading...' : <Table data={employees} />}
    </div>
  )
}

Employees.defaultProps = {
  children: null,
}

Employees.propTypes = {
  children: PropTypes.element,
}

export default Employees

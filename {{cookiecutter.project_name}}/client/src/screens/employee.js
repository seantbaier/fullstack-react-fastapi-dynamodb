/** @jsx jsx */
import { jsx } from '@emotion/react'
import PropTypes from 'prop-types'

// Styles
import * as styles from './styles'

function Employee(props) {
  const employee = props.employee
  return <div css={styles.employee}>{employee.first_name}</div>
}

Employee.defaultProps = {
  employee: {
    first_name: 'default',
    last_name: 'employee',
    position: 'employee',
  },
}

Employee.propTypes = {
  employee: PropTypes.object.isRequired,
}

export default Employee

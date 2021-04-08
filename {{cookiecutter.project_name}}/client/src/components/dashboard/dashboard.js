/** @jsx jsx */
import { jsx } from '@emotion/react'
import PropTypes from 'prop-types'

import DashboardHeader from '../headers/dashboardHeader/dashboardHeader'
import Sidebar from '../sidebar/sidebar'

// Styles
import * as styles from './styles'

function Dashboard(props) {
  const { children } = props
  return (
    <main css={styles.wrapper}>
      <Sidebar />
      <div css={styles.dashboard}>
        <DashboardHeader />
        <div>{children}</div>
      </div>
    </main>
  )
}

Dashboard.defaultProps = {
  children: null,
}

Dashboard.propTypes = {
  children: PropTypes.element,
}

export default Dashboard

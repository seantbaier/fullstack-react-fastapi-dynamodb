/** @jsx jsx  */
import { jsx } from '@emotion/react'
import { useHistory } from 'react-router-dom'
import api from '../../../api'

// Styles
import * as styles from './styles'
import { LOGGED_OUT_REDIRECT_URL } from '../../../utils/constants'

function DashboardHeader() {
  const history = useHistory()

  function handleLogout(e) {
    e.preventDefault()
    api.auth.logout()
    history.push(LOGGED_OUT_REDIRECT_URL)
  }

  return (
    <header css={styles.header}>
      <div className="container">
        <div css={styles.buttons}>
          <button onClick={handleLogout}>Logout</button>
        </div>
      </div>
    </header>
  )
}

export default DashboardHeader

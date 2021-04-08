/** @jsx jsx */
import { jsx } from '@emotion/react'
import PropTypes from 'prop-types'

import { FaSpinner } from 'react-icons/fa'

import * as styles from './styles.js'

function FullPageSpinner({ ariaLabel }) {
  return (
    <div css={styles.fullPageSpinner}>
      <FaSpinner css={styles.spinner} aria-label={ariaLabel} />
    </div>
  )
}

FullPageSpinner.defaultProps = {
  ariaLabel: 'loading',
}

FullPageSpinner.propTypes = {
  ariaLabel: PropTypes.string.isRequired,
}

export default FullPageSpinner

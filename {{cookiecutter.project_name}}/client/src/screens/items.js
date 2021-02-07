/** @jsx jsx */
import { jsx } from '@emotion/react'
import PropTypes from 'prop-types'

import Item from './item'

// Styles
import * as styles from './styles'

function Items(props) {
  return (
    <main css={styles.items}>
      <Item />
    </main>
  )
}

Items.defaultProps = {
  children: null,
}

Items.propTypes = {
  children: PropTypes.element,
}

export default Items

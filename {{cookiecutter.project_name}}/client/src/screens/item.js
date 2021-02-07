/** @jsx jsx */
import { jsx } from '@emotion/react'
import PropTypes from 'prop-types'

// Styles
import * as styles from './styles'

function Item(props) {
  return <div css={styles.item}>{props.item}</div>
}

Item.defaultProps = {
  item: 'Default Item',
}

Item.propTypes = {
  item: PropTypes.string.isRequired,
}

export default Item

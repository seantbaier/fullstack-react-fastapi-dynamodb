/** @jsx jsx */
import { jsx } from '@emotion/react'

// Styles
import * as styles from './styles'

function Button({ text, children, primary, ...props }) {
  const primaryButton = primary ? styles.primary : null

  return (
    <button css={[styles.base, primaryButton, props.style]}>{children}</button>
  )
}

export default Button

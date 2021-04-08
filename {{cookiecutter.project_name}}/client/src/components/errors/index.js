/** @jsx jsx */
import { jsx } from '@emotion/react'

// styles
import * as styles from './styles'

function FullPageErrorFallback({ error }) {
  return (
    <div role="alert" css={styles.fullPageErrorFallback}>
      <p>Uh oh... There's a problem. Try refreshing the app.</p>
      <pre>{error.message}</pre>
    </div>
  )
}

export { FullPageErrorFallback }

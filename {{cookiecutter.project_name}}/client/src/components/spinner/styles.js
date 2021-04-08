import { css, keyframes } from '@emotion/react'

const spin = keyframes({
  '0%': { transform: 'rotate(0deg)' },
  '100%': { transform: 'rotate(360deg)' },
})

const spinner = css`
  animation: ${spin} 1s linear infinite;
`

const fullPageSpinner = css`
  fontsize: 4em;
  height: 100vh;
  display: flex;
  flexdirection: column;
  justifycontent: center;
  alignitems: center;
`

export { spinner, fullPageSpinner }

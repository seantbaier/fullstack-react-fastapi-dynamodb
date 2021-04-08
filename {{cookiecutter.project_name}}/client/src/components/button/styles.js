import { css } from '@emotion/react'

import { gray500 } from '../../styles/utils'

const base = css`
  display: flex;
  align-items: center;
  justify-content: center;
  border: none;
  outline: none;
  background: transparent;
  border-radius: 8px;
  padding: 10px 15px;
  font-size: 1rem;
  cursor: pointer;
`

const primary = css`
  background-color: ${gray500};
  color: white;
`

export { base, primary }

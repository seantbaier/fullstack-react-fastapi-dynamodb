import { css } from '@emotion/react'

import { breakpoints } from '../../../styles/utils'

const inputBase = css`
  border-radius: 8px;
  border: 3px solid #333333;
  box-shadow: 5px 5px 10px 0 rgba(0, 0, 0, 0.1);
  font-size: 1.25rem;
  padding: 15px;

  @media (min-width: ${breakpoints.md}) {
    margin-right: 25px;
    width: 400px;
  }

  ::placeholder {
    color: rgba(0, 0, 0, 0.5);
  }

  :focus {
    outline: none;
  }
`

const inputError = css`
  border-color: red;

  :focus {
    border-color: red;
  }

  ::placeholder {
    color: red;
  }
`

export { inputBase, inputError }

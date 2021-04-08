import { css } from '@emotion/react'

import { gray200, gray500 } from '../../../styles/utils'

const header = css`
  display: flex;
  align-items: center;
  justify-content: center;

  .container {
    width: 100%;
    max-width: 1200px;
    display: flex;
    justify-content: space-between;
    padding: 25px 0;
    border-bottom: 1px solid ${gray200};
  }
`

const buttons = css`
  display: flex;
`

const logoIcon = css`
  height: 25px;
  width: 25px;
  color: ${gray200};
`

const logoText = css`
  color: ${gray200};
`

const loginButton = css`
  color: ${gray200};
  transition: 0.5s;

  :hover {
    color: ${gray500};
  }
`

export { header, buttons, logoIcon, logoText, loginButton }

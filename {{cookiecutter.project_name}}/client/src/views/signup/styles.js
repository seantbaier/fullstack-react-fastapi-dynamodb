import { css } from '@emotion/react'

import { gray500, pageMaxWidth } from '../../styles/utils'

const signup = css`
  height: 100vh;
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
`

const mainWrapper = css`
  display: flex;
  justify-content: center;

  .container {
    max-width: ${pageMaxWidth};
    margin-top: 50px;
    padding: 0 25px;
    margin-bottom: 50px;
  }
`

const headingOne = css`
  font-size: 4rem;
  font-weight: bold;
  margin: 50px 0;
  color: #333333;
  line-height: 4rem;
`

const paragraph = css`
  color: ${gray500};
  font-size: 1.5rem;
  margin-bottom: 50px;
  line-height: 2.5rem;
`

const logoIcon = css`
  height: 40px;
  width: 40px;
`

const logoText = css`
  font-size: 2rem;
`

export { signup, mainWrapper, headingOne, paragraph, logoIcon, logoText }

import { css } from '@emotion/react'

// utils
import * as utils from '../../styles/utils'

const table = css`
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.15);
  width: 100%;
  padding: 25px;
  border-radius: 2px;
  th {
    text-align: left;
    color: ${utils.primaryFontColor};
    padding-bottom: 15px;
  }
  td {
    padding: 15px 0;
  }
`

export default table

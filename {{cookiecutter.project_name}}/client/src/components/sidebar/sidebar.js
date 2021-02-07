/** @jsx jsx */
import { jsx } from '@emotion/react'
import { Link } from 'react-router-dom'

import sidebar from './styles'

function Sidebar() {
  return (
    <div css={sidebar}>
      <div>
        Items
        <Link to="/items" />
      </div>
    </div>
  )
}

export default Sidebar

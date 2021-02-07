/** @jsx jsx  */
import { jsx } from '@emotion/react'
import { useLocation } from 'react-router-dom'

// Styles
import header from './styles'

function Header() {
  const location = useLocation()
  const { pathname } = location
  const title = pathname.split('/')[1]
  return (
    <div css={header}>
      <h1>{title}</h1>
    </div>
  )
}

export default Header

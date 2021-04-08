import React from 'react'
import { Link, useRouteMatch } from 'react-router-dom'

// Components
import { FaFeatherAlt } from 'react-icons/fa'
import { PropTypes } from 'prop-types'
import { REGISTER_URL, LOGGED_OUT_REDIRECT_URL } from '../../../utils/constants'

function Button({ text, path }) {
  return (
    <Link
      to={path}
      className="capitalize text-gray-200 duration-200 hover:text-gray-400"
    >
      {text}
    </Link>
  )
}

Button.propTypes = {
  text: PropTypes.string.isRequired,
  path: PropTypes.string.isRequired,
}

function UnauthenticatedHeader() {
  let { url } = useRouteMatch()

  let path = LOGGED_OUT_REDIRECT_URL
  let buttonText = 'Login'

  if (url === LOGGED_OUT_REDIRECT_URL) {
    path = REGISTER_URL
    buttonText = 'Sign Up'
  }

  return (
    <header className="">
      <div className="md:container md:mx-auto py-8 px-5 md:px-0 flex items-center justify-between">
        <div className="flex items-center">
          <div className="flex items-center mr-4">
            <FaFeatherAlt className="h-5 w-5 text-gray-200" />
          </div>
          <div className="text-gray-200">Cookie Cutter</div>
        </div>
        <Button text={buttonText} path={path} />
      </div>
    </header>
  )
}

export default UnauthenticatedHeader

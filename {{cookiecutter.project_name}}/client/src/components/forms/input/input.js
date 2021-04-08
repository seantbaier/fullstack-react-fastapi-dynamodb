import React, { Fragment } from 'react'
import { PropTypes } from 'prop-types'

function Input({ id, type, placeholder, dataCy }) {
  return (
    <Fragment>
      <label htmlFor="email" className="hidden">
        email
      </label>
      <input
        id={id}
        className={`
          box-border
          rounded
          border-3
          border-charcoal
          ring-0
          focus:ring-0
          outline-none
          focus:outline-none
          focus:border-primary
          shadow
          mb-2
          py-3
          text-lg
          placeholder-gray-400
          text-charcoal
        `}
        type={type}
        placeholder={placeholder}
        data-cy={dataCy}
      />
    </Fragment>
  )
}

Input.defaultProps = {
  placeholder: null,
}

Input.propTypes = {
  type: PropTypes.string.isRequired,
  placeholder: PropTypes.string,
}

export default Input

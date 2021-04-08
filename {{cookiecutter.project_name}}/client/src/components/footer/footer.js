import React from 'react'

// Components
import { FaFeatherAlt } from 'react-icons/fa'

function Footer() {
  return (
    <footer className="py-20 px-5 lg:px-0 bg-gray-100">
      <div className="lg:container lg:mx-auto flex align-center">
        <div className="flex items-center mr-2">
          <FaFeatherAlt className="text-charcoal" />
        </div>
        <div className="text-charcoal">Cookie Cutter</div>
      </div>
    </footer>
  )
}

export default Footer

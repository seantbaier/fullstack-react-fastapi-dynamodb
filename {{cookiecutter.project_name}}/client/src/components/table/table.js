/** @jsx jsx  */
import { jsx } from '@emotion/react'

import table from './styles'

function Table({ data }) {
  return (
    <table css={table}>
      <thead>
        <tr>
          <th>Id</th>
          <th>First Name</th>
          <th>Last Name</th>
          <th>Positon</th>
        </tr>
      </thead>
      <tbody>
        {data.map(datum => {
          return (
            <tr key={datum.uid}>
              {Object.keys(datum).map(key => {
                return <td key={key}>{datum[key]}</td>
              })}
            </tr>
          )
        })}
      </tbody>
    </table>
  )
}

export default Table

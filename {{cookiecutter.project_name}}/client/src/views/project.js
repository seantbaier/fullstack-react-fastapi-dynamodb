/** @jsx jsx */
import { jsx } from '@emotion/react'
import PropTypes from 'prop-types'

// Styles
import * as styles from './styles'

function Project(props) {
  const project = props.project
  return <div css={styles.project}>{project.title}</div>
}

Project.defaultProps = {
  project: {
    title: 'default',
  },
}

Project.propTypes = {
  project: PropTypes.object.isRequired,
}

export default Project

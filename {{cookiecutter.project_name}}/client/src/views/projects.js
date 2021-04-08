/** @jsx jsx */
import { jsx } from '@emotion/react'
import PropTypes from 'prop-types'

// Hooks
import useProjects from '../hooks/useProjects'

// Components
import Project from './project'

// Styles
import * as styles from './styles'

function Projects(props) {
  const { data, error, isFetching } = useProjects()

  if (isFetching) {
    return <span>Loading...</span>
  }

  if (error) {
    return <div>{error}</div>
  }

  const { projects } = data.data || {}

  return (
    <main css={styles.projects}>
      {isFetching
        ? 'loading...'
        : projects.map(project => (
            <Project key={project.tile} project={project} />
          ))}
    </main>
  )
}

Projects.defaultProps = {
  children: null,
}

Projects.propTypes = {
  children: PropTypes.element,
}

export default Projects

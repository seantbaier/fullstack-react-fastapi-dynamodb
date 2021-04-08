/** @jsx jsx */
import { jsx } from '@emotion/react'

// Components
import SignupForm from './form/signupForm'
import UnauthenticatedHeader from '../../components/headers/unauthenticatedHeader/unauthenticatedHeader'
import Footer from '../../components/footer/footer'

// Styles
import * as styles from './styles'

function Signup() {
  return (
    <div css={styles.signup}>
      <UnauthenticatedHeader />
      <main css={styles.mainWrapper}>
        <div className="container">
          <h1 css={styles.headingOne}>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit.
          </h1>
          <p css={styles.paragraph}>
            Sed quis lorem vestibulum nisl mattis sollicitudin ut nec tortor.
            Donec id tortor facilisis, volutpat mi quis, tristique enim. Integer
            cursus dolor ac placerat ultrices.
          </p>
          <SignupForm />
        </div>
      </main>
      <Footer />
    </div>
  )
}

export default Signup

/** @jsx jsx */
import { jsx } from '@emotion/react'
import { Formik, Form } from 'formik'
import * as Yup from 'yup'

// Components
import Input from '../../../components/forms/input/input'

// Styles
import * as styles from './styles'

const validationSchema = Yup.object({
  email: Yup.string().email('example@email.com').required('example@email.com'),
})

const SignupForm = ({ onSubmit }) => {
  function handleSubmit(event) {
    event.preventDefault()
    const { username, password } = event.target.elements

    run(
      onSubmit({
        username: username.value,
        password: password.value,
      }),
    )
  }

  return (
    <Formik
      initialValues={{
        email: '',
      }}
      validationSchema={validationSchema}
      onSubmit={(values, { setSubmitting }) =>
        handleSubmit(values, setSubmitting)
      }
    >
      {formik => {
        const { isValid, touched, values, errors } = formik

        const showErrorMessage = values.email && errors.email

        return (
          <Form css={styles.signupForm}>
            <div className="form-container">
              <Input
                id="signup-email"
                label="Email Address"
                name="email"
                type="email"
                placeholder="example@email.com"
                isValid={isValid}
                dataCy="signup-email"
              />

              <button
                id="signup-submit"
                css={styles.button}
                type="submit"
                disabled={touched && !isValid}
                data-cy="signup-submit"
              >
                Sign up
              </button>
            </div>
            {showErrorMessage ? (
              <span className="error-message">{errors.email}</span>
            ) : null}
          </Form>
        )
      }}
    </Formik>
  )
}

export default SignupForm

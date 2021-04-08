import React from 'react'
import { useHistory, useRouteMatch } from 'react-router-dom'
import useAsync from '../../hooks/useAsync'
import { useAuth } from '../../contexts/auth'

// components
import UnauthenticatedHeader from '../../components/headers/unauthenticatedHeader/unauthenticatedHeader'
import Footer from '../../components/footer/footer'
import Input from '../../components/forms/input/input'

// constants
import { LOGIN_URL, LOGGED_IN_REDIRECT_URL } from '../../utils/constants'

function LoginForm({ onSubmit, buttonText }) {
  const { isError, error, run } = useAsync()
  let history = useHistory()

  if (isError) {
    console.error(error)
  }

  const handleSubmit = event => {
    event.preventDefault()
    const { email, password } = event.target.elements

    run(
      onSubmit({
        email: email.value,
        password: password.value,
      }),
    ).then(() => history.push(LOGGED_IN_REDIRECT_URL))
  }

  return (
    <form className="flex flex-col py-4" onSubmit={handleSubmit}>
      <Input id="email" type="email" placeholder="email" />
      <Input id="password" type="password" placeholder="password" />
      <button
        className={`
          capitalize
          border-box 
          shadow 
          bg-primary 
          h-14
          mt-2
          text-lg 
          text-white 
          hover:bg-secondary 
          duration-200 
          font-bold 
          rounded
          focus:outline-none
        `}
        type="submit"
      >
        {buttonText}
      </button>
    </form>
  )
}

function Login() {
  const { login } = useAuth()
  const { url } = useRouteMatch()

  const buttonText = url === LOGIN_URL ? 'Sign In' : 'Sign Up'

  return (
    <div className="h-screen flex flex-col justify-between">
      <UnauthenticatedHeader />
      <main className="md:container md:mx-auto py-10 px-5 md:px-64">
        <div className="text-4xl font-bold text-charcoal">Login</div>
        <LoginForm onSubmit={login} buttonText={buttonText} />
      </main>
      <Footer />
    </div>
  )
}

export default Login

import Amplify from 'aws-amplify'
import Auth from '@aws-amplify/auth'
import axios from 'axios'

import auth from './auth'
import projects from './projects'

Amplify.configure({
  mandatorySignIn: true,
  region: process.env.REACT_APP_AWS_DEFAULT_REGION,
  userPoolId: process.env.REACT_APP_COGNITO_USER_POOL_ID,
  identityPoolId: process.env.REACT_APP_COGNITO_IDENTITY_POOL_ID,
  userPoolWebClientId: process.env.REACT_APP_COGNITO_APP_CLIENT_ID,
})

const endpointUrl = (type, url) =>
  [
    process.env.REACT_APP_API_URL,
    type,
    process.env.REACT_APP_API_VERSION,
    url,
  ].join('/')

const getJwtToken = async () => {
  let token = null

  try {
    const session = await Auth.currentSession()

    token = session.idToken.jwtToken
  } catch (err) {
    // ignore for now...
  }

  return token
}

// Add auth credentials to all outgoing API requests.
axios.interceptors.request.use(
  async config => {
    if (config.url.includes(process.env.REACT_APP_API_URL)) {
      const token = await getJwtToken()
      if (token) {
        // eslint-disable-next-line no-param-reassign
        config.headers.common.authorization = token
      }
    }

    return config
  },
  error => {
    return Promise.reject(error)
  },
)

const api = {
  auth: auth(Auth),
  projects: projects(endpointUrl),
}

export default api

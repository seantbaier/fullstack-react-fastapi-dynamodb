const auth = Auth => ({
  login: async ({ email, password }) => Auth.signIn({ email, password }),
  register: params => {
    const { email: rawEmail, password, phoneNumber, ...signUpParams } = params
    // Cognito emails are case sensitive (???!??!?!?!?)
    // Ensure lowercase before hitting backend.
    const email = rawEmail.toLowerCase()

    return Auth.signUp({
      username: email,
      password,
      attributes: { email, phone_number: phoneNumber, ...signUpParams },
    }).then(response => {
      response.user.password = password
      response.user.email = email
      return response
    })
  },
  currentSession: () => Auth.currentSession(),
  logout: () => {
    Auth.signOut()
  },
})

export default auth

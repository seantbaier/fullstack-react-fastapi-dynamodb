import React, {
  useCallback,
  useEffect,
  useContext,
  createContext,
  useMemo,
} from 'react'
import { useQueryClient } from 'react-query'
import api from '../api'

// hooks
import useAsync from '../hooks/useAsync'

// Components
import FullPageSpinner from '../components/spinner'
import { FullPageErrorFallback } from '../components/errors'

async function getCurrentUser() {
  try {
    const { accessToken } = await api.auth.currentSession()
    const { payload: user } = accessToken

    if (user) {
      return user
    }

    return null
  } catch (err) {
    console.error('err', err)
  }

  return null
}

const AuthContext = createContext()
AuthContext.displayName = 'AuthContext'

function AuthProvider(props) {
  const queryClient = useQueryClient()

  const {
    data: user,
    status,
    error,
    isLoading,
    isIdle,
    isError,
    isSuccess,
    run,
    setData,
  } = useAsync()

  useEffect(() => {
    const appDataPromise = getCurrentUser()
    run(appDataPromise)
  }, [run])

  const login = useCallback(
    form => api.auth.login(form).then(user => setData(user)),
    [setData],
  )

  const register = useCallback(
    form => api.auth.register(form).then(user => setData(user)),
    [setData],
  )

  const logout = useCallback(() => {
    api.auth.signOut()
    queryClient.invalidateQueries()
    setData(null)
  }, [setData, queryClient])

  const value = useMemo(() => ({ user, login, logout, register }), [
    login,
    logout,
    register,
    user,
  ])

  if (isLoading || isIdle) {
    return <FullPageSpinner />
  }

  if (isError) {
    return <FullPageErrorFallback error={error} />
  }

  if (isSuccess) {
    return <AuthContext.Provider value={value} {...props} />
  }

  throw new Error(`Unhandled status: ${status}`)
}

function useAuth() {
  const context = useContext(AuthContext)
  if (context === undefined) {
    throw new Error(`useAuth must be used within a AuthProvider`)
  }
  return context
}

export { AuthProvider, useAuth }

import api from './api'

export async function login(username, password) {
    try {
      const response = await api.post(
        '/auth/login',
        {
          username,
          password
        },
        {
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
          },
          withCredentials: true, // <-- necessário para cookies + CORS
          transformRequest: [(data) => {
            const params = new URLSearchParams()
            for (const key in data) {
              params.append(key, data[key])
            }
            return params
          }]
        }
      )
  
      const token = response.data.access_token
      localStorage.setItem('token', token)
  
      return true
    } catch (error) {
      console.error('Login failed:', error)
      return false
    }
  }
  
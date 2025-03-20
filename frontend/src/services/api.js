import axios from 'axios'

export const api = axios.create({
  baseURL: 'http://192.168.1.252:8000',
  withCredentials: true
})

export default api

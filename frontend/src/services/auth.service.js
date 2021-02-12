import {LOGIN, LOGOUT, URL, API} from './http-common.js'

class AuthService {
    login(username, password) {
      return LOGIN(username, password)
        .then(response => Promise.resolve(response))
        .catch(error => Promise.reject(error))
    }

    logout(){
      return LOGOUT()
    }

    register(username, email, password, confirm_password) {
      const registerData = {username, email, password, confirm_password}
      return API.post(URL.userCreateUser, registerData)
        .then(response => Promise.resolve(response.data))
        .catch(error => Promise.reject(error))
    }
  }
  
  export default new AuthService();
// login(): POST {username, password} & save JWT to Local Storage
// logout(): remove JWT from Local Storage
// register(): POST {username, email, password, conformpassword}
import Api from './http-common.js'

class AuthService {
    login(user) {
      Api.post('/auth/token/', user)
        .then(response => response.json())
        .then(data => {
          if (data.refresh && data.access) {
            localStorage.setItem('userid', JSON.stringify(data));
            return data
          }else throw new Error(`${data.detail}`)
        })
        .catch(error => console.error(error));
    }
  
    logout() {
      localStorage.removeItem('user');
    }
  
    register(user) {
      return fetch('/api/user/', {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json',  
        },
        credentials: "same-origin",
        body: JSON.stringify(user)
      })
      .then(response => response.json());
    }

    refreshlogin(refresh){
      return refresh
    }
  }
  
  export default new AuthService();
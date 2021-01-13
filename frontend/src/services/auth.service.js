// login(): POST {username, password} & save JWT to Local Storage
// logout(): remove JWT from Local Storage
// register(): POST {username, email, password, conformpassword}

class AuthService {
    login(user) {
      console.log(user)
      return fetch('/api/auth/token/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
          },
          redirect: 'follow',
          credentials: "same-origin",
          body: JSON.stringify(user)
        })
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
  }
  
  export default new AuthService();
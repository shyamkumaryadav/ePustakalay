// login(): POST {username, password} & save JWT to Local Storage
// logout(): remove JWT from Local Storage
// register(): POST {username, email, password, conformpassword}

class AuthService {
    login(user) {
      return fetch('/api/auth/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'  
          },
          credentials: "same-origin",
          body: JSON.stringify(user)
        })
        .then(response => response.json())
        .then(data => {
          if (data.access && data.refresh) {
            localStorage.setItem('user', JSON.stringify(data));
          }
  
          return data;
        });
    }
  
    logout() {
      localStorage.removeItem('user');
    }
  
    register(user) {
      return fetch('/api/user/', {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json'  
        },
        credentials: "same-origin",
        body: JSON.stringify(user)
      })
      .then(response => response.json());
    }
  }
  
  export default new AuthService();
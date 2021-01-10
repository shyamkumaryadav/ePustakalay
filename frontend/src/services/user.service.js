import authHeader from './auth-header';


class UserService {
//   getPublicContent() {
//     return axios.get(API_URL + 'all');
//   }

  getUser() {
    return fetch('/api/user/', {
        headers: authHeader()
    })
    .then(response => response.json())
    .then(data => data)
  }
 
}

export default new UserService();
import authHeader from './auth-header';


class UserService {
//   getPublicContent() {
//     return axios.get(API_URL + 'all');
//   }

  getUser(username) {
    return fetch(`/api/user/${username}/`, {
    })
    .then(response => response.json())
    .then(data => console.log(data))
  }
 
}

export default new UserService();
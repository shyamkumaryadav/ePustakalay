

class UserService {
  getUser(username) {
    return fetch(`/api/user/${username}/`, {
    })
    .then(response => response.json())
    .then(data => console.log(data))
  }
 
}

export default new UserService();
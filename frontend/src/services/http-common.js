import axios from "axios";
/*
 * API
 *
 * This refreshes the request and retries the token if it is invalid.
 * This is what you use to create any requests that need the Tokens.
 * Reference: https://hackernoon.com/110percent-complete-jwt-authentication-with-django-and-react-2020-iejq34ta
 * IMAGE: https://hasura.io/blog/best-practices-of-using-jwt-with-graphql/#jwt_vs_session
 *
 * Example:
 *     API.get(URL,extraParameters)
 *        .then(response=>{
 *          // do something with successful request
 *        }).catch((error)=> {
 *          // handle any errors. if Unauthorized try refreshToken
 *        });
*/
const BASE_URL = '/api';
const ACCESS_TOKEN = 'access_token';
const REFRESH_TOKEN = 'refresh_token';
const xsrfCookieName = 'csrftoken';
const xsrfHeaderName = 'X-CSRFTOKEN';

// List of URL in My API
const URL = {
  "apiRoot": "/",
  "apiLogin": "/auth/login/",
  "apiLogout": "/auth/logout/",
  "gettoken": "/token/obtain/",
  "reftoken": "/token/refresh/",
  "vertoken": "/token/verify/",
  "bookauthorList": "/book-authors/",
  "bookauthorDetail": "/book-authors/{pk}/",
  "genreList": "/book-genres/",
  "genreDetail": "/book-genres/{pk}/",
  "issueList": "/book-issue/",
  "issueDetail": "/book-issue/{pk}/",
  "bookpublishList": "/book-publish/",
  "bookpublishDetail": "/book-publish/{pk}/",
  "bookList": "/books/",
  "bookDetail": "/books/{pk}/",
  "userList": "/user/",
  "userDetail": "/user/{username}/",
  "userChangePassword": "/user/{username}/change_password/",
  "userUpdateUser": "/user/{username}/update_user/",
  "userCreateUser": "/user/create_user/",
  "userPasswordResetConfirm": "/user/password_reset_confirm/",
  "userResetPassword": "/user/reset_password/"
}

// call me any Time any place
const API = axios.create({
  baseURL: BASE_URL,
  // timeout: 5000,
  headers: {
    xsrfCookieName,
    xsrfHeaderName,
  }
});

// Use Me If Auth required
const AUTHAPI = axios.create({
  baseURL: BASE_URL,
  // timeout: 5000,
  headers: {
    Authorization: `Bearer ${window.localStorage.getItem(ACCESS_TOKEN)}`,
    xsrfCookieName,
    xsrfHeaderName,
  },
});

const isCorrectRefreshError = (status) => status === 401; // Unauthorized
//       /\ <-------> \/
const errorInterceptor = (error) => {
  const originalRequest = error.config;
  const { status } = error.response;
  if (isCorrectRefreshError(status)) {
    // Try to Refresh the token if not just reject
    return refreshToken().then(() => {
      const headerAuthorization = `Bearer ${window.localStorage.getItem(ACCESS_TOKEN)}`;
      AUTHAPI.defaults.headers.Authorization = headerAuthorization;
      originalRequest.headers.Authorization = headerAuthorization;
      return AUTHAPI(originalRequest);
    }).catch((tokenRefreshError) => {
      // if token refresh fails, logout the user to avoid potential security risks.
      logout();
      return Promise.reject(tokenRefreshError);
    });
  }
  return Promise.reject(error);
};
// Promise


// To Log The User
const login = (username, password) => {
  const loginData = {username, password};
  return API.post(URL.gettoken, loginData)
  .then(response => {
    window.localStorage.setItem(ACCESS_TOKEN, response.data.access);
    window.localStorage.setItem(REFRESH_TOKEN, response.data.refresh);
    const headerAuthorization = `Bearer ${window.localStorage.getItem(ACCESS_TOKEN)}`;
    AUTHAPI.defaults.headers.Authorization = headerAuthorization;
    return Promise.resolve(response.data);
  })
  .catch(error => Promise.reject(error));
}
// Promise

// To Log Out The User
const logout = () => {
  window.localStorage.removeItem(ACCESS_TOKEN);
  window.localStorage.removeItem(REFRESH_TOKEN);
  AUTHAPI.defaults.headers.Authorization = "";
}

// Auto call if token expired
const refreshToken = () => {
  const refreshData = { 
    refresh: window.localStorage.getItem(REFRESH_TOKEN)
  };
  return API.post(URL.reftoken, refreshData)
    .then(response => {
      window.localStorage.setItem(ACCESS_TOKEN, response.data.access);
      return Promise.resolve(response.data);
    }).catch((error) => Promise.reject(error));
};
// Promise

// if get error of Unauthorized
AUTHAPI.interceptors.response.use(
  (response) => response, // this is for all successful requests.
  (error) => errorInterceptor(error), // handle the request
); 
  
  
export {API, URL, AUTHAPI, login as LOGIN, logout as LOGOUT, ACCESS_TOKEN, REFRESH_TOKEN}
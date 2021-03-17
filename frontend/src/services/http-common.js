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

// List of URL https://documenter.getpostman.com/view/13650818/Tz5qZx48
const URL = {
  "getToken": "/token/obtain/", // POST
  "refToken": "/token/refresh/", // POST
  "verToken": "/token/verify/", // POST
  "bookAuthor": "/book-authors/", // GET POST
  "bookAuthorDetail": "/book-authors/{pk}/", // GET PUT DETELE
  "genre": "/book-genres/", // GET POST
  "genreDetail": "/book-genres/{pk}/", // GET PUT DETELE
  "issue": "/book-issue/", // GET POST
  "issueDetail": "/book-issue/{pk}/", // GET PUT DETELE
  "bookPublish": "/book-publish/", // GET POST
  "bookPublishDetail": "/book-publish/{pk}/", // GET PUT DETELE
  "book": "/books/", // GET POST
  "bookDetail": "/books/{pk}/", // GET PUT DETELE
  "userList": "/users/", // GET
  "userDetail": "/users/{pk}/", // GET PUT DETELE
  "ChangePassword": "/users/{pk}/change_password/", // POST
  "userCreate": "/users/create_user/", // POST
  "passwordResetConfirm": "/users/password_reset_confirm/", // POST
  "resetPassword": "/users/reset_password/" // POST
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
  return API.post(URL.getToken, loginData)
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
  return API.post(URL.refToken, refreshData)
    .then(response => {
      window.localStorage.setItem(ACCESS_TOKEN, response.data.access);
      return Promise.resolve(response.data.statusText);
    }).catch((error) => Promise.reject(error));
};
// Promise

// if get error of Unauthorized
AUTHAPI.interceptors.response.use(
  (response) => response, // this is for all successful requests.
  (error) => errorInterceptor(error), // handle the request
); 
  
  
export {API, URL, AUTHAPI, login as LOGIN, logout as LOGOUT, ACCESS_TOKEN, REFRESH_TOKEN}
import axios from "axios";


// this base url will be change based on
// if you need to point to production.
const BASE_URL = '/api/';
const ACCESS_TOKEN = 'access_token';
const REFRESH_TOKEN = 'refresh_token';
const xsrfCookieName = 'csrftoken';
const xsrfHeaderName = 'X-CSRFTOKEN';

const authApi = axios.create({
  baseURL: BASE_URL,
  headers: {
    xsrfCookieName,
    xsrfHeaderName,
    Authorization: `Bearer ${localStorage.getItem(ACCESS_TOKEN)}`,
  }
})

const Api =  axios.create({
  baseURL: BASE_URL,
  headers: {
    xsrfCookieName,
    xsrfHeaderName,
  }
});


const tokenRequest = axios.create({
  baseURL: BASE_URL,
  timeout: 5000,
  headers: {
    xsrfCookieName,
    xsrfHeaderName,
  },
});

const loginUser = (username, password) => {
  const loginBody = { username, password };
  return tokenRequest.post('token/', loginBody)
    .then((response) => {
      window.localStorage.setItem(ACCESS_TOKEN, response.data.access);
      window.localStorage.setItem(REFRESH_TOKEN, response.data.refresh);
      return Promise.resolve(response.data);
    }).catch((error) => {
      console.log(error);
      return Promise.reject(error);
    });
};

const refreshToken = () => {
  const refreshBody = { refresh: window.localStorage.getItem(REFRESH_TOKEN) };
  return tokenRequest.post('token/refresh/', refreshBody)
    .then((response) => {
      window.localStorage.setItem(ACCESS_TOKEN, response.data.access);
      return Promise.resolve(response.data);
    }).catch((error) => Promise.reject(error));
};

const isCorrectRefreshError = (status) => status === 401;

/*
 * authRequest
 *
 * This refreshes the request and retries the token if it is invalid.
 * This is what you use to create any requests that need the Tokens.
 * Reference: https://hackernoon.com/110percent-complete-jwt-authentication-with-django-and-react-2020-iejq34ta
 * https://hasura.io/blog/best-practices-of-using-jwt-with-graphql/#jwt_vs_session
 *
 * Example:
 *     authRequest.get('/path/to/endpoint/',extraParameters)
 *        .then(response=>{
 *          // do something with successful request
 *        }).catch((error)=> {
 *          // handle any errors.
 *        });
*/
const authApi = axios.create({
  baseURL: BASE_URL,
  timeout: 5000,
  headers: {
    Authorization: `Bearer ${window.localStorage.getItem(ACCESS_TOKEN)}`,
    xsrfCookieName,
    xsrfHeaderName,
  },
});

const logoutUser = () => {
  window.localStorage.removeItem(ACCESS_TOKEN);
  window.localStorage.removeItem(REFRESH_TOKEN);
  authApi.defaults.headers.Authorization = '';
};

const errorInterceptor = (error) => {
  const originalRequest = error.config;
  const { status } = error.response;
  if (isCorrectRefreshError(status)) {
    return refreshToken().then(() => {
      const headerAuthorization = `Bearer ${window.localStorage.getItem(ACCESS_TOKEN)}`;
      authApi.defaults.headers.Authorization = headerAuthorization;
      originalRequest.headers.Authorization = headerAuthorization;
      return authApi(originalRequest);
    }).catch((tokenRefreshError) => {
      // if token refresh fails, logout the user to avoid potential security risks.
      logoutUser();
      return Promise.reject(tokenRefreshError);
    });
  }
  return Promise.reject(error);
};

authApi.interceptors.response.use(
  (response) => response, // this is for all successful requests.
  (error) => errorInterceptor(error), // handle the request
);

export {
  Api as default,
  tokenRequest, loginUser, logoutUser, refreshToken, authApi,
  errorInterceptor, BASE_URL, ACCESS_TOKEN, REFRESH_TOKEN, authApi
};

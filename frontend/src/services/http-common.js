import axios from "axios";


// this base url will be change based on
// if you need to point to production.
// const BASE_URL = 'http://localhost:8000';
// const ACCESS_TOKEN = 'access_token';
// const REFRESH_TOKEN = 'refresh_token';


export default axios.create({
  baseURL: "/api",
  headers: {
    xsrfCookieName: 'csrftoken',
    xsrfHeaderName: 'X-CSRFTOKEN',
    Authorization: `Bearer ${localStorage.getItem('access')}`,
  }
});
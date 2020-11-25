import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Terms from '@/views/Terms.vue'
import Error404 from '@/views/Error404.vue'
import ViewBook from '@/views/ViewBook.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/terms',
    name: 'Terms',
    component: Terms
  },
  {
    path: '/books',
    name: 'ViewBook',
    component: ViewBook
  },
  {
    path: '*',
    name: 'Error404',
    component: Error404
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

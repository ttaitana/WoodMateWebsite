import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import landingPage from '../components/landingPage/base'
import login from '../components/authenticate/login'
import register from '../components/authenticate/register'
import products from '../components/itemsPage/productSelect'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'landingPage',
      component: landingPage
    },
    {
      path: '/login',
      name: 'login',
      component: login
    },
    {
      path: '/register',
      name: 'register',
      component: register
    },
    {
      path: '/products',
      name: 'itemsPage',
      component: products
    }
  ]
})

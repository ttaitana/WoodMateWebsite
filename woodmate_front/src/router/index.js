import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import landingPage from '../components/landingPage/base'
import login from '../components/authenticate/login'

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
    }
  ]
})

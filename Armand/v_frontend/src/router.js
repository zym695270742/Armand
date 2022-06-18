import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
// import Help from './views/Help.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      component: Home
    },
    // {
    //   path: '/help',
    //   component: Help
    // },
  ]
})

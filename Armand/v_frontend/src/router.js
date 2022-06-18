import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Help from './views/Help.vue'
import Project_list from './views/Project_list.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      component: Home
    },
    {
      path: '/help',
      component: Help
    },
    {
      path: '/project_list',
      component: Project_list
    },
  ]
})

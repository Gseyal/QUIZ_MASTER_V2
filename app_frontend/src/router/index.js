import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from '../views/Dashboard.vue'
import store from '../store/store';
const routes = [
  {
    path: '/',
    name: 'home',
    component: Dashboard,
    meta: {requiresAuth: false}
  },
  
  {
    path: '/chapter',
    name: 'chapters',
    component: () => import('../views/chapter.vue'),
    meta: {requiresAuth: false}
  },
  {
    path: '/quiz',
    name: 'quiz',
    component: () => import('../views/Quiz.vue'),
    meta: {requiresAuth: true}
  },
  {
    path: '/score',
    name: 'score',
    component: () => import('../views/score.vue'),
    meta: {requiresAuth: true}
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/login.vue'),
    meta: {requiresAuth: false}
  },
  {
    path: '/stat',
    name: 'stat',
    component: () => import('../views/stat.vue'),
    meta: {requiresAuth: true}
  },
  {
    path: '/signup',
    name: 'register',
    component: () => import('../views/signup.vue'),
    meta: {requiresAuth: false}
  },
  {
    path: '/admin_summary',
    name: 'admin_summary',
    component: () => import('../views/admin_summary.vue'),
    meta: {requiresAuth: false}
  },
  
];
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

router.beforeEach((to,from,next)=>{
  if(to.matched.some(record => record.meta.requiresAuth)){
    if(!store.getters.authenticated){
      next({path: '/login',
            query: {redirect: to.fullPath}
      });
    }else{
      next();
    }
  }else{
    next();
  }
});

export default router

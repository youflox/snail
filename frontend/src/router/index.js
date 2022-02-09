import { createRouter, createWebHashHistory } from "vue-router";
import Home from "../views/Home.vue";
import Login from "../views/Login.vue";
import Signup from "../views/Signup.vue";
import Logout from "../views/Logout.vue";
import DataView from "../views/DataView.vue";
import store from '../store/index'

const routes = [
  {
    path: "/logout",
    name: "Logout",
    component: Logout,
  },
  {
    path: "/signup",
    name: "Signup",
    component: Signup,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/data/:id",
    name: "DataView",
    component: DataView,
    props: true
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: function () {
      return import(/* webpackChunkName: "about" */ "../views/About.vue");
    },
  },
];

const router = createRouter({
  // hashbang: false,
  base: "/",
  history: createWebHashHistory(),
  routes,
});

router.beforeEach(to =>{
  if (to.path !== '/login'){
    if(sessionStorage.getItem('username') !== null && sessionStorage.getItem('password') !== null  ){
      store.state.authenticated = true;
    } else {
      store.state.authenticated = false;
    }
  }
})


export default router;
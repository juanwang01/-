import {createRouter, createWebHistory} from 'vue-router'

// 路由列表
const routes = [
  {
    meta:{
        title: "浮光在线教育-首页",
        keepAlive: true
    },
    path: '/',         // uri访问地址
    name: "Home",
    component: ()=> import("../views/HomePage.vue")
  },
  {
    meta:{
        title: "浮光在线教育-用户登录",
        keepAlive: true
    },
    path:'/login',      // uri访问地址
    name: "Login",
    component: ()=> import("../views/LoginPage.vue")
  }
]

// 路由对象实例化
const router = createRouter({
  // history, 指定路由的模式
  history: createWebHistory(),
  // 路由列表
  routes,
});


// 暴露路由对象
export default router
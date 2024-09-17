import {createRouter, createWebHistory} from 'vue-router'
import store from "@/store";

// 路由列表
const routes = [
    {
        meta: {
            title: "浮光在线教育-首页",
            keepAlive: true,
            authorization: false,
        },
        path: '/',         // uri访问地址
        name: "Home",
        component: () => import("../views/HomePage.vue")
    },
    {
        meta: {
            title: "浮光在线教育-用户登录",
            keepAlive: true,
            authorization: false,
        },
        path: '/login',      // uri访问地址
        name: "Login",
        component: () => import("../views/LoginPage.vue")
    },
    {
        meta: {
            title: "luffy2.0-个人中心",
            keepAlive: true,
            authorization: true,
        },
        path: '/user',
        name: "User",
        component: () => import("../views/UserPage.vue"),
    },
]

// 路由对象实例化
const router = createRouter({
    // history, 指定路由的模式
    history: createWebHistory(),
    // 路由列表
    routes,
});


// 导航守卫
router.beforeEach((to, from, next) => {
    document.title = to.meta.title
    // 初始化vuex
    console.log('进入守卫')
    const vuex = localStorage.getItem('vuex');
    const vuexObject = JSON.parse(vuex);
    console.log('获取vuex：', vuexObject)
    // store.commit('login',vuexObject.user)
    store.commit('login',vuexObject.user)
    // 登录状态验证，需要验证并且没有登入(没有用户信息)则返回登入页面，to是要去的页面
    console.log('判断是否有登入信息显示：', store.getters.getUserInfo)
    if (to.meta.authorization && !store.getters.getUserInfo) {
        console.log('需要登入')
        next({"name": "Login"})
    } else {
        next()
    }
})


// 暴露路由对象
export default router
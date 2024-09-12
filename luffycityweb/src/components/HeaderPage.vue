<template>
    <div class="header-box">
      <div class="header">
        <div class="content">
          <div class="logo">
            <router-link to="/"><img src="../assets/logo.png" alt=""></router-link>
          </div>
          <ul class="nav">
              <li v-for="item in nav.header_nav_list" :key="item.id">
                <a :href="item.link" v-if="item.is_http">{{item.name}}</a>
                <router-link :to="item.link" v-else>{{item.name}}</router-link>
              </li>
          </ul>
          <div class="search-warp">
            <div class="search-area">
              <input class="search-input" placeholder="请输入关键字..." type="text" autocomplete="off">
              <div class="hotTags">
                <router-link to="/search/?words=Vue" target="_blank" class="">Vue</router-link>
                <router-link to="/search/?words=Python" target="_blank" class="last">Python</router-link>
              </div>
            </div>
            <div class="showhide-search" data-show="no"><img class="imv2-search2" src="../assets/search.svg" /></div>
          </div>
          <div class="login-bar">
            <div class="shop-cart full-left">
              <img src="../assets/cart.svg" alt="" />
              <span><router-link to="/cart">购物车</router-link></span>
            </div>
            <div class="login-box full-left">
              <span @click="state.show_login=true">登录</span>
              &nbsp;/&nbsp;
              <span>注册</span>
            </div>
          </div>
        </div>
      </div>
    </div>
    <el-dialog :width="600" v-model="state.show_login">
      <Login></Login>
    </el-dialog>
</template>

<script setup>
import Login from "./LoginPage.vue"
import {reactive} from "vue";
import nav from "../api/nav";

const state = reactive({
  show_login: false,
})

// 获取头部导航
nav.get_header_nav().then(response=>{
  nav.header_nav_list = response.data;
}).catch(error=>{
  console.log(error);
});

</script>
<template>
  <div class="header-box">
    <div class="header">
      <div class="content">
        <div class="logo">
          <!-- 点击图片返回主页 -->
          <router-link to="/"><img src="../assets/logo.svg" alt=""></router-link>
        </div>
        <ul class="nav">
          <li v-for="nav in nav.header_nav_list" :key="nav.id">
            <a :href="nav.link" v-if="nav.is_http">{{ nav.name }}</a>
            <router-link :to="nav.link" v-else>{{ nav.name }}</router-link>
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
          <div class="showhide-search" data-show="no"><img class="imv2-search2" src="../assets/search.svg"/></div>
        </div>
        <div class="login-bar">
          <div class="shop-cart full-left">
            <img src="../assets/cart.svg" alt=""/>
            <span><router-link to="/cart">购物车</router-link></span>
          </div>
          <div class="login-box full-left">
            <span>登录</span>
            &nbsp;/&nbsp;
            <span>注册</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script setup>
import nav from "../api/nav";

// 请求头部导航列表
nav.get_header_nav().then(response=>{
  nav.header_nav_list = response.data
})


</script>

<style>
.header-box .nav {
  display: flex; /* 使用 flexbox 布局，使子元素横向排列 */
  list-style-type: none; /* 去除列表的默认样式 */
  padding: 0;
  margin: 0;
}

.header-box .nav li {
  margin-right: 20px; /* 设置每个导航项之间的间距 */
}

.header-box .nav li:last-child {
  margin-right: 0; /* 最后一个元素不需要右边距 */
}

.header-box a, .header-box router-link {
  text-decoration: none; /* 去掉链接的下划线 */
  color: inherit; /* 继承字体颜色 */
}
</style>
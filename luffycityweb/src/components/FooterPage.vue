<template>
  <div class="footer">
    <ul class="footer-nav">
      <li v-for="nav in nav.footer_nav_list" :key="nav.id">
        <a :href="nav.link" v-if="nav.is_http">{{ nav.name }}</a>
        <router-link :to="nav.link" v-else>{{ nav.name }}</router-link>
      </li>
    </ul>
    <p>Copyright © luffycity.com版权所有 | 京ICP备17072161号-1</p>
  </div>
</template>

<script setup>
import nav from "../api/nav";

// 获取脚部导航列表
nav.get_footer_nav().then(response=>{
  nav.footer_nav_list = response.data
})

</script>

<style>
.footer-nav {
  display: flex; /* 使用 flexbox 布局 */
  list-style-type: none; /* 去掉默认的列表样式 */
  padding: 0; /* 去掉默认的内边距 */
  margin: 0; /* 去掉默认的外边距 */
}

.footer-nav li {
  margin-right: 20px; /* 设置每个列表项的间距 */
}

.footer-nav li:last-child {
  margin-right: 0; /* 最后一个列表项不需要右边距 */
}

.footer a, .footer router-link {
  text-decoration: none; /* 去掉链接的下划线 */
}
</style>

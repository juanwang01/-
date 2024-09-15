<template>
  <div class="home">
    <HeaderPage></HeaderPage>
    <BannerPage></BannerPage>
    <FooterPage></FooterPage>

  </div>

</template>

<script setup>
// vite中导入非ts.js文件时，必须填写文件后缀
import HeaderPage from "@/components/HeaderPage.vue";
import FooterPage from "@/components/FooterPage.vue";
import BannerPage from "@/components/BannerPage.vue";

// 测试CORS的跨域配置是否有问题
// import http from "../utils/http";

// 测试服务端的跨域是否配置成功
// http.get("/api/home/demo/").then(response=>{
//   console.log(response.data);
// })

// 测试服务端的跨域是否配置成功
// http.get("/home/test").then(response=>{
//   console.log(response.data);
// })
</script>

<style scoped>

</style>
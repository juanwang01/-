<template>
   <div class="bk"></div>
   <div class="bgfff banner-box">
    <div class="g-banner pr" @mouseleave="state.current_menu=-1">
     <!-- 商品课程分类信息 -->
     <div class="submenu" v-if="state.current_menu==0">
      <div class="inner-box">
       <h2 class="type">前端开发</h2>
       <div class="tag clearfix">
       </div>
       <div class="lore">
        <span class="title">知识点：</span>
        <p class="lores clearfix"><a target="_blank" href="">Vue.js</a>
          <a target="_blank" href="">Typescript</a>
          <a target="_blank" href="">React.JS</a>
          <a target="_blank" href="">HTML/CSS</a>
          <a target="_blank" href="">JavaScript</a>
          <a target="_blank" href="">Angular</a>
          <a target="_blank" href="">Node.js</a>
          <a target="_blank" href="">jQuery</a>
          <a target="_blank" href="">Bootstrap</a>
          <a target="_blank" href="">Sass/Less</a>
          <a target="_blank" href="">WebApp</a>
          <a target="_blank" href="">小程序</a>
          <a target="_blank" href="">前端工具</a>
          <a target="_blank" href="">CSS</a>
          <a target="_blank" href="">Html5</a>
          <a target="_blank" href="">CSS3</a>
        </p>
       </div>
      </div>
      <div class="recomment clearfix">
        <a href="" target="_blank" title="" class="recomment-item">
        <div class="img" style="background-image: url('../src/assets/60a7779909e3fc1206960344.png'); background-size: 100%; "></div>
        <div class="details">
         <!--路径单独写-->
         <div class="title-box">
          <p class="title"> <span class="text">前端工程师2021</span> <span class="tag tixi">体系</span> </p>
         </div>
         <div class="bottom">
          <span class="discount-name">优惠价</span>
          <span class="price">￥4599.00</span> &middot;
          <span class="difficulty"> 零基础 </span> &middot;
          <span class="num"><i class="imv2-set-sns"></i> 19322</span>
         </div>
        </div> </a>
       <a href="" target="_blank" title="前端框架及项目面试 聚焦Vue3/React/Webpack" class="recomment-item">
        <div class="img" style="background-image: url('../src/assets/5e3cfea008e9a61b06000338-360-202.jpg')"></div>
        <div class="details">
         <!--路径单独写-->
         <div class="title-box">
          <p class="title"> <span class="text">前端框架及项目面试 聚焦Vue3/React/Webpack</span> <span class="tag shizhan">实战</span> </p>
         </div>
         <div class="bottom">
          <span class="price">399.00</span> &middot;
          <span class="difficulty"> 中级 </span> &middot;
          <span class="num"><i class="imv2-set-sns"></i> 2946</span>
         </div>
        </div> </a>
       <a href="" target="_blank" title="从0打造微前端框架，实战汽车资讯平台，系统掌握微前端架构设计与落地能力" class="recomment-item">
        <div class="img" style="background-image: url('../src/assets/60d44ec8084b799712000676-360-202.jpg')"></div>
        <div class="details">
         <!--路径单独写-->
         <div class="title-box">
          <p class="title"><span class="text">从0打造微前端框架，实战汽车资讯平台，系统掌握微前端架构设计与落地能力</span><span class="tag shizhan">实战</span> </p>
         </div>
         <div class="bottom">
          <span class="discount-name">限时优惠</span>
          <span class="price">￥328.00</span> &middot;
          <span class="difficulty"> 高级 </span> &middot;
          <span class="num"><i class="imv2-set-sns"></i> 109</span>
         </div>
        </div> </a>
       <a href="" target="_blank" title="" class="recomment-item">
        <div class="img" style="background-image: url('../src/assets/604f2bab0952610803240324-140-140.png'); background-size: 100%; "></div>
        <div class="details">
         <!--路径单独写-->
         <div class="title-box">
          <p class="title"> <span class="text">Vue.js 从入门到精通</span> <span class="tag lujing">路线</span> </p>
         </div>
         <div class="bottom">
          <span class="difficulty">4步骤</span> &middot;
          <span class="difficulty">4门课</span> &middot;
          <span class="num">19697人收藏</span>
         </div>
        </div> </a>
      </div>
     </div>
     <div class="submenu" v-if="state.current_menu==1">
      <div class="inner-box">
       <h2 class="type">后端开发</h2>
       <div class="tag clearfix">
       </div>
       <div class="lore">
        <span class="title">知识点：</span>
        <p class="lores clearfix">
          <a target="_blank" href="">Java</a>
          <a target="_blank" href="">SpringBoot</a>
          <a target="_blank" href="">Spring Cloud</a>
          <a target="_blank" href="">SSM</a>
          <a target="_blank" href="">PHP</a>
          <a target="_blank" href="">.net</a>
          <a target="_blank" href="">Python</a>
          <a target="_blank" href="">爬虫</a>
          <a target="_blank" href="">Django</a>
          <a target="_blank" href="">Flask</a>
          <a target="_blank" href="">Tornado</a>
          <a target="_blank" href="">Go</a>
          <a target="_blank" href="">C</a>
          <a target="_blank" href="">C++</a>
          <a target="_blank" href="">C#</a>
          <a target="_blank" href="">Ruby</a></p>
       </div>
      </div>
      <div class="recomment clearfix">
        <a href="" target="_blank" title="Java工程师2021" class="recomment-item">
        <div class="img" style="background-image: url('../src/assets/60a777ef0942d7bf06960344.png'); background-size: 100%; "></div>
        <div class="details">
         <div class="title-box">
          <p class="title"> <span class="text">Java工程师2021</span> <span class="tag tixi">体系</span> </p>
         </div>
         <div class="bottom">
          <span class="discount-name">优惠价</span>
          <span class="price">￥4399.00</span> &middot;
          <span class="difficulty"> 零基础 </span> &middot;
          <span class="num"><i class="imv2-set-sns"></i> 15052</span>
         </div>
        </div> </a>
       <a href="" target="_blank" title="Python工程师（全能型）" class="recomment-item">
        <div class="img" style="background-image: url('../src/assets/60a77721093df37606960344.png'); background-size: 100%; "></div>
        <div class="details">
         <!--路径单独写-->
         <div class="title-box">
          <p class="title"> <span class="text">Python工程师（全能型）</span> <span class="tag tixi">体系</span> </p>
         </div>
         <div class="bottom">
          <span class="discount-name">优惠价</span>
          <span class="price">￥4366.00</span> &middot;
          <span class="difficulty"> 零基础 </span> &middot;
          <span class="num"><i class="imv2-set-sns"></i> 10786</span>
         </div>
        </div> </a>
       <a href="" target="_blank" title="Java全栈工程师" class="recomment-item">
        <div class="img" style="background-image: url('../src/assets/5dd6567b09d9d01c06000338.png'); background-size: 100%; "></div>
        <div class="details">
         <!--路径单独写-->
         <div class="title-box">
          <p class="title"> <span class="text">Java全栈工程师</span> <span class="tag tixi">体系</span> </p>
         </div>
         <div class="bottom">
          <span class="discount-name">优惠价</span>
          <span class="price">￥3380.00</span> &middot;
          <span class="difficulty"> 进阶 </span> &middot;
          <span class="num"><i class="imv2-set-sns"></i> 1853</span>
         </div>
        </div> </a>
       <a href="" target="_blank" title="" class="recomment-item">
        <div class="img" style="background-image: url('../src/assets/604f2bb6099d6a8803240324-140-140.png'); background-size: 100%; "></div>
        <div class="details">
         <!--路径单独写-->
         <div class="title-box">
          <p class="title"> <span class="text">SpringBoot从入门到精通</span> <span class="tag lujing">路线</span> </p>
         </div>
         <div class="bottom">
          <span class="difficulty">3步骤</span> &middot;
          <span class="difficulty">5门课</span> &middot;
          <span class="num">11092人收藏</span>
         </div>
        </div> </a>
      </div>
     </div>
     <div class="submenu" v-if="state.current_menu==2">
      <div class="inner-box">
       <h2 class="type">移动开发</h2>
       <div class="tag clearfix">
       </div>
       <div class="lore">
        <span class="title">知识点：</span>
        <p class="lores clearfix"></p>
       </div>
      </div>
      <div class="recomment clearfix">
       <a href="" target="_blank" title="移动端架构师成长体系课" class="recomment-item">
        <div class="img" style="background-image: url('../src/assets/5ec5ddf209cd2c8606000338.png'); background-size: 100%; "></div>
        <div class="details">
         <!--路径单独写-->
         <div class="title-box">
          <p class="title"> <span class="text">移动端架构师成长体系课</span> <span class="tag tixi">体系</span> </p>
         </div>
         <div class="bottom">
          <span class="discount-name">优惠价</span>
          <span class="price">￥4888.00</span> &middot;
          <span class="difficulty"> 进阶 </span> &middot;
          <span class="num"><i class="imv2-set-sns"></i> 402</span>
         </div>
        </div> </a>
       <a href="" target="_blank" title="Flutter高级进阶实战  仿哔哩哔哩APP 一次性深度掌握Flutter高阶技能" class="recomment-item">
        <div class="img" style="background-image: url('../src/assets/60497caf0971842912000676-360-202.png'); background-size: 100%; "></div>
        <div class="details">
         <!--路径单独写-->
         <div class="title-box">
          <p class="title"> <span class="text">Flutter高级进阶实战 仿哔哩哔哩APP 一次性深度掌握Flutter高阶技能</span> <span class="tag shizhan">实战</span> </p>
         </div>
         <div class="bottom">
          <span class="price">368.00</span> &middot;
          <span class="difficulty"> 高级 </span> &middot;
          <span class="num"><i class="imv2-set-sns"></i> 646</span>
         </div>
        </div> </a>
       <a href="" target="_blank" title="音视频基础+ffmpeg原理+项目实战 一课完成音视频技术开发入门" class="recomment-item">
        <div class="img" style="background-image: url('../src/assets/5e5621d0092c054612000676-360-202.png'); background-size: 100%; "></div>
        <div class="details">
         <!--路径单独写-->
         <div class="title-box">
          <p class="title"> <span class="text">音视频基础+ffmpeg原理+项目实战 一课完成音视频技术开发入门</span> <span class="tag shizhan">实战</span> </p>
         </div>
         <div class="bottom">
          <span class="price">288.00</span> &middot;
          <span class="difficulty"> 入门 </span> &middot;
          <span class="num"><i class="imv2-set-sns"></i> 1303</span>
         </div>
        </div> </a>
       <a href="" target="_blank" title="" class="recomment-item">
        <div class="img" style="background-image: url('../src/assets/604f2b52090de67603240324-140-140.png'); background-size: 100%; "></div>
        <div class="details">
         <!--路径单独写-->
         <div class="title-box">
          <p class="title"> <span class="text">Android工程师高薪面试突破路线</span> <span class="tag lujing">路线</span> </p>
         </div>
         <div class="bottom">
          <span class="difficulty">3步骤</span> &middot;
          <span class="difficulty">3门课</span> &middot;
          <span class="num">1471人收藏</span>
         </div>
        </div> </a>
      </div>
     </div>
     <div class="menuContent">
      <div class="item" :class="{'js-menu-item-on': state.current_menu==0}" @mouseover="state.current_menu=0">
       <span class="title">前端开发：</span>
       <span class="sub-title">HTML5 / Vue.js / Node.js</span>
       <i class="imv2-arrow1_r"></i>
      </div>
      <div class="item" :class="{'js-menu-item-on': state.current_menu==1}" @mouseover="state.current_menu=1">
       <span class="title">后端开发：</span>
       <span class="sub-title">Java / Python / Go</span>
       <i class="imv2-arrow1_r"></i>
      </div>
      <div class="item" :class="{'js-menu-item-on': state.current_menu==2}" @mouseover="state.current_menu=2">
       <span class="title">移动开发：</span>
       <span class="sub-title">Flutter / Android / iOS </span>
       <i class="imv2-arrow1_r"></i>
      </div>
     </div>
      <!-- 轮播图-->
      <div class="g-banner-content"  @mouseover="state.current_menu=-1">
        <el-carousel :interval="5000" arrow="always" height="482px" v-if="banner.banner_list[0]">
          <el-carousel-item v-for="item in banner.banner_list" :key="item.key">
            <a :href="item.link" v-if="item.is_http"><img :src="item.image" alt="" style="width: 100%;height: 100%;"></a>
            <router-link :to="item.link" v-else><img :src="item.image" alt="" style="width: 100%;height: 100%;"></router-link>
          </el-carousel-item>
        </el-carousel>
     </div>
    </div>
   </div>
</template>

<script setup>
import {reactive} from "vue"
import banner from "../api/banner";

// 获取轮播广告列表
banner.get_banner_list().then(response=>{
  banner.banner_list = response.data
})

const state = reactive({
  current_menu: -1,
})
</script>
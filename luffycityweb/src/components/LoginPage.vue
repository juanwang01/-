
<template>
  <div class="title">
    <span :class="{active:user.login_type==0}" @click="user.login_type=0">密码登录</span>
    <span :class="{active:user.login_type==1}" @click="user.login_type=1">短信登录</span>
  </div>
  <div class="inp" v-if="user.login_type==0">
    <input v-model="user.account" type="text" placeholder="用户名 / 手机号码" class="user">
    <input v-model="user.password" type="password" class="pwd" placeholder="密码">
    <div id="geetest1"></div>
    <div class="rember">
      <label>
        <input type="checkbox" class="no" v-model="user.remember"/>
        <span>记住密码</span>
      </label>
      <p>忘记密码</p>
    </div>
    <button class="login_btn" @click="loginhandler">登录</button>
    <p class="go_login" >没有账号 <span>立即注册</span></p>
  </div>
  <div class="inp" v-show="user.login_type==1">
    <input v-model="user.mobile" type="text" placeholder="手机号码" class="user">
    <input v-model="user.code"  type="text" class="code" placeholder="短信验证码">
    <el-button id="get_code" type="primary">获取验证码</el-button>
    <button class="login_btn">登录</button>
    <p class="go_login" >没有账号 <span>立即注册</span></p>
  </div>
</template>

<script setup>
import user from "../api/user";
import { ElMessage } from 'element-plus'

// 登录处理
const loginhandler = ()=>{
  // 验证数据
  if(user.account.length<1 || user.password.length<1){
    // 错误提示
    console.log("错了哦，用户名或密码不能为空！");
    ElMessage.error("错了哦，用户名或密码不能为空！");
    return ;
  }

  // 登录请求处理
  user.login().then(response=>{
    console.log(response.data);
    ElMessage.success("登录成功！");
    // eslint-disable-next-line no-unused-vars
  }).catch(error=>{
    ElMessage.error("登录失败！");
  })
}

</script>
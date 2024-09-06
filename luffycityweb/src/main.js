import { createApp } from 'vue'
import App from './views/App.vue'
import router from "./router/index";
createApp(App).mount('#app')


createApp(App)
  .use(router)  // 使用 router
  .mount('#app')
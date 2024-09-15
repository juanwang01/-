import {createApp} from 'vue'
import App from './views/App.vue'
import router from "./router/index";
import ElementPlus from 'element-plus' //全局引入
import 'element-plus/dist/index.css'; // 引入 Element Plus 的样式

const app = createApp(App)
app.use(router)
app.use(ElementPlus)
app.mount('#app')
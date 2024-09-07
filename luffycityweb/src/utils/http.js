import axios from "axios"

const http = axios.create({
    // 如果环境变量存在，优先使用环境变量；否则使用默认值
    baseURL: process.env.VUE_APP_BASE_API || "http://localhost:8000",
    withCredentials: false,  // 是否允许客户端ajax请求时携带cookie
});

// 请求拦截器
http.interceptors.request.use((config) => {
    console.log("http请求之前");
    return config;
}, (error) => {
    console.log("http请求错误");
    return Promise.reject(error);
});

// 响应拦截器
http.interceptors.response.use((response) => {
    console.log("服务端响应数据成功以后，返回结果给客户端的第一时间，执行then之前");
    return response;
}, (error) => {
    console.log("服务端响应错误内容的时候。...");
    return Promise.reject(error);
});

export default http;
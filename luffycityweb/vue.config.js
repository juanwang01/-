const {defineConfig} = require('@vue/cli-service')
module.exports = defineConfig({
    transpileDependencies: true,
    devServer: { // 将 server 改为 devServer
        port: '8080',           // 客户端的运行端口
        host: '0.0.0.0',      // 客户端的运行地址
        proxy: {
            '/api': {
                // 凡是遇到 /api 路径的请求，都映射到 target 属性
                target: process.env.VUE_APP_BASE_API || "http://localhost:8000",  // 注意：需要加上 http://
                changeOrigin: true,
                ws: true,    // 是否支持 websocket 跨域
                pathRewrite: {'^/api': ''}  // 重写路径
            }
        }
    }
})

# 使用官方的 Nginx 镜像作为基础镜像
FROM nginx:latest

# 删除 Nginx 默认的 index.html 文件
RUN rm /usr/share/nginx/html/index.html

# 将自定义的 index.html 文件复制到 Nginx 镜像中的适当位置
COPY index.html /usr/share/nginx/html/index.html

# 暴露80端口供外部访问
EXPOSE 80

# 当容器启动时运行 Nginx
CMD ["nginx", "-g", "daemon off;"]

FROM alpine
RUN echo "http://mirrors.ustc.edu.cn/alpine/v3.7/main/" > /etc/apk/repositories \
    && echo "http://mirrors.ustc.edu.cn/alpine/v3.7/community/" >> /etc/apk/repositories \
    && echo "http://dl-4.alpinelinux.org/alpine/edge/testing/" >> /etc/apk/repositories \
    && apk add --no-cache haproxy
CMD ["haproxy", "-d", "-f", "/etc/haproxy/haproxy.cfg"]

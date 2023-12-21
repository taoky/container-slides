# Containers

<https://docs.google.com/presentation/d/1akIejKbXwT8spd7-jFxSjkgJdpLXlTIs3we0IsG8510/edit?usp=sharing>

## License

- 代码：MIT
- Slides: CC-BY-NC-SA 4.0

## 附件

- compose 前面的部分大概不需要附件（都是直接跑一/几条命令）
- compose-1: 支持 X11 + GPU + Audio 的容器的 docker-compose 配置
- hackergame: 从 <https://github.com/ustclug/hackergame/commit/b66df8547210395a91a72a63fbd6900ec9654d8a> 取的一份完整的无 git 历史代码，加上容器化（compose）修改之后的整个代码库
    - 主要是时间来不及了，所以出此下策（
    - 大概修改不会进入主线，因为目前没有需要
    - 运行需要重命名并修改 `.env.example` -> `.env`
    - 一部分文件还是需要按照 README 改
    - 思考这样的问题：各个容器之间互联用了 TCP socket（而不是 UNIX socket），考虑是什么？
- hmcl: Minecraft!

# 代理和反向代理

## 代理

![proxy](../image/config/proxy.png){width=500}{class=ab-shadow-card}

<br/>

AB 支持 HTTP 代理和 SOCKS5 代理，通过设置代理可以解决一些网络问题。

- **Enable**: 是否启用代理。
- **Type** 为代理类型。
- **Host** 为代理地址。
- **Port** 为代理端口。

需要注意的是，在 HTTP 模式下不支持用户名密码验证，如果你的代理需要用户名密码验证，请使用 **SOCKS5** 模式。

## 反向代理设置

为了应对 [蜜柑计划](https://mikanani.me) 无法访问的情况，AB 增加了三种应对的方式。

1. HTTP 以及 Socks 代理

    老版本的 AB 就有这项功能，升级到 2.6 版本之后只需要在 WebUI 中检查代理配置即可正常访问蜜柑计划。
    
    不过这时候 qBittorrent 无法正常访问蜜柑计划的 RSS 和种子地址，因此需要在 qBittorrent 中添加代理。详情可以查看: [Mikan 被墙怎么办](../faq/mikan-network.md)

2. 自定义反向代理 URL

    2.6 版本的 AB 在配置中增加了 `custom_url` 选项，可以自定义反向代理的 URL。
    可以在配置中设置为自己正确设置的反代 URL。这样 AB 就会使用自定义的 URL 来访问蜜柑计划。并且 QB 也可以正常下载。

3. AB 作为反代中转

    在 AB 配置代理之后，AB 自身可以作为本地的反代中转。不过目前仅开放 RSS 相关功能的反代。
    这时候只需要把 `custom_url` 设置为 `http://abhost:abport` 即可。 `abhost` 为 AB 的 IP 地址，`abport` 为 AB 的端口。
    此时 AB 会把自身地址推送给 qBittorrent，qBittorrent 会使用 AB 的地址作为反代来访问蜜柑计划。
    
    请注意，此时如果你没有用 NGINX 等工具对 AB 进行反代，请填入 `http://` 来保证程序正常运行。

## `config.json` 中的配置选项

在配置文件中对应选项如下：

配置文件部分：`proxy`

| 参数名      | 参数说明   | 参数类型 | WebUI 对应选项 | 默认值   |
|----------|--------|------|------------|-------|
| enable   | 是否启用代理 | 布尔值  | 代理         | false |
| type     | 代理类型   | 字符串  | 代理类型       | http  |
| host     | 代理地址   | 字符串  | 代理地址       |
| port     | 代理端口   | 整数   | 代理端口       |
| username | 代理用户名  | 字符串  | 代理用户名      |
| password | 代理密码   | 字符串  | 代理密码       |

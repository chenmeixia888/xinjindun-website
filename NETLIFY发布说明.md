# Netlify 一键发布指南 - 鑫金顿官网

## 文件夹结构

```
xinjindun-website/
└── index.html          ← 唯一文件，直接拖上去就行
```

所有样式和内容都内嵌在 index.html 中，无需额外文件。

---

## 发布步骤（一共5步，约5分钟）

### 第1步：注册 Netlify 账号
1. 打开浏览器，访问：https://www.netlify.com
2. 点击右上角 "Sign up"
3. 选择 "Sign up with Email"（用邮件注册）
4. 填写邮箱（可用 46465910@qq.com）和密码
5. 去邮箱点击确认链接

### 第2步：发布网站（拖拽上传）
1. 登录后，在首页找到这个区域：
   **"Want to deploy a new site without connecting to Git? Drag and drop your site output folder here"**
2. 打开 D:\WorkBuddy\xinjindun-website\ 文件夹
3. 把整个 **xinjindun-website 文件夹** 拖进去（注意：是整个文件夹，不是里面的文件）
4. 等待几秒钟，网站就发布好了！

### 第3步：获取网址
发布成功后，Netlify 会自动分配一个免费网址，格式类似：
```
https://random-name-123456.netlify.app
```
点击这个网址就能看到你的网站了。

### 第4步：自定义网址（可选）
如果你有自己的域名（如 xinjindun.com），可以绑定：
1. 进入 Netlify 后台 → Site settings → Domain management
2. 点击 "Add a domain"
3. 输入你的域名，按提示操作

如果没有域名，Netlify 的免费域名完全够用，可以先用着。

### 第5步：更新网站内容
以后如果要修改网站内容：
1. 修改 D:\WorkBuddy\xinjindun-website\index.html 文件
2. 进入 Netlify 后台 → 点击你的网站 → Deploys
3. 再次把 xinjindun-website 文件夹拖进去
4. 网站自动更新完成

---

## 常见问题

**Q: 发布后网站打不开？**
A: 等待2-3分钟，Netlify 需要时间完成部署。刷新页面再试。

**Q: 网址太长记不住怎么办？**
A: 在 Netlify 后台 → Site settings → Site details → Change site name，可以改成 xinjindun.netlify.app 这样的短域名。

**Q: 网站免费吗？**
A: Netlify 免费版对于展示型官网完全够用，不限流量，不限访问量。

---

## 文件说明

| 文件 | 说明 |
|------|------|
| index.html | 官网主文件，包含全部内容和样式 |

**最后更新**：2026-04-25

# 福建鑫金顿电气有限公司 官方网站

> 专业监控立杆、对讲立柱、交通设施杆件、智慧综合杆制造商  
> 厂家直供 · 支持定制 · 全国发货  
> 联系电话：13107895588

---

## 文件结构说明

```
xinjindun-website/
├── index.html          ← 网站主页（必须叫这个名字）
├── style.css           ← 网站样式文件
├── images/             ← 所有图片放这里（英文命名）
│   ├── banner-1.jpg    ← 首页轮播图
│   ├── banner-2.jpg
│   ├── banner-3.jpg
│   ├── product-jk-1.jpg  ← 监控立杆产品图
│   ├── product-dj-1.jpg  ← 对讲立柱产品图
│   ├── product-jt-1.jpg  ← 交通设施杆件图
│   ├── company-1.jpg     ← 工厂/公司照片
│   └── 图片重命名说明.md  ← 删掉这个文件再上传
└── README.md           ← 本说明文件
```

---

## 第一步：把图片放进来

1. 打开 `images` 文件夹
2. 把你的产品实物图复制进来
3. 按 `图片重命名说明.md` 里的规则改名
4. **把 `图片重命名说明.md` 删掉**，不需要上传到网上

---

## 第二步：上传到 GitHub

### 方法A：直接拖拽上传（最简单，推荐）

1. 打开浏览器，访问 https://github.com
2. 点右上角 **Sign up** 注册账号（已有账号直接登录）
3. 登录后点右上角 **+** → **New repository**
4. 填写：
   - Repository name：`xinjindun-website`（必须英文）
   - 选 **Public**（公开，Netlify免费版需要）
   - 勾选 **Add a README file**
5. 点 **Create repository**
6. 进入新建的仓库页面，点 **uploading an existing file**
7. 把整个 `xinjindun-website` 文件夹里的**所有文件**拖进去
   - ⚠️ 注意：要把 `index.html`、`style.css`、`images文件夹` **一起拖进去**
8. 页面底部点 **Commit changes**，等待上传完成

---

## 第三步：发布到 Netlify（免费）

1. 打开浏览器，访问 https://app.netlify.com
2. 点 **Sign up** → 选 **Continue with GitHub**（用GitHub账号登录，最方便）
3. 登录后点 **Add new site** → **Import an existing project**
4. 选 **Deploy with GitHub**
5. 找到你刚才建的 `xinjindun-website` 仓库，点进去
6. 设置页面不用改任何东西，直接点 **Deploy site**
7. 等1~2分钟，Netlify自动生成网址，比如：`https://xinjindun.netlify.app`

**搞定！把这个网址发给客户就能看了。**

---

## 如何更新网站内容

以后修改了内容（比如改了产品参数），重新上传到 GitHub 就行：

1. 修改 `index.html` 文件内容
2. 打开你的 GitHub 仓库
3. 点文件名 → 点右上角铅笔图标（编辑）→ 粘贴新内容 → 提交
4. Netlify 会自动检测到更新，1~2分钟后网站自动刷新

---

## 常见问题

**Q：网站打开是空白/样式乱了？**  
A：检查 `style.css` 文件是否在同一个文件夹，和 `index.html` 并排放着。

**Q：图片显示不出来？**  
A：检查图片文件名是否全是英文，有没有中文或空格。

**Q：想换自己的域名怎么办？**  
A：在阿里云/腾讯云买域名（约59元/年），在Netlify后台 Site settings → Domain management 里绑定。

**Q：想修改联系电话怎么办？**  
A：用记事本/Word打开 `index.html`，Ctrl+H 搜索旧电话，替换成新电话，保存重新上传。

---

## 联系我们

- 电话：13107895588  
- 邮箱：46465910@qq.com  
- 微信：cmx13107895588  
- 地址：福建省泉州台商投资区洛阳镇洛阳大道565号4幢

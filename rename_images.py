
import os, shutil

SRC = r"D:\WorkBuddy\xinjindun-website\images"
DST = r"D:\WorkBuddy\xinjindun-website\images"

# 重命名映射：旧文件名 → 新文件名
rename_map = {
    # ── 主图 ──────────────────────────────────────────────────────
    "对讲立柱主图.png":       "intercom-main.png",
    "分段立杆主图.jpg":        "monitor-main.jpg",
    "八角杆主图.jpg":          "octagonal-main.jpg",
    "监控箱主图.png":          "box-main.png",
    "变电站配套钢架主图.jpg":  "substation-main.jpg",

    # ── 对讲立柱细节图（product-intercom-xxx → intercom-detail-xx）
    "product-intercom-a01.png":   "intercom-detail-01.png",
    "product-intercom-a03.png":   "intercom-detail-02.png",
    "product-intercom-a04.png":   "intercom-detail-03.png",
    "product-intercom-a05.png":   "intercom-detail-04.png",
    "product-intercom-a07.png":   "intercom-detail-05.png",
    "product-intercom-a08.png":   "intercom-detail-06.png",
    "product-intercom-a09.png":   "intercom-detail-07.png",
    "product-intercom-a10.png":   "intercom-detail-08.png",
    "product-intercom-a11.png":   "intercom-detail-09.png",
    "product-intercom-a12.png":   "intercom-detail-10.png",
    "product-intercom-a13.png":   "intercom-detail-11.png",
    "product-intercom-a14.png":   "intercom-detail-12.png",
    "product-intercom-a15.png":   "intercom-detail-13.png",
    "product-intercom-a18.png":   "intercom-detail-14.png",
    "product-intercom-a18-2.png": "intercom-detail-15.png",
    "product-intercom-a19.png":   "intercom-detail-16.png",
    "product-intercom-a20.png":   "intercom-detail-17.png",
    "product-intercom-a21.png":   "intercom-detail-18.png",
    "product-intercom-a22.png":   "intercom-detail-19.png",
    "product-intercom-a23.png":   "intercom-detail-20.png",

    # ── 监控立杆细节图（product-monitor-xxx → monitor-detail-xx）
    "product-monitor-02.png":  "monitor-detail-01.png",
    "product-monitor-03.png":  "monitor-detail-02.png",
    "product-monitor-04.png":  "monitor-detail-03.png",
    "product-monitor-05.png":  "monitor-detail-04.png",
    "product-monitor-06.png":  "monitor-detail-05.png",
    "product-monitor-07.png":  "monitor-detail-06.png",
    "product-monitor-08.png":  "monitor-detail-07.png",
    "product-monitor-09.png":  "monitor-detail-08.png",
    "product-monitor-10.png":  "monitor-detail-09.png",
    "product-monitor-11.png":  "monitor-detail-10.png",
    "product-monitor-12.png":  "monitor-detail-11.png",
    "product-monitor-13.png":  "monitor-detail-12.png",
    "product-monitor-14.png":  "monitor-detail-13.png",
    "product-monitor-15.png":  "monitor-detail-14.png",
    "product-monitor-16.png":  "monitor-detail-15.png",
    "product-monitor-18.png":  "monitor-detail-16.png",
    "product-monitor-19.png":  "monitor-detail-17.png",
    "product-monitor-20.png":  "monitor-detail-18.png",
    "product-monitor-21.png":  "monitor-detail-19.png",
    "product-monitor-22.png":  "monitor-detail-20.png",
    "product-monitor-23.png":  "monitor-detail-21.png",
    "product-monitor-24.png":  "monitor-detail-22.png",
    "product-monitor-25.png":  "monitor-detail-23.png",
    "product-monitor-26.png":  "monitor-detail-24.png",
    "product-monitor-28.png":  "monitor-detail-25.png",
    "product-monitor-29.png":  "monitor-detail-26.png",

    # ── 八角杆细节图（product-octagonal-xxx → octagonal-detail-xx）
    "product-octagonal-3-5m-gun.png":      "octagonal-detail-01.png",
    "product-octagonal-3-5m-ball.png":     "octagonal-detail-02.png",
    "product-octagonal-4m-gun.png":        "octagonal-detail-03.png",
    "product-octagonal-4m-ball.png":       "octagonal-detail-04.png",
    "product-octagonal-4-5m-gun.png":      "octagonal-detail-05.png",
    "product-octagonal-4-5m-ball.png":     "octagonal-detail-06.png",
    "product-octagonal-5m-gun.png":        "octagonal-detail-07.png",
    "product-octagonal-5m-ball.png":       "octagonal-detail-08.png",
    "product-octagonal-6m-gun.png":        "octagonal-detail-09.png",
    "product-octagonal-6m-ball.png":       "octagonal-detail-10.png",
    "product-octagonal-6-5m-gun.png":      "octagonal-detail-11.png",
    "product-octagonal-6-5m-ball.png":     "octagonal-detail-12.png",
    "product-octagonal-1gun1ball-arm.png": "octagonal-detail-13.png",

    # ── 监控箱/配电箱细节图
    "201不锈钢监控箱（壁挂）250300150.png":   "box-detail-01.png",
    "201不锈钢监控箱（壁挂）300400200.png":   "box-detail-02.png",
    "201不锈钢监控箱（壁挂）400500200.png":   "box-detail-03.png",
    "201不锈钢监控箱（壁挂）400500250.png":   "box-detail-04.png",
    "201不锈钢监控箱（壁挂）400500300.png":   "box-detail-05.png",
    "201不锈钢监控箱（配抱箍）250300150.png": "box-detail-06.png",
    "201不锈钢监控箱（配抱箍）300400200.png": "box-detail-07.png",
    "201不锈钢监控箱（配抱箍）400500200.png": "box-detail-08.png",
    "201不锈钢监控箱（配抱箍）400500250.png": "box-detail-09.png",
    "201不锈钢监控箱（配抱箍）400500300.png": "box-detail-10.png",
    "室外监控箱（壁挂）250300150 .png":       "box-detail-11.png",
    "室外监控箱（壁挂）300400200.png":        "box-detail-12.png",
    "室外监控箱（壁挂）400500200..png":       "box-detail-13.png",
    "室外监控箱（壁挂）400500200.png":        "box-detail-14.png",
    "室外监控箱（壁挂）400500250..png":       "box-detail-15.png",
    "室外监控箱（配抱箍）250300150.png":      "box-detail-16.png",
    "室外监控箱（配抱箍）300400200.png":      "box-detail-17.png",
    "室外监控箱（配抱箍）400500200.png":      "box-detail-18.png",
    "室外监控箱（抱箍）400500200..png":       "box-detail-19.png",
    "室外监控箱（抱箍）400500250..png":       "box-detail-20.png",
    "抱箍.png":                               "box-detail-21.png",

    # ── 变电站配套钢架细节图（jimeng 系列）
    "jimeng-2026-04-26-4193-把鑫东钢结构改成鑫金顿结构，把186-3183-9165改成1560603550....png": "substation-detail-01.png",
    "jimeng-2026-04-26-4419-监控塔改成变电站门型构架.png":                                    "substation-detail-02.png",
    "jimeng-2026-04-26-5489-把第二张的文字全部改成第一张的，其它不变.png":                    "substation-detail-03.png",
    "jimeng-2026-04-26-6496-把第二张的背景改成第一张的，其它不变.png":                        "substation-detail-04.png",
    "jimeng-2026-04-26-9535-监控塔改成：热镀锌变电站构架立柱，文字不要挡住铁架，可以换行； 右上角的鑫金顿三....png": "substation-detail-05.png",
    "jimeng-2026-04-26-9861-变电站构架配套钢架改成变电站大铁架.png":                          "substation-detail-06.png",
}

ok, skip, err = 0, 0, 0
for old, new in rename_map.items():
    src = os.path.join(SRC, old)
    dst = os.path.join(DST, new)
    if not os.path.exists(src):
        print(f"[跳过-不存在] {old}")
        skip += 1
        continue
    if os.path.exists(dst) and src != dst:
        print(f"[跳过-已存在] {new}")
        skip += 1
        continue
    try:
        os.rename(src, dst)
        print(f"[OK] {old} → {new}")
        ok += 1
    except Exception as e:
        print(f"[ERROR] {old}: {e}")
        err += 1

print(f"\n完成：{ok} 个重命名，{skip} 个跳过，{err} 个错误")

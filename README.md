# pairwise-tiled-superres-seam

## 领域

游戏、图形与多媒体

## 主题

超分辨率分块接缝

## 说明

重叠羽化拼接、全局统计、有效区裁切。

初始状态下 `imaging/tiled_superres.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。

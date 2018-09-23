## Guide
Install lumi.
```
pip install luminoth
```
To see others installation ways see https://luminoth.readthedocs.io/en/latest/usage/installation.html

Checkpoint management is handled by the `lumi checkpoint` subcommand. Run the following to both retrieve and list the existing checkpoints:

```
$ lumi checkpoint refresh
Retrieving remote index... done.
2 new remote checkpoints added.
$ lumi checkpoint list
================================================================================
|           id |                  name |       alias | source |         status |
================================================================================
| 48ed2350f5b2 |   Faster R-CNN w/COCO |    accurate | remote | NOT_DOWNLOADED |
| e3256ffb7e29 |      SSD w/Pascal VOC |        fast |  local | NOT_DOWNLOADED |
================================================================================
```

Additional commands are available for managing checkpoints, including inspection and modification of checkpoints (see Checkpoint management). For now, we’ll download a checkpoint and use it:

```
$ lumi checkpoint download 48ed2350f5b2
Downloading checkpoint...  [####################################]  100%
Importing checkpoint... done.
Checkpoint imported successfully.
```

Let’s start with the first, by running it on an image aptly named image.jpg:

```
$ lumi predict image.jpg
Found 1 files to predict.
Neither checkpoint not config specified, assuming `accurate`.
Predicting image.jpg... done.
{
  "file": "image.jpg",
  "objects": [
    {"bbox": [294, 231, 468, 536], "label": "person", "prob": 0.9997},
    {"bbox": [494, 289, 578, 439], "label": "person", "prob": 0.9971},
    {"bbox": [727, 303, 800, 465], "label": "person", "prob": 0.997},
    {"bbox": [555, 315, 652, 560], "label": "person", "prob": 0.9965},
    {"bbox": [569, 425, 636, 600], "label": "bicycle", "prob": 0.9934},
    {"bbox": [326, 410, 426, 582], "label": "bicycle", "prob": 0.9933},
    {"bbox": [744, 380, 784, 482], "label": "bicycle", "prob": 0.9334},
    {"bbox": [506, 360, 565, 480], "label": "bicycle", "prob": 0.8724},
    {"bbox": [848, 319, 858, 342], "label": "person", "prob": 0.8142},
    {"bbox": [534, 298, 633, 473], "label": "person", "prob": 0.4089}
  ]
}
```

Or execute python code:
```
$ python predict.py

2018-09-23 14:27:37.322349: W tensorflow/core/framework/allocator.cc:122] Allocation of 1605632000 exceeds 10% of system memory.
2018-09-23 14:27:38.074627: W tensorflow/core/framework/allocator.cc:122] Allocation of 401408000 exceeds 10% of system memory.
2018-09-23 14:27:38.247523: W tensorflow/core/framework/allocator.cc:122] Allocation of 802816000 exceeds 10% of system memory.
2018-09-23 14:27:42.167474: W tensorflow/core/framework/allocator.cc:122] Allocation of 802816000 exceeds 10% of system memory.
2018-09-23 14:27:45.586090: W tensorflow/core/framework/allocator.cc:122] Allocation of 802816000 exceeds 10% of system memory.
[{'prob': 0.9883, 'bbox': [465.0, 2248.0, 881.0, 2535.0], 'label': u'car'}, {'prob': 0.9841, 'bbox': [1072.0, 2143.0, 1404.0, 2403.0], 'label': u'car'}, {'prob': 0.9805, 'bbox': [3723.0, 1703.0, 3974.0, 1858.0], 'label': u'car'}, {'prob': 0.9483, 'bbox': [1431.0, 1775.0, 1600.0, 1913.0], 'label': u'car'}, {'prob': 0.9457, 'bbox': [945.0, 1991.0, 1226.0, 2217.0], 'label': u'car'}, {'prob': 0.9443, 'bbox': [2385.0, 1875.0, 2554.0, 2010.0], 'label': u'car'}, {'prob': 0.9363, 'bbox': [1612.0, 1682.0, 1731.0, 1793.0], 'label': u'car'}, {'prob': 0.9167, 'bbox': [1567.0, 2054.0, 1839.0, 2295.0], 'label': u'car'}, {'prob': 0.9161, 'bbox': [1948.0, 1755.0, 2091.0, 1881.0], 'label': u'car'}, {'prob': 0.9046, 'bbox': [66.0, 1701.0, 401.0, 1897.0], 'label': u'car'}, {'prob': 0.8996, 'bbox': [181.0, 1681.0, 451.0, 1843.0], 'label': u'car'}, {'prob': 0.8941, 'bbox': [1736.0, 1743.0, 1887.0, 1877.0], 'label': u'car'}, {'prob': 0.894, 'bbox': [3560.0, 1552.0, 3615.0, 1636.0], 'label': u'car'}, {'prob': 0.8855, 'bbox': [2965.0, 1277.0, 3646.0, 1592.0], 'label': u'train'}, {'prob': 0.8762, 'bbox': [3991.0, 1637.0, 4052.0, 1765.0], 'label': u'person'}, {'prob': 0.8531, 'bbox': [1326.0, 2239.0, 1716.0, 2605.0], 'label': u'car'}, {'prob': 0.8516, 'bbox': [1804.0, 1913.0, 2018.0, 2091.0], 'label': u'car'}, {'prob': 0.8477, 'bbox': [435.0, 1668.0, 711.0, 1820.0], 'label': u'car'}, {'prob': 0.8115, 'bbox': [1449.0, 1937.0, 1691.0, 2118.0], 'label': u'car'}, {'prob': 0.8039, 'bbox': [2050.0, 1683.0, 2172.0, 1791.0], 'label': u'car'}, {'prob': 0.7995, 'bbox': [1618.0, 1827.0, 1785.0, 1980.0], 'label': u'car'}, {'prob': 0.7855, 'bbox': [1990.0, 1256.0, 2037.0, 1298.0], 'label': u'car'}, {'prob': 0.7583, 'bbox': [2435.0, 1403.0, 2502.0, 1493.0], 'label': u'car'}, {'prob': 0.7491, 'bbox': [905.0, 1583.0, 975.0, 1744.0], 'label': u'person'}, {'prob': 0.7315, 'bbox': [1108.0, 1511.0, 1260.0, 1596.0], 'label': u'car'}, {'prob': 0.7135, 'bbox': [658.0, 1630.0, 835.0, 1748.0], 'label': u'car'}, {'prob': 0.7065, 'bbox': [702.0, 1252.0, 788.0, 1318.0], 'label': u'car'}, {'prob': 0.7054, 'bbox': [4153.0, 1738.0, 4244.0, 1883.0], 'label': u'fire hydrant'}, {'prob': 0.7024, 'bbox': [1424.0, 1331.0, 1649.0, 1491.0], 'label': u'truck'}, {'prob': 0.697, 'bbox': [2051.0, 1412.0, 2179.0, 1521.0], 'label': u'car'}, {'prob': 0.6951, 'bbox': [3317.0, 1202.0, 3485.0, 1318.0], 'label': u'truck'}, {'prob': 0.6919, 'bbox': [1935.0, 1278.0, 2001.0, 1319.0], 'label': u'car'}, {'prob': 0.6892, 'bbox': [1803.0, 1284.0, 1901.0, 1340.0], 'label': u'car'}, {'prob': 0.6882, 'bbox': [3071.0, 1209.0, 3160.0, 1269.0], 'label': u'car'}, {'prob': 0.6873, 'bbox': [13.0, 1744.0, 315.0, 1932.0], 'label': u'car'}, {'prob': 0.6866, 'bbox': [1195.0, 1263.0, 1282.0, 1309.0], 'label': u'car'}, {'prob': 0.6764, 'bbox': [2731.0, 1966.0, 2976.0, 2193.0], 'label': u'car'}, {'prob': 0.6645, 'bbox': [1191.0, 1244.0, 1269.0, 1283.0], 'label': u'car'}, {'prob': 0.6641, 'bbox': [1235.0, 1267.0, 1323.0, 1317.0], 'label': u'car'}, {'prob': 0.6613, 'bbox': [3908.0, 1480.0, 4013.0, 1576.0], 'label': u'chair'}, {'prob': 0.6367, 'bbox': [2641.0, 1355.0, 2765.0, 1491.0], 'label': u'car'}, {'prob': 0.6313, 'bbox': [3412.0, 1305.0, 3595.0, 1384.0], 'label': u'car'}, {'prob': 0.6253, 'bbox': [1972.0, 1272.0, 2036.0, 1318.0], 'label': u'car'}, {'prob': 0.6174, 'bbox': [1723.0, 1643.0, 1832.0, 1740.0], 'label': u'car'}, {'prob': 0.6173, 'bbox': [1987.0, 1240.0, 2043.0, 1288.0], 'label': u'car'}, {'prob': 0.6116, 'bbox': [1323.0, 1449.0, 1482.0, 1539.0], 'label': u'car'}, {'prob': 0.607, 'bbox': [2338.0, 2257.0, 2610.0, 2523.0], 'label': u'car'}, {'prob': 0.591, 'bbox': [1161.0, 1245.0, 1231.0, 1286.0], 'label': u'car'}, {'prob': 0.591, 'bbox': [2338.0, 2255.0, 2606.0, 2514.0], 'label': u'truck'}, {'prob': 0.5787, 'bbox': [1207.0, 1254.0, 1258.0, 1289.0], 'label': u'car'}, {'prob': 0.5748, 'bbox': [466.0, 1558.0, 650.0, 1679.0], 'label': u'car'}, {'prob': 0.5731, 'bbox': [4150.0, 1731.0, 4243.0, 1883.0], 'label': u'person'}, {'prob': 0.5672, 'bbox':[1140.0, 1897.0, 1367.0, 2064.0], 'label': u'car'}, {'prob': 0.5627, 'bbox': [1208.0, 1273.0, 1259.0, 1311.0], 'label': u'car'}, {'prob': 0.5621, 'bbox': [1747.0, 1625.0, 1847.0, 1715.0], 'label': u'car'}, {'prob': 0.5598, 'bbox': [633.0, 1481.0, 901.0, 1705.0], 'label': u'truck'}, {'prob': 0.5588, 'bbox': [1165.0, 1269.0, 1237.0, 1306.0], 'label': u'car'}, {'prob': 0.5527, 'bbox': [2823.0, 1229.0, 2934.0, 1350.0], 'label': u'train'}, {'prob':0.5365, 'bbox': [283.0, 1520.0, 467.0, 1628.0], 'label': u'car'}, {'prob': 0.5324, 'bbox': [1848.0, 1666.0, 1968.0, 1747.0], 'label': u'car'}, {'prob': 0.5244, 'bbox': [3568.0, 1538.0, 3632.0, 1609.0], 'label': u'car'}, {'prob': 0.5199, 'bbox': [1789.0, 1296.0, 1890.0, 1358.0], 'label': u'car'}, {'prob': 0.5178, 'bbox': [1814.0, 1716.0, 1935.0, 1780.0], 'label': u'car'}, {'prob': 0.516, 'bbox': [1397.0, 1434.0, 1508.0, 1496.0], 'label': u'car'}, {'prob': 0.5136, 'bbox': [3129.0, 1201.0, 3244.0, 1277.0], 'label': u'car'}, {'prob': 0.5128, 'bbox': [1166.0, 1259.0, 1210.0, 1290.0], 'label': u'car'}]
```
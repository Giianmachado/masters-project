## Guide
Install luminoth.
```
pip install luminoth
```
To see others installation ways see https://luminoth.readthedocs.io/en/latest/usage/installation.html.

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
  "objects": [{
		"bbox": [465.0, 2248.0, 881.0, 2535.0],
		"label": "car",
		"prob": 0.9883
	},
	{
		"bbox": [1072.0, 2143.0, 1404.0, 2403.0],
		"label": "car",
		"prob": 0.9841
	},
	{
		"bbox": [3723.0, 1703.0, 3974.0, 1858.0],
		"label": "car",
		"prob": 0.9805
	},
    ...
  ]
}
```

Or execute python code:
```
$ python predict.py

[{
		"bbox": [465.0, 2248.0, 881.0, 2535.0],
		"label": "car",
		"prob": 0.9883
	},
	{
		"bbox": [1072.0, 2143.0, 1404.0, 2403.0],
		"label": "car",
		"prob": 0.9841
	},
	{
		"bbox": [3723.0, 1703.0, 3974.0, 1858.0],
		"label": "car",
		"prob": 0.9805
	},
    ...
]
```
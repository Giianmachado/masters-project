import os
import json
from PIL import Image

from luminoth.tools.checkpoint import get_checkpoint_config
from luminoth.utils.predicting import PredictorNetwork

# config network
config = get_checkpoint_config('e1c2565b51e9')
network = PredictorNetwork(config)
image = Image.open(os.path.abspath('image.jpg')).convert('RGB')
objects = network.predict_image(image)

# log objects
print(json.dumps(objects, indent=4, sort_keys=True))
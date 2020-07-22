!pip install pretrainedmodels
from fastai.vision import *
import pretrainedmodels
from fastai.callbacks import SaveModelCallback

								  
model =  pretrainedmodels.__dict__["se_resnext50_32x4d"](num_classes=1000,pretrained="imagenet")
model._fc = nn.Linear(1000,2)

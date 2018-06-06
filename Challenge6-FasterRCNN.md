# Challenge 6

Link to original tutorial: [Object detection using Faster R-CNN](https://docs.microsoft.com/en-us/cognitive-toolkit/Object-Detection-using-Faster-R-CNN)


> For this challenge we use Deep Learning image in Azure 

* Activate conda virtual environment

```bash
$ source activate py35
```

* Getting CNTK

```bash
$ git clone https://github.com/Microsoft/CNTK.git
$ cd CNTK/Example/Image/Detection/FastRCNN 
```

> We need to execute script from FAST RCNN (not FasteR RCNN)

* Getting data and model

```bash
$ python install_data_and_model.py
```

* Run fitting model in images from example

```
$ cd ..
$ python FasterRCNN/run_faster_rcnn.py
```

and getting something that
```bash
Selected GPU[0] Tesla K80 as the process wide default device.
Using base model:   AlexNet
lr_per_sample:      [0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 1e-05]
Training model for 20 epochs.
Training 57513152 parameters in 27 parameter tensors.
-------------------------------------------------------------------
Build info:

                Built time: Jan 31 2018 15:03:41
                Last modified date: Tue Jan 30 03:26:13 2018
                Build type: release
                Build target: GPU
                With 1bit-SGD: no
                With ASGD: yes
                Math lib: mkl
                CUDA version: 9.0.0
                CUDNN version: 7.0.4
                Build Branch: HEAD
                Build SHA1: a70455c7abe76596853f8e6a77a4d6de1e3ba76e
                MPI distribution: Open MPI
                MPI version: 1.10.7
-------------------------------------------------------------------
PROGRESS: 0.00%
PROGRESS: 0.00%
Finished Epoch[1 of 20]: [Training] loss = 0.371160 * 75, metric = 3.27% * 75 80.644s (  0.9 samples/s);
PROGRESS: 0.00%
PROGRESS: 0.00%
Finished Epoch[2 of 20]: [Training] loss = 0.248294 * 75, metric = 2.38% * 75 72.159s (  1.0 samples/s);
PROGRESS: 0.00%
PROGRESS: 0.00%
```

Prediction end up after 20 epochs

```
Finished Epoch[20 of 20]: [Training] loss = 0.343846 * 20, metric = 5.51% * 20 21.224s (  0.9 samples/s);
creating eval model
Stored eval model at /home/anatoliy/notebooks/CNTK/Examples/Image/Detection/FasterRCNN/Output/faster_rcnn_eval_AlexNet_e2e.model
Evaluating Faster R-CNN model for 5 images.
Number of rois before non-maximum suppression: 352
Number of rois  after non-maximum suppression: 58
AP for            milk = 1.0000
AP for       champagne = 1.0000
AP for          gerkin = 1.0000
AP for         joghurt = 1.0000
AP for         ketchup = 0.6667
AP for          pepper = 1.0000
AP for           water = 0.5000
AP for           onion = 1.0000
AP for         mustard = 1.0000
AP for          tomato = 1.0000
AP for     orangeJuice = 1.0000
AP for         tabasco = 1.0000
AP for          eggBox = 1.0000
AP for         avocado = 1.0000
AP for          orange = 1.0000
AP for          butter = 1.0000
Mean AP = 0.9479
Plotting results from for 5 images.
```

* Preparing our data for object detectioin
    * Find images :)
    * Install [VoTT](https://github.com/Microsoft/VoTT)
    * Boxing images in VoTT and export tags for CNTK-FasterRCNN

* Create new folder ```Helmet``` in folder ```CNTK/Examples/Image/DataSet```
* Copy exported folders to ```CNTK/Examples/Image/DataSet/Helmet```
* Edit helper file ```CNTK/Example/Image/Detection/FasterRCNN/utils/annotations/annotations_helper.py```. Set path to Helmet DataSet.

```py
if __name__ == '__main__':
    abs_path = os.path.dirname(os.path.abspath(__file__))
    data_set_path = os.path.join(abs_path, "../../../DataSets/Helmet")

    class_dict = create_class_dict(data_set_path)
    create_map_files(data_set_path, class_dict, training_set=True)
    create_map_files(data_set_path, class_dict, training_set=False)
```

* Run helper while in ```CNTK/Example/Image/Detection/FasterRCNN```

```bash
$python utils/annotations/annotations_helper.py
```

After that we have next state of our folder:

```bash
anatoliy@anatoliydl:~/notebooks/CNTK/Examples/Image/DataSets/Helmet$ ls -lha
total 48K
drwxrwxr-x  5 anatoliy anatoliy 4.0K Jun  6 10:09 .
drwxrwxr-x 12 anatoliy anatoliy 4.0K Jun  6 10:07 ..
drwxrwxr-x  2 anatoliy anatoliy 4.0K Jun  6 13:05 negative
drwxrwxr-x  2 anatoliy anatoliy  12K Jun  6 13:05 positive
drwxrwxr-x  2 anatoliy anatoliy 4.0K Jun  6 13:05 testImages
-rw-rw-r--  1 anatoliy anatoliy  613 Jun  6 10:09 test_img_file.txt
-rw-rw-r--  1 anatoliy anatoliy  891 Jun  6 10:09 test_roi_file.txt
-rw-rw-r--  1 anatoliy anatoliy 2.1K Jun  6 10:09 train_img_file.txt
-rw-rw-r--  1 anatoliy anatoliy 3.8K Jun  6 10:09 train_roi_file.txt
```

* Make a new python file for our dataset in ```CNTK/Examples/Image/Detection/utils/configs/Helmet_config.py```

```py
# Copyright (c) Microsoft. All rights reserved.

# Licensed under the MIT license. See LICENSE.md file in the project root
# for full license information.
# ==============================================================================

# `pip install easydict` if you don't have it
from easydict import EasyDict as edict

__C = edict()
__C.DATA = edict()
cfg = __C

# data set config
__C.DATA.DATASET = "Helmet"
__C.DATA.MAP_FILE_PATH = "../../DataSets/Helmet"
__C.DATA.CLASS_MAP_FILE = "class_map.txt"
__C.DATA.TRAIN_MAP_FILE = "train_img_file.txt"
__C.DATA.TRAIN_ROI_FILE = "train_roi_file.txt"
__C.DATA.TEST_MAP_FILE = "test_img_file.txt"
__C.DATA.TEST_ROI_FILE = "test_roi_file.txt"
__C.DATA.NUM_TRAIN_IMAGES = 75
__C.DATA.NUM_TEST_IMAGES = 16
__C.DATA.PROPOSAL_LAYER_SCALES = [4, 8, 12]

# overwriting proposal parameters for Fast R-CNN
# minimum relative width/height of an ROI
__C.roi_min_side_rel = 0.04
# maximum relative width/height of an ROI
__C.roi_max_side_rel = 0.4
# minimum relative area of an ROI
__C.roi_min_area_rel = 2 * __C.roi_min_side_rel * __C.roi_min_side_rel
# maximum relative area of an ROI
__C.roi_max_area_rel = 0.33 * __C.roi_max_side_rel * __C.roi_max_side_rel
# maximum aspect ratio of an ROI vertically and horizontally
__C.roi_max_aspect_ratio = 4.0

# For this data set use the following lr factor for Fast R-CNN:
# __C.CNTK.LR_FACTOR = 10.0

```

* Edit file ```CNTK/Examples/Image/FasterRCNN/run_faster_rcnn.py```. Find function ```def get_configuration():``` and change line when imported library with alias ```dataset_cfg``` to ```Helmet_config.py``` file.

resultant function
```py
def get_configuration():
    # load configs for detector, base network and data set
    from FasterRCNN_config import cfg as detector_cfg
    # for VGG16 base model use:         from utils.configs.VGG16_config import cfg as network_cfg
    # for AlexNet base model use:       from utils.configs.AlexNet_config import cfg as network_cfg
    from utils.configs.AlexNet_config import cfg as network_cfg
    from utils.configs.Helmet_config import cfg as dataset_cfg

    return merge_configs([detector_cfg, network_cfg, dataset_cfg])
```

* Run fit in new dataset
```bash
$python FasterRCNN/run_faster_rcnn.py
```









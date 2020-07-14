# symbols_detection
&nbsp
This repository represents Symbols detection in complex engineering drawings and open-source research into future object detection methods. Incorporates my lessons learned and best practices evolved over the training of models on custom client datasets. **All code and models are under active development, and are subject to modification or deletion without notice.** Use at your own risk.

## Requirements

Python 3.7 or later with all `requirements.txt` dependencies installed, including `torch >= 1.5`. To install run:
```bash
$ pip install -U -r requirements.txt
```

## Inference

Inference can be run on most common media formats. Model [checkpoints] avilable in (/weights). Results are saved to `./inference/output`.
```bash
$ python detect.py --source file.jpg  # image 
                            file.mp4  # video
                            ./dir  # directory
                            0  # webcam
                            rtsp://170.93.143.139/rtplive/470011e600ef003a004ee33696235daa  # rtsp stream
                            http://112.50.243.8/PLTV/88888888/224/3221225900/1.m3u8  # http stream
```

To run inference on examples in the `./inference/images` folder:

```bash
$ python detect.py --source ./inference/images/ --weights weights/best_PandIDs.pt --conf 0.4

Namespace(agnostic_nms=False, augment=False, classes=None, conf_thres=0.4, device='', fourcc='mp4v', half=False, img_size=640, iou_thres=0.5, output='inference/output', save_txt=False, source='./inference/images/', view_img=False, weights='best_PandIDs.pt')
Using CUDA device0 _CudaDeviceProperties(name='Tesla P100-PCIE-16GB', total_memory=16280MB)

Downloading https://drive.google.com/uc?export=download&id=1R5T6rIyy3lLwgFXNms8whc-387H0tMQO as yolov5s.pt... Done (2.6s)

image 1/2 inference/images/bus.jpg: 640x512 3 persons, 1 buss, Done. (0.009s)
image 2/2 inference/images/zidane.jpg: 384x640 2 persons, 2 ties, Done. (0.009s)
Results saved to inference/output
```


## About Me

Over 4+ years of experience in the IT industry contributing to design, development, automation, testing, continuous integration and monitoring services. Strong expertise in Deep Learning, Machine Learning, Quantitative Analytics,  Design Patterns, Data Modelling and DB management. I offer a wide range of vision AI services, spanning from simple expert advice up to delivery of fully customized, end-to-end production solutions, including:

- **Cloud-based AI** systems operating on **hundreds of HD video streams in realtime.**
- **Custom data training**, hyperparameter evolution, and model exportation to any destination.


## Contact

**Issues should be raised directly in the repository.** For business inquiries or professional support requests please email Mohan Krishna V at mohankrishna_v@outlook.com.

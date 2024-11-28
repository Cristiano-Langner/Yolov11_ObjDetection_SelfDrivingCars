# Object Detection for Self-driving Cars (UFSC)

 
 This repository contains a final project for our Computer Vision Class at the Federal University of Santa Catarina (UFSC). We developed a custom dataset of the region of Florianópolis to train a YOLO model for our task of detecting objects for a self-driving car application, using known tools such as Ultralytics and Roboflow.

 The structure of the repository is explained below:
- kitti_dataset_related: folder to store the results obtained of our older approach of train the models on the KITTI dataset
- old_models_yolo: folder storing the older models trained on KITTI
- utils: folder to store the scripts that were useful to us, such as extracting random frames from videos to construct our dataset
- objdetec-4-autonomousdriving.ipynb: the main notebook where the final models were trained
- yolo*.pt: default models downloaded from Ultralytics website
- results_yolo11m_custom_dataset.zip: zip file containing the results on our custom dataset, metrics and the trained models. 
 

# **YOLO Model for Sinusitis Detection and Classification**

This folder contains experiments using YOLO (You Only Look Once) models for **sinusitis detection, segmentation, and classification**. The goal is to compare YOLO's accuracy against other models to determine the best approach for sinusitis analysis in X-ray images.

---

**This is still on testing and may not work some python notebooks as expected**

## **Folder Structure**

```plaintext
annotate_maxillary
│
├── yolo/
│    │
│    ├── dataset/ # ignored in the .gitignore.
│    │    │── data_segment/
│    │    │   ├── images/
│    │    │   │   ├── test/  # Test set images
│    │    │   │   ├── train/ # Training set images
│    │    │   │   └── val/   # Validation set images
│    │    │   └── labels/
│    │    │       ├── test/  # Test set annotations
│    │    │       ├── train/ # Training set annotations
│    │    │       └── val/   # Validation set annotations\
│    │    │
│    │    └── detect/        # YOLO model predictions
│    │        ├── images/    # Output images after detection
│    │        └── labels/    # Output labels after detection
│    ├── runs/               # Model output results
│    │   └── detect/         # detection runs
│    │   └── segment/        # segment runs
│    ├── test/               # Testing output files
│    ├── config.yaml         # YOLO configuration
│    ├── predict.ipynb       # Script to run predictions
│    ├── train.ipynb         # Script to train the YOLO models
│    ├── yolo11n-seg.pt      # Pretrained model for segmentation
│    ├── yolo11n.pt          # Pretrained model for classification
│    ├── yolo8n-seg.pt       # YOLOv8 pretrained segmentation model
│    │
│    └── README.md           # Documentation for YOLO folder
└── extract_maxillary_coordinates.ipynb  # Annotation script
```
### Dataset Requirements
   - The dataset should be organized in the dataset/data_segment/ folder.
   - **Images:** Place all training, validation, and test images inside the respective subdirectories (train/, val/, test/).
   - **Labels:** Use YOLO-compatible annotation files (e.g., .txt) for bounding boxes or segmentation masks and place them in the corresponding labels folder.

### Data Annotation

Use [Open Data Annotation Platform](https://www.cvat.ai/) For annotate the maxillary area

### How to Use This Folder
   1. Train the Model
      - Open train.ipynb to configure and train YOLO models.
      - Ensure the dataset paths in config.yaml match the dataset directory structure.
   2. Run Predictions

      - Use predict.ipynb to generate predictions on new images.
      - Place input images in the appropriate folder (detect/images) and check the output in the output/runs folder.
   3. Annotate Dataset
      - Use annotate_maxillary_sinus.ipynb or extract_maxillary_coordinates ipynb to generate bounding boxes or segmentation masks for your dataset.

### Objective of YOLO Models in This Research

This folder focuses on using YOLO for:

1. Detection: Locating the sinus regions in X-rays.
2. Segmentation: Accurately marking sinus areas pixel-by-pixel.
3. Classification: Categorizing sinusitis severity levels.

### Results and Output
   - Outputs are saved in the **runs/** folder.
   - Test Results include annotated images and predictions in the **test/** folder.
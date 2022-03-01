# YOLOv5 on a custom dataset

## Annotations conversion to YOLO format
The provided annotations are in Pascal VOC .xml format and need to be converted to YOLO .txt files accordingly. We use "convert_voc_to_yolo.py" for this purpose. We put all the training images and their corresponding annotations in a new subfolder within the main folder where the aforementioned .py file is located. On line 8 of the code, we insert the name of the folder containing the images and annotations. After running the code in the terminal, a new subfolder named "yolo" is created that contains the corresponding .txt annotation files in YOLO format. <br>

## YOLOv5 installation
Within our main working directory, we clone the YOLOv5 GitHub repository and install its requirements by running the following commands in the terminal: <br>
git clone https://github.com/ultralytics/yolov5  <br>
cd yolov5 <br>
pip install -r requirements.txt  <br>

## Split the data into training and validation sets
Inside the "yolov5" folder, we add "train_val_split.py" and create a new subfolder called "datasets". Within this new "datasets" folder, we create a new subfolder (name it "images_annotations" for example) and copy all the training images with their new .txt annotation files into it. Now, we go back to the "yolov5" folder and run "train_val_split.py" to randomly split the data into training and validation sets. Before running this code, we need to modify line 10 of it, where we have to put the complete absolute path to the "datasets" folder we just created. Next, we can run this code in the terminal inside "yolov5" folder that should take 3 parser arguments: <br><br>
1- The name of the folder that contains the images and annotations together inside the "datasets" folder. For instance, "images_annotations" as mentioned above. <br>
2- The name of the folder that we would like to have this split occurs within the "datasets" folder. Let us take "ReTech_Labs" as an example. <br>
3- The last argument is the split ratio. For instance, if we want to keep 90% of the data as the training data and the remaining 10% as the validation set, this ratio should be set to 0.1. <br><br>
We can then run this code the following way as an example: <br><br>
python3 train_val_split.py --source 'images_annotations' --dest 'ReTech_Labs' --val_ratio 0.1

## Dataset configuration
We can copy the present "retech_labs.yaml" file to the "data" subfolder within the "yolov5" folder and use it as it is unless the name of the folder containing the training and validation data is different from what is given in this file, in which case it has to be changed accordingly.

## Training
We can perform 6 different experiments: <br><br>
1- Training with the small model size and 100, 150, 200 number of epochs. <br>
2- Training with the medium model size and 150, 200, 250 epochs. <br><br>
As an example, to train the small model on 150 epochs, we run "train.py" in the "yolov5" folder as below: <br><br>
python train.py --img 640 --batch 16 --epochs 150 --data 'data/retech_labs.yaml' --weights yolov5s.pt <br><br>
By doing this, a new folder named "runs" is created within the "yolov5" folder that contains a "train" folder which has a folder called "exp" that has the results associated with this training experiment.

## Inference
To use the trained model from the above example for running inference on the test images, we run the "detect.py" code inside the "yolov5" folder with the following arguments: <br><br>
python detect.py --source '<complete absolute path to the test images>' --weights 'runs/train/exp/weights/best.pt'

## Referenes
https://github.com/ultralytics/yolov5 <br>
https://gist.github.com/Amir22010/a99f18ca19112bc7db0872a36a03a1ec

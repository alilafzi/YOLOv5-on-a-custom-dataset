import shutil, os, argparse, glob, random, numpy as np
random.seed(27)

parser = argparse.ArgumentParser (description = 'random splitting')
parser.add_argument('source' , type = str)
parser.add_argument('dest' , type = str)
parser.add_argument('val_ratio' , type = float)
args , unknown = parser.parse_known_args()

root = <complete path to the dataset>
os.chdir(root)
if not os.path.isdir(args.dest):
	os.mkdir(args.dest)
os.chdir(args.dest)
if not os.path.isdir('images'):
	os.mkdir('images')
if not os.path.isdir('labels'):
	os.mkdir('labels')
os.chdir('images')
if not os.path.isdir('train'):
	os.mkdir('train')
if not os.path.isdir('val'):
	os.mkdir('val')
os.chdir('..')
os.chdir('labels')
if not os.path.isdir('train'):
	os.mkdir('train')
if not os.path.isdir('val'):
	os.mkdir('val')

path = os.path.join(root, args.source)
image_files = glob.glob(path + '/**/*.jpg' , recursive = True)
label_files = glob.glob(path + '/**/*.txt' , recursive = True)

for img in image_files:
	shutil.copy(img, os.path.join(root, args.dest, 'images' , 'train'))
for lbl in label_files:
	shutil.copy(lbl, os.path.join(root, args.dest, 'labels' , 'train'))

train_images = os.listdir(os.path.join(root , args.dest , 'images' , 'train'))
train_labels = os.listdir(os.path.join(root , args.dest , 'labels' , 'train'))
val_images = random.sample(train_images, int(args.val_ratio * len(image_files)))
val_labels = []
for name in val_images:
	name = name.split('.')	
	name = name[0] + '.txt'
	val_labels.append(name)

val_images_indices = []
for img in val_images:
	val_images_indices.append(train_images.index(img))

val_labels_indices = []
for lbl in val_labels:
	val_labels_indices.append(train_labels.index(lbl))
for index in val_images_indices:
	shutil.move(os.path.join(root, args.dest, 'images' , 'train' , train_images[index]) ,
os.path.join(root, args.dest , 'images' , 'val'))

for index in val_labels_indices:
	shutil.move(os.path.join(root, args.dest, 'labels' , 'train' , train_labels[index]) ,
os.path.join(root, args.dest , 'labels' , 'val'))

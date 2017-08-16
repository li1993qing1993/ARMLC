import sys
import os, random
import shutil
import argparse
import image_transformation

data_dir = '/media/qingli/C8EA71A3EA718E86/ARMLC/dataset/image'
data_dir_parent = '/media/qingli/C8EA71A3EA718E86/ARMLC/dataset'

def format_dataset(data_dir):
    print('Determining list of input files and labels from %s.' % data_dir)

    filenames = os.listdir(data_dir)
    filenames_labeled = [(data_dir + '/' + f[:10]) for f in filenames]
    dir_count = 0
    for i in range(len(filenames)):
        if not os.path.isdir(filenames_labeled[i]):
            os.mkdir(filenames_labeled[i])
            dir_count += 1
            os.rename(os.path.join(data_dir, filenames[i]), os.path.join(filenames_labeled[i], filenames[i]))
        else:
            os.rename(os.path.join(data_dir, filenames[i]), os.path.join(filenames_labeled[i], filenames[i]))
    print('Created %d directories' % dir_count)
"""
for i in range(len(filenames_labeled)):
    if os.path.isdir(filenames_labeled[i]):
        files = os.listdir(filenames_labeled[i])
        if len(files) < 30:
            for f in files:
                f_full_path = os.path.join(filenames_labeled[i], f)
                times = 30 / len(files)
                if not os.path.isfile(f_full_path):
                    continue
                for t in range(int(times)):
                    new_f_full_path = os.path.join(filenames_labeled[i], ('duplicate_%d' % t) + f)
                    shutil.copy(f_full_path, new_f_full_path)
"""

"""
Split dataset into training and validation datasets.
The output format:
$TRAIN_DIR/dog/image0.jpeg
  $TRAIN_DIR/dog/image1.jpg
  $TRAIN_DIR/dog/image2.png
  ...
  $TRAIN_DIR/cat/weird-image.jpeg
  $TRAIN_DIR/cat/my-image.jpeg
  $TRAIN_DIR/cat/my-image.JPG
  ...
  $VALIDATION_DIR/dog/imageA.jpeg
  $VALIDATION_DIR/dog/imageB.jpg
  $VALIDATION_DIR/dog/imageC.png
  ...
  $VALIDATION_DIR/cat/weird-image.PNG
  $VALIDATION_DIR/cat/that-image.jpg
  $VALIDATION_DIR/cat/cat.JPG
"""
def split_data(data_dir, validation_percentage, output_val_dir, output_train_dir):
    if not os.path.exists(output_train_dir):
        os.mkdir(output_train_dir, 0755)
    if not os.path.exists(output_val_dir):
        os.mkdir(output_val_dir, 0755)
    print('splitting data to training set and validation set.')
    labels = os.listdir(data_dir)
    c = 0
    for l in labels:
        print('split data for label %s' % l)
        label_dir = os.path.join(data_dir, l)
        image_list = os.listdir(label_dir)
        image_filenames = [os.path.join(label_dir, im) for im in image_list]
        val_num = int(len(image_filenames) * validation_percentage)
        if val_num <= 0:
            print('validation set for this label is 0')
            continue
        val_list = random.sample(image_filenames, val_num)
        for val in val_list:
            val_dest = os.path.join(output_val_dir, l)
            if not os.path.exists(val_dest):
                os.mkdir(val_dest, 0755)
            val_file = os.path.basename(val)
            val_dest = os.path.join(val_dest, val_file)
            os.rename(val, val_dest)
        if os.path.exists(os.path.join(output_train_dir, l)):
            shutil.rmtree(os.path.join(output_train_dir, l))
        shutil.copytree(label_dir, os.path.join(output_train_dir, l))
        shutil.rmtree(label_dir)

"""
Combine the training dataset and validation dataset. This function is the revert funtion of split_data function
"""
def combine_data(train_dir, val_dir, output_dir):
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    labels = os.listdir(train_dir)
    for l in labels:
        label_dir = os.path.join(train_dir, l)
        image_list = os.listdir(label_dir)
        image_filenames = [os.path.join(label_dir, im) for im in image_list]
        for image in image_filenames:
            basename = os.path.basename(image)
            dest = os.path.join(output_dir, l)
            if not os.path.exists(dest):
                os.mkdir(dest, 0755)
            dest_file = os.path.join(dest, basename)
            if not os.path.exists(dest_file):
                os.rename(image, dest_file)
    labels = os.listdir(val_dir)
    for l in labels:
        label_dir = os.path.join(val_dir, l)
        image_list = os.listdir(label_dir)
        image_filenames = [os.path.join(label_dir, im) for im in image_list]
        for image in image_filenames:
            basename = os.path.basename(image)
            dest = os.path.join(output_dir, l)
            if not os.path.exists(dest):
                os.mkdir(dest, 0755)
            dest_file = os.path.join(dest, basename)
            if not os.path.exists(dest_file):
                os.rename(image, dest_file)

def create_label_file(data_dir, label_file_path):
    print('Creating label_file at %s' % label_file_path)
    if not os.path.exists(data_dir):
        raise ValueError('Invalid data directory path.')
    labels = os.listdir(data_dir)
    if os.path.isfile(label_file_path):
        print('File already exists, deleting it.')
        os.remove(label_file_path)
    with open(label_file_path, 'w') as f:
        for label in labels:
            f.write(label)
            f.write('\n')

"""
Don't use this function. Too slow, use the following command instead.
find . -type f | sed 's/.*\.//' | sort | uniq -c
"""
def count_jpg(jpg_file):
    count = 0
    if os.path.isdir(jpg_file):
        folder_list = os.listdir(jpg_file)
        for f in folder_list:
            count += count_jpg(os.path.join(jpg_file, f))
        return count
    elif jpg_file.endswith('.jpg'):
        return 1


#format_dataset(data_dir)
#image_transformation.transform_image(data_dir)
#split_data(data_dir, 0.2, data_dir_parent + '/subTrainingSet_val', data_dir_parent + '/subTrainingSet_train')
#combine_data('/media/qingli/C8EA71A3EA718E86/ARMLC/tf_files/subTrainingSet_val', '/media/qingli/C8EA71A3EA718E86/ARMLC/tf_files/subTrainingSet_train', '/media/qingli/C8EA71A3EA718E86/ARMLC/tf_files/subTrainingSet_2')
#create_label_file(data_dir_parent + '/subTrainingSet_train', data_dir_parent + '/label_file.txt')
#image_transformation.resize_all(data_dir_parent + '/subTrainingSet_val', 299, 299)
#image_transformation.resize_all(data_dir_parent + '/subTrainingSet_train', 299, 299)
print(count_jpg(data_dir_parent + '/subTrainingSet_train'))
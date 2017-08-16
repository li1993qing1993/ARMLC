#!/usr/bin/env bash
# location to where to save the TFRecord data.
OUTPUT_DIRECTORY=/media/qingli/C8EA71A3EA718E86/ARMLC/dataset/my-custom-data
echo 'Building the image. Make output directory...'
if [ -d "$OUTPUT_DIRECTORY" ]; then
    echo 'Output directory already exist, cleaning it and recreate the folder.'
    rm -rf ${OUTPUT_DIRECTORY}/*
fi
    mkdir -p ${OUTPUT_DIRECTORY}

TRAIN_DIR=/media/qingli/C8EA71A3EA718E86/ARMLC/dataset/subTrainingSet_train
VALIDATION_DIR=/media/qingli/C8EA71A3EA718E86/ARMLC/dataset/subTrainingSet_val
LABELS_FILE=/media/qingli/C8EA71A3EA718E86/ARMLC/dataset/label_file.txt

cd $HOME/tensorflow_repo/models/inception
bazel build //inception:build_image_data

bazel-bin/inception/build_image_data \
  --train_directory="${TRAIN_DIR}" \
  --validation_directory="${VALIDATION_DIR}" \
  --output_directory="${OUTPUT_DIRECTORY}" \
  --labels_file="${LABELS_FILE}" \
  --train_shards=1280\
  --validation_shards=240\
  --num_threads=8
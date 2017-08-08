#!/usr/bin/env bash
# location to where to save the TFRecord data.
OUTPUT_DIRECTORY=/media/qingli/C8EA71A3EA718E86/ARMLC/my-custom-data
echo 'Building the image. Make output directory...'
if [ -d "$OUTPUT_DIRECTORY" ]; then
    echo 'Output directory already exist, cleaning it and recreate the folder.'
    rm -rf ${OUTPUT_DIRECTORY}/*
else
    mkdir -p ${OUTPUT_DIRECTORY}
fi

TRAIN_DIR=/media/qingli/C8EA71A3EA718E86/ARMLC/tf_files/subTrainingSet_train
if [ -d "$TRAIN_DIR" ]; then
    echo 'Training directory already exists, cleaning it.'
    rm -rf ${TRAIN_DIR}/*
else
    mkdir -p ${TRAIN_DIR}
fi
VALIDATION_DIR=/media/qingli/C8EA71A3EA718E86/ARMLC/tf_files/subTrainingSet_val
if [ -d "$VALIDATION_DIR" ]; then
    echo 'Validation directory already exists, cleaning it.'
    rm -rf ${VALIDATION_DIR}/*
else
    mkdir -p ${VALIDATION_DIR}
fi
LABELS_FILE=/media/qingli/C8EA71A3EA718E86/ARMLC/tf_files/label_file.txt

cd $HOME/tensorflow_repo/models/inception
bazel build //inception:build_image_data

bazel-bin/inception/build_image_data \
  --train_directory="${TRAIN_DIR}" \
  --validation_directory="${VALIDATION_DIR}" \
  --output_directory="${OUTPUT_DIRECTORY}" \
  --labels_file="${LABELS_FILE}" \
  --train_shards=128 \
  --validation_shards=24 \
  --num_threads=8
#!/usr/bin/env bash
INCEPTION_MODEL_DIR=$HOME/inception-v3-model
if [ ! -d "$INCEPTION_MODEL_DIR" ]; then
    mkdir -p ${INCEPTION_MODEL_DIR}
    cd ${INCEPTION_MODEL_DIR}

    # download the Inception v3 model
    curl -O http://download.tensorflow.org/models/image/imagenet/inception-v3-2016-03-01.tar.gz
    tar xzf inception-v3-2016-03-01.tar.gz
fi

# this will create a directory called inception-v3 which contains the following files.

# Build the model. Note that we need to make sure the TensorFlow is ready to
# use before this as this command will not build TensorFlow.
cd $HOME/tensorflow_repo/models/inception
bazel build //inception:flowers_train

# Path to the downloaded Inception-v3 model.
MODEL_PATH="${INCEPTION_MODEL_DIR}/inception-v3/model.ckpt-157585"

# Directory where the flowers data resides.
DATA_DIR=/media/qingli/C8EA71A3EA718E86/ARMLC/dataset/my-custom-data/

# Directory where to save the checkpoint and events files.
TRAIN_DIR=/media/qingli/C8EA71A3EA718E86/ARMLC/train_data

# Run the fine-tuning on the flowers data set starting from the pre-trained
# Imagenet-v3 model.
bazel-bin/inception/flowers_train \
  --train_dir="${TRAIN_DIR}" \
  --data_dir="${DATA_DIR}" \
  --pretrained_model_checkpoint_path="/media/qingli/C8EA71A3EA718E86/ARMLC/train_data_280000/model.ckpt-280000" \
  --fine_tune=False \
  --initial_learning_rate=0.005 \
  --input_queue_memory_factor=1 \
  --batch_size=5
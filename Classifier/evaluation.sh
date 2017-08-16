#!/usr/bin/env bash
# Build the model. Note that we need to make sure the TensorFlow is ready to
# use before this as this command will not build TensorFlow.
cd $HOME/ARMLC/Classifier/model/inception/
bazel build //inception:flowers_eval

# Directory where we saved the fine-tuned checkpoint and events files.
TRAIN_DIR=/media/qingli/C8EA71A3EA718E86/ARMLC/train_data

# Directory where the flowers data resides.
DATA_DIR=/media/qingli/C8EA71A3EA718E86/ARMLC/my-custom-data

# Directory where to save the evaluation events files.
EVAL_DIR=/media/qingli/C8EA71A3EA718E86/ARMLC/eval_data

# Evaluate the fine-tuned model on a hold-out of the flower data set.
bazel-bin/inception/flowers_eval \
  --eval_dir="${EVAL_DIR}" \
  --data_dir="${DATA_DIR}" \
  --subset=validation \
  --num_examples=5500 \
  --checkpoint_dir="${TRAIN_DIR}" \
  --input_queue_memory_factor=1 \
  --run_once
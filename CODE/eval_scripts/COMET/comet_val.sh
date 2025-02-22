#!/bin/bash
export CUDA_VISIBLE_DEVICES=2

# 参数列表
JSON_FILE_PATH="/mnt/data/home/usera6k06/wjk/WMT/results/inference_results/ar22_evaluation_results.json"
MODEL_PATH="/mnt/data/home/usera6k06/wjk/WMT/COMET_checkpoints/checkpoints/model.ckpt"
OUTPUT_FILE_PATH="/mnt/data/home/usera6k06/wjk/WMT/results/comet_results/ar22_comet_results.json"
GPUS=1

# 启动Python脚本
python comet_val.py $JSON_FILE_PATH $MODEL_PATH $OUTPUT_FILE_PATH $GPUS
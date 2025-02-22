#!/bin/bash
export CUDA_VISIBLE_DEVICES=1,2

//注意请首先下载相应的BLEURT的checkpoint

# 参数设置
DATA_FILE=""
# 注意选择相应的checkpoint
CHECKPOINT="/BLEURT_checkpoints/BLEURT-20"  
OUTPUT_FILE=""

# 运行 Python 脚本
python bleurt_val.py $DATA_FILE $CHECKPOINT $OUTPUT_FILE
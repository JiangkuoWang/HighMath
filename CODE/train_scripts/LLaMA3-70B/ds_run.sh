export MODEL_PATH=''
export SAVE_PATH=''

export GLOO_SOCKET_IFNAME="lo"
export NCCL_SOCKET_IFNAME="lo"
export CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7




deepspeed train_math.py \
    --deepspeed "" \
    --model_name_or_path $MODEL_PATH \
    --data_path "" \
    --data_length 10000000 \
    --output_dir $SAVE_PATH \
    --num_train_epochs 3 \
    --per_device_train_batch_size 1 \
    --per_device_eval_batch_size 1 \
    --gradient_accumulation_steps 8 \
    --evaluation_strategy "no" \
    --save_strategy "epoch" \
    --save_total_limit 30 \
    --logging_steps 100 \
    --bf16 True \
    --learning_rate 1e-6 \
    --warmup_steps 1000


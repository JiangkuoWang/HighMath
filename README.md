## ENHANCING MULTILINGUAL REASONING IN LLMS:INSIGHTS FROM CROSS-LINGUISTIC CORRELATIONS AND OPTIMAL DATA PROPORTIONS

<p align="center">
  <a href="https://openreview.net/forum?id=S6cBH99BhB"> 📃 Paper</a> | 
  <a href="https://huggingface.co/datasets/svadvcx/HighMath"> 🤗 Huggingface</a> | 
  <a href="https://github.com/DeepShareAI"> 📭 Contact</a> 
</p>

![alt text](picture\highmath.png)

### :mountain: Overview 
* This repository shares the code and dataset of our latest work on multilingual reasoning. In this work, we present a novel  construction of dataset which performs targeted language alignment for best use of the LLMs English reasoning abilities.
* Utilizing this dataset, you can finetune open-source LLMs into strong multilingual reasoning systems. For example, our fine-tuned LLaMA2-7B achieves superior multilingual performance, significantly outperforming baseline models of equivalent size.
* Overall, our method effectively reduces the performance disparity of LLMs across English and non-English languages, showing a new paradigm to unlock LLM’s capabilities to accompolish multilingual tasks.
* Please note that the core contribution of our work is to provide an idea for constructing datasets and to open-source the HighMath dataset. The code in the repository is just an example of how to use it, so please adjust the usage according to your actual situation.


### :chart_with_upwards_trend: Benchmarks

Below we present LLMs' average answer accuracy (zero-shot) on multilingual reasoning benchmarks. With HighMath, our fine-tuned LLM
surpasses the unaligned counterpart and the translate-training baseline  by a large margin.


|         System (7B)        | Monolingual Supervision | Multilingual Supervision | mGSM | mSVAMP |
|:--------------------------:|:-----------------------:|:------------------------:|:----:|:------:|
| [HighMath (ours)](https://huggingface.co/datasets/svadvcx/HighMath) |        -       |          HighMath          | 52.5 |  65.2  |      
|         [MetaMath](https://huggingface.co/meta-math/MetaMath-7B-V1.0)          |        MetaMathQA       |             -            | 38.4 |  46.2  |         
|         [MathOctopus](https://huggingface.co/Mathoctopus/Parallel_7B)        |            -            |       GSM8KInstruct      | 40.0 |  44.1  |         
|         [WizardMath](https://huggingface.co/WizardLM/WizardMath-7B-V1.0)         |          GSM8K & MATH          |             -            | 23.0 |  32.5  |          
|         [MAmmoTh](https://huggingface.co/TIGER-Lab/MAmmoTH-7B)          |          MathInstruct         |             -            | 21.3 |  26.3  |       
|         [RFT](https://huggingface.co/OFA-Sys/gsm8k-rft-llama7b2-u13b/tree/main)            |           GSM8k-ScRel         |             -            | 20.6 |  31.3  |          
|         [SFT]()           |          GSM8K          |             -            | 22.6 |  30.9  |       


### :open_file_folder: Dataset
In the table below, we list datasets that are used in this project. All datasets are available through the url.

|    Dataset    |    Usage   |   Size  |           Languages           |
|:-------------:|:----------:|:-------:|:-----------------------------:|
| [HighMath](https://huggingface.co/datasets/svadvcx/HighMath) |  Training  |  395,000 | En, Bn, Th, Sw, Ja, Zh, De, Fr, Ru, Es |
|   [MetaMathQA](https://huggingface.co/datasets/meta-math/MetaMathQA)  |  Training  | 395,000 |               En              | 
| [GSM8KInstruct](https://huggingface.co/datasets/Mathoctopus/GSM8KInstruct_Parallel) |  Training  |  73,559 | En, Bn, Th, Sw, Ja, Zh, De, Fr, Ru, Es |
|     [mGSM](https://huggingface.co/datasets/juletxara/mgsm)     | Evaluation |  2,500  | En, Bn, Th, Sw, Ja, Zh, De, Fr, Ru, Es | 
|    [mSVAMP](https://huggingface.co/datasets/Mathoctopus/MSVAMP)    | Evaluation |  10,000 | En, Bn, Th, Sw, Ja, Zh, De, Fr, Ru, Es | 





### :hammer_and_wrench: Training
We develope our training pipeline based on the [stanford_alpaca](https://github.com/tatsu-lab/stanford_alpaca) repository. 

To perform finetuning on pre-trained LLMs, use the following command. When fine-tuning the 70B model, we utilize [DeepSpeed](https://github.com/microsoft/DeepSpeed) to save memory. You can find our deepspeed configuration in the repo.

Please note that the training configuration in the repository is provided as a reference example. Please customize the settings according to your actual requirements and hardware conditions.

The recommended configuration is 8xA100 GPUs.
* Exanple: finetuning LLaMA2-7B
```bash
bash ./ds_run.sh
```


### :evergreen_tree: Citation
If you find this repository helpful, feel free to cite our paper:
```
@inproceedings{
wang2025enhancing,
title={Enhancing Multilingual Reasoning in {LLM}s: Insights from Cross-Linguistic Correlations and Optimal Data Proportions},
author={Jiangkuo Wang and Suyv Ma and Mingpeng Wei},
booktitle={The Thirteenth International Conference on Learning Representations},
year={2025},
url={https://openreview.net/forum?id=S6cBH99BhB}
}
```
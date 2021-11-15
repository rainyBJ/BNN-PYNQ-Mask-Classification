# BNN-PYNQ Mask Classification

## 数据集

MaskedFace_Net

https://github.com/cabani/MaskedFace-Net

从四个分类中随机抽取等量图片，

- CMFD
- IMFD1
- IMFD2
- IMFD3

做数据增强，得到 32x32 格式（类似于 Cifar10）的图片，

- 训练集：80k

- 测试集：20k

## 精度

-  网络结构均采用与 MASK_1W1A 相同的结构，更改输出分类数（10>4）
- 调整 channel-width
  - 1x
  - 0.5x
  - 0.25x

| Name                | Input quantization | Weight quantization | Channel Width | Dataset    | Top1 accuracy |
| ------------------- | ------------------ | ------------------- | ------------- | ---------- | ------------- |
| MASK_1W1A(CNV_1W1A) | 1 bit              | 1 bit               | 1 x           | MaskedFace | 99.15%        |
| MASK_1W1A_0.5       | 1 bit              | 1 bit               | 0.5 x         | MaskedFace | 97.84%        |
| MASK_1W1A_0.25      | 1 bit              | 1 bit               | 0.25 x        | MaskedFace | 93.37%        |

## 准备

1. 下载数据集，将解压的文件放到 ./data 路径下

   链接: https://pan.baidu.com/s/1F9XYCaUo3M5ZWB7PvZRQAQ 提取码: maa1

2. 下载预训练权重 chkpt，将解压的文件放到 ./experiment 路径下

   链接: https://pan.baidu.com/s/12X_Wiy4zK8wom4YJoY3kyw 提取码: qqn2

## Eval & Train

1. Eval

​		brevitas_bnn_pynq_train --evaluate --network mask_1w1a --resume /path/to/checkpoint.tar

2. Train

​		brevitas_bnn_pynq_train --network mask_1w1a --experiments /path/to/experiments

---

---

---

# 参考 repo

基于brevitas的量化感知训练

https://github.com/Xilinx/brevitas/tree/master/src/brevitas_examples/bnn_pynq

## BNN-PYNQ Brevitas experiments

This repo contains training scripts and pretrained models to recreate the LFC and CNV models
used in the [BNN-PYNQ](https://github.com/Xilinx/BNN-PYNQ) repo using [Brevitas](https://github.com/Xilinx/brevitas).
These pretrained models and training scripts are courtesy of 
[Alessandro Pappalardo](https://github.com/volcacius) and [Ussama Zahid](https://github.com/ussamazahid96).

### Experiments

| Name     | Input quantization           | Weight quantization | Activation quantization | Dataset       | Top1 accuracy |
|----------|------------------------------|---------------------|-------------------------|---------------|---------------|
| TFC_1W1A | 1 bit                        | 1 bit               | 1 bit                   |  MNIST        |    93.17%     |
| TFC_1W2A | 2 bit                        | 1 bit               | 2 bit                   |  MNIST        |    94.79%     |
| TFC_2W2A | 2 bit                        | 2 bit               | 2 bit                   |  MNIST        |    96.60%     |
| SFC_1W1A | 1 bit                        | 1 bit               | 1 bit                   |  MNIST        |    97.81%     |
| SFC_1W2A | 2 bit                        | 1 bit               | 2 bit                   |  MNIST        |    98.31%     |
| SFC_2W2A | 2 bit                        | 2 bit               | 2 bit                   |  MNIST        |    98.66%     |
| LFC_1W1A | 1 bit                        | 1 bit               | 1 bit                   |  MNIST        |    98.88%     |
| LFC_1W2A | 2 bit                        | 1 bit               | 2 bit                   |  MNIST        |    98.99%     |
| CNV_1W1A | 8 bit                        | 1 bit               | 1 bit                   |  CIFAR10      |    84.22%     |
| CNV_1W2A | 8 bit                        | 1 bit               | 2 bit                   |  CIFAR10      |    87.80%     |
| CNV_2W2A | 8 bit                        | 2 bit               | 2 bit                   |  CIFAR10      |    89.03%     |

### Train

A few notes on training:
- An experiments folder at */path/to/experiments* must exist before launching the training.
- Set training to 1000 epochs for 1W1A networks, 500 otherwise. 
- Enabling the JIT with the env flag BREVITAS_JIT=1 significantly speeds up training.

To start training a model from scratch, e.g. LFC_1W1A, run:
 ```bash
BREVITAS_JIT=1 brevitas_bnn_pynq_train --network LFC_1W1A --experiments /path/to/experiments
 ```

### Evaluate

To evaluate a pretrained model, e.g. LFC_1W1A, run:
 ```bash
BREVITAS_JIT=1 brevitas_bnn_pynq_train --evaluate --network LFC_1W1A --pretrained
 ```

To evaluate your own checkpoint, of e.g. LFC_1W1A, run:
 ```bash
BREVITAS_JIT=1 brevitas_bnn_pynq_train --evaluate --network LFC_1W1A --resume /path/to/checkpoint.tar
 ```

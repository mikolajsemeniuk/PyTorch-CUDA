# PyTorch-CUDA
Installation of PyTorch with CUDA toolkit
### Links:
* [Visual Studio Community 2019](https://visualstudio.microsoft.com/)
* [CUDA Toolkit 11.3](https://developer.nvidia.com/cuda-11.3.0-download-archive?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exe_local)
* [PyTorch - Stable (1.10)](https://pytorch.org/)
### Steps to reproduce
remember to run inside `ANACONDA Prompt (miniconda3)`
```sh
conda create -n torch_cuda python=3.9
conda activate torch_cuda
conda env list
conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch
python main.py
```

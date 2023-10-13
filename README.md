# Fine Tuning Falcon40b

## License
This template is licensed to Customer subject to the terms of the license agreement between Domino and the Customer on file.

## About this project
This reference project shows how to fine tune the Falcon-40b on a [dataset](https://huggingface.co/datasets/samsum) to summarize conversations using the Huggingface Trainer. In this project, we will use the 4bit and 8bit quantized version of the model and train a LoRA adapter. We used a `g4dn.12xlarge` AWS instance to train the model.

Here is a list of important files in the project that you might need to edit in order to customize this further for your use case.

*hf_falcon_40b-4bit.ipynb* : This file contains all the code to load and finetune the Falcon-40B model on the [samsum](https://huggingface.co/datasets/samsum) dataset. The bitsandbytes configuration loads the model in 4 bit and trains a LoRA adapter

*hf_falcon_40b-8bit.ipynb* : This file contains all the code to load and finetune the Falcon-40B model on the [samsum](https://huggingface.co/datasets/samsum) dataset. The bitsandbytes configuration loads the model in 8 bit and trains a LoRA adapter

*generate-4bit.ipynb* : This file contains code to load the Falcon-40B model in 4 bit precision, add an adapter to the model and take a user prompt to generate an output

*generate-4bit.ipynb* : This file contains code to load the Falcon-40B model in 8 bit precision, add an adapter to the model and take a user prompt to generate an output

*save_8_bit.ipynb* : This file saves the Falcon-40B model in 8 bit to disc so it can be used in future runs without having to download the model again from the Huggingface Hub. If you are using a model saved to disc, please change the value of the `model_id` variable in the `hf_falcon_40b-4bit.ipynb` and `hf_falcon_40b-4bit.ipynb` notebooks to point to the location of the model on disc.

The functions in the notebooks can be parameterized to work with either the 4 bit or 8 bit versions of the models but have been provided as separate notebooks for convinience. 


## Setup instructions

This project requires the following [compute environments](https://docs.dominodatalab.com/en/latest/user_guide/f51038/environments/) to be present. Also please ensure the [‘Automatically make compatible with Domino’](https://docs.dominodatalab.com/en/latest/user_guide/4e0c34/create-a-domino-environment-with-a-pre-built-image/) checkbox is selected and create the environment afresh instead of duplicating an existing environment that does not use the same base image and dependencies.


### hf-falcon-40b
**Environment Base** 

```nvcr.io/nvidia/pytorch:23.06-py3```

**Dockerfile Instructions**

```
# System-level dependency injection runs as root
USER root:root

# Validate base image pre-requisites
# Complete requirements can be found at
# https://docs.dominodatalab.com/en/latest/user_guide/a00d1b/automatic-adaptation-of-custom-images/#_pre_requisites_for_automatic_custom_image_compatibility_with_domino
RUN /opt/domino/bin/pre-check.sh

# Configure /opt/domino to prepare for Domino executions
RUN /opt/domino/bin/init.sh

# Validate the environment
RUN /opt/domino/bin/validate.sh

RUN pip uninstall -y protobuf && \
    pip install \
    "protobuf==3.20.3" \
    -q -U \
    bitsandbytes==0.39.1 \
    "datasets>=2.10.0,<3" \
    ipywidgets \
    py7zr \
    einops \
    tensorboardX \
    git+https://github.com/huggingface/transformers.git@850cf4af0ce281d2c3e7ebfc12e0bc24a9c40714 \
    git+https://github.com/huggingface/peft.git@e2b8e3260d3eeb736edf21a2424e89fe3ecf429d \
    git+https://github.com/huggingface/accelerate.git@b76409ba05e6fa7dfc59d50eee1734672126fdba

RUN pip uninstall -y apex
```
Don't forget to expose the relevant IDEs as pluggable workspaces, as described in the [Domino Documentation](https://docs.dominodatalab.com/en/latest/user_guide/03e062/add-workspace-ides/).

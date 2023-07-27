*Disclaimer - Domino Reference Projects are starter kits built by Domino researchers. They are not officially supported by Domino. Once loaded, they are yours to use or modify as you see fit. We hope they will be a beneficial tool on your journey!

# reference-project-finetune-falcon40b
This reference project shows how to fine tune the Falcon-40b on a [dataset](https://huggingface.co/datasets/samsum) to summarize conversations using the Huggingface Trainer. In this project, we will use the 4bit and 8bit quantized version of the model and train a LoRA adapter. We used a `g4dn.12xlarge` AWS instance to train the model.

Here are a list of important files in the project that you might need to edit in order to customize this further for your use case.

*[hf_falcon_40b-4bit.ipynb](hf_falcon_40b-4bit.ipynb) : This file contains all the code to load and finetune the Falcon-40B model on the [samsum](https://huggingface.co/datasets/samsum) dataset. The bitsandbytes configuration loads the model in 4 bit and trains a LoRA adapter
*[hf_falcon_40b-8bit.ipynb](hf_falcon_40b-8bit.ipynb) : This file contains all the code to load and finetune the Falcon-40B model on the [samsum](https://huggingface.co/datasets/samsum) dataset. The bitsandbytes configuration loads the model in 8 bit and trains a LoRA adapter
*[generate-4bit.ipynb](generate-4bit.ipynb) : This file contains code to load the Falcon-40B model in 4 bit precision, add an adapter to the model and take a user prompt to generate an output
*[generate-4bit.ipynb](generate-8bit.ipynb) : This file contains code to load the Falcon-40B model in 8 bit precision, add an adapter to the model and take a user prompt to generate an output
*[save_8_bit.ipynb](save_8_bit.ipynb) : This file saves the Falcon-40B model in 8 bit to disc so it can be used in future runs without having to download the model again from the Huggingface Hub. If you are using a model saved to disc, please change the value of the `model_id` variable in the `hf_falcon_40b-4bit.ipynb` and `hf_falcon_40b-4bit.ipynb` notebooks to point to the location of the model on disc.

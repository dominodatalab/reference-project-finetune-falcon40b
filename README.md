*Disclaimer - Domino Reference Projects are starter kits built by Domino researchers. They are not officially supported by Domino. Once loaded, they are yours to use or modify as you see fit. We hope they will be a beneficial tool on your journey!

# reference-project-finetune-falcon40b
This reference project shows how to fine tune the Falcon-40b on a [dataset](https://huggingface.co/datasets/samsum) to summarize conversations using the Huggingface Trainer. In this project, we will use the 4bit and 8bit quantized version of the model and train a LoRA adapter. We used a `g4dn.12xlarge` AWS instance to train the model.

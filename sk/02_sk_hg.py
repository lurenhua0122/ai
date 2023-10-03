import semantic_kernel as sk
from semantic_kernel.connectors.ai.hugging_face import HuggingFaceTextCompletion

kernel = sk.Kernel()

kernel.add_text_completion_service("huggingface", HuggingFaceTextCompletion("gpt2", task="text-generation"))

print("You made an open source kernel using an open source AI model!")
import sys
from llama_cpp import Llama
from transformers import LlamaModel, LlamaConfig
import os



home_dir=os.path.expanduser("~")
print(home_dir)
configuration = LlamaConfig()


input_str = sys.stdin.read()

llm = Llama(model_path=f"{home_dir}/AI/models/ggml-model-q4_1.bin")

try:
    output = llm(f"Q: {input_str}A: ", max_tokens=256, stop=["Q:", "\n"], echo=True)
except AttributeError as e:
    print(e)
    print("Maybe you not have a model, please download model and put in \
          '~/AI/models' directory")
    exit()
print(output.get("choices")[0].get("text"))
# print(output)

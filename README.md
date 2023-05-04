# Ask Llama for a voice

## Introduction

The program who decode you voice and send query to llama model via alpaca_cpp, after this show answer in tkinter window.

## Requirements

- Linux
- [wihsper](https://github.com/openai/whisper)
- llama_cpp for Python
- ggml model for llama_cpp 
- Festival TTS

## Installation

1. Install whisper
2. Download llama ggml model for llama_cpp for example this https://huggingface.co/Pi3141/alpaca-lora-30B-ggml/tree/main and put to '$HOME_DIR/AI/models'
3. Select size languge model in main file ask_cli.py (default is medium) in line 91 (MODEL parametr)
4. Setup decode language in ask_cli.py in function decode() line 64

## Usage

Start programm in shell "python ask_cli.py" and wait voice sounde from file "im_listen.txt" ask anything and wait result.
I bind 8'th button mouse via xbindkeys, and ask Llama very easy.
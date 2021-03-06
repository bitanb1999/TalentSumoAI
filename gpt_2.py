# -*- coding: utf-8 -*-
"""GPT-2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1b359TZHn6DmG2Ap8qeKvzssjfRgwEykk
"""

def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)


install_and_import('transformers[tf-cpu]')
install_and_import('tensorflow')

#for reproducability
SEED = 34

#maximum number of words in output text
MAX_LEN = 70

"""###I. Intro
A language model is a machine learning model that can look at part of a sentence and predict the next word/sequence of words. Much like the autofill features on your iPhone/Android, GPT-2 is capable of next word prediction on a much larger and more sophisticated scale. For reference, the smallest available GPT-2 has 117 million parameters, whereas the largest one (invisible to the public) has over 1.5 billion parameters. The largest one available for public use is half the size of their main GPT-2 model

😊 Transformers makes it very easy to import this model with both PyTorch and TensorFlow - in this notebook we will be using TensorFlow but it is just as easy in PyTorch. Both the model and its Tokenizer can be imported from the transformers library that anyone can get by typing !pip install transformers. Let's see just how simple it is to generate text with a neural network. We begin with our input sequence:
"""

input_sequence = "I am enthusiastic,diligent and hardowking. I am very passionate about my work and am a very good communicator. I "

#get transformers
from transformers import TFGPT2LMHeadModel, GPT2Tokenizer

#get large GPT2 tokenizer and GPT2 model
tokenizer = GPT2Tokenizer.from_pretrained("gpt2-large")
GPT2 = TFGPT2LMHeadModel.from_pretrained("gpt2-large", pad_token_id=tokenizer.eos_token_id)
GPT2.summary()

#get deep learning basics
import tensorflow as tf
tf.random.set_seed(SEED)

# encode context the generation is conditioned on
input_ids = tokenizer.encode(input_sequence, return_tensors='tf')
# set return_num_sequences > 1
beam_outputs = GPT2.generate(
    input_ids, 
    max_length = MAX_LEN, 
    num_beams = 5, 
    no_repeat_ngram_size = 2, 
    num_return_sequences = 5, 
    early_stopping = True
)

print('')
print("Output:\n" + 50 * '-')

# now we have 3 output sequences
for i, beam_output in enumerate(beam_outputs):
      print("{}: {}".format(i, tokenizer.decode(beam_output, skip_special_tokens=True)))

# use temperature to decrease the sensitivity to low probability candidates
sample_output = GPT2.generate(
                             input_ids, 
                             do_sample = True, 
                             max_length = MAX_LEN, 
                             top_k = 0, 
                             temperature = 0.8
)

print("Output:\n" + 100 * '-')
print(tokenizer.decode(sample_output[0], skip_special_tokens = True))

#sample only from 80% most likely words
sample_output = GPT2.generate(
                             input_ids, 
                             do_sample = True, 
                             max_length = MAX_LEN, 
                             top_p = 0.8, 
                             top_k = 0
)

print("Output:\n" + 100 * '-')
print(tokenizer.decode(sample_output[0], skip_special_tokens = True), '...')

#combine both sampling techniques
sample_outputs = GPT2.generate(
                              input_ids,
                              do_sample = True, 
                              max_length = 2*MAX_LEN,                              #to test how long we can generate and it be coherent
                              #temperature = .7,
                              top_k = 50, 
                              top_p = 0.85, 
                              num_return_sequences = 5
)

print("Output:\n" + 100 * '-')
for i, sample_output in enumerate(sample_outputs):
    print("{}: {}...".format(i, tokenizer.decode(sample_output, skip_special_tokens = True)))
    print('')

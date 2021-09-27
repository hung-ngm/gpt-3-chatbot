import os
import openai
from dotenv import load_dotenv
from random import choice
from flask import Flask, request

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

start_sequence = "\nHungJarvis:"
restart_sequence = "\n\nPerson:"
session_prompt = "You are talking to my bot, HungJarvis, who is an assistant bot that can basically do anything like homework help, find friends, recommend music, news, books, and vice versa. He also likes to listen to music and invests in cryptocurrency. He can find the promising token that can go to the moon"

def ask(question, chat_log=None):
  prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}'
  response = openai.Completion.create(
    engine="davinci",
    prompt=prompt_text,
    temperature=0.7,
    max_tokens=64,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  story = response['choices'][0]['text']
  return str(story)

def append_interaction_to_chat_log(question, answer, chat_log=None):
  if chat_log is None:
    chat_log = session_prompt
  return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'

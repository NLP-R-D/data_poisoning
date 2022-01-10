#!/usr/bin/env python

import numpy as np
from sklearn.model_selection import train_test_split

__all__ = ['extract_result', 'tts_dataset']

def extract_result(result):
  rstr = 'Accuracy:\n'
  rstr += f"TorchMetrics: {result[0]['tm_accuracy']*100:0.2f}%\n"
  rstr += f"Sklearn: {result[0]['sk_accuracy']*100:0.2f}%\n"
  rstr += '*'*40
  rstr += '\n'
  rstr += 'Recall:\n'
  rstr += f"TorchMetrics: {result[0]['tm_recall']*100:0.2f}%\n"
  rstr += f"Sklearn: {result[0]['sk_recall']*100:0.2f}%\n"
  rstr += '*'*40
  rstr += '\n'
  rstr += 'Precision:\n'
  rstr += f"TorchMetrics: {result[0]['tm_precision']*100:0.2f}%\n"
  rstr += f"Sklearn: {result[0]['sk_precision']*100:0.2f}%\n"
  rstr += '*'*40
  rstr += '\n'
  rstr += 'F1:\n'
  rstr += f"TorchMetrics: {result[0]['tm_f1']*100:0.2f}%\n"
  rstr += f"Sklearn: {result[0]['sk_f1']*100:0.2f}%\n"
  
  return rstr

def tts_dataset(ds, split_pct=0.2, seed=None):
  train_idxs, val_idxs = train_test_split(np.arange(len(ds)), test_size=split_pct, random_state=seed)
  return ds.select(train_idxs), ds.select(val_idxs)
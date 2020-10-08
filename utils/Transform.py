from PIL import Image
import os
import os.path
import torch.utils.data
import torchvision.transforms as transforms
import numpy as np
import torch

from utils.randaugment import RandAugment

class TransformFix(object):
    def __init__(self, imResize, imsize, mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5]):
        
        self.none = transforms.Compose([
            transforms.Resize(imResize),
            transforms.CenterCrop(imsize),
            transforms.ToTensor(),
            transforms.Normalize(mean=mean, std=std),
            ])
        
        self.weak = transforms.Compose([
            transforms.Resize(imResize),
            transforms.CenterCrop(imsize),
            transforms.RandomHorizontalFlip(),
            transforms.RandomVerticalFlip(),
            transforms.ToTensor(),
            transforms.Normalize(mean=mean, std=std),
            ])

        self.strong = transforms.Compose([
            transforms.Resize(imResize),
            transforms.CenterCrop(imsize),
            transforms.RandomHorizontalFlip(),
            transforms.RandomVerticalFlip(),
            RandAugment(n=2, m=10),
            transforms.ToTensor(),
            transforms.Normalize(mean=mean, std=std)
            ])
    
    def __call__(self):
        weak = self.weak
        strong = self.strong
        none = self.none
        return none, weak, strong
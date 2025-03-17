import torch
import torchvision.transforms as T

def get_augmentations(train: bool = True) -> T.Compose:
    trans = []
    trans.append(T.Resize((224, 224)))
    if train:
        trans.append(T.RandomHorizontalFlip(p=0.5))
    trans.append(T.ToTensor())
    trans.append(T.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5]))
    transforms = T.Compose(trans)
    return transforms
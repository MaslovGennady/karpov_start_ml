import torch
import torchvision.models as models

def get_pretrained_model(model_name: str, num_classes: int, pretrained: bool = True):
    if model_name == 'alexnet':
        model = models.alexnet(pretrained=pretrained)
        model.classifier[6] = torch.nn.Linear(model.classifier[6].in_features, num_classes)
    elif model_name == 'vgg11':
        model = models.vgg11(pretrained=pretrained)
        model.classifier[6] = torch.nn.Linear(model.classifier[6].in_features, num_classes)
    elif model_name == 'googlenet':
        model = models.googlenet(pretrained=pretrained)
        # Изменение выходного слоя для основного выхода
        model.fc = torch.nn.Linear(model.fc.in_features, num_classes)
        # Изменение выходных слоев для вспомогательных выходов
        if hasattr(model, 'aux_logits') and model.aux_logits:
            model.aux1 = models.googlenet.InceptionAux(512, num_classes, dropout=0.7)# torch.nn.Linear(1024, num_classes)
            model.aux2 = models.googlenet.InceptionAux(528, num_classes, dropout=0.7)# torch.nn.Linear(1024, num_classes)   
    elif model_name == 'resnet18':
        model = models.resnet18(pretrained=pretrained)
        model.fc = torch.nn.Linear(model.fc.in_features, num_classes)
    else:
        raise ValueError("Model name not recognized. Please choose from 'alexnet', 'vgg11', 'googlenet', or 'resnet18'.")
    
    return model
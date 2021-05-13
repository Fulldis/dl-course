from engine import Tensor, Value
import numpy as np


class Module:
    """
    Base class for every layer.
    """

    def forward(self, *args, **kwargs):
        """Depends on functionality"""
        pass

    def __call__(self, *args, **kwargs):
        """For convenience we can use model(inp) to call forward pass"""
        return self.forward(*args, **kwargs)

    def parameters(self):
        """Return list of trainable parameters"""
        return []


class Linear(Module):
    def __init__(self, in_features, out_features, bias: bool = True):
        """Initializing model"""
        # Create Linear Module

    def forward(self, inp):
        """Y = W * x + b"""
        return ...

    def parameters(self):
        # return 1-d list of all parameters List[Value]
        return ...


class ReLU(Module):
    """The most simple and popular activation function"""

    def forward(self, inp):
        # Create ReLU Module
        return ...


class CrossEntropyLoss(Module):
    """Cross-entropy loss for multi-class classification"""

    def forward(self, inp, label):
        # Create CrossEntropy Loss Module
        return ...

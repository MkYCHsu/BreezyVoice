"""Placeholder for the project's conditional flow model implementation."""

import torch.nn as nn


class ConditionalCFM(nn.Module):
    """Extension point for the project's future conditional flow model."""

    def __init__(self, *args, **kwargs):
        super().__init__()
        raise NotImplementedError(
            "ConditionalCFM is a placeholder. Implement your model here."
        )

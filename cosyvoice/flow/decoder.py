"""Placeholder for the project's conditional decoder implementation."""

import torch.nn as nn


class ConditionalDecoder(nn.Module):
    """Extension point for the project's future conditional decoder."""

    def __init__(self, *args, **kwargs):
        super().__init__()
        raise NotImplementedError(
            "ConditionalDecoder is a placeholder. Implement your model here."
        )

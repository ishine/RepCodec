import torch.nn as nn

from model.layers.conv_layer import Conv1d, Conv1d1x1


class ResidualUnit(nn.Module):
    def __init__(
            self,
            in_channels: int,
            out_channels: int,
            kernel_size=3,
            dilation=1,
            bias=False,
            nonlinear_activation="ELU",
            nonlinear_activation_params={},
    ):
        super().__init__()
        self.activation = getattr(nn, nonlinear_activation)(**nonlinear_activation_params)
        self.conv1 = Conv1d(
            in_channels=in_channels,
            out_channels=out_channels,
            kernel_size=kernel_size,
            stride=1,
            dilation=dilation,
            bias=bias,
        )
        self.conv2 = Conv1d1x1(out_channels, out_channels, bias)

    def forward(self, x):
        y = self.conv1(self.activation(x))
        y = self.conv2(self.activation(y))
        return x + y
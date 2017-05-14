# draw_convnet

Python script for illustrating Convolutional Neural Network (ConvNet)

## Example image
![](https://raw.githubusercontent.com/gwding/draw_convnet/master/convnet_fig.png)

## Known issues
`Line2D` doesn't seem to work well under `python3 + matplotlib 2.0.0` as pointed out by @ahoereth 

The solution is to use follow these instructions.
```
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements_python3.txt
```

## Using the code
It is NOT required to cite anything to use the code.

If you are not facing space limitation and it does not break the flow of the paper, you might consider adding something like "This figure is generated by adapting the code from https://github.com/gwding/draw_convnet" (maybe in the footnote).

FYI, originally I used the code to generate the convnet figure in this paper "Automatic moth detection from trap images for pest management".
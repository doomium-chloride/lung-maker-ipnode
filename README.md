## Lung maker

### What is this

This is a python script that can construct a lung using 3 weights

### How does it construct a lung using weights

This is based on PCA

### What are weights

They are a like a coordinate transformation that's made from doing the PCA

This one uses 3 weights

### How to use

This is a command line program
The weights are mandatory arguments, the filename prepend is optional

```shell
python lung-maker.py <weight 1> <weight 2> <weight 3> [filename prepend]
```

### Examples

to generate an ipnode with the weights 0,0,0
files generated will be called "left-0-0-0.ipnode" and "right-0-0-0.ipnode"

```shell
python lung-maker.py 0 0 0
```

to generate an ipnode with the weights 1,2,-3
files generated will be called "left-1-2--3.ipnode" and "right-1-2--3.ipnode"

```shell
python lung-maker.py 1 2 -3
```

to generate an ipnode with the weights 0.5 -1 0 with the filename starting with "bob"
files generated will be called "bob-left-0.5--1-0.ipnode" and "bob-right-0.5--1-0.ipnode"

```shell
python lung-maker.py 0.5 -1 0 bob
```
# ASCII IMAGE

This is an open source project to convert any image into an `ASCII Art`.

# Getting started

## Cloning/Downloading

To use this program, either download the repository or clone using

```
$ https://github.com/ivanrj7j/Ascii-Image.git
```

After downloading/cloning the repo, go to the directory by

```
$ cd Ascii-Image
```

## Getting Dependencies

### Python

If you are using normal Python

```
$ pip install -r requirements.txt
```

### Anaconda

If you are using anaconda

```
$ conda env create -f environment.yml
```

# Usage

To use the application,

```
$ python main.py -i "<input image location>" -c <chunk size> -o "<output path>"
```

## Arguments:

- `--inp`/`-i`: The File location of the image to be converted to ascii art, this field must be specified
- `[OPTIONAL]` `--chunk`/`-c`: The size of the chunk, default is `10`. `Lower` the parameter, the higher the resolution.
- `[OPTIONAL]` `--out`/`-o`: The output path of the image, default is `out.png`
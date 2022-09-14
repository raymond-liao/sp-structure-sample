# sp-structure-sample

Automation Web UI Test structure sample of [chromium](https://www.chromium.org/)
and [pytest](https://docs.pytest.org/en/latest/)

## Environment

* macOS: 10.0.0 above
* pip: 20.0.2
* Virtual ENV: pipenv, version 2022.9.8
* Language: python 3.7.5
* Chrome: Version 105.0.5195.102 (Official Build)
* Firefox: 73.0.1 (64 bit)

# Setup

1. Install [python](https://www.python.org/) on your machine, [pip](https://pypi.org/project/pip/) will be installed
   with this python installation；
2. Install [pipenv](https://github.com/pypa/pipenv);
3. Copy file `chromedriver` and `geckodriver` to `/usr/local/bin`;

docker run -d -p 4444:4444 -p 7900:7900 --shm-size="2g" selenium/standalone-firefox:4.4.0-20220831
docker run -d -p 4444:4444 --shm-size="2g" selenium/standalone-chrome:4.4.0-20220831

# Manual

1. Enter the pipenv:

```shell
$ pipenv shell
```

2. Install the requirements libraries:

```shell
$ pipenv install
```

3. Run test:

```shell
$ python main.py
```

## License

`sp-structure-sample` is avaliable under the MIT license. See
the [LICENSE](https://github.com/gaoshanyu/sp-structure-sample/master/LICENSE) file for more info.

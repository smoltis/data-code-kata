
## Problem 1 - Solution

#### Build Docker image
```bash
docker build -t data-code-kata-stan .
```

#### Run tests
```bash
docker run -it --rm data-code-kata-stan pytest
```

#### Run linter
```bash
docker run -it --rm data-code-kata-stan flake8
```

#### Get usage help
```bash
docker run -it --rm data-code-kata-stan python generate.py -h
docker run -it --rm data-code-kata-stan python parse.py -h
```

#### Run the app

The commands below must be executed in Bash CLI (tested on OSX 10.15.6, Docker Desktop 2.3.0.4).

##### Generate FWF file 
* with random alphanumeric characters 
* with 1501 lines incl. the header
* using spec.json in the current dir
* produces FWF named fixed.txt in the current dir

```bash
docker run -it --rm -v $(pwd):/out data-code-kata-stan python generate.py -r -s /out/spec.json -n 1500 -o /out/fixed.txt
```

##### Parse FWF file, produce CSV
* takes fixed.txt in the current dir
* using spec.json in the current dir
* produces CSV named delimited.csv in the current dir

```bash
docker run -it --rm -v $(pwd):/out data-code-kata-stan python parse.py -i /out/fixed.txt -s /out/spec.json -o /out/delimited.csv
```
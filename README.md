# flask algo analyzer

a simple flask api that visualizes time complexity of sorting and search algorithms.

## setup

```bash
git clone https://github.com/owizdom/cool-analyzer-in-Flask.git
cd cool-analyzer-in-Flask
pip install flask numpy matplotlib
python app.py
```

## usage

```
get /analyze?algo=bubble&n=200&steps=20
```

**params:**
- `algo` - bubble, linear, binary, nested
- `n` - max elements
- `steps` - increment size

returns json with execution time and base64 graph.

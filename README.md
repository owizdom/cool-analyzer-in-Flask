# Time Complexity Visualizer

A Flask-based REST API that visualizes the time complexity of various sorting and search algorithms. The application executes algorithms with increasing input sizes, measures execution time, and returns a JSON response containing performance metrics and a Base64-encoded graph.

## Features

- **Algorithms Supported:** Bubble Sort, Linear Search, Binary Search, Nested Loops.
- **Dynamic Analysis:** Configurable input size (n) and step values via query parameters.
- **Visualization:** Generates a real-time performance graph using Matplotlib.
- **API Output:** Returns JSON data including execution time and the graph image.

## Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/menes-ux/flask-algo-analyzer.git](https://github.com/menes-ux/flask-algo-analyzer.git)
   cd flask-algo-analyzer

2. Create a virtual environment:
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Mac/Linux
   python3 -m venv venv
   source venv/bin/activate

3. Install dependencies:
```bash
    pip install flask numpy matplotlib

The server will run locally at http://127.0.0.1:3000.

## API Documentation

### Analyze Algorithm

**Endpoint:**  
`GET /analyze`

#### Query Parameters

- **algo** (`string`): The algorithm to test.  
  Options: `bubble`, `linear`, `binary`, `nested`  
  Default: `bubble`

- **n** (`int`): The maximum number of elements to process.  
  Default: `500`

- **steps** (`int`): The step increment for input sizes.  
  Default: `10`

#### Example Request

[http://127.0.0.1:3000/analyze?algo=bubble&n=200&steps=20](http://127.0.0.1:3000/analyze?algo=bubble&n=200&steps=20)

#### Example Response

```json
{
  "algorithm": "bubble",
  "n_elements": 200,
  "step_value": 20,
  "total_analysis_time_seconds": 0.45,
  "image_base64": "iVBORw0KGgoAAAANSUhEUgAA..."
}

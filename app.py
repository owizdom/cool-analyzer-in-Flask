from flask import Flask, request, jsonify
import time
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Important: This makes matplotlib work without a pop-up window
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

# --- The Algorithms (Copied from your class activity) ---
def bubble_sort(n):
    arr = np.random.randint(0, 100, n)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def linear_search(n):
    for i in range(n):
        if i == n-1: return i

def binary_search(n):
    # Binary search runs on sorted arrays, so we don't count sort time
    arr = list(range(n)) 
    target = -1 # Worst case
    left, right = 0, n - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target: return mid
        elif arr[mid] < target: left = mid + 1
        else: right = mid - 1

def nested_loops(n):
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1

# Map names to functions
ALGORITHMS = {
    "bubble": bubble_sort,
    "linear": linear_search,
    "binary": binary_search,
    "nested": nested_loops
}

@app.route('/analyze')
def analyze():
    # 1. Get Query Parameters
    algo_name = request.args.get('algo', 'bubble')
    n_max = int(request.args.get('n', 500))
    step = int(request.args.get('steps', 10))

    if algo_name not in ALGORITHMS:
        return jsonify({"error": "Unknown algorithm. Use bubble, linear, binary, or nested"}), 400

    selected_algo = ALGORITHMS[algo_name]

    # 2. Run the Analysis
    input_sizes = list(range(10, n_max + 1, step))
    times = []
    
    analysis_start = time.time()
    
    for n in input_sizes:
        start_t = time.time()
        selected_algo(n)
        end_t = time.time()
        times.append(end_t - start_t)

    analysis_end = time.time()
    total_analysis_time = analysis_end - analysis_start

    # 3. Generate the Graph
    plt.figure(figsize=(10, 6))
    plt.plot(input_sizes, times, 'o-', label=algo_name)
    plt.title(f'Time Complexity: {algo_name}')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.legend()

    # 4. Save Graph to Base64 String
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()

    # 5. Return JSON Response
    return jsonify({
        "algorithm": algo_name,
        "n_elements": n_max,
        "step_value": step,
        "total_analysis_time_seconds": total_analysis_time,
        "image_base64": graph_url
    })

if __name__ == '__main__':
    # Run on port 3000 as requested
    app.run(port=3000, debug=True)
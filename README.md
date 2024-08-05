# 3D GLTF/GLB Viewer

This is a Streamlit-based web application that allows users to upload and visualize 3D models in GLTF and GLB formats. The application uses `trimesh` to load and parse the 3D models and `plotly` to render the 3D visualizations.

![demo](demo/demo.gif)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/codemaker2015/3d-viewer-python.git
    cd 3d-viewer-python
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate # On Ubuntu
    venv\Scripts\activate    # On Windows
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running the App Locally

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. Open your web browser and navigate to `http://localhost:8501`.

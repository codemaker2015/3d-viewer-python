import streamlit as st
import plotly.graph_objects as go
import trimesh
import numpy as np
import os

def load_gltf(file_path):
    try:
        # Load the GLTF/GLB file using trimesh
        scene = trimesh.load(file_path)
        
        # Initialize lists for vertices and faces
        all_vertices = []
        all_faces = []
        
        # Check if the scene has a geometry
        if isinstance(scene, trimesh.Scene):
            for name, geom in scene.geometry.items():
                vertices = geom.vertices
                faces = geom.faces
                all_vertices.append(vertices)
                all_faces.append(faces)
        
        # Stack vertices and faces to form a single mesh
        if len(all_vertices) > 0:
            vertices = np.vstack(all_vertices)
            faces = np.vstack(all_faces)
        else:
            vertices = np.array([])
            faces = np.array([])

        return vertices, faces
    except Exception as e:
        st.error(f"Error loading file: {e}")
        return np.array([]), np.array([])

def create_3d_plot(vertices, faces):
    if vertices.size == 0 or faces.size == 0:
        return go.Figure()

    fig = go.Figure(
        data=[
            go.Mesh3d(
                x=vertices[:, 0],
                y=vertices[:, 1],
                z=vertices[:, 2],
                i=faces[:, 0],
                j=faces[:, 1],
                k=faces[:, 2],
                opacity=0.5,
                color='lightblue'
            )
        ]
    )
    
    fig.update_layout(
        scene=dict(
            aspectmode='data',
            xaxis=dict(title='X-axis'),
            yaxis=dict(title='Y-axis'),
            zaxis=dict(title='Z-axis'),
        )
    )
    return fig

def display_metadata(vertices, faces):
    st.sidebar.header("Model Metadata")
    st.sidebar.write(f"Number of vertices: {vertices.shape[0]}")
    st.sidebar.write(f"Number of faces: {faces.shape[0]}")

def main():
    st.title('Enhanced 3D Viewer for GLTF/GLB Files')
    
    uploaded_file = st.file_uploader("Upload a GLTF or GLB file", type=["glb", "gltf"])
    
    if uploaded_file is not None:
        if not os.path.exists("temp"):
            os.makedirs("temp")
        
        file_path = os.path.join("temp", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        vertices, faces = load_gltf(file_path)
        
        if vertices.size > 0 and faces.size > 0:
            display_metadata(vertices, faces)
            fig = create_3d_plot(vertices, faces)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.error("Failed to load the model. Please check the file and try again.")

if __name__ == "__main__":
    main()

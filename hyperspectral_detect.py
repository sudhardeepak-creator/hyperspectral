import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn import datasets

# Hyperspectral image simulation (replace with your hyperspectral data)
# For demonstration purposes, we'll use sklearn's dataset or generate random data.
# Hyperspectral images have many bands (channels), typically in the hundreds.
# Here we simulate a hyperspectral image with 100 pixels (samples) and 200 features (bands).
n_samples = 100  # Number of pixels (samples)
n_bands = 200    # Number of bands (features)

# Generate a random hyperspectral image dataset (replace this with actual data)
X = np.random.rand(n_samples, n_bands)  # Hyperspectral image data

# Step 1: Standardize the data (important for PCA)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 2: Apply PCA for dimensionality reduction
n_components = 50  # Reduce the data to 50 components
pca = PCA(n_components=n_components)
X_pca = pca.fit_transform(X_scaled)

# Step 3: Visualize the variance explained by each principal component
explained_variance_ratio = pca.explained_variance_ratio_

# Plot the explained variance ratio for each principal component
plt.figure(figsize=(8, 6))
plt.plot(range(1, n_components + 1), explained_variance_ratio, marker='o', linestyle='--', color='b')
plt.title("Explained Variance by Each Principal Component")
plt.xlabel("Principal Component")
plt.ylabel("Explained Variance Ratio")
plt.grid(True)
plt.show()

# Step 4: Visualizing the reduced data (optional)
# If you reduce to 2D (n_components=2), you can visualize the data
if n_components == 2:
    plt.scatter(X_pca[:, 0], X_pca[:, 1], c='r', edgecolors='k', s=50)
    plt.title('PCA of Hyperspectral Image')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.grid(True)
    plt.show()

# Output reduced data (X_pca) and the explained variance ratio
print("Reduced Data Shape:", X_pca.shape)
print("Explained Variance Ratio:", explained_variance_ratio)

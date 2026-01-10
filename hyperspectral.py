import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from scipy.io import loadmat
import urllib.request
import zipfile
import tempfile

def download_and_extract_dataset():
    """Download and extract the Indian Pines dataset with proper error handling"""
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()
    data_dir = os.path.join(temp_dir, 'IndianPines')
    os.makedirs(data_dir, exist_ok=True)
    
    # Download the dataset from a reliable source
    data_url = "https://www.ehu.eus/ccwintco/uploads/6/67/Indian_pines_corrected.mat"
    gt_url = "https://www.ehu.eus/ccwintco/uploads/c/c4/Indian_pines_gt.mat"
    
    try:
        print("Downloading dataset files...")
        urllib.request.urlretrieve(data_url, os.path.join(data_dir, 'Indian_pines_corrected.mat'))
        urllib.request.urlretrieve(gt_url, os.path.join(data_dir, 'Indian_pines_gt.mat'))
        print("Download completed successfully.")
        return data_dir
    except Exception as e:
        print(f"Download failed: {e}")
        return None

def load_data(data_dir):
    """Load the dataset from .mat files with proper key handling"""
    try:
        data_path = os.path.join(data_dir, 'Indian_pines_corrected.mat')
        gt_path = os.path.join(data_dir, 'Indian_pines_gt.mat')
        
        # Try different possible variable names in the .mat files
        mat_data = loadmat(data_path)
        mat_gt = loadmat(gt_path)
        
        # Common variable names used in different versions of the dataset
        possible_data_keys = ['indian_pines_corrected', 'indian_pines', 'img']
        possible_gt_keys = ['indian_pines_gt', 'gt']
        
        # Find the correct key for data
        data = None
        for key in possible_data_keys:
            if key in mat_data:
                data = mat_data[key]
                break
        
        # Find the correct key for ground truth
        gt = None
        for key in possible_gt_keys:
            if key in mat_gt:
                gt = mat_gt[key]
                break
        
        if data is None or gt is None:
            raise ValueError("Could not find data or ground truth in .mat files")
            
        return data, gt
    except Exception as e:
        print(f"Error loading data: {e}")
        return None, None

def preprocess_data(data, gt):
    """Preprocess the hyperspectral data"""
    height, width, bands = data.shape
    X = data.reshape((height * width, bands))
    y = gt.reshape((height * width))
    
    # Remove NaN/inf values and normalize
    X = np.nan_to_num(X)
    X = (X - np.mean(X, axis=0)) / np.std(X, axis=0)
    
    # Only use labeled pixels (class 0 is unlabeled)
    labeled_pixels = y > 0
    return X[labeled_pixels], y[labeled_pixels], height, width

def main():
    print("Starting hyperspectral image classification...")
    
    # Step 1: Download and load data
    data_dir = download_and_extract_dataset()
    if data_dir is None:
        print("Failed to download dataset. Please check your internet connection.")
        return
    
    data, gt = load_data(data_dir)
    if data is None:
        print("Failed to load dataset.")
        return
    
    # Step 2: Preprocess data
    X, y, height, width = preprocess_data(data, gt)
    
    # Step 3: Split into train/test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y)
    
    # Step 4: Apply PCA (retain 95% variance)
    print("Applying PCA for dimensionality reduction...")
    pca = PCA(n_components=0.95)
    X_train_pca = pca.fit_transform(X_train)
    X_test_pca = pca.transform(X_test)
    print(f"Reduced from {X.shape[1]} to {X_train_pca.shape[1]} dimensions")
    
    # Step 5: Train classifier
    print("Training Random Forest classifier...")
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train_pca, y_train)
    
    # Step 6: Evaluate
    y_pred = clf.predict(X_test_pca)
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    print(f"Overall Accuracy: {accuracy_score(y_test, y_pred):.4f}")
    
    # Step 7: Visualize results
    print("Displaying ground truth...")
    plt.figure(figsize=(10, 5))
    plt.imshow(gt, cmap='jet')
    plt.title('Ground Truth')
    plt.colorbar()
    plt.show()

if __name__ == "__main__":
    main()
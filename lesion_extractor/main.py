import cv2
import numpy as np
import os

# --- CONFIGURATION ---
# 1. The Clean, Original Image
ORIGINAL_PATH = "../ramie-disease-dataset/images/ramie_leaf_images/anthracnose_leaf_spot/1.jpg" 

# 2. The SAM Download (with the colored outlines/blobs)
SAM_OUTPUT_PATH = "../ramie-disease-dataset/images/ramie_leaf_images/anthracnose_leaf_spot/SAM_OUTPUT/Sam_1.png"

# 3. Output Folder
OUTPUT_DIR = "lesion_bank"

# --- MAIN SCRIPT ---
if not os.path.exists(OUTPUT_DIR): os.makedirs(OUTPUT_DIR)

print("Loading images...")
original = cv2.imread(ORIGINAL_PATH)
sam_result = cv2.imread(SAM_OUTPUT_PATH)

# Safety Check: Dimensions MUST match
if original.shape != sam_result.shape:
    print("❌ ERROR: Dimension Mismatch!")
    print(f"Original: {original.shape}")
    print(f"SAM Output: {sam_result.shape}")
    print("They must be exactly the same size for this trick to work.")
    exit()

print("Calculating difference...")

# 1. Compute the Absolute Difference
# Any pixel that is identical becomes Black (0).
# Any pixel with a colored line becomes Bright (>0).
diff = cv2.absdiff(original, sam_result)

# 2. Convert to Grayscale & Threshold
# We turn the difference into a simple Black & White Map
gray_diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
_, mask = cv2.threshold(gray_diff, 10, 255, cv2.THRESH_BINARY)

# 3. Clean Up Noise (Optional)
# This removes tiny single-pixel differences caused by compression artifacts
kernel = np.ones((3,3), np.uint8)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)
# Dilate slightly to make sure we capture the whole spot, not just the outline
mask = cv2.dilate(mask, kernel, iterations=2) 

# 4. Find Contours (The Blobs)
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print(f"Found {len(contours)} potential lesions based on the difference.")

count = 0
for i, cnt in enumerate(contours):
    # Filter: Ignore tiny noise specks
    area = cv2.contourArea(cnt)
    if area < 50: continue 

    # --- EXTRACT FROM ORIGINAL ---
    
    # Create a local mask for just this one spot
    single_spot_mask = np.zeros_like(gray_diff)
    cv2.drawContours(single_spot_mask, [cnt], -1, 255, -1)
    
    # Create Transparency (RGBA)
    b, g, r = cv2.split(original)
    rgba = cv2.merge([b, g, r, single_spot_mask])
    
    # Crop Tightly
    x, y, w, h = cv2.boundingRect(cnt)
    lesion_crop = rgba[y:y+h, x:x+w]
    
    # Save
    filename = f"{OUTPUT_DIR}/extracted_{count}.png"
    cv2.imwrite(filename, lesion_crop)
    count += 1

print(f"✅ Success! Extracted {count} clean lesions to '{OUTPUT_DIR}'")
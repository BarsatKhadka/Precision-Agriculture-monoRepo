import cv2
import numpy as np
import os

# --- CONFIGURATION ---
# We need both images to know what is "Background" and what is "Leaf"
ORIGINAL_PATH = "ramie-disease-dataset/images/ramie_leaf_images/healthy/Boehmeria_nivea.jpg"
HIGHLIGHTED_PATH = "ramie-disease-dataset/images/ramie_leaf_images/healthy/sam/1.png"
OUTPUT_DIR = "ramie-disease-dataset/images/ramie_leaf_images/healthy/masks"

# --- SETUP ---
if not os.path.exists(OUTPUT_DIR): os.makedirs(OUTPUT_DIR)

print(f"Processing Cut & Fill Mask...")

# 1. LOAD
orig = cv2.imread(ORIGINAL_PATH)
high = cv2.imread(HIGHLIGHTED_PATH)

if orig is None or high is None: print("❌ Error: Check paths."); exit()

# Resize safety
h, w = orig.shape[:2]
if high.shape[:2] != (h, w): high = cv2.resize(high, (w, h))

# --- STEP 1: THE FILL (Make everything solid white) ---
# Find where the image is different (The Leaves)
diff = cv2.absdiff(orig, high)
diff_gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

# Threshold to get the rough shape
_, rough_mask = cv2.threshold(diff_gray, 10, 255, cv2.THRESH_BINARY)

# FILL HOLES: We find the outlines and color the insides WHITE.
# This fixes the "black content inside" problem.
contours, _ = cv2.findContours(rough_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
solid_mask = np.zeros_like(rough_mask)
for cnt in contours:
    # Only fill decently sized blobs (ignore tiny noise)
    if cv2.contourArea(cnt) > 500:
        cv2.drawContours(solid_mask, [cnt], -1, 255, -1)

# --- STEP 2: THE CUT (Replace color lines with black lines) ---
# We look for sharp color changes in the HIGHLIGHTED image.
# Since SAM uses different colors for different leaves, the edge between them will be sharp.

# Blur slightly to ignore leaf texture, but keep the color edges
blurred_high = cv2.GaussianBlur(high, (5, 5), 0)

# Canny Edge Detection finds the boundaries
edges = cv2.Canny(blurred_high, 50, 150)

# Make the edges thick enough to be a visible "cut"
kernel = np.ones((3,3), np.uint8)
thick_edges = cv2.dilate(edges, kernel, iterations=1)

# --- STEP 3: COMBINE ---
# Final = (Solid White Block) MINUS (Black Edge Lines)
final_mask = cv2.bitwise_and(solid_mask, solid_mask, mask=cv2.bitwise_not(thick_edges))

# --- SAVE ---
output_filename = "cut_and_fill_mask.png"
cv2.imwrite(os.path.join(OUTPUT_DIR, output_filename), final_mask)

print(f"✅ Success! Saved to: {os.path.join(OUTPUT_DIR, output_filename)}")
print("Result: Solid white leaves, separated by clean black cuts.")
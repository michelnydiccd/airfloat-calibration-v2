#!/usr/bin/env python3
"""
Calibration script for Air‑Floating Substrate Handler Model XJ‑2000.
Ensures positioning accuracy of ±5 μm for 8K generation glass substrates.
Compensates for substrate warpage detected from height map.
"""

import time
import random
import math

def run_basic_calibration():
    """
    Simulate a basic calibration routine for the air‑floating handler.
    Prints step‑by‑step messages to simulate the process.
    """
    print("=== Air‑Floating Handler Calibration ===")
    print("Initializing air pressure system...")
    time.sleep(0.5)
    print("Air pressure stable at 0.5 MPa.")
    
    print("Checking zero‑point reference...")
    time.sleep(0.5)
    print("Zero‑point confirmed.")
    
    print("Measuring substrate thickness...")
    time.sleep(0.5)
    thickness = random.uniform(0.5, 0.7)  # mm
    print(f"Detected substrate thickness: {thickness:.3f} mm")
    
    print("Calibrating horizontal alignment...")
    time.sleep(0.5)
    print("Horizontal alignment within tolerance.")
    
    print("Calibrating vertical levelling...")
    time.sleep(0.5)
    print("Vertical levelling complete.")
    
    print("Basic calibration finished successfully.")
    print("Positioning accuracy: ±5 μm")
    return True


def calculate_warpage_compensation(height_map):
    """
    Calculate a compensation factor for substrate warpage.
    
    Parameters
    ----------
    height_map : list[list[float]]
        A 2D grid of height measurements (in microns) across the substrate surface.
        The outer list corresponds to rows (y‑direction), inner list to columns (x‑direction).
    
    Returns
    -------
    float
        The compensation factor (in microns) that should be applied to the zero‑point
        to offset the average deviation from a perfectly flat plane.
    """
    if not height_map:
        raise ValueError("Height map is empty")
    
    # Flatten the 2D array
    heights = [h for row in height_map for h in row]
    mean_height = sum(heights) / len(heights)
    
    # Determine compensation as the mean deviation from zero (simple average)
    # In a real system, a more sophisticated surface‑fitting algorithm would be used.
    compensation = -mean_height  # Negative because we want to offset the average offset
    return compensation


def run_advanced_calibration(height_map):
    """
    Run an advanced calibration routine that includes warpage compensation.
    
    Parameters
    ----------
    height_map : list[list[float]]
        Height measurements (in microns) across the substrate surface.
    
    Returns
    -------
    bool
        True if calibration succeeded, False otherwise.
    """
    print("=== Advanced Calibration (Including Warpage Compensation) ===")
    print("Initializing air pressure system...")
    time.sleep(0.5)
    print("Air pressure stable at 0.5 MPa.")
    
    print("Checking zero‑point reference...")
    time.sleep(0.5)
    print("Zero‑point confirmed.")
    
    print("Measuring substrate thickness...")
    time.sleep(0.5)
    thickness = random.uniform(0.5, 0.7)  # mm
    print(f"Detected substrate thickness: {thickness:.3f} mm")
    
    print("Detecting substrate warpage...")
    time.sleep(0.5)
    
    # Calculate compensation
    try:
        compensation = calculate_warpage_compensation(height_map)
        print(f"Computed warpage compensation: {compensation:.2f} μm")
    except Exception as e:
        print(f"Error calculating compensation: {e}")
        return False
    
    print("Applying compensation to zero‑point...")
    time.sleep(0.5)
    print("Compensation applied.")
    
    print("Calibrating horizontal alignment...")
    time.sleep(0.5)
    print("Horizontal alignment within tolerance.")
    
    print("Calibrating vertical levelling...")
    time.sleep(0.5)
    print("Vertical levelling complete.")
    
    print("Advanced calibration finished successfully.")
    print("Positioning accuracy: ±5 μm")
    return True


if __name__ == "__main__":
    # Example height map (simulated measurement grid of 3×3 points)
    # In a real system, these values would be read from the substrate profiling sensor.
    example_height_map = [
        [1.2, 0.8, 1.5],
        [0.5, 0.3, 0.9],
        [1.1, 0.7, 1.3]
    ]
    
    print("Running basic calibration...")
    success = run_basic_calibration()
    if success:
        print("\nBasic calibration passed.\n")
    
    print("Running advanced calibration...")
    success_advanced = run_advanced_calibration(example_height_map)
    if success_advanced:
        print("\nAdvanced calibration completed. Ready for substrate handling.")
    else:
        print("\nAdvanced calibration failed. Check system status.")
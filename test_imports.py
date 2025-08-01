#!/usr/bin/env python3
"""
Test script to verify all imports work correctly for deployment
"""

def test_imports():
    """Test all required imports"""
    print("Testing imports...")
    
    try:
        import streamlit as st
        print("✅ streamlit imported successfully")
    except ImportError as e:
        print(f"❌ streamlit import failed: {e}")
        return False
    
    try:
        import numpy as np
        print("✅ numpy imported successfully")
    except ImportError as e:
        print(f"❌ numpy import failed: {e}")
        return False
    
    try:
        import matplotlib.pyplot as plt
        import matplotlib.patches as patches
        print("✅ matplotlib imported successfully")
    except ImportError as e:
        print(f"❌ matplotlib import failed: {e}")
        return False
    
    try:
        import pandas as pd
        print("✅ pandas imported successfully")
    except ImportError as e:
        print(f"❌ pandas import failed: {e}")
        return False
    
    try:
        # Try different import paths for different Qiskit versions
        try:
            from qiskit.primitives import Sampler
            print("✅ qiskit.primitives.Sampler imported successfully")
        except ImportError:
            try:
                from qiskit.algorithms import Sampler
                print("✅ qiskit.algorithms.Sampler imported successfully")
            except ImportError:
                from qiskit import Sampler
                print("✅ qiskit.Sampler imported successfully")
        print("✅ qiskit imported successfully")
    except ImportError as e:
        print(f"❌ qiskit import failed: {e}")
        return False
    
    try:
        from quantum_solver import NQueensQuantumSolver
        print("✅ quantum_solver imported successfully")
    except ImportError as e:
        print(f"❌ quantum_solver import failed: {e}")
        return False
    
    print("\n🎉 All imports successful!")
    return True

if __name__ == "__main__":
    test_imports() 
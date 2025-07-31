#!/usr/bin/env python3
"""
Test script to verify that all dependencies are properly installed
and the quantum puzzle solver can be imported and used.
"""

def test_imports():
    """Test that all required packages can be imported."""
    print("🔍 Testing imports...")
    
    try:
        import streamlit as st
        print("✅ Streamlit imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import Streamlit: {e}")
        return False
    
    try:
        import numpy as np
        print("✅ NumPy imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import NumPy: {e}")
        return False
    
    try:
        import matplotlib.pyplot as plt
        print("✅ Matplotlib imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import Matplotlib: {e}")
        return False
    
    try:
        from qiskit import QuantumCircuit
        from qiskit_aer import Aer
        from qiskit.primitives import Sampler
        print("✅ Qiskit imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import Qiskit: {e}")
        return False
    
    try:
        from qiskit.visualization import plot_histogram
        print("✅ Qiskit visualization imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import Qiskit visualization: {e}")
        return False
    
    return True

def test_quantum_solver():
    """Test that the quantum solver can be imported and used."""
    print("\n🧮 Testing quantum solver...")
    
    try:
        from quantum_solver import NQueensQuantumSolver, create_visualization
        print("✅ Quantum solver module imported successfully")
        
        # Test creating a solver
        solver = NQueensQuantumSolver(4)
        print("✅ NQueensQuantumSolver created successfully")
        
        # Test solving
        result = solver.solve(shots=100)
        print("✅ Quantum simulation completed successfully")
        
        # Test visualization
        fig = create_visualization(result['most_probable'], 4)
        print("✅ Visualization created successfully")
        
        return True
        
    except ImportError as e:
        print(f"❌ Failed to import quantum solver: {e}")
        return False
    except Exception as e:
        print(f"❌ Error testing quantum solver: {e}")
        return False

def test_basic_quantum_circuit():
    """Test basic quantum circuit creation and execution."""
    print("\n⚛️ Testing basic quantum circuit...")
    
    try:
        from qiskit import QuantumCircuit
        from qiskit.primitives import Sampler
        
        # Create a simple circuit
        qc = QuantumCircuit(2)
        qc.h(0)
        qc.cx(0, 1)
        qc.measure_all()
        
        # Execute on simulator
        sampler = Sampler()
        job = sampler.run(qc, shots=100)
        result = job.result()
        counts = result.quasi_dists[0]
        
        print("✅ Basic quantum circuit executed successfully")
        print(f"   Results: {counts}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing basic quantum circuit: {e}")
        return False

def main():
    """Run all tests."""
    print("🚀 Quantum Puzzle Solver - Installation Test")
    print("=" * 50)
    
    # Test imports
    imports_ok = test_imports()
    
    # Test basic quantum circuit
    circuit_ok = test_basic_quantum_circuit()
    
    # Test quantum solver (if imports are ok)
    solver_ok = False
    if imports_ok:
        solver_ok = test_quantum_solver()
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 Test Summary:")
    print(f"   Imports: {'✅ PASS' if imports_ok else '❌ FAIL'}")
    print(f"   Basic Circuit: {'✅ PASS' if circuit_ok else '❌ FAIL'}")
    print(f"   Quantum Solver: {'✅ PASS' if solver_ok else '❌ FAIL'}")
    
    if imports_ok and circuit_ok:
        print("\n🎉 Installation successful! You can now run:")
        print("   streamlit run app.py")
    else:
        print("\n⚠️  Some tests failed. Please check your installation.")
        print("   Try running: pip install -r requirements.txt")

if __name__ == "__main__":
    main() 
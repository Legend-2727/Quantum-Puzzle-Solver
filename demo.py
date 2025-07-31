#!/usr/bin/env python3
"""
Demo script for the Quantum Puzzle Solver
This script demonstrates the N-Queens quantum solver functionality.
"""

import numpy as np
from quantum_solver import NQueensQuantumSolver, create_visualization
import matplotlib.pyplot as plt

def main():
    """Run a demonstration of the quantum solver."""
    print("🚀 Quantum Puzzle Solver Demo")
    print("=" * 40)
    
    # Test with 4-Queens problem
    n = 4
    print(f"\n🎯 Solving {n}-Queens problem with quantum algorithm...")
    
    # Create solver
    solver = NQueensQuantumSolver(n)
    print(f"✅ Created solver for {n}x{n} board")
    
    # Solve the problem
    print("⚛️ Running quantum simulation...")
    result = solver.solve(shots=1000, use_simplified_oracle=True)
    
    print(f"✅ Simulation completed with {result['shots']} shots")
    print(f"📊 Most probable result: {result['most_probable']}")
    
    # Verify the solution
    is_valid = solver.verify_solution(result['most_probable'])
    print(f"🔍 Solution verification: {'✅ VALID' if is_valid else '❌ INVALID'}")
    
    if is_valid:
        # Get coordinates
        coordinates = solver.get_solution_coordinates(result['most_probable'])
        print(f"👑 Queen positions: {coordinates}")
        
        # Create visualization
        print("🎨 Creating visualization...")
        fig = create_visualization(result['most_probable'], n)
        
        # Save the plot
        plt.savefig('n_queens_solution.png', dpi=150, bbox_inches='tight')
        print("💾 Solution saved as 'n_queens_solution.png'")
        
        # Show some statistics
        print(f"\n📈 Solution Statistics:")
        print(f"   Total possible states: {2**(n*n)}")
        print(f"   Circuit depth: {result['circuit'].depth()}")
        print(f"   Number of gates: {result['circuit'].count_ops()}")
        
        # Show top results
        print(f"\n🏆 Top 3 results:")
        sorted_results = sorted(result['counts'].items(), key=lambda x: x[1], reverse=True)
        for i, (bitstring, count) in enumerate(sorted_results[:3]):
            validity = "✅" if solver.verify_solution(bitstring) else "❌"
            print(f"   {i+1}. {bitstring} (count: {count}) {validity}")
    
    else:
        print("⚠️ No valid solution found in this run.")
        print("   This can happen due to the probabilistic nature of quantum algorithms.")
        print("   Try running again or increase the number of shots.")
    
    print(f"\n🎉 Demo completed!")
    print(f"   To run the interactive web app: streamlit run app.py")

if __name__ == "__main__":
    main() 
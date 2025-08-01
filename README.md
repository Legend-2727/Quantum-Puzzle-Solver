# ⚛️ Quantum Puzzle Solver Suite

## 🎯 Project Overview

A comprehensive quantum computing application that demonstrates multiple quantum algorithms solving different computational problems. This project showcases the power of quantum computing through interactive visualizations and real-time simulations.

### 🚀 Key Features

- **Multiple Quantum Algorithms**: N-Queens, Graph Coloring, Quantum Machine Learning, and Deutsch-Jozsa
- **Interactive Web Interface**: Built with Streamlit for easy access and visualization
- **Real-time Quantum Simulations**: Live circuit execution and result visualization
- **Educational Focus**: Designed to teach quantum computing concepts through practical examples
- **Visual Demonstrations**: Circuit diagrams, measurement results, and solution visualizations

## 🧩 Supported Problems

### 1. 👑 N-Queens Problem
- **Algorithm**: Grover's Search Algorithm
- **Purpose**: Find valid queen placements on N×N chessboard
- **Quantum Advantage**: Quadratic speedup over classical search

### 2. 🎨 Graph Coloring Problem
- **Algorithm**: Quantum Approximate Optimization Algorithm (QAOA)
- **Purpose**: Color graph vertices with minimum colors
- **Quantum Advantage**: Efficient constraint satisfaction

### 3. 🤖 Quantum Machine Learning (QSVM)
- **Algorithm**: Quantum Support Vector Machine
- **Purpose**: Binary classification using quantum feature maps
- **Quantum Advantage**: Quantum feature space exploration

### 4. 🔬 Deutsch-Jozsa Algorithm
- **Algorithm**: Deutsch-Jozsa Algorithm
- **Purpose**: Determine if function is constant or balanced
- **Quantum Advantage**: Exponential speedup (1 query vs 2^(n-1)+1)

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Legend-2727/Quantum-Puzzle-Solver.git
cd Quantum-Puzzle-Solver
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app_enhanced_real_time.py
```

4. Open your browser and navigate to `http://localhost:8501`

## 🧮 How It Works

### Quantum Algorithm Implementations

#### N-Queens with Grover's Algorithm
1. **Problem Encoding**: Each square represented by a qubit
2. **Superposition**: All possible configurations created simultaneously
3. **Oracle**: Marks valid solutions with phase flip
4. **Amplification**: Grover iterations amplify solution amplitudes
5. **Measurement**: Reveals valid solution with high probability

#### Graph Coloring with QAOA
1. **Problem Formulation**: Convert to optimization problem
2. **Parameterized Circuits**: Create variational quantum circuits
3. **Cost Function**: Minimize color conflicts
4. **Optimization**: Classical optimization of quantum parameters
5. **Solution**: Extract optimal coloring from measurements

#### QSVM for Classification
1. **Feature Mapping**: Transform data to quantum feature space
2. **Kernel Construction**: Build quantum kernel matrix
3. **Support Vectors**: Identify key training points
4. **Classification**: Predict new data points
5. **Visualization**: Show decision boundaries and support vectors

#### Deutsch-Jozsa Algorithm
1. **Function Oracle**: Encode function as quantum oracle
2. **Superposition**: Put input qubits in superposition
3. **Oracle Application**: Apply function to all inputs simultaneously
4. **Interference**: Hadamard gates create interference patterns
5. **Measurement**: Result reveals function type in one query

## 📊 Technical Implementation

### Dependencies
- **qiskit==0.44.0**: Quantum computing framework
- **qiskit-aer==0.12.0**: High-performance quantum simulators
- **streamlit==1.33.0**: Web application framework
- **numpy==1.24.3**: Numerical computing
- **matplotlib==3.7.2**: Data visualization
- **plotly==5.17.0**: Interactive visualizations

### Architecture
```
Quantum-Puzzle-Solver/
├── app_enhanced_real_time.py  # Main Streamlit application
├── quantum_solver.py          # Core quantum algorithms
├── requirements.txt           # Python dependencies
└── README.md                 # Project documentation
```

## 🎓 Educational Value

This project serves as an excellent introduction to:
- **Quantum Circuit Design**: Building complex quantum circuits
- **Algorithm Implementation**: Converting classical problems to quantum
- **Quantum Advantage**: Understanding when quantum beats classical
- **Hybrid Quantum-Classical**: Combining quantum and classical computing
- **Real-world Applications**: Practical quantum computing use cases

## 🌟 Key Achievements

- **Multiple Algorithms**: 4 different quantum algorithms implemented
- **Interactive Interface**: User-friendly web application
- **Real-time Visualization**: Live quantum circuit execution
- **Educational Content**: Comprehensive explanations and tutorials
- **Robust Implementation**: Error handling and fallback systems

## 🔮 Future Enhancements

- [ ] Real quantum hardware execution via IBM Quantum
- [ ] Additional quantum algorithms (Shor's, Quantum Fourier Transform)
- [ ] Performance optimizations and qubit-efficient encoding
- [ ] Advanced quantum machine learning algorithms
- [ ] Multi-user collaboration features

## 📚 References

- [Qiskit Documentation](https://qiskit.org/documentation/)
- [Grover's Algorithm](https://quantum-computing.ibm.com/composer/docs/iqx/guide/grovers-algorithm)
- [Deutsch-Jozsa Algorithm](https://en.wikipedia.org/wiki/Deutsch%E2%80%93Jozsa_algorithm)
- [Quantum Machine Learning](https://qiskit.org/ecosystem/machine-learning/)
- [Streamlit Documentation](https://docs.streamlit.io/)

## 👨‍💻 Author

**Legend-2727** - *Quantum Computing Enthusiast* - [GitHub](https://github.com/Legend-2727)

---

**Built for CQhack25** - Exploring the frontiers of quantum computing through practical applications and educational demonstrations.
# 👑 Quantum Puzzle Solver

## About

A quantum computing application that solves the N-Queens puzzle using Grover's algorithm. This project demonstrates how quantum algorithms can provide quadratic speedup for combinatorial search problems.

## 🎯 Project Overview

The Quantum Puzzle Solver is an interactive web application that showcases the power of quantum computing in solving classic combinatorial puzzles. By implementing Grover's search algorithm using Qiskit, it provides a hands-on way to explore quantum solutions to the N-Queens problem.

### Key Features

- **Interactive Web Interface**: Built with Streamlit for easy access and visualization
- **Quantum Algorithm Implementation**: Custom Grover's algorithm with problem-specific oracle
- **Real-time Visualization**: Circuit diagrams, measurement histograms, and chessboard solutions
- **Educational Focus**: Designed to teach quantum computing concepts through practical examples

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
streamlit run app.py
```

4. Open your browser and navigate to `http://localhost:8501`

## 🧮 How It Works

### The N-Queens Problem

The N-Queens puzzle requires placing N queens on an N×N chessboard so that no two queens can attack each other. This means:
- No two queens in the same row
- No two queens in the same column  
- No two queens on the same diagonal

### Quantum Solution with Grover's Algorithm

1. **Problem Encoding**: Each square on the board is represented by a qubit
2. **Superposition**: All possible board configurations are created simultaneously
3. **Oracle**: Marks valid solutions with a phase flip
4. **Amplification**: Grover iterations amplify the amplitude of solutions
5. **Measurement**: Reveals a valid solution with high probability

### Technical Implementation

- **Framework**: Qiskit for quantum circuit construction and simulation
- **Algorithm**: Grover's search algorithm with custom oracle
- **Visualization**: Matplotlib for circuit diagrams and solution display
- **Web Interface**: Streamlit for interactive user experience

## 📊 Supported Board Sizes

Currently supports:
- **3×3 board**: 9 qubits, search space of 2^9 = 512 states
- **4×4 board**: 16 qubits, search space of 2^16 = 65,536 states

*Note: Larger board sizes require exponentially more qubits and computational resources.*

## 🎓 Educational Value

This project serves as an excellent introduction to:
- Quantum circuit design
- Grover's algorithm implementation
- Quantum oracle construction
- Quantum-classical hybrid applications
- NP-complete problem solving with quantum methods

## 🔧 Technical Details

### Dependencies

- **qiskit**: Quantum computing framework
- **qiskit-aer**: High-performance quantum simulators
- **streamlit**: Web application framework
- **numpy**: Numerical computing
- **matplotlib**: Data visualization

### Architecture

```
Quantum-Puzzle-Solver/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md          # Project documentation
```

## 🌐 Deployment

### Streamlit Community Cloud

1. Push your code to GitHub
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Deploy with `app.py` as the main file

### Hugging Face Spaces

1. Create a new Space on Hugging Face
2. Choose Streamlit as the SDK
3. Upload your files
4. The app will automatically deploy

## 🔮 Future Enhancements

- [ ] Support for larger board sizes (5×5, 6×6)
- [ ] Real quantum hardware execution via IBM Quantum
- [ ] Additional puzzle types (Sudoku, Graph Coloring)
- [ ] Performance optimizations and qubit-efficient encoding
- [ ] Advanced quantum algorithms comparison

## 📚 References

- [Grover's Algorithm - IBM Quantum](https://quantum-computing.ibm.com/composer/docs/iqx/guide/grovers-algorithm)
- [N-Queens Problem - Wikipedia](https://en.wikipedia.org/wiki/Eight_queens_puzzle)
- [Qiskit Documentation](https://qiskit.org/documentation/)
- [Streamlit Documentation](https://docs.streamlit.io/)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Legend-2727** - *Initial work* - [GitHub](https://github.com/Legend-2727)

---

**Built for CQhack25** - Exploring the frontiers of quantum computing through practical applications.
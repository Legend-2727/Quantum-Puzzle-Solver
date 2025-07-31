# 🚀 Deployment Guide for Quantum Puzzle Solver

This guide provides step-by-step instructions for deploying the Quantum Puzzle Solver application to various cloud platforms.

## 📋 Prerequisites

Before deploying, ensure you have:

1. **GitHub Account**: For hosting the source code
2. **Python 3.8+**: For local testing
3. **Required Dependencies**: All packages listed in `requirements.txt`

## 🏠 Local Development Setup

### 1. Clone and Setup

```bash
git clone https://github.com/Legend-2727/Quantum-Puzzle-Solver.git
cd Quantum-Puzzle-Solver
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Test Locally

```bash
streamlit run app.py
```

The application will be available at `http://localhost:8501`

## ☁️ Cloud Deployment Options

### Option A: Streamlit Community Cloud (Recommended)

**Pros:**
- Free hosting
- Automatic deployment from GitHub
- Built specifically for Streamlit apps
- Easy setup

**Steps:**

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Sign in with your GitHub account
   - Click "New app"
   - Select your repository: `Legend-2727/Quantum-Puzzle-Solver`
   - Set main file path: `app.py`
   - Click "Deploy!"

3. **Configuration**
   - **Python version**: 3.9 (recommended)
   - **Main file**: `app.py`
   - **Requirements file**: `requirements.txt` (auto-detected)

### Option B: Hugging Face Spaces

**Pros:**
- Free hosting
- Git-based workflow
- Good for ML/AI projects
- Integrated with Hugging Face ecosystem

**Steps:**

1. **Create a Space**
   - Visit [huggingface.co/spaces](https://huggingface.co/spaces)
   - Click "Create new Space"
   - Choose settings:
     - **Owner**: Your username
     - **Space name**: `quantum-puzzle-solver`
     - **SDK**: Streamlit
     - **License**: MIT
     - **Visibility**: Public

2. **Upload Files**
   ```bash
   git clone https://huggingface.co/spaces/YOUR_USERNAME/quantum-puzzle-solver
   cd quantum-puzzle-solver
   # Copy your files here
   cp ../Quantum-Puzzle-Solver/* .
   git add .
   git commit -m "Initial commit"
   git push
   ```

3. **Configure README.md**
   Add this YAML front matter to your README.md:
   ```yaml
   ---
   title: Quantum Puzzle Solver
   emoji: 👑
   colorFrom: blue
   colorTo: purple
   sdk: streamlit
   app_file: app.py
   ---
   ```

### Option C: Heroku

**Pros:**
- Scalable
- Good for production apps
- Custom domain support

**Steps:**

1. **Create Heroku App**
   ```bash
   heroku create quantum-puzzle-solver
   ```

2. **Add Buildpacks**
   ```bash
   heroku buildpacks:add heroku/python
   ```

3. **Create Procfile**
   Create a file named `Procfile`:
   ```
   web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
   ```

4. **Deploy**
   ```bash
   git add .
   git commit -m "Heroku deployment"
   git push heroku main
   ```

## 🔧 Configuration Files

### requirements.txt
```txt
# Core quantum computing framework
qiskit==1.0.2
qiskit-aer==0.13.3

# Web application framework
streamlit==1.33.0

# Scientific computing and visualization
numpy==1.26.4
matplotlib==3.8.3

# Additional dependencies for Qiskit
qiskit-ibm-runtime==0.20.2
qiskit-visualization==0.1.0
```

### .streamlit/config.toml (Optional)
```toml
[theme]
primaryColor = "#FF6B6B"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"

[server]
maxUploadSize = 200
enableXsrfProtection = false
enableCORS = false
```

## 🐛 Troubleshooting

### Common Issues

1. **Import Errors**
   - Ensure all dependencies are in `requirements.txt`
   - Check Python version compatibility

2. **Memory Issues**
   - Reduce the number of shots in the quantum simulation
   - Use simplified oracle for faster execution

3. **Deployment Failures**
   - Check build logs for specific error messages
   - Verify file paths and names
   - Ensure all files are committed to Git

### Platform-Specific Issues

**Streamlit Cloud:**
- Build timeout: Reduce circuit complexity
- Memory limit: Use smaller board sizes

**Hugging Face Spaces:**
- Git push issues: Check authentication
- Build failures: Verify YAML configuration

**Heroku:**
- Dyno timeout: Optimize quantum circuits
- Memory limit: Use simplified implementations

## 📊 Performance Optimization

### For Production Deployment

1. **Reduce Circuit Complexity**
   - Use simplified oracle for faster execution
   - Limit board sizes to 3×3 and 4×4

2. **Optimize Dependencies**
   - Pin specific versions in requirements.txt
   - Remove unused packages

3. **Caching**
   - Implement result caching for repeated queries
   - Use Streamlit's caching decorators

## 🔒 Security Considerations

1. **Input Validation**
   - Validate board size parameters
   - Sanitize user inputs

2. **Resource Limits**
   - Limit maximum shots and board sizes
   - Implement timeout mechanisms

3. **Error Handling**
   - Graceful error messages
   - Fallback to classical solutions

## 📈 Monitoring and Analytics

### Recommended Tools

1. **Streamlit Analytics** (if using Streamlit Cloud)
2. **Custom logging** for quantum circuit performance
3. **Error tracking** with services like Sentry

### Metrics to Track

- Number of successful quantum simulations
- Average execution time
- Most popular board sizes
- Error rates and types

## 🚀 Advanced Deployment

### Docker Deployment

Create a `Dockerfile`:
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Kubernetes Deployment

For enterprise deployments, consider:
- Kubernetes clusters
- Load balancing
- Auto-scaling
- Health checks

## 📞 Support

If you encounter issues:

1. Check the [Streamlit documentation](https://docs.streamlit.io/)
2. Review [Qiskit installation guide](https://qiskit.org/documentation/getting_started.html)
3. Open an issue on the GitHub repository
4. Check platform-specific documentation

## 🎯 Success Metrics

A successful deployment should achieve:

- ✅ Application loads without errors
- ✅ Quantum simulations complete successfully
- ✅ Visualizations render correctly
- ✅ User interface is responsive
- ✅ All features work as expected

---

**Happy Deploying! 🚀**

For more information, visit the [main project repository](https://github.com/Legend-2727/Quantum-Puzzle-Solver). 
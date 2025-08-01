# Deployment Fix Guide - Matplotlib Import Error

## Problem
You encountered a `ModuleNotFoundError` for `matplotlib` during deployment. This is a common issue on deployment platforms like Streamlit Cloud.

## Root Cause
The error occurs because:
1. Matplotlib has complex dependencies that may not be properly installed in the deployment environment
2. Some deployment platforms have restrictions on certain packages
3. Version conflicts between matplotlib and its dependencies

## Solutions

### Solution 1: Use the Updated Requirements Files
I've updated both `requirements.txt` and `requirements_deployment.txt` with more compatible versions:

```bash
# Use the deployment-optimized requirements
pip install -r requirements_deployment.txt
```

### Solution 2: Platform-Specific Fixes

#### For Streamlit Cloud:
1. Make sure your `requirements.txt` is in the root directory
2. Use the updated `requirements_deployment.txt` which has more conservative version ranges
3. If still failing, try adding these explicit dependencies:

```
matplotlib-base>=3.6.0,<3.9.0
matplotlib-inline>=0.1.0
```

#### For Heroku:
1. Add a `runtime.txt` file specifying Python version:
```
python-3.9.18
```

2. Use the deployment requirements file

#### For Railway:
1. Use the deployment requirements file
2. Set build command: `pip install -r requirements_deployment.txt`

### Solution 3: Alternative Visualization (If Matplotlib Still Fails)
The application now has graceful fallbacks. If matplotlib fails to import:
- The app will show a warning message
- Core functionality will still work
- Visualizations will show error messages instead of crashing

### Solution 4: Manual Package Installation
If the above doesn't work, try installing matplotlib manually:

```bash
pip install matplotlib==3.7.2
pip install numpy==1.24.3
```

## Testing Your Fix

1. Run the test script locally:
```bash
python test_imports.py
```

2. If all imports work locally, try deploying again

3. Check the deployment logs for any remaining errors

## Common Deployment Platforms and Their Requirements

### Streamlit Cloud
- Use `requirements.txt` (not `requirements_deployment.txt`)
- Ensure all packages are compatible with Python 3.9+
- Avoid packages that require system-level dependencies

### Heroku
- Use `requirements_deployment.txt`
- Add `runtime.txt` for Python version
- May need `Procfile` for web processes

### Railway
- Use `requirements_deployment.txt`
- Set build command in Railway dashboard

## If All Else Fails

If matplotlib continues to cause issues, you can:

1. **Remove matplotlib dependency**: The app will work without visualizations
2. **Use alternative visualization libraries**: Consider plotly (already included) or streamlit's built-in charts
3. **Deploy without visualizations**: The core quantum functionality will still work

## Next Steps

1. Try deploying with the updated `requirements_deployment.txt`
2. If it still fails, check the deployment platform's specific requirements
3. Run `python test_imports.py` locally to verify everything works
4. Check the deployment logs for specific error messages

The application is now more robust and will handle missing matplotlib gracefully, so even if the import fails, the core functionality will still work. 
# Use Python 3.11 slim as base
FROM python:3.11-slim

# Install common data science packages
# These will be available when user code runs
RUN pip install --no-cache-dir \
    pandas==2.1.4 \
    numpy==1.26.3 \
    matplotlib==3.8.2 \
    seaborn==0.13.1 \
    requests==2.31.0 \
    scikit-learn==1.4.0 \
    scipy==1.12.0\
    statsmodels==0.14.1

# Set working directory
WORKDIR /workspace

# Note: This container is for CODE EXECUTION only
# AutoGen, Streamlit, LangChain run OUTSIDE this container


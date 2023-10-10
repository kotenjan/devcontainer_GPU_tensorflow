# Use the official TensorFlow GPU image as the base image
FROM tensorflow/tensorflow:latest-gpu-jupyter

# Set up environment variables for Jupyter
ENV JUPYTER_ENABLE_LAB=yes
ENV JUPYTER_PORT=8888
ENV JUPYTER_TOKEN=my_secret_token

# Create a non-root user and switch to that user
ARG NB_USER=dev
ARG NB_UID=1000
ARG NB_GID=10000

RUN groupadd -g ${NB_GID} ${NB_USER} && \
    useradd -m -u ${NB_UID} -g ${NB_GID} -s /bin/bash ${NB_USER}

# Change ownership of the home directory
RUN chown -R ${NB_USER}:${NB_USER} /home/${NB_USER}

# Switch to the non-root user
USER ${NB_USER}

# Create a working directory and set it as the default
WORKDIR /home/${NB_USER}/workspace

# Copy the requirements file into the working directory
COPY --chown=${NB_USER}:${NB_USER} requirements.txt .

# Install the requirements
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Jupyter Notebook port
EXPOSE ${JUPYTER_PORT}

# Start the Jupyter Notebook server
CMD ["jupyter-notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=my_secret_token"]

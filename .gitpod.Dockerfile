FROM gitpod/workspace-full

# Install Python packages
RUN pip install --upgrade pip && \
    pip install \
        google-api-python-client \
        google-auth \
        google-auth-oauthlib \
        google-auth-httplib2

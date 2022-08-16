# Use Python 3.6 or later as a base image
FROM python:3.6
# Copy contents into image
COPY . .
# Install pip dependencies from requirements
RUN  pip install -r requirements.txt 
# Set YOUR_NAME environment variable
ENV DATABASE_URI=sqlite:///demo.db SECRET_KEY=585C71B9C1DFF767
# Expose the correct port
EXPOSE 5000
# Running create.py 
RUN python3 create.py 
# Create an entrypoint
ENTRYPOINT ["python", "app.py"]

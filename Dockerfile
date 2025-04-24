# 1. Base Python image
FROM python:3.10-slim

# 2. Create & switch into our app dir
WORKDIR /var/www

# 3. Copy & install Python requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the rest of your application code in
COPY . .

# 5. Expose the Flask port
EXPOSE 8080

# 6. Set Flask environment variables
ENV FLASK_APP=app.py \
    FLASK_ENV=development

# 7. Launch Flask on 0.0.0.0:8080
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]

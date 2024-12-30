FROM python
WORKDIR /app/
COPY . .

RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install --with-deps
CMD ["python", "-m", "pytest", "-s", "--alluredir=results/", "/app/"]

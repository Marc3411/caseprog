FROM python:3.11-slim
            # Sæt arbejdsdirectoriet i containeren
WORKDIR /app

            # Installere dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

            # Kopiere alle filer til containeren
COPY . .

            # Eksponere porten som Flask-appen kører på
EXPOSE 5000

            # Kør Flask-appen
CMD ["python", "Main.py"]

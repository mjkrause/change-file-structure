FROM python:3.6
COPY src/change_file_structure.py .
ENTRYPOINT ["python", "change_file_structure.py"]
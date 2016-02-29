FROM python:3.5-onbuild
RUN chmod 755 cvs2w3id.py
CMD ["./cvs2w3id.py", "--help"]

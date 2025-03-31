# GPT Assistant on document

Add main document:
- POST /documents/main/addpdf

Add additional documents:
- POST /documents/addpdf
- POST /documents/addtxt

Ask the question
- POST /ask

Get questions suggestions:
- GET /suggestion

### Start
```bash
uvicorn app.main:app  --host 0.0.0.0 --port 3000 --reload
```

### Start wiht docker

# Build the image
```bash
docker build -t gpt-chroma-app .

# Run the container
docker run -p 3000:3000 gpt-chroma-app
```


## TODO:
- Add static data about SignNow and signing process (save to chroma on the initialisation stage and use to search the appropriate data)
- tune prompts for more accurate suggestions
- Investigate file sending by postman (currently dont work)
- Save context? (do we need to save it?)
- Multiuser, auth
- 


### bash requestrs to send documents
Change the path to your file

```bash
curl -X POST http://localhost:3000/documents/main/addpdf \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@/Users/tymur/Documents/Tim/Projects/AI/FastAPI/samples/fillable rental agreement.pdf"


curl -X POST http://localhost:3000/documents/addpdf \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@/Users/tymur/Documents/Tim/Projects/AI/FastAPI/samples/rental_ukraine.txt"
```

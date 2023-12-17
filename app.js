const express = require('express');
const multer = require('multer');
const xlsx = require('xlsx'); 

const app = express();
const upload = multer({ dest: 'uploads/' });

app.post('/convert', upload.single('file'), (req, res) => {
  if (!req.file) {
    return res.status(400).send('No file uploaded');
  }

  if (!req.file.originalname.endsWith('.xlsx')) {
    return res.status(400).send('Invalid file format. Please provide an XLSX file.');
  }
  const workbook = xlsx.readFile(req.file.path);
  const jsonData = xlsx.utils.sheet_to_json(workbook.Sheets[workbook.SheetNames[0]]);

  res.status(200).json(jsonData);
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
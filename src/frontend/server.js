let express = require('express');
let app = express();
let multer = require('multer')
let cors = require('cors');

app.use(cors());

let storage = multer.diskStorage({
    destination: function(req, file, cb) {
        cb(null, 'public')
    },
    filename: function(req, file, cb) {
        cb(null, Date.now() + '_' + file.originalname)
    }
});

let upload = multer({storage: storage}).single('file');

app.post('/upload', function(req, res) {
    upload(req, res, function(err) {
        if (err instanceof multer.MulterError) {
            return res.status(500).json(err);
        } else if(err) {
            return res.status(500).json(err);
        }
    })
    return res.status(200).send(req.file)
})

app.listen(8000, function() {
    console.log('App is running on port 8000');
})
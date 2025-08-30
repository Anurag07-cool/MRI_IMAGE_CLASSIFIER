# AI Brain Tumor Classifier

A modern, professional web application for classifying brain tumors from MRI scans using deep learning. This application provides an intuitive interface for healthcare professionals and researchers to analyze brain MRI images.

## Features

### 🧠 AI-Powered Analysis
- **Deep Learning Model**: Pre-trained convolutional neural network for accurate tumor detection
- **Multiple Tumor Types**: Classifies gliomas, meningiomas, pituitary tumors, and detects healthy scans
- **Confidence Scoring**: Provides confidence percentages for each prediction

### 🎨 Modern User Interface
- **Professional Medical Design**: Clean, medical-grade interface with intuitive controls
- **Drag & Drop Upload**: Easy image upload with drag-and-drop functionality
- **Real-time Preview**: Instant image preview before analysis
- **Responsive Design**: Works seamlessly on desktop and mobile devices

### 🔬 Medical Information
- **Educational Content**: Detailed information about each tumor type
- **Medical Disclaimers**: Appropriate warnings about AI-assisted diagnosis
- **Professional Standards**: Built with healthcare professionals in mind

## Tumor Types Classified

1. **Glioma** - Tumors that occur in the brain and spinal cord
2. **Meningioma** - Tumors forming on brain and spinal cord membranes
3. **Pituitary Tumor** - Tumors in the pituitary gland
4. **No Tumor** - Healthy brain scans

## Installation

### Prerequisites
- Python 3.7 or higher
- TensorFlow 2.x
- Flask

### Setup
1. Clone or download the project files
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure the `brain_tumor_classifier.h5` model file is in the project directory
4. Run the application:
   ```bash
   python app.py
   ```
5. Open your browser and navigate to `http://localhost:5000`

## Usage

### Uploading Images
1. **Drag & Drop**: Simply drag an MRI image onto the upload area
2. **Click to Browse**: Click the upload area to select a file from your computer
3. **Supported Formats**: JPG, JPEG, PNG
4. **Image Requirements**: Minimum 64x64 pixels, high-quality brain MRI scans

### Analysis Process
1. Upload your MRI image
2. The system automatically validates the image
3. AI analysis processes the scan
4. Results display with confidence scores and tumor information
5. Educational content about the detected tumor type

### Understanding Results
- **Prediction**: The detected tumor type or "No Tumor"
- **Confidence**: Percentage indicating the AI's confidence in the result
- **Information**: Educational content about the detected condition
- **Disclaimer**: Important medical disclaimers

## Technical Details

### Backend
- **Framework**: Flask web framework
- **AI Model**: TensorFlow/Keras deep learning model
- **Image Processing**: PIL (Pillow) for image handling
- **File Management**: Secure file upload with validation

### Frontend
- **HTML5**: Semantic markup with accessibility features
- **CSS3**: Modern styling with CSS variables and animations
- **JavaScript**: ES6+ with async/await for smooth user experience
- **Responsive**: Mobile-first design approach

### Model Specifications
- **Input Size**: 64x64 pixels
- **Preprocessing**: Normalization (0-1 scale)
- **Architecture**: Convolutional Neural Network
- **Training Data**: Thousands of annotated MRI scans

## File Structure

```
Brain Classifier App/
├── app.py                 # Main Flask application
├── brain_tumor_classifier.h5  # Pre-trained AI model
├── requirements.txt       # Python dependencies
├── Procfile             # Heroku deployment configuration
├── README.md            # This documentation
├── static/
│   └── uploads/         # Temporary image storage
└── templates/
    └── index.html       # Main application interface
```

## Security & Privacy

- **File Validation**: All uploaded images are validated for security
- **Temporary Storage**: Images are stored temporarily and can be cleaned up
- **No Data Persistence**: Uploaded images are not permanently stored
- **Local Processing**: All analysis happens locally on your server

## Medical Disclaimer

⚠️ **Important**: This application is for educational and research purposes only. 

- AI-assisted analysis should **NOT** replace professional medical diagnosis
- Always consult with qualified healthcare professionals for medical decisions
- Results are provided as-is without medical guarantees
- Use at your own risk and responsibility

## Deployment

### Local Development
```bash
python app.py
```

### Production Deployment
1. Set `debug=False` in `app.py`
2. Use a production WSGI server (Gunicorn, uWSGI)
3. Configure proper security headers
4. Set up HTTPS for production use

### Heroku Deployment
The included `Procfile` allows for easy Heroku deployment:
```bash
git push heroku main
```

## Troubleshooting

### Common Issues

1. **Model Loading Error**
   - Ensure `brain_tumor_classifier.h5` is in the project directory
   - Check TensorFlow version compatibility

2. **Image Upload Issues**
   - Verify image format (JPG, PNG, JPEG)
   - Ensure image meets minimum size requirements
   - Check file permissions

3. **Analysis Failures**
   - Verify image quality and format
   - Check server logs for error details
   - Ensure sufficient system resources

### Performance Tips

- Use high-quality, properly formatted MRI images
- Ensure adequate server resources for model inference
- Consider image compression for large files
- Monitor server performance during peak usage

## Contributing

This is a research and educational project. Contributions are welcome:

1. Fork the repository
2. Create a feature branch
3. Make your improvements
4. Submit a pull request

## License

This project is provided for educational and research purposes. Please ensure compliance with local regulations and medical device laws if used in clinical settings.

## Support

For technical support or questions:
- Check the troubleshooting section above
- Review the code comments for implementation details
- Ensure all dependencies are properly installed

---




# Simple Calculator Application

A beautiful, responsive calculator web application with HTML frontend and Python Flask backend.

## Features

- ✨ Modern, glassmorphism UI design
- 🧮 Basic arithmetic operations (+, -, ×, ÷)
- ⌨️ Keyboard support
- 📱 Responsive design for mobile devices
- 🐍 Python Flask backend for calculations
- 🎨 Beautiful CSS animations and effects

## Technologies Used

- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Python Flask
- **Styling**: Modern CSS with gradients and glassmorphism effects

## Setup Instructions

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd cicd
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to:
```
http://localhost:5000
```

## Usage

- Click on number buttons to input numbers
- Use operation buttons (+, -, ×, ÷) for calculations
- Press "=" or Enter key to calculate
- Press "C" or Escape to clear
- Press "←" or Backspace to delete last character
- Supports keyboard input for all operations

## Project Structure

```
cicd/
├── index.html          # Main HTML file
├── style.css          # CSS styling
├── script.js          # Frontend JavaScript
├── app.py            # Python Flask backend
├── requirements.txt   # Python dependencies
└── README.md         # This file
```

## Features Explanation

### Frontend (HTML/CSS/JS)
- **index.html**: Main structure with calculator layout
- **style.css**: Beautiful styling with glassmorphism effects
- **script.js**: Interactive functionality and API communication

### Backend (Python Flask)
- **app.py**: Flask server handling calculations
- Validates expressions for security
- Handles mathematical operations safely
- Serves static files

## API Endpoints

- `GET /` - Serves the main calculator page
- `POST /calculate` - Processes calculation requests

## Contributing

This is a simple calculator project for educational purposes. Feel free to enhance it with additional features like:
- Scientific calculator functions
- History of calculations
- Themes and customization
- Unit tests

## License

This project is open source and available under the MIT License.
# Gauge & Yardage Calculator

A simple Flask web app that computes total stitches, rows, and estimated yarn yardage for knitting and crochet projects based on your gauge and swatch.

## 🚀 Features

- **Gauge Calculation**: Calculates total stitches and rows from your stitches-per-inch and rows-per-inch.
- **Yardage Estimation**: Estimates how many yards of yarn you’ll need, based on a measured swatch.
- **Web UI**: User-friendly form input and results pages built with Flask and HTML templates.
- **Responsive Styling**: Basic CSS for a clean, centered layout.

## 🛠️ Prerequisites

- Python 3.7 or higher  
- `pip` package manager  
- (Optional) Virtual environment tool such as `venv` or `virtualenv`

## 📦 Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/shek-titus/gauge-calculator.git
   cd YOUR_REPO
   ```

2. **Create and activate a virtual environment**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate      # macOS/Linux
   venv\Scripts\activate       # Windows
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ Running Locally

1. **Set the Flask environment** (optional, for debug info)  
   ```bash
   export FLASK_ENV=development   # macOS/Linux
   set FLASK_ENV=development      # Windows
   ```

2. **Start the server**  
   ```bash
   flask run
   ```

3. **Open your browser** at `http://127.0.0.1:5000`


## 🤝 Contributing

Contributions welcome! To propose improvements:

1. Fork the repo  
2. Create a feature branch (`git checkout -b feature-name`)  
3. Commit your changes (`git commit -m "Add new feature"`)  
4. Push to your branch (`git push origin feature-name`)  
5. Open a Pull Request

## 📄 License

This project is licensed under the [MIT License](LICENSE).

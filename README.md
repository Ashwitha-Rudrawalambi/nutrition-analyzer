# NutriLens AI - Food Nutrition Analysis

🍎 **AI-powered food recognition and nutritional analysis using DenseNet-161**

## 🚀 Key Features

- **Food Image Recognition**: Upload food images for automatic classification
- **Nutritional Analysis**: Get detailed nutritional information for identified foods
- **High Accuracy**: 93.27% Top-1 accuracy on Food-101 dataset
- **Web Interface**: User-friendly Flask application
- **Responsive Design**: Works on desktop and mobile devices

## 🏆 Performance

| Model | Top-1 Accuracy | Top-5 Accuracy |
|-------|----------------|----------------|
| **DenseNet-161 (Ours)** | **93.27%** | **99.02%** |
| ResNet-200 | 88.38% | 97.85% |
| Inception V3 | 88.28% | 96.88% |
| DeepFood | 77.4% | 93.7% |

## 🛠️ Technology Stack

- **Backend**: Python, Flask
- **AI Model**: DenseNet-161 (PyTorch)
- **Frontend**: HTML, CSS, JavaScript
- **Styling**: Tailwind CSS
- **Dataset**: Food-101 (101 food categories)

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/NutriLens-AI-Food-Nutrition.git
   cd NutriLens-AI-Food-Nutrition
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser** and go to `http://localhost:5000`

## 🎯 Usage

1. **Upload Image**: Click "Choose File" and select a food image
2. **Or Enter Food Name**: Type the name of a food item
3. **Get Results**: View nutritional information and analysis

## 📁 Project Structure

```
NutriLens-AI-Food-Nutrition/
├── app.py                 # Main Flask application
├── inference.py           # AI model inference
├── Nutridata.py          # Nutrition data handling
├── food_classifier.pt    # Trained model file
├── templates/            # HTML templates
├── static/               # Static files (CSS, JS)
└── Assets/              # Images and assets
```

## 🔬 Technical Details

- **Model**: DenseNet-161 with transfer learning
- **Dataset**: Food-101 (101,000 images across 101 food categories)
- **Training**: 4-5 days on Apple M3 Pro with 18GB RAM
- **Optimizer**: Adam with learning rate 0.001
- **Data Augmentation**: Random rotation, crop, flip, ImageNet policy

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📞 Contact

- **Email**: iam.vivekgera@gmail.com
- **GitHub**: [@Vivek-Gera](https://github.com/Vivek-Gera)

## 📄 License

This project is licensed under the MIT License.

---

**Made with ❤️ by Vivek Gera**

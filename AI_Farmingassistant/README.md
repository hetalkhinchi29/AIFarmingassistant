# 🌾 Smart Farming Assistant

An AI-powered agricultural recommendation system built with Streamlit and Google's Gemini 1.5 API. This application provides farmers with personalized, data-driven insights for crop management, pest control, irrigation strategies, and more.

## 🌟 Features

- **Intelligent Crop Recommendations**: Get stage-specific advice for your crops
- **Pest & Disease Management**: AI-powered strategies for protecting your harvest
- **Water Management**: Optimized irrigation schedules based on crop needs
- **Fertilizer Guidance**: NPK requirements and application schedules
- **Budget-Conscious Solutions**: Recommendations tailored to your budget constraints
- **Analytics Dashboard**: Visualize your farming queries and trends
- **Query History**: Access all your previous recommendations
- **Multi-Device Support**: Responsive design works on desktop, tablet, and mobile

## 🚀 Live Demo

**Deployed App URL**: [Will be available after Streamlit Cloud deployment]

## 📋 Prerequisites

- Python 3.8 or higher
- Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))
- Git (for version control)

## 🛠️ Local Installation

### Step 1: Clone the Repository

```bash
git clone <your-repository-url>
cd smart-farming-assistant
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

## 🌐 Deployment on Streamlit Cloud

### Step 1: Prepare Your GitHub Repository

1. Create a new repository on GitHub
2. Push your code:

```bash
git init
git add .
git commit -m "Initial commit: Smart Farming Assistant"
git branch -M main
git remote add origin <your-repository-url>
git push -u origin main
```

### Step 2: Deploy on Streamlit Cloud

1. Go to [Streamlit Cloud](https://streamlit.io/cloud)
2. Sign in with your GitHub account
3. Click "New app"
4. Select your repository and branch (main)
5. Set the main file path: `app.py`
6. Click "Deploy"

### Step 3: Configuration

- The app will automatically install dependencies from `requirements.txt`
- Deployment typically takes 2-5 minutes
- You'll receive a public URL like: `https://your-app-name.streamlit.app`

## 🔑 Getting Your Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the key and paste it in the app's sidebar

**Note**: Keep your API key secure and never commit it to GitHub!

## 📱 Testing Across Devices

### Desktop Testing
- **Chrome**: Full functionality ✅
- **Firefox**: Full functionality ✅
- **Safari**: Full functionality ✅
- **Edge**: Full functionality ✅

### Mobile Testing
- **iOS Safari**: Responsive design ✅
- **Android Chrome**: Responsive design ✅
- **Tablet View**: Optimized layout ✅

### Testing Checklist
- [ ] Form inputs work correctly
- [ ] API calls execute successfully
- [ ] Visualizations render properly
- [ ] Download buttons function
- [ ] Navigation between tabs works
- [ ] History stores correctly
- [ ] Responsive layout on small screens

## 📂 Project Structure

```
smart-farming-assistant/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # Documentation (this file)
└── .gitignore            # Git ignore file
```

## 🎯 How to Use

1. **Enter API Key**: Paste your Gemini API key in the sidebar
2. **Fill Location Details**: Provide your farming location and environment info
3. **Enter Crop Information**: Specify your crop, stage, and farm size
4. **Set Preferences**: Choose farming type, irrigation method, and concerns
5. **Get Recommendations**: Click the button to receive AI-powered advice
6. **View Analytics**: Check the Analytics tab for insights
7. **Access History**: Review previous queries in the History tab

## 🔍 Features Breakdown

### 1. Get Recommendations Tab
- Interactive form with multiple input fields
- Real-time API integration with Gemini 1.5
- Formatted, comprehensive recommendations
- Download functionality for offline access

### 2. Analysis & Insights Tab
- Query statistics and metrics
- Crop distribution bar chart
- Growth stage pie chart
- Recent queries table

### 3. History Tab
- Chronological list of all queries
- Expandable recommendation cards
- Individual download options

## 📊 Libraries Used

| Library | Purpose |
|---------|---------|
| `streamlit` | Web interface and UI components |
| `google-generativeai` | Gemini API integration |
| `requests` | HTTP requests handling |
| `pandas` | Data manipulation and analysis |
| `matplotlib` | Data visualization (charts) |
| `seaborn` | Enhanced chart styling |

## 🐛 Troubleshooting

### API Key Issues
- **Error**: "Invalid API key"
  - **Solution**: Verify your key at Google AI Studio
  - Ensure no extra spaces when pasting

### Import Errors
- **Error**: "Module not found"
  - **Solution**: Run `pip install -r requirements.txt`
  - Check Python version (3.8+)

### Deployment Issues
- **Error**: "App failed to build"
  - **Solution**: Verify requirements.txt format
  - Check for syntax errors in app.py

## 🔒 Security Notes

- **Never commit API keys** to GitHub
- Use environment variables for sensitive data
- The app stores history in session state (cleared on refresh)
- No permanent data storage or user tracking

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Authors

- **Your Name** - *Initial work*

## 🙏 Acknowledgments

- Google Gemini AI for powerful language models
- Streamlit for the amazing web framework
- Agricultural experts for domain knowledge
- Open source community for libraries and tools

## 📞 Support

For questions or issues:
- Open an issue on GitHub
- Contact: your-email@example.com

## 🔮 Future Enhancements

- [ ] Weather API integration for real-time data
- [ ] Image upload for pest/disease identification
- [ ] Multi-language support
- [ ] Export recommendations as PDF
- [ ] User authentication and data persistence
- [ ] Community forum for farmers
- [ ] Market price integration
- [ ] Crop yield prediction models

---

**Built with ❤️ for farmers | Powered by AI | Deploy with Confidence**

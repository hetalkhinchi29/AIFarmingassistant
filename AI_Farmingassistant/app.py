import streamlit as st
import google.generativeai as genai
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import json

# Page configuration
st.set_page_config(
    page_title="🌾 Smart Farming Assistant",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #2E7D32;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 1.1rem;
        padding: 0.5rem 2rem;
        border-radius: 10px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .recommendation-box {
        background-color: #f0f8f0;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #4CAF50;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'history' not in st.session_state:
    st.session_state.history = []

# Sidebar for API key and settings
with st.sidebar:
    st.header("⚙️ Configuration")
    api_key = st.text_input(
        "Enter Gemini API Key",
        type="password",
        help="Get your API key from Google AI Studio: https://makersuite.google.com/app/apikey"
    )
    
    st.markdown("---")
    st.header("📊 App Statistics")
    st.metric("Total Queries", len(st.session_state.history))
    
    st.markdown("---")
    st.header("ℹ️ About")
    st.info("""
    **Smart Farming Assistant** uses Google's Gemini 1.5 AI to provide:
    - Crop recommendations
    - Pest management advice
    - Irrigation strategies
    - Fertilizer suggestions
    - Weather-based insights
    """)
    
    if st.button("Clear History"):
        st.session_state.history = []
        st.rerun()

# Main header
st.markdown('<h1 class="main-header">🌾 Smart Farming Assistant</h1>', unsafe_allow_html=True)
st.markdown("##### Get AI-powered agricultural recommendations tailored to your farming needs")

# Check if API key is provided
if not api_key:
    st.warning("⚠️ Please enter your Gemini API key in the sidebar to continue.")
    st.info("""
    **To get started:**
    1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
    2. Create or sign in to your Google account
    3. Generate an API key
    4. Paste it in the sidebar
    """)
    st.stop()

# Configure Gemini API
try:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"❌ Error configuring API: {str(e)}")
    st.stop()

# Create tabs for different sections
tab1, tab2, tab3 = st.tabs(["🌱 Get Recommendations", "📈 Analysis & Insights", "📜 History"])

with tab1:
    # Input form
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📍 Location Details")
        location = st.text_input(
            "Location/Region",
            placeholder="e.g., Punjab, India",
            help="Enter your farming location for region-specific advice"
        )
        
        climate = st.selectbox(
            "Climate Type",
            ["Tropical", "Subtropical", "Temperate", "Arid", "Semi-Arid", "Mediterranean"]
        )
        
        soil_type = st.selectbox(
            "Soil Type",
            ["Clay", "Sandy", "Loamy", "Silt", "Peat", "Chalky", "Not Sure"]
        )
    
    with col2:
        st.subheader("🌾 Crop Information")
        crop_name = st.text_input(
            "Crop Name",
            placeholder="e.g., Wheat, Rice, Cotton",
            help="Enter the crop you're growing or planning to grow"
        )
        
        crop_stage = st.selectbox(
            "Current Crop Stage",
            [
                "Planning/Pre-Sowing",
                "Sowing/Planting",
                "Germination",
                "Vegetative Growth",
                "Flowering",
                "Fruiting/Grain Filling",
                "Maturity/Harvest"
            ]
        )
        
        farm_size = st.number_input(
            "Farm Size (acres)",
            min_value=0.1,
            max_value=10000.0,
            value=10.0,
            step=0.5
        )
    
    st.subheader("🎯 Farming Preferences & Concerns")
    
    col3, col4 = st.columns(2)
    
    with col3:
        farming_type = st.selectbox(
            "Farming Type",
            ["Conventional", "Organic", "Mixed/Integrated", "Precision Farming"]
        )
        
        irrigation_type = st.selectbox(
            "Irrigation Method",
            ["Drip", "Sprinkler", "Flood", "Rain-fed", "Mixed Methods"]
        )
    
    with col4:
        specific_concerns = st.multiselect(
            "Specific Concerns/Focus Areas",
            [
                "Pest Control",
                "Disease Management",
                "Fertilizer Optimization",
                "Water Management",
                "Yield Improvement",
                "Cost Reduction",
                "Soil Health",
                "Weather Challenges"
            ]
        )
        
        budget_constraint = st.selectbox(
            "Budget Level",
            ["Low Budget", "Moderate Budget", "High Budget", "No Constraint"]
        )
    
    additional_info = st.text_area(
        "Additional Information (Optional)",
        placeholder="Any other details about your farming situation, challenges, or specific questions...",
        height=100
    )
    
    # Generate recommendations button
    if st.button("🚀 Get AI Recommendations", use_container_width=True):
        if not location or not crop_name:
            st.error("❌ Please fill in at least Location and Crop Name to continue.")
        else:
            with st.spinner("🤖 Analyzing your farming data and generating recommendations..."):
                try:
                    # Create detailed prompt for Gemini
                    prompt = f"""
As an expert agricultural consultant, provide comprehensive farming recommendations based on the following details:

**Location & Environment:**
- Location: {location}
- Climate Type: {climate}
- Soil Type: {soil_type}

**Crop Information:**
- Crop: {crop_name}
- Current Stage: {crop_stage}
- Farm Size: {farm_size} acres

**Farming Practices:**
- Farming Type: {farming_type}
- Irrigation Method: {irrigation_type}
- Budget Level: {budget_constraint}

**Focus Areas:** {', '.join(specific_concerns) if specific_concerns else 'General recommendations'}

**Additional Context:** {additional_info if additional_info else 'None'}

Please provide:
1. **Stage-Specific Recommendations**: Detailed advice for the current crop stage
2. **Pest & Disease Management**: Prevention and treatment strategies
3. **Fertilizer & Nutrition**: NPK requirements and application schedule
4. **Water Management**: Irrigation frequency and quantity
5. **Expected Timeline**: Key dates and milestones
6. **Cost Estimates**: Approximate costs for recommended interventions
7. **Best Practices**: Tips for maximizing yield and quality
8. **Risk Alerts**: Potential challenges to watch for

Format the response clearly with sections and bullet points for easy reading.
"""
                    
                    # Call Gemini API
                    response = model.generate_content(prompt)
                    recommendations = response.text
                    
                    # Store in history
                    st.session_state.history.append({
                        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        'location': location,
                        'crop': crop_name,
                        'stage': crop_stage,
                        'recommendations': recommendations
                    })
                    
                    # Display recommendations
                    st.success("✅ Recommendations generated successfully!")
                    st.markdown('<div class="recommendation-box">', unsafe_allow_html=True)
                    st.markdown(recommendations)
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    # Download button
                    st.download_button(
                        label="📥 Download Recommendations (TXT)",
                        data=recommendations,
                        file_name=f"farming_recommendations_{crop_name}_{datetime.now().strftime('%Y%m%d')}.txt",
                        mime="text/plain"
                    )
                    
                except Exception as e:
                    st.error(f"❌ Error generating recommendations: {str(e)}")
                    st.info("Please check your API key and try again.")

with tab2:
    st.subheader("📊 Farming Analytics Dashboard")
    
    if st.session_state.history:
        # Create DataFrame from history
        df = pd.DataFrame(st.session_state.history)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Total Queries", len(df))
        
        with col2:
            unique_crops = df['crop'].nunique()
            st.metric("Unique Crops", unique_crops)
        
        with col3:
            most_common_crop = df['crop'].mode()[0] if len(df) > 0 else "N/A"
            st.metric("Most Queried Crop", most_common_crop)
        
        # Visualizations
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Crop Distribution")
            crop_counts = df['crop'].value_counts()
            
            fig, ax = plt.subplots(figsize=(8, 6))
            colors = sns.color_palette("Greens", len(crop_counts))
            crop_counts.plot(kind='bar', ax=ax, color=colors)
            ax.set_xlabel("Crop Name", fontsize=12)
            ax.set_ylabel("Number of Queries", fontsize=12)
            ax.set_title("Queries by Crop Type", fontsize=14, fontweight='bold')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            st.pyplot(fig)
        
        with col2:
            st.subheader("Growth Stage Distribution")
            stage_counts = df['stage'].value_counts()
            
            fig, ax = plt.subplots(figsize=(8, 6))
            colors = sns.color_palette("YlGn", len(stage_counts))
            ax.pie(stage_counts, labels=stage_counts.index, autopct='%1.1f%%',
                   startangle=90, colors=colors)
            ax.set_title("Queries by Crop Stage", fontsize=14, fontweight='bold')
            st.pyplot(fig)
        
        # Show recent queries table
        st.markdown("---")
        st.subheader("Recent Queries Overview")
        display_df = df[['timestamp', 'location', 'crop', 'stage']].copy()
        display_df = display_df.sort_values('timestamp', ascending=False).head(10)
        st.dataframe(display_df, use_container_width=True)
        
    else:
        st.info("📊 No data available yet. Generate some recommendations to see analytics!")

with tab3:
    st.subheader("📜 Query History")
    
    if st.session_state.history:
        # Reverse to show newest first
        for idx, entry in enumerate(reversed(st.session_state.history)):
            with st.expander(
                f"🌾 {entry['crop']} - {entry['location']} | {entry['timestamp']}",
                expanded=(idx == 0)
            ):
                st.markdown(f"**Crop Stage:** {entry['stage']}")
                st.markdown("**Recommendations:**")
                st.markdown(entry['recommendations'])
                
                st.download_button(
                    label="📥 Download This Recommendation",
                    data=entry['recommendations'],
                    file_name=f"recommendation_{entry['crop']}_{entry['timestamp'].replace(':', '-')}.txt",
                    mime="text/plain",
                    key=f"download_{idx}"
                )
    else:
        st.info("📜 No history available yet. Start by getting some recommendations!")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>🌾 Smart Farming Assistant | Powered by Google Gemini 1.5 API</p>
    <p>Built with ❤️ using Streamlit | © 2025</p>
</div>
""", unsafe_allow_html=True)

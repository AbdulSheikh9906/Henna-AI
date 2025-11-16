from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import streamlit as st
from dotenv import load_dotenv
import os
import random
import base64

# Helper: Convert image to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# Step 1: Configure API key
load_dotenv()
api_key = os.getenv("API_KEY")
client = genai.Client(api_key=api_key)

# Step 2: Streamlit page setup
st.set_page_config(
    page_title="Khushi Mehndi Arts",
    page_icon="logo.jpg",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Step 3: Custom CSS for modern UI
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #fff5f7, #f9fafb);
    font-family: 'Segoe UI', sans-serif;
}
section[data-testid="stSidebar"] {
    background: #fdf2f8;
}
.main-title {
    color: #2d3748;
    font-size: 3rem;
    font-weight: bold;
    text-align: center;
    margin-top: 1.5rem;
    animation: fadeIn 2s ease-in-out;
}
.subtitle {
    color: #e75480;
    font-size: 1.5rem;
    text-align: center;
    margin-bottom: 2rem;
    font-style: italic;
}
.stButton>button {
    background: linear-gradient(90deg, #e75480, #2563eb);
    color: white;
    border-radius: 10px;
    font-weight: bold;
    border: none;
    padding: 0.6rem 1.8rem;
    transition: 0.3s;
}
.stButton>button:hover {
    background: linear-gradient(90deg, #2563eb, #e75480);
    transform: scale(1.05);
}
.element-container img {
    border: 4px solid #e75480;
    border-radius: 16px;
    background: #fff;
    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
}
@keyframes fadeIn {
    from {opacity: 0;}
    to {opacity: 1;}
}
</style>
""", unsafe_allow_html=True)

# Step 4: App header
image_base64 = get_base64_image("logo.jpg")
st.markdown(f"""
<div style="display:flex; justify-content:center; margin-top:1rem;">
    <div style="width:200px; height:200px; border-radius:50%; overflow:hidden; 
                box-shadow:0 0 15px rgba(0,0,0,0.3);">
        <img src="data:image/jpeg;base64,{image_base64}" style="width:100%; height:100%; object-fit:cover;">
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🌸 Khushi Mehndi Arts</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">✨ Let us color your hands with elegance ✨</div>', unsafe_allow_html=True)

mehndi_quotes = [
    "🌿 Mehndi adds a touch of magic to every celebration.",
    "💫 Let your hands shine with the charm of beautiful Mehndi designs.",
    "🎉 No festive look is complete without a swirl of Mehndi.",
    "🌸 Mehndi brings color, joy, and elegance to every occasion.",
    "😊 The darker the Mehndi, the brighter the smiles!"
]

# Step 5: Sidebar
with st.sidebar:
    st.image("logo.jpg", caption="Khushi Mehndi Arts", use_container_width=True)
    mehndi_type = st.selectbox("🎨 Select Mehndi Style", [
        "Pakistani Mehndi Design - Intricate floral & geometric motifs",
        "Arabic Mehndi Design - Bold floral with flowing lines",
        "Indian Mehndi Design - Peacock motifs & rich patterns",
        "Portrait Mehndi Design - Artistic faces & portraits",
        "Moroccan Mehndi Design - Geometric symmetric bold patterns",
        "Bridal Mehndi Design - Complex wedding designs (hands & feet)",
        "Jewellery Mehndi Design - Inspired by jewelry curves",
        "Tattoo Mehndi Design - Minimalist tattoo-like designs",
        "Western-style Mehndi - Fusion of Mehndi & Western art",
        "African Mehndi Design - Bold circular & linear patterns",
        "Punjabi Mehndi Design - Vibrant cultural motifs"
    ])
    hand_type = st.selectbox("🖐 Select Hand Type", [
        "Toddlerhood (2-4 years)",
        "Childhood (5-12 years)",
        "Adolescence (13-19 years)",
        "Young Adulthood (20-39 years)",
        "Middle Adulthood (40-59 years)",
        "Senior Adulthood (60+ years)"
    ])
    occasion = st.selectbox("🎊 Select Occasion", ['Eid', 'Wedding', 'Festival', 'Party', 'Casual', 'Other'], index=0)
    complexity = st.slider("⚡ Complexity Level", 1, 5, 2, step=1, help="1 = Simple, 5 = Complex")
    user_command = st.text_input("✍️ Add Custom Text on Hand (optional):", value="")
    num_images = st.slider("🖼 Number of Designs", min_value=1, max_value=6, value=3)

# Step 6: Helper functions
def add_white_background(img):
    img = img.convert("RGBA")
    if img.mode == 'RGBA':
        background = Image.new("RGBA", img.size, (255, 255, 255, 255))
        background.paste(img, (0, 0), img)
        img = background.convert("RGB")
    else:
        img = img.convert("RGB")
    return img

def get_hand_description(hand_type):
    mapping = {
        "Toddlerhood (2-4 years)": "a toddler's hand (palm & back)",
        "Childhood (5-12 years)": "a child's hand (palm & back)",
        "Adolescence (13-19 years)": "a teenager's hand (palm & back)",
        "Young Adulthood (20-39 years)": "an adult's hand (palm & back)",
        "Middle Adulthood (40-59 years)": "a middle-aged adult's hand (palm & back)",
        "Senior Adulthood (60+ years)": "a senior adult's hand (palm & back)"
    }
    return mapping.get(hand_type, "an adult's hand (palm & back)")

# Step 7: Generate button
if st.button("✨ Generate Mehndi Design ✨"):
    with st.spinner("🎨 Crafting your beautiful Mehndi design..."):
        st.success(random.choice(mehndi_quotes))
        hand_description = get_hand_description(hand_type)
        detailed_command = (
            "You are an expert Mehndi artist. Generate ONE realistic human hand — "
            "with EXACTLY 5 fingers (1 thumb + 4 fingers). "
            f"The hand must resemble: {hand_description}. "
            "Show only a single hand with a white background. "
            f"Apply {mehndi_type} style Mehndi suitable for {occasion}, "
            f"with complexity level {complexity}. "
            "Do NOT generate more than one hand or any other object."
        )
        if user_command.strip():
            detailed_command += f" Also, write this text: '{user_command.strip()}'"

        images = []
        for _ in range(num_images):
            try:
                response = client.models.generate_content(
                    model="gemini-2.0-flash-exp-image-generation",
                    contents=detailed_command,
                    config=types.GenerateContentConfig(response_modalities=['Text', 'Image'])
                )
                for part in response.candidates[0].content.parts:
                    if part.inline_data is not None:
                        image = Image.open(BytesIO(part.inline_data.data))
                        image = add_white_background(image)
                        images.append(image)
            except Exception as e:
                st.error(f"Error: {e}")
                break

        if images:
            cols = st.columns(len(images))
            for idx, img in enumerate(images):
                img = img.resize((600, 700))
                with cols[idx]:
                    st.image(img, caption=f"🌸 Mehndi Design {idx + 1}", use_container_width=False)
        else:
            st.error("⚠️ No images generated. Please try again.")

import streamlit as st
import requests
from fpdf import FPDF
from bs4 import BeautifulSoup

# Initialize session state
if 'itinerary' not in st.session_state:
    st.session_state.itinerary = None

# Configuration
OLLAMA_MODEL = "llama3"
OLLAMA_URL = "http://localhost:11434/api/generate"

# Generate itinerary using local AI model
def generate_itinerary(location, destination, days, interests, budget_inr):
    prompt = f"""
    You are a helpful travel assistant. Create a {days}-day itinerary for someone traveling from {location} to {destination}.
    They are interested in {interests}, and have a total budget of ₹{budget_inr}.
    Break each day into morning, afternoon, and evening plans.
    Add estimated INR costs per day.
    Be realistic, creative, and concise.
    """
    payload = {"model": OLLAMA_MODEL, "prompt": prompt, "stream": False}

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        return response.json().get("response", "❌ No response generated.").strip()
    except requests.exceptions.ConnectionError:
        return "⚠️ Ollama server not reachable. Is it running?"
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

# Simple PDF generator using built-in font
def create_pdf_bytes(text):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    sanitized_text = text.replace("₹", "Rs. ")  # Replace ₹ if font unsupported
    for line in sanitized_text.split("\n"):
        pdf.multi_cell(0, 10, line)
    return pdf.output(dest='S').encode('latin1')

# Google Image Scraper – returns multiple image URLs
def get_multiple_images_from_google(destination, count=5):
    headers = {"User-Agent": "Mozilla/5.0"}
    query = destination.replace(' ', '+')
    url = f"https://www.google.com/search?tbm=isch&q={query}"
    image_urls = []

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        img_tags = soup.find_all('img')

        for img_tag in img_tags:
            # Prefer 'data-src' for better quality thumbnails
            src = img_tag.get('data-src') or img_tag.get('src')
            if src and src.startswith('http'):
                image_urls.append(src)
                if len(image_urls) >= count:
                    break
    except Exception as e:
        st.warning(f"Failed to fetch images: {e}")
    return image_urls


# UI setup
st.set_page_config(page_title="AI Travel Planner", page_icon="🧳")
st.title("🧭 Offline AI Travel Planner")
st.markdown("_Plan your trip privately using a local AI model._")

with st.expander("🌍 Travel Info"):
    col1, col2 = st.columns(2)
    with col1:
        location = st.text_input("Your Current Location", placeholder="e.g., Delhi")
    with col2:
        destination = st.text_input("Destination", placeholder="e.g., Tokyo")

with st.expander("✨ Preferences"):
    col3, col4 = st.columns(2)
    with col3:
        days = st.slider("Trip Length", 1, 14, 5)
    with col4:
        budget_inr = st.number_input("Total Budget (INR ₹)", min_value=1000, step=500, value=20000)
    interests = st.text_area("Interests", placeholder="e.g., hiking, cafes, museums")

st.divider()

# Generate itinerary
if st.button("🚀 Generate Itinerary"):
    if not location or not destination or not interests:
        st.warning("Please fill all fields.")
    else:
        with st.spinner("Planning your itinerary..."):
            itinerary = generate_itinerary(location, destination, days, interests, budget_inr)
            st.session_state.itinerary = itinerary

        st.success("Itinerary generated!")
        st.code(itinerary, language="markdown")

        # Show multiple destination images
            # Show multiple destination images in a grid
        st.subheader("📸 Destination Images")
        image_urls = get_multiple_images_from_google(destination, count=5)
        if image_urls:
            cols = st.columns(len(image_urls))
            for idx, (col, url) in enumerate(zip(cols, image_urls)):
                with col:
                    st.image(url, caption=f"{destination} ({idx+1})", use_container_width=True)
        else:
            st.warning("No images found for the destination.")


# Export section
if st.session_state.itinerary:
    st.subheader("📤 Export Options")

    # PDF Export
    try:
        pdf_bytes = create_pdf_bytes(st.session_state.itinerary)
        st.download_button(
            label="📄 Export as PDF",
            data=pdf_bytes,
            file_name="itinerary.pdf",
            mime="application/pdf"
        )
    except Exception as e:
        st.error(f"PDF generation failed: {str(e)}")

    # TXT Export
    st.download_button(
        label="📝 Export as TXT",
        data=st.session_state.itinerary.encode('utf-8'),
        file_name="itinerary.txt",
        mime="text/plain"
    )

    # Budget breakdown
    st.subheader("💰 Budget Breakdown")
    daily = round(budget_inr / days, 2)
    st.markdown(f"**Daily Estimated Budget:** Rs. {daily}")

    # Google Maps link
    maps_url = f"https://www.google.com/maps/dir/{location}/{destination}".replace(" ", "+")
    st.markdown(f"🗺️ [Open Google Maps]({maps_url})")

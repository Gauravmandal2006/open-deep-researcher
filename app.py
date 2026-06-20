from dotenv import load_dotenv
load_dotenv()


import streamlit as st
from datetime import datetime
from memory import HistoryManager
from utils import extract_pdf_text
from graph_builder import build_graph

# ===============================
# 🖼️ GEMINI VISION - IMAGE ANALYZER
# ===============================
import google.generativeai as genai
from PIL import Image as PILImage

def analyze_image(uploaded_image, api_key: str) -> str:
    """Analyze an uploaded image using Gemini Vision and return a text summary."""
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.5-flash")
    image = PILImage.open(uploaded_image)
    response = model.generate_content([
        """
        Analyze this image in detail.

        Extract:
        - Main topic
        - Important objects
        - Charts or graphs (if present)
        - Research insights
        - Key findings
        """,
        image
    ])
    return response.text

# ===============================
# 🎨 GLOBAL ADVANCED CSS
# ===============================
st.markdown("""
<style>

/* ---------- GLOBAL ---------- */
html, body, [class*="css"] {
    color: #e5e7eb !important;
    background-color: #020617 !important;
    font-family: 'Segoe UI', sans-serif;
}

/* ---------- MAIN APP ---------- */
.stApp {
    background: radial-gradient(circle at top, #020617, #020617);
}

/* ---------- SIDEBAR ---------- */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #020617, #020617);
    border-right: 1px solid #1f2937;
}

section[data-testid="stSidebar"] * {
    color: #e5e7eb !important;
}

/* ---------- HEADINGS ---------- */
.hero-title {
    font-size: 3rem;
    font-weight: 800;
    background: linear-gradient(90deg, #38bdf8, #22c55e);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* ---------- SETTINGS TITLES ---------- */
h1, h2, h3, h4 {
    color: #e5e7eb !important;
}

/* ---------- INPUT ---------- */
.stChatInput textarea {
    background: #020617 !important;
    color: #e5e7eb !important;
    border-radius: 14px;
    border: 1px solid #1f2937;
}

/* ---------- CHAT MESSAGES ---------- */
.stChatMessage {
    background: #020617;
    border-radius: 16px;
    padding: 16px;
    border: 1px solid #1f2937;
}

/* Assistant message */
.stChatMessage[data-testid="chat-message-assistant"] {
    background: #020617;
}

/* User message */
.stChatMessage[data-testid="chat-message-user"] {
    background: #020617;
}

/* ---------- MARKDOWN OUTPUT ---------- */
.stMarkdown, .stMarkdown p, .stMarkdown li {
    color: #e5e7eb !important;
}

/* ---------- BUTTONS ---------- */
.stButton > button {
    width: 100%;
    padding: 0.7rem;
    border-radius: 14px;
    font-weight: 600;
    background: linear-gradient(90deg,#2563eb,#22c55e);
    color: white;
    border: none;
    transition: all 0.2s ease-in-out;
}

.stButton > button:hover {
    transform: scale(1.03);
    opacity: 0.9;
}

/* ---------- EXPANDERS ---------- */
details {
    background: #020617;
    border-radius: 12px;
    border: 1px solid #1f2937;
    padding: 10px;
}

/* ---------- STATUS BOX ---------- */
div[data-testid="stStatusWidget"] {
    background: #020617;
    border-radius: 14px;
    border: 1px solid #1f2937;
    color: #e5e7eb;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# 🔐 IMPORT API KEYS FROM CONFIG
# ==========================================
from config import GOOGLE_API_KEY, TAVILY_API_KEY
# ==========================================

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Open Deep Research Agent",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- INITIALIZATION ---
memory = HistoryManager()

if "messages" not in st.session_state:
    st.session_state.messages = []
if "pdf_context" not in st.session_state:
    st.session_state.pdf_context = ""
if "pdf_name" not in st.session_state:
    st.session_state.pdf_name = None
# ✅ FIX 1: Added missing image session states
if "image_context" not in st.session_state:
    st.session_state.image_context = ""
if "image_name" not in st.session_state:
    st.session_state.image_name = None

# --- SIDEBAR ---
with st.sidebar:

    # TABS
    tab_settings, tab_upload, tab_history = st.tabs(["⚙️ Settings", "📎 Upload", "📚 History"])

    # --- TAB 1: SETTINGS ---
    with tab_settings:
        if GOOGLE_API_KEY and TAVILY_API_KEY:
            st.success(" API Keys Loaded successfully")
        else:
            st.error("❌ Keys missing in config.py")

        st.divider()

        st.subheader("🔍 Search Focus")
        search_mode = st.radio("Target:", ["General Web", "Academic Papers"], index=0)

        st.divider()

        st.subheader("📝 Output Length")
        report_type = st.radio("Detail Level:", ["Detailed Report", "Short Summary"], index=0)
        length_map = {"Detailed Report": "Detailed", "Short Summary": "Short"}
        selected_length = length_map[report_type]

    # ✅ FIX 2: Entire tab_upload block is now correctly indented inside with tab_upload:
    # --- TAB 2: PDF & IMAGE UPLOAD ---
    with tab_upload:
        st.subheader("📄📷 Research Context")

        # ==========================
        # PDF UPLOAD
        # ==========================
        st.markdown("### 📄 Upload PDF")

        if not st.session_state.pdf_name:
            uploaded_file = st.file_uploader(
                "Choose PDF",
                type=["pdf"],
                key="pdf_uploader"
            )

            if uploaded_file:
                with st.spinner("Extracting PDF text..."):
                    raw_text = extract_pdf_text(uploaded_file)
                    st.session_state.pdf_context = raw_text
                    st.session_state.pdf_name = uploaded_file.name
                    st.success("PDF uploaded successfully")
                    st.rerun()

        else:
            st.success(f"📄 Active PDF: {st.session_state.pdf_name}")

            if st.button("❌ Remove PDF"):
                st.session_state.pdf_context = ""
                st.session_state.pdf_name = None
                st.rerun()

        st.divider()

        # image upload lives here — user can drop any chart, diagram or screenshot
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #0f172a, #1e293b);
            border: 1px solid #334155;
            border-radius: 14px;
            padding: 16px 18px 10px 18px;
            margin-bottom: 10px;
        ">
            <div style="font-size:1.1rem; font-weight:700; color:#38bdf8; margin-bottom:4px;">
                📷 Upload Image
            </div>
            <div style="font-size:0.8rem; color:#64748b;">
                Drop a chart, diagram, or any research image — Gemini will read it for you
            </div>
        </div>
        """, unsafe_allow_html=True)

        # nothing uploaded yet — show the file picker
        if not st.session_state.image_name:
            uploaded_image = st.file_uploader(
                "Choose an image file",
                type=["png", "jpg", "jpeg"],
                key="image_uploader",
                label_visibility="collapsed"
            )

            if uploaded_image:
                # preview it immediately so user knows it came through
                st.image(
                    uploaded_image,
                    caption=f"📎 {uploaded_image.name}",
                    use_container_width=True
                )

                # pass it to Gemini Vision and save what it finds
                with st.spinner("🔍 Gemini is reading your image..."):
                    try:
                        image_summary = analyze_image(uploaded_image, GOOGLE_API_KEY)
                        st.session_state.image_context = image_summary
                        st.session_state.image_name = uploaded_image.name

                        st.success("✅ Image analyzed and ready to use in research!")

                        # let the user peek at what Gemini extracted
                        with st.expander("🧠 See what Gemini extracted"):
                            st.markdown(image_summary)

                    except Exception as e:
                        st.error(f"Something went wrong during image analysis: {e}")

        else:
            # image already loaded — show a clean status card instead of uploader
            st.markdown(f"""
            <div style="
                background: #0f2a1a;
                border: 1px solid #22c55e;
                border-radius: 12px;
                padding: 12px 16px;
                margin-bottom: 10px;
            ">
                <span style="color:#22c55e; font-weight:600;">📷 Active Image</span><br>
                <span style="color:#94a3b8; font-size:0.85rem;">{st.session_state.image_name}</span>
            </div>
            """, unsafe_allow_html=True)

            # let them review what Gemini found
            with st.expander("🧠 View image analysis"):
                st.markdown(st.session_state.image_context)

            # swap it out if they want a different image
            if st.button("🗑️ Remove Image", key="remove_image_btn"):
                st.session_state.image_context = ""
                st.session_state.image_name = None
                st.rerun()

    # --- BUTTONS (inside sidebar but outside tabs) ---
    # NEW CHAT BUTTON
    if st.button("Start New Chat"):
        st.session_state.messages = []
        st.session_state.pdf_context = ""
        st.session_state.pdf_name = None
        st.session_state.image_context = ""
        st.session_state.image_name = None
        st.rerun()

    # 🧹 CLEAR HISTORY
    if st.button("🧹 Clear History"):
        memory.clear_history()
        st.session_state.last_report = None
        st.warning("History cleared")

    if st.button("🧹 Clear Text", key="clear_text_btn"):
        st.session_state.pop("search_text", None)
        st.rerun()

    # --- TAB 3: HISTORY ---
    with tab_history:
        st.subheader("Past Researches")
        history = memory.load_history()
        if not history:
            st.caption("No history yet.")
        else:
            for entry in reversed(history):
                try:
                    dt_obj = datetime.strptime(entry['timestamp'], "%Y-%m-%d %H:%M")
                    date_label = dt_obj.strftime("%d %b %Y")
                except:
                    date_label = entry['timestamp']

                short_input = entry['input'][:15] + "..." if len(entry['input']) > 15 else entry['input']
                label = f"{date_label} - {short_input}"

                with st.expander(label):
                    st.caption(f"*Full Topic:* {entry['input']}")

                    col1, col2, col3 = st.columns(3)

                    with col1:
                        if st.button("👁️ View", key=f"view_{entry['id']}"):
                            @st.dialog("📜 Research Report")
                            def show_report():
                                st.subheader(entry['input'])
                                st.markdown(entry['report'])
                            show_report()

                    with col2:
                        if st.button("🔄 Resume", key=f"load_{entry['id']}"):
                            saved_history = entry.get('chat_history', None)
                            if saved_history:
                                st.session_state.messages = saved_history
                            else:
                                st.session_state.messages = [
                                    {"role": "user", "content": entry['input']},
                                    {"role": "assistant", "content": entry['report']}
                                ]
                            st.success("Chat Loaded!")
                            st.rerun()

                    with col3:
                        if st.button("🗑️ Delete", key=f"del_{entry['id']}"):
                            memory.delete_entry(entry['id'])
                            st.rerun()

# --- MAIN CHAT ---
if not st.session_state.messages:
    st.markdown("""
<div style="text-align:center; margin-top:30px; margin-bottom:10px;">
  <h1 class="hero-title">
    Open Deep Research Agent
  </h1>
  <p style="color:#94a3b8; font-size:1.1rem;">
    What would you like to research today ?
  </p>
</div>
""", unsafe_allow_html=True)

else:
    st.caption("Open Deep Research Agent")
    if st.session_state.pdf_name:
        st.info(f" *Active Context:* {st.session_state.pdf_name}")
    if st.session_state.image_name:
        st.info(f"📷 *Active Image:* {st.session_state.image_name}")

# Display Messages
for msg in st.session_state.messages:
    avatar = "🧑" if msg["role"] == "user" else "🤖"
    with st.chat_message(msg["role"], avatar=avatar):
        st.markdown(msg["content"])

# Chat Input
placeholder = "Ask a research question..." if st.session_state.messages else "Enter a topic..."

if prompt := st.chat_input(placeholder):
    if not GOOGLE_API_KEY or not TAVILY_API_KEY:
        st.error("⚠️ API Keys are missing in config.py!")
        st.stop()

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.rerun()

# Backend Execution
if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
    prompt = st.session_state.messages[-1]["content"]

    # --- BALANCED HISTORY STRATEGY ---
    recent_messages = st.session_state.messages[:-1]
    formatted_history = []

    for i, msg in enumerate(reversed(recent_messages)):
        role = msg['role'].upper()
        content = msg['content']
        if i > 2 and len(content) > 500:
            content = content[:200] + "... [Old Context Truncated]"
        formatted_history.insert(0, f"{role}: {content}")

    final_history_str = "\n".join(formatted_history[-10:])

    # ✅ FIX 4 & 5: Build final_topic handling all combinations of PDF + Image + Text
    final_topic = prompt
    mode = "Text"

    has_pdf = bool(st.session_state.pdf_context)
    has_image = bool(st.session_state.image_context)

    if has_pdf and has_image:
        pdf_limit = 100000
        final_topic = f"""User Query:
{prompt}

PDF Context:
{st.session_state.pdf_context[:pdf_limit]}

Image Context:
{st.session_state.image_context}"""
        mode = "PDF + Image"

    elif has_pdf:
        pdf_limit = 100000
        final_topic = f"User Query: {prompt}\n\nReference PDF Content: {st.session_state.pdf_context[:pdf_limit]}"
        mode = "PDF"

    elif has_image:
        final_topic = f"User Query: {prompt}\n\nImage Context:\n{st.session_state.image_context}"
        mode = "Image"

    with st.chat_message("assistant", avatar="🤖"):
        try:
            app_graph = build_graph(GOOGLE_API_KEY, TAVILY_API_KEY)

            # Status Indicator
            status_placeholder = st.status("🤖 Agent Working...", expanded=False)
            status_placeholder.write("🧠 Planner: Planning strategy...")
            status_placeholder.write("🔎 Searcher: Gathering papers via Tavily...")
            status_placeholder.write(f"✍️ Writer: Drafting {search_mode}...")

            final_state = app_graph.invoke({
                "topic": final_topic,
                "chat_history": final_history_str,
                "summary_length": selected_length,
                "search_mode": search_mode
            })

            report = final_state['final_report']
            status_placeholder.update(label="Complete", state="complete", expanded=False)

            st.markdown(report)

            st.session_state.messages.append({"role": "assistant", "content": report})
            memory.save_entry(prompt, mode, report, st.session_state.messages)

        except Exception as e:
            st.error(f"An error occurred: {e}")

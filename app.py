import streamlit as st
import joblib

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="MindMate",
    page_icon="🧠",
    layout="centered"
)

# -----------------------------
# Load trained AI model
# -----------------------------
model = joblib.load("emotion_model.pkl")


# -----------------------------
# Chatbot response functions
# -----------------------------
def get_response(emotion):
    responses = {
        "stress": (
            "It sounds like you're dealing with quite a lot of pressure right now. "
            "Try breaking the situation into one small task you can handle first."
        ),

        "anxiety": (
            "It sounds like your thoughts may be focused on what could happen next. "
            "Try bringing your attention back to what you can control right now."
        ),

        "sadness": (
            "It sounds like you're having a difficult moment. "
            "It may help to give yourself some time and consider talking to someone "
            "you trust about how you're feeling."
        ),

        "calmness": (
            "It's good to hear that you're feeling relatively calm. "
            "You could use this moment to reflect, relax, or continue something "
            "that you enjoy."
        )
    }

    return responses.get(
        emotion,
        "Thanks for sharing how you're feeling."
    )


# -----------------------------
# CBT thought reframing
# -----------------------------
def reframe_thought(text):
    return (
        "Let's look at that thought from a more balanced perspective.\n\n"
        f"**Your thought:** {text}\n\n"
        "**A possible balanced perspective:** "
        "This situation may be difficult, but one difficult moment does not "
        "necessarily determine the final outcome. Consider what is within "
        "your control and what small step you can take next."
    )


# -----------------------------
# Mindfulness exercise
# -----------------------------
def mindfulness_exercise():
    return (
        "### 🧘 Short Mindfulness Exercise\n\n"
        "1. Sit comfortably and take a slow breath.\n"
        "2. Notice your breathing without trying to change it.\n"
        "3. Notice a few things you can see around you.\n"
        "4. Notice the sensations you can feel.\n"
        "5. Bring your attention back to the present moment.\n"
        "6. Take one more comfortable breath."
    )


# -----------------------------
# Page heading
# -----------------------------
st.title("🧠 MindMate")
st.subheader("AI Emotional Wellness Chatbot")

st.write(
    "Share what's on your mind and MindMate will identify a possible "
    "emotional category and provide a supportive response."
)

st.info(
    "MindMate is an educational AI project and is not a replacement "
    "for a mental-health professional."
)


# -----------------------------
# Chat history
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# -----------------------------
# User input
# -----------------------------
user_input = st.chat_input("How are you feeling today?")


if user_input:

    # Add user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Predict emotion
    emotion = model.predict([user_input])[0]

    # Generate response
    response = get_response(emotion)

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Display AI response
    with st.chat_message("assistant"):
        st.markdown(response)
        st.caption(f"Detected emotion: {emotion.capitalize()}")


# -----------------------------
# Extra tools
# -----------------------------
st.divider()

st.subheader("🌱 Wellness Tools")

col1, col2 = st.columns(2)

with col1:
    if st.button("🧠 Reframe a Thought"):
        st.session_state.show_reframe = True

with col2:
    if st.button("🧘 Mindfulness Exercise"):
        st.session_state.show_mindfulness = True


if st.session_state.get("show_reframe", False):

    thought = st.text_input(
        "Enter a thought you'd like to examine:"
    )

    if thought:
        st.markdown(reframe_thought(thought))


if st.session_state.get("show_mindfulness", False):

    st.markdown(mindfulness_exercise())


# -----------------------------
# Footer
# -----------------------------
st.divider()

st.caption(
    "MindMate • AI Emotional Wellness Project"
)
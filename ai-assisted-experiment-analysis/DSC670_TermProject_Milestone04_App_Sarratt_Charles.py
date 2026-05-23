import os
from openai import OpenAI
from dotenv import load_dotenv
import streamlit as st


load_dotenv("openai.env")

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

FINE_TUNED_MODEL = (
    "ft:gpt-4o-mini-2024-07-18:personal:"
    "experiment-analysis-v3:DbSPQHKQ"
)


st.set_page_config(
    page_title="AI-Assisted Experiment Analysis",
    page_icon="📊",
    layout="centered"
)


st.title("AI-Assisted Experiment Analysis")
st.write(
    "This application uses a fine-tuned OpenAI model to interpret "
    "A/B test results and generate a structured recommendation."
)


with st.sidebar:
    st.header("Project Note")
    st.write(
        "This app was built for the DSC670 final project. The model was "
        "fine-tuned using synthetic A/B test scenarios, so the results should "
        "be treated as experimental rather than production-ready."
    )

    st.header("Synthetic Data Limitation")
    st.write(
        "Synthetic data was used because real experimentation data may be "
        "proprietary, sensitive, or unavailable. However, synthetic examples "
        "can reflect the assumptions of the system that created them and may "
        "not fully represent noisy real-world experiment data."
    )


st.subheader("Enter A/B Test Metrics")

control_rate = st.number_input(
    "Control Conversion Rate (%)",
    min_value=0.0,
    max_value=100.0,
    value=10.2,
    step=0.1
)

variant_rate = st.number_input(
    "Variant Conversion Rate (%)",
    min_value=0.0,
    max_value=100.0,
    value=11.8,
    step=0.1
)

sample_size = st.number_input(
    "Sample Size Per Group",
    min_value=1,
    value=8000,
    step=100
)

p_value = st.number_input(
    "P-value",
    min_value=0.0,
    max_value=1.0,
    value=0.04,
    step=0.01,
    format="%.3f"
)

lift = st.number_input(
    "Lift (%)",
    value=15.7,
    step=0.1
)


def build_prompt():
    return (
        f"Control Conversion Rate: {control_rate}%\n"
        f"Variant Conversion Rate: {variant_rate}%\n"
        f"Sample Size: {sample_size:,} per group\n"
        f"P-value: {p_value}\n"
        f"Lift: {lift:+.1f}%"
    )


def analyze_experiment(prompt):
    response = client.chat.completions.create(
        model=FINE_TUNED_MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a digital experimentation analyst. "
                    "Interpret A/B test results using the provided metrics."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content


if st.button("Analyze Experiment"):
    prompt = build_prompt()

    st.subheader("Input Sent to Model")
    st.code(prompt)

    with st.spinner("Analyzing experiment results..."):
        result = analyze_experiment(prompt)

    st.subheader("Model Recommendation")

    formatted_result = result.replace(
        "Summary:",
        "\n\n### Summary\n"
    ).replace(
        "Interpretation:",
        "\n\n### Interpretation\n"
    ).replace(
        "Recommendation:",
        "\n\n### Recommendation\n"
    )

    st.markdown(formatted_result)
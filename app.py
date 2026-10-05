import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans

st.title("🤖 AI Customer Segmentation Tool")

st.write("Upload customer data and create customer segments using K-Means AI.")

uploaded_file = st.file_uploader(
    "Upload Customer CSV",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    # Customer Data
    st.subheader("Customer Data")
    st.dataframe(df)

    # Select features for AI
    features = df[["Age", "AnnualIncome", "SpendingScore"]]

    # Create K-Means model
    model = KMeans(
        n_clusters=3,
        random_state=42,
        n_init=10
    )

    # Create customer segments
    df["Segment"] = model.fit_predict(features)

    # Show segmented customers
    st.subheader("Customer Segments")
    st.dataframe(df)

    st.success("AI Customer Segmentation completed!")

    # Customer Segments Chart
    st.subheader("📊 Customer Segments Chart")

    chart_data = df.groupby("Segment")["CustomerID"].count()

    st.bar_chart(chart_data)

    # Segment Summary
    st.subheader("📋 Segment Summary")

    summary = df.groupby("Segment")[[
        "Age",
        "AnnualIncome",
        "SpendingScore"
    ]].mean()

    st.dataframe(summary)
```

st.subheader("💡 Customer Recommendations")

recommendations = {
    "Low Value Customers": "Offer discounts and special promotions",
    "Potential Customers": "Send personalized offers to increase spending",
    "High Value Customers": "Give loyalty rewards and premium offers"
}

df["Recommendation"] = df["Segment Name"].map(recommendations)

st.dataframe(
    df[[
        "CustomerID",
        "Segment Name",
        "Recommendation"
    ]]
)

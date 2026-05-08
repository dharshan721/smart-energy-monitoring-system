import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Smart Energy Monitoring System")

st.title("Smart Energy Consumption Analysis System")

units = st.number_input("Enter Electricity Units", min_value=0)

if st.button("Analyze"):

    # Tamil Nadu Electricity Bill Calculation
    if units <= 100:
        bill = 0

    elif units <= 200:
        bill = (units - 100) * 2.35

    elif units <= 400:
        bill = (100 * 2.35) + ((units - 200) * 4.70)

    elif units <= 500:
        bill = (100 * 2.35) + (200 * 4.70) + \
               ((units - 400) * 6.30)

    else:
        bill = (100 * 2.35) + (200 * 4.70) + \
               (100 * 6.30) + ((units - 500) * 8.40)

    st.subheader(f"Tamil Nadu EB Bill: Rs {bill:.2f}")

    # Monthly Usage Data
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    usage = [units-20, units-10, units,
             units+10, units+20, units+15]

    # Bar Chart
    st.subheader("Energy Usage Analysis")

    fig, ax = plt.subplots()
    ax.bar(months, usage)

    ax.set_xlabel("Months")
    ax.set_ylabel("Units")

    st.pyplot(fig)

    # Pie Chart
    st.subheader("Electricity Usage Distribution")

    pie_data = [40, 25, 20, 15]
    labels = ['AC', 'Lights', 'Fans', 'Others']

    fig2, ax2 = plt.subplots()
    ax2.pie(pie_data, labels=labels, autopct='%1.1f%%')

    st.pyplot(fig2)

    # Suggestions
    st.subheader("Eco-Friendly Suggestions")

    if units > 300:
        st.warning("""
        - Use LED bulbs
        - Reduce AC usage
        - Turn off unused devices
        - Use energy efficient appliances
        """)
    else:
        st.success("""
        - Good Energy Usage
        - Maintain current usage habits
        """)

    # Save Report
    data = pd.DataFrame({
        'Month': months,
        'Energy Usage': usage
    })

    csv = data.to_csv(index=False)

    st.download_button(
        "Download Report",
        csv,
        "Energy_Report.csv",
        "text/csv"
    )

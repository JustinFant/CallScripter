import streamlit as st
import datetime
import pythoncom
from functions.format_script import format_script
from functions.verify_inputs import format_phone, verify_email, format_candidate_name, format_entries


st.set_page_config(page_title="BEPC-CallScripter", page_icon=":telephone_receiver:", layout="wide")
pythoncom.CoInitialize() # Initialize COM for threading

st.title("CallScripter")

# Get User Inputs || Eventually API call to get info
recruiter_name = st.text_input("Recruiter Name")
recruiter_phone = format_phone(st.text_input("Recruiter Phone Number")) # Auto Format Phone Number
candidate_name = st.text_input("Candidate Name")
application_location = st.selectbox("Application Location", ["Indeed", "Location 2", "Location 3"])
pay_rate = st.number_input("Pay Rate", value=None, step=0.01)
contract_length = st.number_input("Contract Length (Months)", value=None, step=1, max_value=12)
client_name = st.selectbox("Client Name", ["Client 1", "Client 2", "Client 3"])
work_location = st.text_input("Work Location")

# Auto Generate Email Based On Name
recruiter_email = verify_email(recruiter_name)

# Format Names
recruiter_name, candidate_name, work_location = format_entries(recruiter_name, candidate_name, work_location)

# Set Greeting Based On Time of Day
current_hour = datetime.datetime.now().hour
if current_hour < 12:
  greeting = "morning"
else:
  greeting = "afternoon"


if st.button("Generate Script", type="primary"):
  if recruiter_name and recruiter_email and recruiter_phone and candidate_name and application_location and pay_rate and contract_length and client_name and work_location:
    with st.spinner("Generating Script..."):
      # Format Script
      script = format_script(greeting, recruiter_name, recruiter_email, recruiter_phone, candidate_name, application_location, pay_rate, contract_length, client_name, work_location)

      # Display Results
      st.success("Script Generated!")
      st.download_button("Download Script", data=script.getvalue(), file_name=f"{format_candidate_name(candidate_name)}_CALL_SCRIPT.pdf", mime="application/pdf")
          
  # Throw Error if any fields are empty
  else:
    st.error("Please fill in all fields before generating script.")
   
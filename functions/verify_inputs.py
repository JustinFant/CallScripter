# Functions to verify and format user inputs
import re

# Format Phone Number
def format_phone(recruiter_phone) -> str:
  stripped_phone = re.sub(r'\D', '', recruiter_phone)
  return f"({stripped_phone[:3]}) {stripped_phone[3:6]}-{stripped_phone[6:]}"


# Format Candidate Name for File Name
def format_candidate_name(candidate_name) -> str:
  return candidate_name.upper().replace(" ", "_")


# Format Email from Recruiter Name
def verify_email(recruiter_name) -> str:
  recruiter_name = recruiter_name.lower().strip().replace(" ", ".")
  recruiter_email = recruiter_name + "@bepcinc.com"
  return recruiter_email


# Format Names for Script
def format_entries(recruiter_name, candidate_name, work_location) -> tuple[str, str, str]:
  return recruiter_name.title(), candidate_name.title(), work_location.title()
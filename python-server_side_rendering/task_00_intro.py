import os

def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template and list of attendee dictionaries.
    Handles errors and missing data gracefully.

    Args:
        template (str): Template string with placeholders.
        attendees (list): List of dictionaries with attendee data.
    """
    # Check if template is a string
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    # Check if attendees is a list of dictionaries
    if not (isinstance(attendees, list) and all(isinstance(a, dict) for a in attendees)):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Check empty template
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # Check empty attendees
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # For each attendee, generate a personalized invitation
    for idx, attendee in enumerate(attendees, 1):
        # Prepare values and replace None or missing with "N/A"
        values = {}
        for key in ["name", "event_title", "event_date", "event_location"]:
            val = attendee.get(key)
            if val is None:
                values[key] = "N/A"
            else:
                values[key] = str(val)

        # Replace placeholders
        invitation = template
        for key in values:
            invitation = invitation.replace("{" + key + "}", values[key])

        # Write to output file
        filename = f"output_{idx}.txt"
        try:
            with open(filename, "w") as f:
                f.write(invitation)
        except Exception as e:
            print(f"Error writing to {filename}: {e}")

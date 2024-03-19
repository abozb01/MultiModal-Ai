def identify_issue(user_input):
    # List of keywords related to common issues
    common_issues = ['Microsoft Teams', 'login', 'video call', 'audio issues', 'screen sharing']

    # Check if any keyword is present in the user input
    for keyword in common_issues:
        if keyword.lower() in user_input.lower():
            return keyword
    
    # If no keyword is found, return a default issue
    return "general troubleshooting"
  
def retrieve_images(issue):
    # Dictionary mapping issues to lists of image URLs
    image_database = {
        'Microsoft Teams': ['https://example.com/teams_issue1.jpg', 'https://example.com/teams_issue2.jpg'],
        'login': ['https://example.com/login_issue1.jpg', 'https://example.com/login_issue2.jpg'],
        # Add more issues and corresponding image URLs as needed
    }

    # Retrieve images for the given issue
    if issue in image_database:
        return image_database[issue]
    else:
        # If no images are available for the issue, return a default image
        return ["https://via.placeholder.com/500x300.png?text=Troubleshooting+Image"]

def generate_audio_instructions(issue):
    # Dictionary mapping issues to generic audio instructions
    audio_instructions = {
        'Microsoft Teams': "To troubleshoot Microsoft Teams, please try restarting the application and checking your internet connection.",
        'login': "To troubleshoot login issues, please try resetting your password or contacting your system administrator.",
        # Add more issues and corresponding audio instructions as needed
    }

    # Generate audio instruction for the given issue
    if issue in audio_instructions:
        text = audio_instructions[issue]
    else:
        # If no specific instructions are available, provide a generic instruction
        text = "To troubleshoot {}, please try restarting the application and checking your internet connection.".format(issue)

    # Use text-to-speech to generate audio instructions
    tts = gTTS(text=text, lang='en')
    audio_file = BytesIO()
    tts.save(audio_file)
    audio_file.seek(0)
    return audio_file


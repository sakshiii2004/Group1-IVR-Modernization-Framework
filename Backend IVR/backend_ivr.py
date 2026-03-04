from fastapi import FastAPI, Form
from fastapi.responses import Response
from twilio.twiml.voice_response import VoiceResponse, Gather

app = FastAPI()

# Your current ngrok public URL
BASE_URL = "https://intercorporate-rikki-uncautiously.ngrok-free.dev"

# Indian English voice
IVR_VOICE = "Polly.Aditi"

@app.post("/voice")
async def main_menu():
    """
    Step 1 & 2: Welcome Prompt and Main Menu
    """
    response = VoiceResponse()

    gather = Gather(
        num_digits=1,
        action=f"{BASE_URL}/handle-main-menu",
        method="POST"
    )

    gather.say(
        "Welcome to the In Patient Service Request and Facility Dispatch system. "
        "For housekeeping and sanitation, press 1. "
        "For room maintenance and repairs, press 2. "
        "For I T and entertainment support, press 3. "
        "To speak with the central nursing station, press 4.",
        voice=IVR_VOICE
    )

    response.append(gather)

    response.say(
        "We did not receive any input. Please try again.",
        voice=IVR_VOICE
    )

    response.redirect(f"{BASE_URL}/voice")

    return Response(content=str(response), media_type="application/xml")


@app.post("/handle-main-menu")
async def handle_main_menu(Digits: str = Form(default=None)):
    """
    Step 3: Handle Main Menu Selection
    """
    response = VoiceResponse()

    if Digits == "1":
        gather = Gather(
            num_digits=1,
            action=f"{BASE_URL}/handle-housekeeping",
            method="POST"
        )

        gather.say(
            "You have selected Housekeeping. "
            "Press 1 for routine room cleaning. "
            "Press 2 for urgent spill clean up. "
            "Press 3 for fresh linens.",
            voice=IVR_VOICE
        )

        response.append(gather)

    elif Digits == "2":
        response.say(
            "You have selected Facility Maintenance. "
            "A work order has been initiated and a technician will be dispatched shortly.",
            voice=IVR_VOICE
        )
        response.hangup()

    elif Digits == "3":
        response.say(
            "You have selected I T support. "
            "Please ensure your device is turned on while we connect you to the next available agent.",
            voice=IVR_VOICE
        )
        response.hangup()

    elif Digits == "4":
        response.say(
            "Connecting you to the central nursing station. Please hold.",
            voice=IVR_VOICE
        )
        response.hangup()
        # Example if you want to dial real number later:
        # response.dial("+919876543210")

    else:
        response.say(
            "Invalid entry. Returning to the main menu.",
            voice=IVR_VOICE
        )
        response.redirect(f"{BASE_URL}/voice")

    return Response(content=str(response), media_type="application/xml")


@app.post("/handle-housekeeping")
async def handle_housekeeping(Digits: str = Form(default=None)):
    """
    Handle Housekeeping Sub-Menu
    """
    response = VoiceResponse()

    if Digits == "1":
        response.say(
            "Routine cleaning requested. Staff will arrive shortly.",
            voice=IVR_VOICE
        )
        response.hangup()

    elif Digits == "2":
        response.say(
            "Urgent spill reported. An emergency janitorial team has been dispatched.",
            voice=IVR_VOICE
        )
        response.hangup()

    elif Digits == "3":
        response.say(
            "Fresh linens requested. They will be delivered to your room.",
            voice=IVR_VOICE
        )
        response.hangup()

    else:
        response.say(
            "Invalid entry. Returning to main menu.",
            voice=IVR_VOICE
        )
        response.redirect(f"{BASE_URL}/voice")

    return Response(content=str(response), media_type="application/xml")
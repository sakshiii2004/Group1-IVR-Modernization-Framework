from twilio.rest import Client

account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token = "your_auth_token"

client = Client(account_sid, auth_token)

call = client.calls.create(
    to="+91VERFIED_PHONE_NUMBER",
    from_="+12765337252",
    url="https://intercorporate-rikki-uncautiously.ngrok-free.dev/voice"
)

print("Call initiated:", call.sid)

"""
1. trigger_call.py sends API request to Twilio.
2. Twilio places outbound call to verified phone number.
3. Caller answers.
4. Twilio sends HTTP POST request to /voice endpoint.
5. FastAPI receives webhook at /voice.
6. TwiML response is generated dynamically.
7. TwiML includes:
      - Welcome message (Text-to-Speech)
      - <gather> verb for DTMF input.
8. Twilio plays the main menu.
9. Caller presses a digit.
10. Twilio sends POST to /handle-main-menu.
11. Backend extracts Digits parameter.
12. Conditional routing occurs:

      1 → Housekeeping submenu
      2 → Maintenance confirmation
      3 → IT Support message
      4 → Nursing station message
      Invalid → Redirect to main menu
13. Twilio plays housekeeping submenu.
14. Caller presses 1 / 2 / 3.
15. Twilio sends POST to /handle-housekeeping.
16. Backend generates final confirmation message.
17. Call ends with hangup()."""
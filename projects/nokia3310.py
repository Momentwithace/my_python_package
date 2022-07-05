def main_menu():

    user_response = int(input("""
            NOKIA 3310
            MAIN MENU
            1: PhoneBook
            2: Message
            3: Chat
            4: Call Register
            5: Tones
            6: Settings
            7: Call Divert
            8: Games
            9: Calculator
            10: Reminder
            11: Clock
            12: Profile
            13: SIM Services
            0: Exit
        >>>"""))
    return user_response


# def main_menu():
#     user_response = int(input("""
#         NOKIA 3310
#         MAIN MENU
#         1: PhoneBook
#         2: Message
#         3: Chat
#         4: Call Register
#         5: Tones
#         6: Settings
#         7: Call Divert
#         8: Games
#         9: Calculator
#         10: Reminder
#         11: Clock
#         12: Profile
#         13: SIM Services
#         0: Exit
#     >>>"""))


def search():
    user_response = int(input("""
        Nothing to show for search
        0 -> back
    """))
    if user_response == 0: phonebook()
    pass


def service_nos():
    user_response = int(input("""
        No service number saved
        0 -> back
    """))
    if user_response == 0: phonebook()
    pass


def add_name():
    user_response = int(input("""
        Add Name
        0 -> Back
    """))
    if user_response == 0: phonebook()
    pass


def erase():
    user_response = int(input("""
            Nothing to erase
            0 -> Back
        """))
    if user_response == 0: phonebook()
    pass


def edit():
    user_response = int(input("""
            Nothing to edit
            0 -> Back
        """))
    if user_response == 0: phonebook()
    pass


def assign_tone():
    user_response = int(input("""
            Tones not available
            0 -> Back
        """))
    if user_response == 0: phonebook()
    pass


def sendBcard():
    user_response = int(input("""
            B'card not available
            0 -> Back
        """))
    if user_response == 0: phonebook()
    pass


def type_of_view():
    user_response = int(input("""
            Views not available
            0 -> Back
        """))
    if user_response == 0: options()
    pass


def Memory_status():
    user_response = int(input("""
            32gb
            0 -> Back
        """))
    if user_response == 0: options()
    pass


def options():
    user_response = int(input("""
            1 -> Type of view
            2 -> Memory status
            0 -> Back
        """))
    if user_response == 1: type_of_view()
    elif user_response == 2: Memory_status()
    elif user_response == 0: phonebook()
    else:
        print("command not recognize")
    pass


def speedDial():
    user_response = int(input("""
            Speed dials not available
            0 -> Back
        """))
    if user_response == 0: phonebook()
    pass


def voiceTag():
    user_response = int(input("""
            Voice tags not available
            0 -> Back
        """))
    if user_response == 0: phonebook()
    pass


def phonebook():
    user_input = int(input("""
        1: Search
        2: Service Nos
        3: Add Name
        4: Erase
        5: Edit
        6: Assign Tone
        7: Send B'card
        8: Options
        9: Speed dial
        10: Voice tags
        0: Back
    >>>"""))
    match user_input:
        case 1: search()
        case 2: service_nos()
        case 3: add_name()
        case 4: erase()
        case 5: edit()
        case 6: assign_tone()
        case 7: sendBcard()
        case 8: options()
        case 9: speedDial()
        case 10: voiceTag()
        case 0: main_menu()
    pass


def writemessage():
    user_response = int(input("""
        Sorry messages can't be writing now
        0 -> Back
    """))
    if user_response == 0: message_menu()
    pass


def inbox():
    user_response = int(input("""
           No messages available
           0 -> Back
       """))
    if user_response == 0: message_menu()
    pass


def outbox():
    user_response = int(input("""
           Sorry you can't access this service now
           0 -> Back
       """))
    if user_response == 0: message_menu()
    pass


def pictureMessage():
    user_response = int(input("""
              Sorry you can't access this service now
              0 -> Back
          """))
    if user_response == 0: message_menu()
    pass


def template():
    user_response = int(input("""
              Sorry you can't access this service now
              0 -> Back
          """))
    if user_response == 0: message_menu()
    pass


def smileys():
    user_response = int(input("""
              Sorry you can't access this service now
              0 -> Back
          """))
    if user_response == 0: message_menu()
    pass


def messageSettings():
    user_response = int(input("""
              Sorry you can't access this service now
              0 -> Back
          """))
    if user_response == 0: message_menu()
    pass


def infoService():
    user_response = int(input("""
              Sorry you can't access this service now
              0 -> Back
          """))
    if user_response == 0: message_menu()
    pass


def voiceMail():
    user_response = int(input("""
              Sorry you can't access this service now
              0 -> Back
          """))
    if user_response == 0: message_menu()
    pass


def serviceCommandEditor():
    user_response = int(input("""
      Sorry you can't access this service now
      0 -> Back
  >>>"""))
    if user_response == 0: message_menu()
    pass


def message_menu():
    user_response = int(input("""
        1: Write Message
        2: Inbox
        3: Outbox
        4: Picture Message
        5: Template
        6: Smileys
        7: Message Settings
        8: Info Service
        9: Voice mailbox number
        10: Service command editor
        0. Back
    >>>"""))
    match user_response:
        case 1: writemessage()
        case 2: inbox()
        case 3: outbox()
        case 4: pictureMessage()
        case 5: template()
        case 6: smileys()
        case 7: messageSettings()
        case 8: infoService()
        case 9: voiceMail()
        case 10: serviceCommandEditor()
        #case 0:
    pass


def chat():
    user_response = int(input("""
      Sorry you can't access this service now
      0 -> Back
    >>>"""))
    if user_response == 0: message_menu()
    pass


def prepaid_credit():
    user_response = int(input("""
     Sorry you can't access this service now
     0 -> Back
     >>>"""))
    if user_response == 0: message_menu()
    pass


def call_cost_limit():
    user_response = int(input("""
    Sorry you can't access this service now
    0 -> Back
    >>>"""))
    if user_response == 0: call_cost_settings()
    pass


def show_cost_in():
    user_response = int(input("""
    Sorry you can't access this service now
    0 -> Back
    >>>"""))
    if user_response == 0: call_cost_settings()
    pass


def call_cost_settings():
    user_response = int(input("""
        1 -> Call Cost Limit
        2 -> Show Cost In
        0 -> Back
    """))
    match user_response:
        case 1: call_cost_limit()
        case 2: show_cost_in()
        case 0: show_call_cost()
    pass


def last_call_cost():
    user_response = int(input("""
    Sorry you can't access this service now
    0 -> Back
    >>>"""))
    if user_response == 0: show_call_cost()
    pass


def all_call_cost():
    user_response = int(input("""
    Sorry you can't access this service now
    0 -> Back
    >>>"""))
    if user_response == 0: show_call_cost()
    pass


def clear_counter():
    user_response = int(input("""
    Sorry you can't access this service now
    0 -> Back
    >>>"""))
    if user_response == 0: show_call_cost()
    pass


def show_call_cost():
    user_response = int(input("""
        1 -> Last Call Cost
        2 -> All Call's Cost
        3 -> Clear Counters
        0 -> Back
    >>>"""))
    match user_response:
        case 1: last_call_cost()
        case 2: all_call_cost()
        case 3: clear_counter()
        case 0: call_register()
    pass


def last_call_duration():
    user_response = int(input("""
     Sorry you can't access this service now
     0 -> Back
    >>>"""))
    if user_response == 0: call_register()
    pass


def all_calls_duration():
    user_response = int(input("""
     Sorry you can't access this service now
     0 -> Back
    >>> """))
    if user_response == 0: call_register()
    pass


def received_calls_duration():
    user_response = int(input("""
     Sorry you can't access this service now
     0 -> Back
    >>> """))
    if user_response == 0: call_register()
    pass


def dialed_called_duration():
    user_response = int(input("""
     Sorry you can't access this service now
     0 -> Back
    >>>"""))
    if user_response == 0: call_register()
    pass


def clear_timer():
    user_response = int(input("""
     Sorry you can't access this service now
     0 -> Back
     >>>"""))
    if user_response == 0: call_register()
    pass


def show_call_duration():
    user_response = int(input("""
        1 -> Last Call Duration
        2 -> All Call's Duration
        3 -> Received Call's Duration
        4 -> Dialled Call's Duration
        5 -> Clear Timers
        0 -> Back
    >>>"""))
    match user_response:
        case 1: last_call_duration()
        case 2: all_calls_duration()
        case 3: received_calls_duration()
        case 4: dialed_called_duration()
        case 5: clear_timer()
        case 0: call_register()
    pass


def erase_recent_call_list():
    user_response = int(input("""
     Sorry you can't access this service now
     0 -> Back
    >>>"""))
    if user_response == 0: call_register()
    pass


def dialed_numbers():
    user_response = int(input("""
     Sorry you can't access this service now
     0 -> Back
    >>>"""))
    if user_response == 0: call_register()
    pass


def received_calls():
    user_response = int(input("""
     Sorry you can't access this service now
     0 -> Back
    >>>"""))
    if user_response == 0: call_register()
    pass


def missed_calls():
    user_response = int(input("""
     Sorry you can't access this service now
     0 -> Back
     >>>"""))
    if user_response == 0: call_register()
    pass


def call_register():
    user_response = int(input("""
        1: Missed calls
        2: Received calls
        3: Dialled Numbers
        4: Erase Recent Call List
        5: Show Call Duration
        6: Show Call Cost
        7: Call Cost Settings
        8: Prepaid Credit
        0: Back 
    >>>"""))
    match user_response:
        case 1: missed_calls()
        case 2: received_calls()
        case 3: dialed_numbers()
        case 4: erase_recent_call_list()
        case 5: show_call_duration()
        case 6: show_call_cost()
        case 7: call_cost_settings()
        case 8: prepaid_credit()
        case 0: call_register()
    pass


def ringing_tone():
    user_response = int(input("""
     Sorry you can't access this service now
     0 -> Back
    >>>"""))
    if user_response == 0: tones()
    pass


def ringing_volume():
    user_response = int(input("""
     Sorry you can't access this service now
     0 -> Back
     >>>"""))
    if user_response == 0: tones()
    pass


def incoming_call_alert():
    user_response = int(input("""
     Sorry you can't access this service now
     0 -> Back
    >>>"""))
    if user_response == 0: tones()
    pass


def composer():
    user_response = int(input("""
     Sorry you can't access this service now
     0 -> Back
    >>>"""))
    if user_response == 0: tones()
    pass


def message_alert_tones():
    user_response = int(input("""
     Sorry you can't access this service now
     0 -> Back
     >>>"""))
    if user_response == 0: tones()
    pass


def keypad_tones():
    user_response = int(input("""
     Sorry you can't access this service now
     0 -> Back
     >>>"""))
    if user_response == 0: tones()
    pass


def warming_and_game_tone():
    user_response = int(input("""
     Sorry you can't access this service now
     0 -> Back
    >>>"""))
    if user_response == 0: tones()
    pass


def vibrating_tone():
    user_response = int(input("""
     Sorry you can't access this service now
     0 -> Back
    >>>"""))
    if user_response == 0: tones()
    pass


def screen_saver():
    user_response = int(input("""
     Sorry you can't access this service now
     0 -> Back
    >>>"""))
    if user_response == 0: tones()
    pass


def tones():
    user_response = int(input("""
        1: Ringing Tone
        2: Ringing Volume
        3: Incoming Call Alert
        4: Composer
        5: Message Alert Tone
        6: Keypad Tones
        7: Warning and Game Tones
        8: Vibrating Alert
        9: Screen Saver
        0: Back
    """))
    match user_response:
        case 1: ringing_tone()
        case 2: ringing_volume()
        case 3: incoming_call_alert()
        case 4: composer()
        case 5: message_alert_tones()
        case 6: keypad_tones()
        case 7: warming_and_game_tone()
        case 8: vibrating_tone()
        case 9: screen_saver()

    pass


def restore_factory_settings():
    user_response = int(input("""
     Sorry you can't access this service now
     0 -> Back
    >>>"""))
    if user_response == 0: settings()
    pass


def security_settings():
    user_response = int(input("""
     Sorry you can't access this service now
     0 -> Back
    >>>"""))
    if user_response == 0: settings()
    pass


def phone_settings():
    user_response = int(input("""
     Sorry you can't access this service now
     0 -> Back
    >>>"""))
    if user_response == 0: settings()
    pass


def call_settings():
    user_response = int(input("""
     Sorry you can't access this service now
     0 -> Back
    >>>"""))
    if user_response == 0: settings()
    pass


def settings():
    user_response = int(input("""
        1: Call Settings
        2: Phone Settings
        3: Security Settings
        4: Restore Factory Settings
        0: Back
    >>>"""))
    match user_response:
        case 1: call_settings()
        case 2: phone_settings()
        case 3: security_settings()
        case 4: restore_factory_settings()

    pass


def call_divert():
    user_response = int(input("""
        Service Not Available
        0 -> Back
    """))
    if user_response == 0:
        main_menu()
    pass


def games():
    user_response = int(input("""
           Service Not Available
           0 -> Back
       """))
    if user_response == 0:
        main_menu()
    pass


def calculator():
    user_response = int(input("""
           Service Not Available
           0 -> Back
       """))
    if user_response == 0:
        main_menu()
    pass


def reminder():
    user_response = int(input("""
           Service Not Available
           0 -> Back
       """))
    if user_response == 0:
        main_menu()
    pass


def clock_menu():
    user_response = int(input("""
           Service Not Available
           0 -> Back
       """))
    if user_response == 0:
        main_menu()
    pass


def profile():
    user_response = int(input("""
           Service Not Available
           0 -> Back
       """))
    if user_response == 0:
        main_menu()
    pass


def sim_service():
    user_response = int(input("""
           Service Not Available
           0 -> Back
       """))
    if user_response == 0:
        main_menu()
pass


match main_menu():
    case 1: phonebook()
    case 2: message_menu()
    case 3: chat()
    case 4: call_register()
    case 5: tones()
    case 6: settings()
    case 7: call_divert()
    case 8: games()
    case 9: calculator()
    case 10: reminder()
    case 11: clock_menu()
    case 12: profile()
    case 13: sim_service()
    case 0: main_menu()
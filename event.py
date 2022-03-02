import sys
from collections import deque

last_receieved_status = ''

def Push(data):
    event_list.appendleft(data)

def Pop():
    popped_event = event_list.pop()
    if popped_event[0] == 'S':
        print(f'EventStatus(Pop): {popped_event[0]}, {popped_event[1]}, {popped_event[2]}')
    else:
        print(f'EventRequest(Pop): {popped_event[0]}, {popped_event[1]}')
    return popped_event


def pop_all_events():
    while len(event_list) > 0:
        global last_receieved_status
        data = Pop()
        if data[0] == 'R': # POP EventRequest
            if last_receieved_status:
                if last_receieved_status in ['C', 'T']:
                    print(f'EventRequest: R, {str(data[1])}')
            else:
                push_back_event = [data[0], int(data[1]) + 1]
                Push(push_back_event)
        else: # POP EventStatus
            last_receieved_status = data[1]
            if data[1] in ['C', 'T'] and int(data[2]) < 2:
                push_back_event = [data[0], data[1], int(data[2]) + 1]
                Push(push_back_event)
            else:
                print(f'EventStatus: S, {str(data[1])}, {str(data[2])}')


def initialise():
    global last_receieved_status
    while True:
        try:
            event = [character for character in input() if character.isalnum()]
        except EOFError:
            break
        input_event_length = len(event)
        if input_event_length >= 2 and input_event_length <= 3:
            if input_event_length == 2:
                if not event[0] == 'R':
                    sys.exit("Invalid Event Type. System exit code 1")
            if input_event_length == 3:
                if not event[0] == 'S':
                    sys.exit("Invalid Event Type. System exit code 1")
                last_receieved_status = event[1]
        else:
            sys.exit("Invalid Input. System exit code 1")
        event_list.appendleft(event)

event_list = deque()
initialise()
pop_all_events()
# DolatCapital
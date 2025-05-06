import numpy as np

def decode_vfTDC_word(word):
    """
    Decode a vfTDC word into its components.

    Args:
        word (int): The vfTDC word to decode.

    Returns:
        tuple: A tuple containing the decoded components:
            - data type code: The data type code (five bit binary code).
            - slot (int): The slot number (3-19).
            - channel (int): The channel number (0-255).
            - time (float): The time in nanoseconds.
            - overflow (bool): True if overflow occurred, False otherwise.
    """
    # Extract the data type code (5 bits)
    data_type_word = (word >> 27) & 0x1F

    if (data_type_word == 0x10):
        print("VF TDC data type word: 10000 ... Block Header")
    if (data_type_word == 0x12):
        print("VF TDC data type word: 10010 ... Event Header")
    elif (data_type_word == 0x13):
        print("VF TDC data type word: 10011 ... Trigger Time 1")
    elif (data_type_word == 0x00):
        print("VF TDC data type word: 00000 ... Trigger Time 2")
    elif (data_type_word == 0x17):
        print("VF TDC data type word: 10111 ... TDC Data")
    else:
        print("VF TDC data type word: Unknown: ", bin(data_type_word),
              hex(data_type_word))

    if (data_type_word == 0x12):
        # Event Header
        # Extract the slot number (3 bits)
        slot = (word >> 24) & 0x7
        # Extract the event time
        event_number = (word & 0x003FFFFF)
        # Print the decoded components
        print(f"Slot: {slot}")
        print(f"Event Number: {event_number}")
        return data_type_word, slot, event_number
    elif (data_type_word == 0x13):
        # Trigger Time 1
        # Extract the event time
        event_trigger_time_1 = (word & 0x00FFFFFF)
        # Print the decoded components
        print(f"Event Trigger Time 1: {event_trigger_time_1}")
        # Return the decoded components
        return data_type_word, event_trigger_time_1, None
    elif (data_type_word == 0x00):
        # Trigger Time 2
        # Extract the event time
        event_trigger_time_2 = (word & 0x00FFFFFF)
        # Print the decoded components
        print(f"Event Trigger Time 2: {event_trigger_time_2}")
        return data_type_word, event_trigger_time_2, None
    elif (data_type_word == 0x17):
        # TDC Data
        # Extract the group number (3 bits)
        group_number = (word >> 24) & 0x7
        # Extract the channel number (5 bits)
        channel = (word >> 19) & 0x1F
        # extract the edge type (1 bit)
        edge_type = ((word >> 18) & 0x1)
        edge_type = 1 if edge_type == 0 else -1 # 0 for leading edge, 1 for trailing edge
        # Extract the course time (10 bits)
        course_time = (word >> 8) & 0x3FF
        # Extract the two ns bit (1 bit)
        two_ns_bit = (word >> 7) & 0x1
        # Extract the fine time (7 bits)
        fine_time = word & 0x7F

        channel = group_number * 32 + channel

        # Calculate the time in nanoseconds
        time_ns = edge_type * ((4000.0*course_time) + (2000.0*two_ns_bit)  + 2000.0*fine_time/105.59)
        # Print the decoded components
        #print(f"Group Number: {group_number}")
        #print(f"Channel: {channel}")
        #print(f"Edge Type: {edge_type}")
        #print(f"Course Time: {course_time}")
        #print(f"Two ns Bit: {two_ns_bit}")
        #print(f"Fine Time: {fine_time}")
        print(f"Channel: {channel}")
        print(f"Time (ns): {time_ns}")
        return data_type_word, channel , time_ns
    elif (data_type_word == 0x10):
        # Block Header
        # Extract the slot number (5 bits)
        slot = (word >> 22) & 0x1F
        # Extract the board id (4 bit)
        board_id = (word >> 18) & 0xF
        # Print the decoded components
        print(f"Slot: {slot}")
        print(f"Board ID: {board_id}")
        return data_type_word, slot, board_id
    else:
        return None, None, None

# Example usage

if __name__ == "__main__":
    # Example vfTDC word
    #vfTDC_word = 0xB1234567  # Replace with actual vfTDC word
    # Get word from user input
    #vfTDC_word = int(input("Enter vfTDC word (in hex): "), 16)

    word_list = [0x94c531b5, 0x98855c20, 0x00028001, 0xbc8c2060,
                 0xbc882794, 0xbc8c85cc, 0xbc888e60, 0xbc8c3618]

    # Decode the vfTDC word
    for vfTDC_word in word_list:
        print(f"Decoding vfTDC word: {hex(vfTDC_word)}")
        data_type, slot, channel = decode_vfTDC_word(vfTDC_word)


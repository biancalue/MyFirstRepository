def find_state():
    white_space = [",", "\n"]
    state_list = []
    last_split_position = 0
    with open("eligible_voters.txt") as file:
        state_data = file.read()
    string_length = len(state_data)
    for character_index in range(string_length):
        current_character = state_data[character_index]
        if current_character in white_space:
            sliced_string = state_data[last_split_position : character_index]
            state_list.append(sliced_string)
            last_split_position = character_index +1
    print(state_list)

        
find_state()

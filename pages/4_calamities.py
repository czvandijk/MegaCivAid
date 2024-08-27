import streamlit as st

# Title of the app
st.title("Calamities in the Game")

# Available advancements for the user to select, sorted in alphabetical order
advancements = sorted([
    "Agriculture", "Anatomy", "Calendar", "Cartography", "Coinage", "Deism", "Democracy", "Diplomacy", 
    "Drama and Poetry", "Engineering", "Enlightenment", "Fundamentalism", "Law", "Library", "Medicine", 
    "Military", "Mining", "Monarchy", "Masonry", "Music", "Mythology", "Naval Warfare", "Philosophy", 
    "Pottery", "Provincial Empire", "Roadbuilding", "Sculpture", "Theocracy", "Theology", "Trade Empire", 
    "Universal Doctrine", "Wonder of the World"
])

# Allow the user to select advancements they hold
selected_advancements = st.multiselect("Select the advancements you hold:", advancements)

# Allow the user to decide if they want to see the Minor Calamities
show_minor_calamities = st.checkbox("Show Minor Calamities")

# Calamity descriptions (verbatim)
calamities = {
    "2 Minor: Tempest": "Take 2 damage in total from coastal areas of your choice and lose 5 treasury tokens.",
    "3 Minor: Squandered Wealth": "Lose 10 treasury tokens.",
    "4 Minor: City Riots": "Reduce 1 of your cities and lose 5 treasury tokens.",
    "5 Minor: City in Flames": "Destroy 1 of your cities. You may choose to pay 10 treasury tokens to prevent this.",
    "6 Minor: Tribal Conflict": "Take 5 damage.",
    "7 Minor: Minor Uprising": "Destroy 1 of your cities.",
    "8 Minor: Banditry": "Discard 2 commodity cards of your choice. For each card you must discard, you may choose to pay 4 treasury tokens to prevent it.",
    "9 Minor: Coastal Migration": "Destroy 1 of your coastal cities and lose 5 treasury tokens.",
    
    "2 Major Non-Tradable: Volcanic Eruption/Earthquake": "Only if you have a city on a volcano this calamity is a ‘Volcanic Eruption’, otherwise this is an ‘Earthquake’. "
                                   "**Volcanic Eruption**: Destroy all units (irrespective of ownership) in the area(s) touched by the volcano. "
                                   "If you have cities in more than one area with a volcano, select the one volcano that would affect the most of your unit points. "
                                   "**Earthquake**: Select and destroy 1 of your cities and select and reduce 1 city adjacent by land or water (irrespective of ownership).",
    "3 Major Non-Tradable: Famine": "Take 10 damage and assign 5 damage to each of 3 players of your choice.",
    "4 Major Non-Tradable: Flood": "Only if you have any units on a flood plain, take 15 damage from the flood plain. If you have any units on more than 1 flood plain, select the flood plain where the most of your units would be affected. "
             "All other players with units on the same flood plain take 5 damage from that flood plain as well. Cities built on black city sites are not considered to be on the flood plain. If you have no units on a flood plain, take 5 damage in total from coastal areas of your choice instead.",
    "5 Major Non-Tradable: Civil War": "The beneficiary annexes all your units in excess of 35 unit points. You select the units. Count all units points that you have on the board and select units in excess of 35. "
                 "All units selected this way must be in areas adjacent to each other if possible, and in each of these areas all of your units must be selected. If you have 35 unit points or less there is no Civil War.",
    "6 Major Non-Tradable: Cyclone": "The open sea area that has the most of your cities directly adjacent to it becomes the Cyclone area. You select 3 of your cities adjacent to the Cyclone area. All other players with cities directly adjacent to the Cyclone area must select 2 of their cities adjacent to the Cyclone area as well.",
    "7 Major Non-Tradable: Tyranny": "The beneficiary selects and annexes 15 of your unit points. All units selected this way must be in areas adjacent to each other if possible, and in each of these areas all of your units must be selected.",
    "8 Major Non-Tradable: Corruption": "Discard commodity cards with a total face value (not set value) of at least 10 points.",
    "9 Major Non-Tradable: Regression": "Your succession marker on the A.S.T. is moved 1 step backward.",
    
    "2 Major Tradable: Treachery": "The beneficiary selects and annexes 1 of your cities.",
    "3 Major Tradable: Slave Revolt": "Immediately perform an additional check for city support, during which your city support rate is increased by 2. Reduce cities until you have sufficient support.",
    "4 Major Tradable: Superstition": "Reduce 3 of your cities.",
    "5 Major Tradable: Barbarian Hordes": "One of your cities is attacked by 15 barbarian tokens, which will continue attacking your units until there are no areas with barbarian tokens in which the population limit is exceeded. "
                        "Place 15 barbarian tokens in one of your cities selected by the beneficiary (if possible a wilderness city) and resolve a city attack. After this conflict, the beneficiary moves all remaining barbarian tokens in excess of the population limit to an area adjacent by land or water that contains any of your units and conflict is resolved again. "
                        "The beneficiary may only move barbarian tokens into an area that contains a city if the attack would be successful. This process is repeated until no population limit is exceeded by the barbarian tokens or no new area can be chosen legally. Any barbarian tokens in excess of a population limit are then destroyed.",
    "6 Major Tradable: Epidemic": "Take 15 damage and select 2 other players that must take 10 damage as well. The beneficiary may not be selected as a secondary victim.",
    "7 Major Tradable: Civil Disorder": "Reduce all but 3 of your cities.",
    "8 Major Tradable: Iconoclasm and Heresy": "Reduce 4 of your cities and select 2 other players that must reduce 1 of their cities as well. The beneficiary may not be selected as a secondary victim.",
    "9 Major Tradable: Piracy": "The beneficiary selects 2 of your coastal cities, which are replaced by pirate cities. Then you select from 2 other players 1 coastal city each, which are also replaced by pirate cities. The beneficiary may not be selected as a secondary victim."
}

# Advances and their effects for each calamity
calamity_advances = {
    "2 Major Non-Tradable: Volcanic Eruption/Earthquake": {
        "Engineering": "➕ In the case of an Earthquake, your city is reduced rather than destroyed."
    },
    "3 Major Non-Tradable: Famine": {
        "Agriculture": "➖ If you are the primary victim, take 5 additional damage.",
        "Pottery": "➕ Prevent 5 damage.",
        "Calendar": "➕ Prevent 5 damage."
    },
    "4 Major Non-Tradable: Flood": {
        "Engineering": "➕ Prevent 5 damage."
    },
    "5 Major Non-Tradable: Civil War": {
        "Music": "➕ Select 5 less unit points.",
        "Drama and Poetry": "➕ Select 5 less unit points.",
        "Democracy": "➕ Select 10 less unit points.",
        "Philosophy": "➖ Select 5 additional unit points.",
        "Military": "➖ Select 5 additional unit points."
    },
    "6 Major Non-Tradable: Cyclone": {
        "Trade Empire": "➖ You must select 1 additional city in an area adjacent to the open sea area.",
        "Masonry": "➕ Deselect 1 of your selected cities.",
        "Calendar": "➕ Deselect 2 of your selected cities."
    },
    "7 Major Non-Tradable: Tyranny": {
        "Sculpture": "➕ The beneficiary selects and annexes 5 less unit points.",
        "Law": "➕ The beneficiary selects and annexes 5 less unit points.",
        "Monarchy": "➖ The beneficiary selects and annexes 5 additional unit points.",
        "Provincial Empire": "➖ The beneficiary selects and annexes 5 additional unit points."
    },
    "8 Major Non-Tradable: Corruption": {
        "Law": "➕ Discard 5 less points of face value.",
        "Coinage": "➖ Discard 5 additional points of face value.",
        "Provincial Empire": "➖ Discard 5 additional points of face value."
    },
    "9 Major Non-Tradable: Regression": {
        "Fundamentalism": "➖ Your marker is moved backward 1 additional step.",
        "Library": "➕ Your marker is moved backward 1 less step.",
        "Enlightenment": "➕ For each step backward, you may choose to prevent the effect by destroying 2 of your cities (if possible non-coastal)."
    },
    "2 Major Tradable: Treachery": {
        "Diplomacy": "➖ The beneficiary selectes and annexes 1 less city."},
    "3 Major Tradable: Slave Revolt": {
        "Mythology": "➕ Your city support rate is decreased by 1 during the resolution of Slave Revolt.",
        "Enlightenment": "➕ Your city support rate is decreased by 1 during the resolution of Slave Revolt.",
        "Mining": "➖ Your city support rate is increased by 1 during the resolution of Slave Revolt."
    },
    "4 Major Tradable: Superstition": {
        "Enlightenment": "➕ Reduce 1 less city.",
        "Mysticism": "➕ Reduce 1 less city.",
        "Deism": "➕ Reduce 1 less city.",
        "Universal Doctrine": "➖ Reduce 1 additional city."
    },
    "5 Major Tradable: Barbarian Hordes": {
        "Monarchy": "➕ 5 less barbarian tokens are used.",
        "Politics": "➖ 5 additional barbarian tokens are used.",
        "Provincial Empire": "➖ 5 additional barbarian tokens are used."
    },
    "6 Major Tradable: Epidemic": {
        "Medicine": "➕ Prevent 5 damage.",
        "Enlightenment": "➕ If you are the primary victim, prevent 5 damage.",
        "Anatomy": "➕ If you are a secondary victim, prevent 5 damage.",
        "Roadbuilding": "➖ If you are the primary victim, take 5 additional damage.",
        "Trade Empire": "➖ If you are the primary victim, take 5 additional damage."
    },
    "7 Major Tradable: Civil Disorder": {
        "Music": "➕ Reduce 1 less city.",
        "Drama and Poetry": "➕ Reduce 1 less city.",
        "Law": "➕ Reduce 1 less city.",
        "Advanced Military": "➖ Reduce 1 additional city.",
        "Naval Warfare": "➖ Reduce 1 additional city."
    },
    "8 Major Tradable: Iconoclasm and Heresy": {
        "Philosophy": "➕ Reduce 2 less cities.",
        "Theology": "➕ Reduce 3 less cities.",
        "Monotheism": "➖ Reduce 1 additional city.",
        "Theocracy": "➕ You may choose to discard 2 commodity cards to prevent the city reduction effect for you."
    },
    "9 Major Tradable: Piracy": {
        "Cartography": "➖ The beneficiary selects and replaces 1 additional coastal city.",
        "Naval Warfare": "➕ The beneficiary selects and replaces 1 less coastal city. You may not be selected as a secondary victim."
    }
}

# Function to display advancements for each calamity
def display_advances(advances, selected_advances):
    # First, display selected advancements upright
    for advance, effect in advances.items():
        if advance in selected_advances:
            st.write(f"**{advance}:** {effect}")
    # Then, display unselected advancements italicized
    for advance, effect in advances.items():
        if advance not in selected_advances:
            st.write(f"*{advance}:* *{effect}*")

# Display calamities and their details
st.header("Calamities Overview")

# Subheader for Minor Calamities
if show_minor_calamities:
    st.subheader("Minor Calamities")
    for calamity, description in calamities.items():
        if "Minor" in calamity:
            with st.expander(calamity):
                st.write(description)  # Calamity description

# Subheader for Major Non-Tradable Calamities
st.subheader("Major Non-Tradable Calamities")
st.write("*The beneficiary is the player with most cities in stock. If this is a tie, it is the player between them with the most population units in stock (boats do not count, neither do Treasury tokens). Between them, the A.S.T.-ranking breaks ties (the player with the highest ranking/lowest number is the beneficiary). The primary victim cannot be the beneficiary.*")
for calamity, description in calamities.items():
    if "Major Non-Tradable" in calamity:
        with st.expander(calamity):
            st.write(description)  # Calamity description
            if calamity in calamity_advances:  # Check if there are advances for this calamity
                display_advances(calamity_advances[calamity], selected_advancements)

# Subheader for Major Tradable Calamities
st.subheader("Major Tradable Calamities")
st.write("*The beneficiary is the player who last traded you the calamity card. If this appears to be untracable or if the calamity was not traded, the same rules apply as for Major Non-Tradable calamities. Again, the primary victim cannot be the beneficiary.*")
for calamity, description in calamities.items():
    if "Major Tradable" in calamity:
        with st.expander(calamity):
            st.write(description)  # Calamity description
            if calamity in calamity_advances:  # Check if there are advances for this calamity
                display_advances(calamity_advances[calamity], selected_advancements)

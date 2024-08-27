# Define the advancement class 
class Advancement:
    def __init__(self, name, cost, groups, discounts, description, calamity_effect, ability=None):
        self.name = name
        self.cost = cost
        self.groups = groups
        self.discounts = discounts
        self.description = description
        self.calamity_effect = calamity_effect
        self.ability = ability

advancements = [
    Advancement("Mysticism", 50, ['Arts', 'Religion'], {'Arts': 5, 'Religion': 5, 'Monument': 10},
                "None",
                "➕ SUPERSTITION: Reduce 1 less city."),
    Advancement("Monument", 180, ['Crafts', 'Religion'], {'Crafts': 10, 'Religion': 10, 'Wonder of the World': 20}, 
                "Acquire 20 additional points of credit tokens in any combination of colors.",
                "None"),
    Advancement("Wonder of the World", 290, ['Arts', 'Crafts'], {'Arts': 20, 'Crafts': 20}, 
                "During the Trade cards acquisition phase, you may acquire 1 additional trade card for free from a stack number that is higher than your number of cities in play. Wonder of the World counts as a city during the A.S.T.-alteration phase.",
                "➖ CORRUPTION: Discard 5 additional points of face value."),
    Advancement("Sculpture", 50, ['Arts'], {'Arts': 10, 'Civics': 5, 'Architecture': 10}, 
                "None",
                "➕ TYRANNY: The beneficiary selects and annexes 5 less unit points."),
    Advancement("Architecture", 140, ['Arts'], {'Arts': 10, 'Science': 5, 'Mining': 20}, 
                "Once per turn, when constructing a city, you may choose to pay up to half of the required number of tokens from treasury.",
                "None"),
    Advancement("Mining", 230, ['Crafts'], {'Crafts': 20, 'Science': 5}, 
                "During the Trade cards acquisition phase, you may acquire additional trade cards from stack 6 and/or stack 8 for 13 treasury tokens per card. Treasury tokens are worth 2 points when purchasing Civilization Advances.",
                "➖ SLAVE REVOLT: Your city support rate is increased by 1 during the resolution of Slave Revolt."),
    Advancement("Cloth Making", 50, ['Crafts'], {'Arts': 5, 'Crafts': 10, 'Naval Warfare': 10}, 
                "Your ships are allowed to move 5 steps.",
                "None"),
    Advancement("Naval Warfare", 160, ['Civics'], {'Civics': 10, 'Crafts': 5, 'Diaspora': 20}, 
                "Your ships are allowed to carry 6 tokens. In conflicts, you may choose to remove ships from the conflict area instead of tokens. After each round of token removal a new check for token majority must be made.",
                "➕ PIRACY: If you are the primary victim, the beneficiary selects and replaces 1 less coastal city. You may not be selected as a secondary victim.\n\
                ➖ CIVIL DISORDER: Reduce 1 additional city."),
    Advancement("Diaspora", 270, ['Religion'], {'Arts': 5, 'Religion': 20}, 
                "SPECIAL ABILITY: You may choose to take up to 5 of your tokens from the board and place them anywhere else on the board, providing that no population limits are exceeded.",
                "None"),
    Advancement("Urbanism", 50, ['Civics'], {'Civics': 10, 'Science': 5, 'Diplomacy': 10}, 
                "Once per turn, when constructing a wilderness city you may choose to use up to 4 tokens from areas adjacent by land.",
                "None"),
    Advancement("Diplomacy", 160, ['Arts'], {'Arts': 10, 'Civics': 5, 'Provincial Empire': 20}, 
                "Players are not allowed to move tokens into areas containing your cities, except for areas where a conflict situation already occurs. This does not count for players holding Diplomacy or Military.",
                "➖ TREACHERY: The beneficiary selects and annexes 1 additional city."),
    Advancement("Provincial Empire", 260, ['Civics'], {'Civics': 20, 'Religion': 5}, 
                "SPECIAL ABILITY: You may choose to select up to 5 players that have units adjacent by land or water to your units. These players must choose and give you a commodity card with a face value of at least 2. Players holding Provincial Empire or Public Works may not be selected.",
                "➖ BARBARIAN HORDES: 5 additional barbarian tokens are used.\n\
                ➖ TYRANNY: The beneficiary selects and annexes 5 additional unit points."),
    Advancement("Monarchy", 60, ['Civics'], {'Civics': 10, 'Religion': 5, 'Law': 10}, 
                "You may choose to increase your tax rate by 1.",
                "➕ BARBARIAN HORDES: 5 less barbarian tokens are used.\n\
                ➖ TYRANNY: The beneficiary selects and annexes 5 additional unit points."),
    Advancement("Law", 150, ['Civics'], {'Civics': 10, 'Religion': 5, 'Cultural Ascendancy': 20},
                "None",
                "➕ TYRANNY: The beneficiary selects and annexes 5 less unit points.\n\
                ➕ CIVIL DISORDER: Reduce 1 less city.\n\
                ➕ CORRUPTION: Discard 5 less points of face value."),
    Advancement("Cultural Ascendancy", 280, ['Arts'], {'Arts': 20, 'Religion': 5}, 
                "Players are not allowed to cause conflict in areas containing your units, except for areas where a conflict situation already occurs. This does not count for players holding Cultural Ascendancy or Advanced Military. Your units are protected against the effect of Politics. Your default city support rate is increased by 1.",
                "None"),
    Advancement("Written Record", 60, ['Civics', 'Science'], {'Civics': 5, 'Science': 5, 'Cartography': 10}, 
                "Acquire 10 additional points of credit tokens in any combination of colors.",
                "None"),
    Advancement("Cartography", 160, ['Science'], {'Arts': 5, 'Science': 10, 'Library': 20}, 
                "During the Trade cards acquisition phase, you may acquire additional trade cards from stack 2 for 5 treasury tokens and/or from stack 7 for 13 treasury tokens per card.",
                "None"),
    Advancement("Library", 220, ['Science'], {'Arts': 5, 'Science': 20}, 
                "You may discount the cost of 1 other Civilization Advance that you purchase in the same turn as Library by 40 points.",
                "➕ REGRESSION: Your marker is moved backward 1 step less."),
    Advancement("Pottery", 60, ['Crafts'], {'Arts': 5, 'Crafts': 10, 'Agriculture': 10},
                "None",
                "➕ FAMINE: Prevent 5 damage."),
    Advancement("Agriculture", 120, ['Crafts'], {'Crafts': 10, 'Science': 5, 'Democracy': 20}, 
                "The population limit of ‘0’, ‘1’ and ‘2’ areas on the board is increased by 1 for you as long as these areas do not contain any other player’s units or barbarian tokens.",
                "➖ FAMINE: If you are the primary victim, take 5 additional damage."),
    Advancement("Democracy", 220, ['Civics'], {'Arts': 5, 'Civics': 20}, 
                "During the Tax collection phase you collect tax as usual but your cities do not revolt as a result of a shortage in tax collection.",
                "➕ CIVIL WAR: Select 10 less unit points.\n\
                ➕ CIVIL DISORDER: Reduce 1 less city."),
    Advancement("Masonry", 60, ['Crafts'], {'Crafts': 10, 'Science': 5, 'Engineering': 10}, 
                "None",
                "➕ CYCLONE: Reduce 1 less of your selected cities."),
    Advancement("Engineering", 160, ['Crafts', 'Science'], {'Crafts': 10, 'Science': 10, 'Roadbuilding': 20}, 
                "Other players or barbarians require 8 tokens to successfully attack your cities. Your cities are then replaced with 7 tokens. This does not apply when the attacking player also holds Engineering. You require 6 tokens to successfully attack other player’s cities or pirate cities. Their cities are then replaced with 5 tokens. This does not apply when the defending player also holds Engineering.",
                "➕ EARTHQUAKE: Your city is reduced instead of destroyed.\n\
                ➕ FLOOD: Prevent 5 damage."),
    Advancement("Roadbuilding", 220, ['Crafts'], {'Crafts': 20, 'Science': 5}, 
                "When moving over land, your tokens may move 2 areas. Tokens that are in a conflict situation after 1 step are not allowed to move any further. Your hand limit of trade cards is increased by 1.",
                "➖ EPIDEMIC: If you are the primary victim, take 5 additional damage."),
    Advancement("Mythology", 60, ['Religion'], {'Arts': 5, 'Religion': 10}, 
                "None",
                "➕ SLAVE REVOLT: Your city support rate is decreased by 1 during the resolution of Slave Revolt."),
    Advancement("Literacy", 110, ['Arts', 'Civics'], {'Arts': 10, 'Civics': 10, 'Crafts': 5, 'Religion': 5, 'Science': 10, 'Mathematics': 20}, 
                "None",
                "None"),
    Advancement("Mathematics", 250, ['Arts', 'Science'], {'Arts': 20, 'Civics': 10, 'Crafts': 10, 'Religion': 10, 'Science': 20}, 
                "None",
                "None"),
    Advancement("Empiricism", 60, ['Science'], {'Arts': 5, 'Civics': 10, 'Crafts': 5, 'Religion': 5, 'Science': 10, 'Medicine': 10}, 
                "None",
                "None"),
    Advancement("Medicine", 140, ['Science'], {'Crafts': 5, 'Science': 10, 'Anatomy': 20}, 
                "None",
                "➕ EPIDEMIC: Take 5 less damage."),
    Advancement("Anatomy", 270, ['Science'], {'Crafts': 5, 'Science': 20}, 
                "Upon purchase, you may choose to acquire 1 science card with an undiscounted cost price of less than 100 for free.",
                "➕ EPIDEMIC: If you are a secondary victim, prevent 5 damage."),
    Advancement("Deism", 70, ['Religion'], {'Crafts': 5, 'Religion': 10, 'Fundamentalism': 10}, 
                "None",
                "➕ SUPERSTITION: Reduce 1 less city."),
    Advancement("Fundamentalism", 150, ['Religion'], {'Arts': 5, 'Religion': 10, 'Monotheism': 20}, 
                "SPECIAL ABILITY: You may choose to destroy all units in an area adjacent by land to your units. Barbarian tokens, pirate cities and units belonging to players holding Fundamentalism or Philosophy are unaffected.",
                "➖ REGRESSION: Your marker is moved backward 1 additional step."),
    Advancement("Monotheism", 240, ['Religion'], {'Civics': 5, 'Religion': 20}, 
                "SPECIAL ABILITY: You may choose to annex all units in an area adjacent by land to your units. Barbarian tokens, pirate cities and units belonging to players holding Monotheism or Theology are unaffected.",
                "➖ ICONOCLASM AND HERESY: Reduce 1 additional city."),
    Advancement("Theocracy", 80, ['Religion', 'Civics'], {'Civics': 5, 'Religion': 5, 'Universal Doctrine': 10},
                "None",
                "➕ ICONOCLASM AND HERESY: You may choose and discard 2 commodity cards to prevent the city reduction effect for you."),
    Advancement("Universal Doctrine", 160, ['Religion'], {'Civics': 5, 'Religion': 10, 'Theology': 20}, 
                "SPECIAL ABILITY: You may choose to annex 1 pirate city or up to 5 barbarian tokens anywhere on the board.",
                "➖ SUPERSTITION: Reduce 1 additional city."),
    Advancement("Theology", 250, ['Religion'], {'Science': 5, 'Religion': 20}, 
                "None",
                "➕ ICONOCLASM AND HERESY: Reduce 3 less cities."),
    Advancement("Drama and Poetry", 80, ['Arts'], {'Arts': 10, 'Religion': 5, 'Rhetoric': 10}, 
                "None",
                "➕ CIVIL WAR: Select 5 less unit points.\n\
                ➕ CIVIL DISORDER: Reduce 1 less city."),
    Advancement("Rhetoric", 130, ['Arts'], {'Civics': 5, 'Arts': 10, 'Politics': 20}, 
                "During the Trade cards acquisition phase, you may acquire additional trade cards from stack 3 for 9 treasury tokens per card.",
                "None"),
    Advancement("Politics", 230, ['Arts'], {'Religion': 5, 'Arts': 20}, 
                "SPECIAL ABILITY: You may choose 1 of 2 options: 1) Gain up to 5 treasury tokens from stock. 2) Annex all units in an area adjacent by land to your units. Pay treasury tokens equal to the number of unit points annexed, or the effect is canceled. Barbarian tokens, pirate cities and units belonging to players holding Politics or Cultural Ascendancy are unaffected.",
                "None"),
    Advancement("Music", 80, ['Arts'], {'Religion': 5, 'Arts': 10, 'Enlightenment': 10}, 
                "None",
                "➕ CIVIL WAR: Select 5 less unit points.\n\
                ➕ CIVIL DISORDER: Reduce 1 less city."),
    Advancement("Enlightenment", 160, ['Religion'], {'Crafts': 5, 'Religion': 10, 'Philosophy': 20},
                "None",
                "➕ SUPERSTITION: Reduce 1 less city.\n\
                ➕ SLAVE REVOLT: Your city support rate is decreased by 1 during the resolution of Slave Revolt.\n\
                ➕ EPIDEMIC: If you are the primary victim, prevent 5 damage.\n\
                ➕ REGRESSION: For each step backward, you may choose to prevent the effect by destroying 2 of your cities (if possible non-coastal)."),
    Advancement("Philosophy", 220, ['Science', 'Religion'], {'Religion': 20, 'Science': 20}, 
                "Your units are protected against the effect of Fundamentalism.",
                "➕ ICONOCLASM AND HERESY: Reduce 2 less cities.\n\
                ➖ CIVIL WAR: Select 5 additional unit points."),
    Advancement("Astronavigation", 80, ['Science'], {'Religion': 5, 'Science': 10, 'Calendar': 10}, 
                "Your ships are allowed to move through open sea areas.",
                "None"),
    Advancement("Calendar", 180, ['Science'], {'Civics': 5, 'Science': 10, 'Public Works': 20}, 
                "None",
                "➕ FAMINE: Prevent 5 damage.\n\
                ➕ CYCLONE: Reduce 2 less selected cities."),
    Advancement("Public Works", 230, ['Civics'], {'Crafts': 5, 'Civics': 20}, 
                "Areas containing your cities may also contain 1 of your tokens. You are protected against the effect of Provincial Empire.",
                "None"),
    Advancement("Coinage", 90, ['Science'], {'Civics': 5, 'Science': 10, 'Trade Routes': 10}, 
                "You may choose to increase or decrease your tax rate by 1.",
                "➖ CORRUPTION: Discard 5 additional points of face value."),
    Advancement("Trade Routes", 180, ['Crafts'], {'Religion': 5, 'Crafts': 10, 'Trade Empire': 20}, 
                "SPECIAL ABILITY: You may choose to discard any number of commodity cards to gain treasury tokens at twice the face value of the commodity cards discarded this way.",
                "None"),
    Advancement("Trade Empire", 250, ['Crafts'], {'Civics': 5, 'Crafts': 20}, 
                "Once per turn, you may choose to use 1 substitute commodity card of at least the same face value when turning in an incomplete set of commodity cards.",
                "➖ CYCLONE: Select and reduce 1 additional city adjacent to the open sea area.\n\
                ➖ EPIDEMIC: If you are the primary victim, take 5 additional damage."),
    Advancement("Metalworking", 90, ['Crafts'], {'Civics': 5, 'Crafts': 10, 'Military': 10}, 
                "In conflicts, for each round of token removal all other players not holding Metalworking must remove their token first.",
                "None"),
    Advancement("Military", 170, ['Civics'], {'Civics': 10, 'Crafts': 5, 'Advanced Military': 20}, 
                "Your movement phase is after all other players not holding Military have moved. You are allowed to move tokens into areas containing cities belonging to players holding Diplomacy.",
                "None"),
    Advancement("Advanced Military", 240, ['Civics'], {'Civics': 20, 'Science': 5}, 
                "In conflicts, you may choose to remove tokens from areas adjacent by land. After each round of token removal a new check for token majority must be made. You may decide to wait for other token conflicts to be resolved first. You are allowed to cause conflict in areas containing units belonging to players holding Cultural Ascendancy.",
                "➖ CIVIL DISORDER: Reduce 1 additional city.") 
]

import streamlit as st

# Group colors for advancements and background coloring for discounts
GROUP_COLORS = {
    "Arts": "#00BFFF",  # Bright blue
    "Civics": "#FF4500",  # Bright red
    "Religion": "#FFFF00",  # Yellow
    "Science": "#00FF00",  # Brighter green
    "Crafts": "#FFA500"  # Orange
}

# Initialize session state for special advancements
if 'written_record_tokens' not in st.session_state:
    st.session_state['written_record_tokens'] = {"Arts": 0, "Civics": 0, "Religion": 0, "Science": 0, "Crafts": 0}
if 'monument_tokens' not in st.session_state:
    st.session_state['monument_tokens'] = {"Arts": 0, "Civics": 0, "Religion": 0, "Science": 0, "Crafts": 0}
if 'claimed_free_science' not in st.session_state:
    st.session_state['claimed_free_science'] = False
if 'applied_library_discount' not in st.session_state:
    st.session_state['applied_library_discount'] = False

# Helper functions for coloring and discount formatting
def get_group_color(groups):
    if len(groups) == 1:
        return f"background-color: {GROUP_COLORS[groups[0]]};"
    colors = [GROUP_COLORS.get(group, "#FFFFFF") for group in groups]
    return f"background: linear-gradient(90deg, {' ,'.join(colors)});"

def format_discount_with_colors(discounts):
    formatted_discounts = []
    for group, discount in discounts.items():
        color = GROUP_COLORS.get(group, "#FFFFFF")
        formatted_discounts.append(f'<span style="background-color: {color}; padding: 2px 4px; border-radius: 3px;">{group}</span>: {discount}')
    return ', '.join(formatted_discounts)

# Function to calculate the discounted price for an advancement
def calculate_discounted_cost(advancement, owned_advances, group_discounts):
    max_group_discount = 0
    for group in advancement.groups:
        group_discount = group_discounts.get(group, 0)
        max_group_discount = max(max_group_discount, group_discount)

    specific_discount = sum([owned.discounts.get(advancement.name, 0) for owned in owned_advances])
    total_discount = max_group_discount + specific_discount
    return max(advancement.cost - total_discount, 0)

# Function to calculate total group discounts based on owned advancements, starting tokens, Written Record, and Monument
def calculate_group_discounts(owned_advances, starting_tokens):
    total_discounts = {"Arts": 0, "Civics": 0, "Religion": 0, "Science": 0, "Crafts": 0}
    for adv in owned_advances:
        for group, discount in adv.discounts.items():
            if group in total_discounts:
                total_discounts[group] += discount
    # Add the starting tokens to the calculated discounts
    for group in total_discounts:
        total_discounts[group] += starting_tokens.get(group, 0)

    # Add discounts from Written Record and Monument
    written_record = st.session_state.get("written_record_tokens", {})
    monument = st.session_state.get("monument_tokens", {})
    
    for group in total_discounts:
        total_discounts[group] += written_record.get(group, 0)
        total_discounts[group] += monument.get(group, 0)
    
    return total_discounts

# Function to calculate Victory Points (VPs) based on the undiscounted cost
def calculate_vps(cost):
    if cost < 100:
        return 1
    elif 100 <= cost < 200:
        return 3
    else:
        return 6

# Function to calculate total cost of selected advancements
def calculate_total_cost(selected_advancements, owned_advances, group_discounts):
    total_cost = 0
    for adv in selected_advancements:
        total_cost += calculate_discounted_cost(adv, owned_advances, group_discounts)
    return total_cost

# Calculate total Victory Points for selected advancements (undiscounted cost)
def calculate_total_vps(selected_advancements):
    total_vps = 0
    for adv in selected_advancements:
        total_vps += calculate_vps(adv.cost)
    return total_vps

# Special advancements functions
def handle_written_record_sidebar():
    st.sidebar.warning("You've purchased Written Record! Please select 10 free credit tokens in multiples of 5.")
    
    if not st.session_state.get("written_record_locked", False):
        arts = st.sidebar.number_input("Arts (in multiples of 5)", min_value=0, max_value=10, step=5, key="record_arts")
        civics = st.sidebar.number_input("Civics (in multiples of 5)", min_value=0, max_value=10, step=5, key="record_civics")
        religion = st.sidebar.number_input("Religion (in multiples of 5)", min_value=0, max_value=10, step=5, key="record_religion")
        science = st.sidebar.number_input("Science (in multiples of 5)", min_value=0, max_value=10, step=5, key="record_science")
        crafts = st.sidebar.number_input("Crafts (in multiples of 5)", min_value=0, max_value=10, step=5, key="record_crafts")
        
        total_tokens = arts + civics + religion + science + crafts

        if total_tokens == 10:
            if st.sidebar.button("Lock Distribution", key=None):
                st.session_state["written_record_tokens"] = {"Arts": arts, "Civics": civics, "Religion": religion, "Science": science, "Crafts": crafts}
                st.session_state["written_record_locked"] = True
                st.sidebar.success(f"Written Record discount is locked: {arts} to Arts, {civics} to Civics, {religion} to Religion, {science} to Science, {crafts} to Crafts.\nPlease press the button again to apply the discounts.")
        else:
            st.sidebar.error("Total tokens must equal 10.")
    else:
        tokens = st.session_state["written_record_tokens"]
        st.sidebar.success(f"Written Record discount is locked: {tokens['Arts']} to Arts, {tokens['Civics']} to Civics, {tokens['Religion']} to Religion, {tokens['Science']} to Science, {tokens['Crafts']} to Crafts.")


def handle_monument_sidebar():
    st.sidebar.warning("You've purchased Monument! Please select 20 free credit tokens in multiples of 5.")
    
    if not st.session_state.get("monument_locked", False):
        arts = st.sidebar.number_input("Arts (in multiples of 5)", min_value=0, max_value=20, step=5, key="monument_arts")
        civics = st.sidebar.number_input("Civics (in multiples of 5)", min_value=0, max_value=20, step=5, key="monument_civics")
        religion = st.sidebar.number_input("Religion (in multiples of 5)", min_value=0, max_value=20, step=5, key="monument_religion")
        science = st.sidebar.number_input("Science (in multiples of 5)", min_value=0, max_value=20, step=5, key="monument_science")
        crafts = st.sidebar.number_input("Crafts (in multiples of 5)", min_value=0, max_value=20, step=5, key="monument_crafts")
        
        total_tokens = arts + civics + religion + science + crafts

        if total_tokens == 20:
            if st.sidebar.button("Lock Distribution", key=None):
                st.session_state["monument_tokens"] = {"Arts": arts, "Civics": civics, "Religion": religion, "Science": science, "Crafts": crafts}
                st.session_state["monument_locked"] = True
                st.sidebar.success(f"Monument discount is locked: {arts} to Arts, {civics} to Civics, {religion} to Religion, {science} to Science, {crafts} to Crafts.\nPlease press the button again to apply the discounts.")
        else:
            st.sidebar.error("Total tokens must equal 20.")
    else:
        tokens = st.session_state["monument_tokens"]
        st.sidebar.success(f"Monument discount is locked: {tokens['Arts']} to Arts, {tokens['Civics']} to Civics, {tokens['Religion']} to Religion, {tokens['Science']} to Science, {tokens['Crafts']} to Crafts.")

def handle_anatomy_discount(selected_advances):
    st.warning("You've selected Anatomy! You can choose another Science advancement under 100, and it will be free.")

    # List of science advances under 100 that the user doesn't own, sorted alphabetically by name
    science_advances = sorted([adv for adv in advancements if 'Science' in adv.groups and adv.cost < 100 and adv not in selected_advances], key=lambda x: x.name)
    
    free_science = st.selectbox("Select a Science advancement for free", options=[adv.name for adv in science_advances])

    claim_free_adv_button = st.button("Claim Free Science Advancement")

    if claim_free_adv_button and not st.session_state["claimed_free_science"]:
        for adv in science_advances:
            if adv.name == free_science:
                adv.cost = 0
                selected_advances.append(adv)
                st.session_state["claimed_free_science"] = True
                st.success(f"You've claimed {free_science} for free!")


def handle_library_discount(selected_advances):
    st.warning("You've selected Library! You get an additional 40-point discount on another advancement.")
    
    # List of unowned advancements, sorted alphabetically by name
    unowned_advances = sorted([adv for adv in advancements if adv not in selected_advances], key=lambda x: x.name)

    discounted_adv = st.selectbox("Select an advancement to apply the 40-point discount", options=[adv.name for adv in unowned_advances])

    apply_discount_button = st.button("Apply Library Discount")

    if apply_discount_button and not st.session_state["applied_library_discount"]:
        for adv in unowned_advances:
            if adv.name == discounted_adv:
                adv.cost = max(adv.cost - 40, 0)  # Apply the discount
                selected_advances.append(adv)
                st.session_state["applied_library_discount"] = True
                st.success(f"You've applied the discount to {discounted_adv}, reducing its cost by 40!")

# Streamlit App Structure
st.title("Advancement Cost Calculator")

# Sidebar for owned advancements selection
st.sidebar.subheader("Select Your Owned Advances")

# Let user select owned advancements in the sidebar
owned_advances_names = st.sidebar.multiselect(
    "Select owned advancements (sorted alphabetically)",
    sorted([adv.name for adv in advancements])  # Owned advancements are sorted alphabetically
)

# Find the actual advancement objects based on the selected names
owned_advances = [adv for adv in advancements if adv.name in owned_advances_names]

# Sidebar for sorting unowned advancements
st.sidebar.subheader("Sorting Options for Unowned Advances")
sorting_method = st.sidebar.radio(
    "Sort unowned advancements by:",
    options=["Alphabetical Order", "Discounted Cost"]
)

# Sidebar for total discounts per group and total VPs
st.sidebar.header("Total VPs and Discounts")
total_owned_vps = calculate_total_vps(owned_advances)
st.sidebar.write(f"Total Victory Points (VP) from owned advancements: {total_owned_vps}")

# Add radio buttons for starting tokens
st.sidebar.header("Starting Tokens")
starting_token_option = st.sidebar.radio(
    "Select starting tokens:",
    options=[
        "3 players short/normal or 5 players normal (10 tokens per group)",
        "4 players short/normal or 6/12 players normal (5 tokens per group)",
        "5-6 players short or 7-11/13-18 players any game (0 tokens per group)"
    ],
    index=2  # Set the default option to 0 tokens
)

# Assign starting tokens based on the selected option
starting_tokens = {"Arts": 0, "Civics": 0, "Religion": 0, "Science": 0, "Crafts": 0}

if starting_token_option == "3 players short/normal or 5 players normal (10 tokens per group)":
    starting_tokens = {"Arts": 10, "Civics": 10, "Religion": 10, "Science": 10, "Crafts": 10}
elif starting_token_option == "4 players short/normal or 6/12 players normal (5 tokens per group)":
    starting_tokens = {"Arts": 5, "Civics": 5, "Religion": 5, "Science": 5, "Crafts": 5}

# Calculate group discounts based on owned advancements and starting tokens
group_discounts = calculate_group_discounts(owned_advances, starting_tokens)

# Special advancements handling
if "Written Record" in owned_advances_names:
    handle_written_record_sidebar()
if "Monument" in owned_advances_names:
    handle_monument_sidebar()

# Sorting the unowned advancements based on the user's selection
unowned_advancements = [adv for adv in advancements if adv.name not in owned_advances_names]
if sorting_method == "Alphabetical Order":
    unowned_advancements.sort(key=lambda adv: adv.name)
else:
    unowned_advancements.sort(key=lambda adv: calculate_discounted_cost(adv, owned_advances, group_discounts))

# Main screen for selecting unowned advancements to buy
st.subheader("Available Advances")
selected_advancements = []

for advancement in unowned_advancements:
    discounted_cost = calculate_discounted_cost(advancement, owned_advances, group_discounts)
    vps = calculate_vps(advancement.cost)  # VP is based on the undiscounted cost

    # Display advancement details with group color backgrounds and description
    discount_info = format_discount_with_colors(advancement.discounts)
    color_background = get_group_color(advancement.groups)

    st.markdown(
        f'<div style="padding: 10px; border: 1px solid #ddd; {color_background}; color: black;">'
        f'<strong>{advancement.name}</strong><br>'
        f'Description: {advancement.description}<br>'
        f'Calamity effects: {advancement.calamity_effect}<br>'
        f'Cost: {advancement.cost} | Discounted Cost: {discounted_cost}<br>'
        f'Groups: {", ".join(advancement.groups)}<br>'
        f'Discounts: {discount_info}<br>'
        f'Victory Points (VP): {vps}'
        f'</div>', 
        unsafe_allow_html=True
    )

    # Add a checkbox to select/deselect the advancement
    selected = st.checkbox(f"Select {advancement.name}")

    # Update the selected_advancements list based on checkbox status
    if selected:
        selected_advancements.append(advancement)
    elif advancement in selected_advancements:
        selected_advancements.remove(advancement)

# Make an array for selected advancements
selected_advancements_name = ([adv.name for adv in selected_advancements])

# Handle special advancements in the main body
if "Anatomy" in selected_advancements_name:
    handle_anatomy_discount(selected_advancements)
if "Library" in selected_advancements_name:
    handle_library_discount(selected_advancements)

# Summary of selected advancements
if selected_advancements:
    st.subheader("Selected Advances")
    total_selected_cost = calculate_total_cost(selected_advancements, owned_advances, group_discounts)
    total_selected_vps = calculate_total_vps(selected_advancements)

    st.write(f"The selected advancements are: ", *selected_advancements_name)
    st.write(f"Total cost of selected advancements: {total_selected_cost} tokens")
    st.write(f"Total Victory Points (VP) from selected advancements: {total_selected_vps}")

# Display group discounts in the sidebar with colors
st.sidebar.write("Total Group Discounts:")

for group, discount in group_discounts.items():
    # Get the background color for the group
    group_color_style = get_group_color([group])
    
    # Use HTML to style the group name with the background color
    st.sidebar.markdown(
        f'<div style="{group_color_style}; padding: 2px 4px; border-radius: 3px; display: inline-block;">'
        f'{group}</div>: {discount}',
        unsafe_allow_html=True
    )

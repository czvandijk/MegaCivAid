import streamlit as st

# Preset civilizations
preset_civilisations = {
    "3 players East": ["10. Kushan", "16. Indus", "18. Parthia"],
    "4 players East": ["10. Kushan", "12. Persia", "16. Indus", "18. Parthia"],
    "5 players East": ["2. Saba", "6. Babylon", "12. Persia", "14. Nubia", "18. Parthia"],
    "6 players East": ["2. Saba", "6. Babylon", "10. Kushan", "12. Persia", "16. Indus", "18. Parthia"],
    "7 players East": ["2. Saba", "6. Babylon", "10. Kushan", "12. Persia", "14. Nubia", "16. Indus", "18. Parthia"],
    "8 players East": ["2. Saba", "4. Maurya", "6. Babylon",  "8. Dravidia", "10. Kushan", "12. Persia", "16. Indus", "18. Parthia"],
    "9 players East": ["2. Saba", "4. Maurya", "6. Babylon",  "8. Dravidia", "10. Kushan", "12. Persia", "14. Nubia", "16. Indus", "18. Parthia"],
    "3 players West": ["1. Minoa", "9. Hatti", "15. Hellas"],
    "4 players West": ["1. Minoa", "3. Assyria", "9. Hatti", "15. Hellas"],
    "5 players West": ["1. Minoa", "3. Assyria", "9. Hatti", "15. Hellas", "17. Egypt"],
    "6 players West": ["1. Minoa", "7. Carthage", "9. Hatti", "13. Iberia", "15. Hellas", "17. Egypt"],
    "7 players West": ["1. Minoa", "3. Assyria", "7. Carthage", "9. Hatti", "11. Rome", "15. Hellas", "17. Egypt"],
    "8 players West": ["1. Minoa", "3. Assyria", "7. Carthage", "9. Hatti", "11. Rome", "13. Iberia", "15. Hellas", "17. Egypt"],
    "9 players West": ["1. Minoa", "3. Assyria", "5. Celt", "7. Carthage", "9. Hatti", "11. Rome", "13. Iberia", "15. Hellas", "17. Egypt"],
    "10 players": ["1. Minoa", "2. Saba", "3. Assyria", "6. Babylon", "9. Hatti", "12. Persia", "14. Nubia", "15. Hellas", "17. Egypt", "18. Parthia"],
    "11 players": ["2. Saba", "3. Assyria", "4. Maurya", "6. Babylon", "8. Dravidia", "10. Kushan", "12. Persia", "14. Nubia", "16. Indus", "17. Egypt", "18. Parthia"],
    "12 players": ["1. Minoa", "2. Saba", "3. Assyria", "6. Babylon", "7. Carthage", "9. Hatti", "11. Rome", "12. Persia", "14. Nubia", "15. Hellas", "17. Egypt", "18. Parthia"],
    "13 players": ["1. Minoa", "2. Saba", "3. Assyria", "6. Babylon", "7. Carthage", "9. Hatti", "11. Rome", "12. Persia", "13. Iberia", "14. Nubia", "15. Hellas", "17. Egypt", "18. Parthia"],
    "14 players": ["1. Minoa", "2. Saba", "3. Assyria", "5. Celt", "6. Babylon", "7. Carthage", "9. Hatti", "11. Rome", "12. Persia", "13. Iberia", "14. Nubia", "15. Hellas", "17. Egypt", "18. Parthia"],
    "15 players": ["1. Minoa", "2. Saba", "3. Assyria", "6. Babylon", "7. Carthage", "9. Hatti", "10. Kushan", "11. Rome", "12. Persia", "13. Iberia", "14. Nubia", "15. Hellas", "16. Indus", "17. Egypt", "18. Parthia"],
    "16 players": ["1. Minoa", "2. Saba", "3. Assyria", "5. Celt", "6. Babylon", "7. Carthage", "9. Hatti", "10. Kushan", "11. Rome", "12. Persia", "13. Iberia", "14. Nubia", "15. Hellas", "16. Indus", "17. Egypt", "18. Parthia"],
    "17 players": ["1. Minoa", "2. Saba", "3. Assyria", "4. Maurya", "6. Babylon", "7. Carthage", "8. Dravidia", "9. Hatti", "10. Kushan", "11. Rome", "12. Persia", "13. Iberia", "14. Nubia", "15. Hellas", "16. Indus", "17. Egypt", "18. Parthia"],
    "18 players": ["1. Minoa", "2. Saba", "3. Assyria", "4. Maurya", "5. Celt", "6. Babylon", "7. Carthage", "8. Dravidia", "9. Hatti", "10. Kushan", "11. Rome", "12. Persia", "13. Iberia", "14. Nubia", "15. Hellas", "16. Indus", "17. Egypt", "18. Parthia"]
}

# List of all civilizations (used for custom selection)
civilisations_list = [
    "1. Minoa", "2. Saba", "3. Assyria", "4. Maurya", "5. Celt", "6. Babylon", 
    "7. Carthage", "8. Dravidia", "9. Hatti", "10. Kushan", "11. Rome", 
    "12. Persia", "13. Iberia", "14. Nubia", "15. Hellas", "16. Indus", 
    "17. Egypt", "18. Parthia"
]

# Default civilization timers
default_timer = 300  # Default 300 seconds (5 minutes)

# Helper function to get AST rank from civilization string
def get_ast_rank(civilization):
    return int(civilization.split(".")[0])

# Function to calculate movement order
def calculate_movement_order(players):
    players_sorted = sorted(
        players, 
        key=lambda x: (
            x['has_military'],        # Sort first by Military (Military last)
            -x['tokens'],                 # Then by number of tokens (Higher first)
            get_ast_rank(x['civilisation'])  # Lastly, by AST number (Lower first)
        )
    )
    return players_sorted

# Function to generate timers in HTML
def generate_timer_html(player_id, player_name, civilization_name, time_left):
    timer_html = f"""
    <script>
    let timer{player_id} = {time_left};
    let running{player_id} = false;
    let interval{player_id};

    function startTimer{player_id}() {{
        if (!running{player_id}) {{
            running{player_id} = true;
            interval{player_id} = setInterval(() => {{
                if (timer{player_id} > 0) {{
                    timer{player_id}--;
                    document.getElementById("timer_display_{player_id}").innerHTML = 
                        Math.floor(timer{player_id} / 60) + ":" + ('0' + timer{player_id} % 60).slice(-2);
                }} else {{
                    clearInterval(interval{player_id});
                }}
            }}, 1000);
        }}
    }}

    function pauseTimer{player_id}() {{
        running{player_id} = false;
        clearInterval(interval{player_id});
    }}

    function resetTimer{player_id}() {{
        timer{player_id} = {time_left};
        document.getElementById("timer_display_{player_id}").innerHTML = 
            Math.floor(timer{player_id} / 60) + ":" + ('0' + timer{player_id} % 60).slice(-2);
    }}
    </script>

    <div>
        <h4>{civilization_name} - {player_name}'s Timer</h4>
        <div id="timer_display_{player_id}">
            {time_left // 60}:{'0' + str(time_left % 60)}
        </div>
        <button onclick="startTimer{player_id}()">Start</button>
        <button onclick="pauseTimer{player_id}()">Pause</button>
        <button onclick="resetTimer{player_id}()">Reset</button>
    </div>
    """
    return timer_html

# Streamlit App
st.title("Mega Civilization Movement Tool")

# Select preset or custom civilization setup
preset = st.selectbox("Choose Preset or Custom Setup", ["Custom Setup"] + list(preset_civilisations.keys()))

players = []
if preset != "Custom Setup":
    selected_civs = preset_civilisations[preset]
    num_players = len(selected_civs)
else:
    num_players = st.number_input("Number of Players", min_value=1, max_value=18, value=3)
    selected_civs = [st.selectbox(f"Choose Civilisation for Player {i+1}", civilisations_list) for i in range(num_players)]

# Collect player data
for i in range(num_players):
    civ_name = selected_civs[i]  # Get civilization from preset or custom
    player_name = st.text_input(f"{civ_name} - Player {i+1}", f"Player {i+1}")
    tokens = st.number_input(f"{player_name}'s Tokens on Board", min_value=0, max_value=55, value=30)
    has_military = st.checkbox(f"Does {player_name} have Military?", key=f"military_{i}")
    
    players.append({
        "player_name": player_name,
        "tokens": tokens,
        "has_military": has_military,
        "civilisation": civ_name,
    })

# Calculate movement order based on the inputs
movement_order = calculate_movement_order(players)

# Display the movement order
st.subheader("Player Movement Order")
for i, player in enumerate(movement_order, 1):
    st.write(f"{i}: {player['civilisation']} - {player['player_name']} (Military: {player['has_military']}, Tokens: {player['tokens']})")

# Timer settings
default_time = st.number_input("Default Timer Duration (in seconds)", min_value=1, max_value=3600, value=300)

# Display timers for each player based on the movement order
st.subheader("Timers (in Movement Order)")
for i, player in enumerate(movement_order, 1):
    custom_time = st.number_input(f"{player['player_name']}'s Timer Duration (in seconds)", min_value=1, max_value=3600, value=default_time)
    timer_html = generate_timer_html(i, player['player_name'], player['civilisation'], custom_time)
    st.components.v1.html(timer_html, height=150)

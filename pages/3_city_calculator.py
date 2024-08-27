import streamlit as st

# Title of the app 
st.title("City Building Calculator")

# Instructions
st.write("""
This app calculates the maximum number of cities you can build in a round based on your population tokens and cities on the board.\n
A regular city needs 6 population tokens to be built. You can construct a regular city in an area with a city site. In an area without sity site, you can build a wilderness city for 12 population tokens. The population limit of an area containing a wilderness city cannot be 0 (even if you hold Agriculture).\n
Normally, the city support rate is 2. This means you need at least two population tokens for every city during a city support check.\n         
Two advancements influence city building:
- **Architecture**: Once per turn, when constructing a city, you may choose to pay up to half of the required number of tokens from treasury. You are allowed to use the ability when building a wilderness city. 
- **Cultural Ascendancy**: Your default city support rate is increased by 1 (so is usually 3 instead of 2).
""")

# Input sliders for number of tokens and cities
tokens_on_board = st.slider("Number of tokens on the board:", 0, 55, 0)
cities_on_board = st.slider("Number of cities on the board:", 0, 9, 0)

# Checkbox for advances
has_architecture = st.checkbox("Do you hold Architecture?", value=False)
has_cultural_ascendancy = st.checkbox("Do you hold Cultural Ascendancy?", value=False)

# Adjust the number of tokens required for maintaining cities based on Cultural Ascendancy
tokens_per_city = 3 if has_cultural_ascendancy else 2

# Calculate the remaining tokens after supporting current cities
available_tokens = tokens_on_board - tokens_per_city * cities_on_board

# If there are not enough tokens to support the current cities
if available_tokens < 0:
    st.error(f"Not enough tokens to maintain the current cities. You need {abs(available_tokens)} more token(s).")
elif cities_on_board >= 9:
    st.error(f"You already have the maximum number of cities (9). You cannot build any more cities.")
else:
    max_new_cities = []
    # Loop through all possible numbers of wilderness cities
    for wilderness_cities in range(0, (9 - cities_on_board) + 1):
        # Cost for building wilderness cities
        if wilderness_cities == 0:
            wilderness_cost = 0
        elif has_architecture:
            wilderness_cost = 6 + (wilderness_cities - 1) * 12  # First wilderness city is discounted
        else:
            wilderness_cost = wilderness_cities * 12

        remaining_tokens = available_tokens - wilderness_cost - wilderness_cities * tokens_per_city

        # If remaining tokens are sufficient, calculate the number of regular cities
        if remaining_tokens >= 0:
            max_regular_cities = 0
            # First regular city with Architecture discount
            if has_architecture and wilderness_cities == 0 and remaining_tokens >= (3 + tokens_per_city):
                remaining_tokens -= (3 + tokens_per_city)  # Architecture discount applied to first regular city
                max_regular_cities += 1

            # Subsequent regular cities (without Architecture discount)
            while remaining_tokens >= (6 + tokens_per_city) and (cities_on_board + wilderness_cities + max_regular_cities) < 9:
                remaining_tokens -= (6 + tokens_per_city)
                max_regular_cities += 1
            
            max_new_cities.append({
                "wilderness": wilderness_cities,
                "regular": max_regular_cities,
                "spare_tokens": remaining_tokens
            })

    # Display results
    st.write("Possible combinations:")
    for option in max_new_cities:
        st.success(
            f"- In the optimal case, you can build and support {option['wilderness']} wilderness city/cities and {option['regular']} regular city/cities and have {option['spare_tokens']} spare population token(s)."
        )

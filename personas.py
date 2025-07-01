def get_persona(name):
    name = name.strip().lower()
    
    if name == "the dreamer":
        return {
            "name": "The Dreamer",
            "traits": {
                "happiness_boost": 5,
                "stress_penalty": 3,
                "growth_modifier": -2,
                "description": "Optimistic and free-spirited. Values fulfillment over money."
            }
        }

    elif name == "the hustler":
        return {
            "name": "The Hustler",
            "traits": {
                "happiness_boost": -2,
                "stress_penalty": 5,
                "growth_modifier": 8,
                "description": "Ambitious and driven. Chases growth, but often at a personal cost."
            }
        }

    elif name == "the balanced one":
        return {
            "name": "The Balanced One",
            "traits": {
                "happiness_boost": 2,
                "stress_penalty": 1,
                "growth_modifier": 2,
                "description": "Disciplined and calm. Aims for harmony in all aspects of life."
            }
        }

    else:
        return {
            "name": "Unknown",
            "traits": {
                "happiness_boost": 0,
                "stress_penalty": 0,
                "growth_modifier": 0,
                "description": "Default mode with no influence."
            }
        }

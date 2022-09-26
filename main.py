# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

# 1 greeting template


def greet(name, greeting_template="Hello, <name>!"):
    message = greeting_template.replace("<name>", name)
    return message


# 2 force= mass*gravity


planets = {
    "sun": 274,
    "jupiter": 24.9,
    "neptune": 11.2,
    "saturn": 10.4,
    "earth": 9.8,
    "uranus": 8.9,
    "venus": 8.9,
    "mars": 3.7,
    "mercury": 3.7,
    "moon": 1.6,
    "pluto": 0.6
}


def force(mass, body="earth"):
    gravity = planets[body]
    force = mass * gravity
    return force


# 3 pull= G*((m1*m2)/d**2)


def pull(m1, m2, d):
    g = 6.674*10**-11
    pull = g*((m1*m2)/d**2)

    return pull


print(greet("Pietje", "Wassup, <name>!"))
print(force(274, "sun"))
print(pull(0.6, 274, 7.500000000))

define g = Character("Grim Reaply", color=Color("#aa0000"))
define c = Character("Chairmaker", color=Color("#208030"))

label start:

label enter_chairmaker_shack:

    scene bg chairmaker_shack

    "As you enter the shack, you see a small kitchen in the corner, and a small living area with a small bed."

    "Most of the space, however, is clearly used as a workshop. Blocks of wood lie on the work surfaces and a variety of tools hang from the wall."

    "A door at the back leads into a room cluttered with furniture. There is a woman hunched over a table in the living area, drinking something hot."

label chairmaker_shack_interactions:

    menu:

        "Investigate the tools":
            jump investigate_chairmaker_tools
        "Approach the woman":
            jump meet_chairmaker
        "Enter the room of furniture":
            jump enter_chair_warehouse
        "Leave":
            jump leave_chairmaker_shack

label meet_chairmaker:

    g "Hi."

    "The woman looks at you in silence."

    jump chairmaker_shack_interactions

label investigate_chairmaker_tools:

    "Some of the tools look like they are used for carpentry, others for metalworking. Some look so specific you couldn't guess what they might be used for."

    jump chairmaker_shack_interactions

label enter_chair_warehouse:

    "The warehouse is full of chairs, all different shapes and size, made with a range of materials."

    "There are a few other pieces of furniture dotted around. A coffee table, a footstool, a chest of drawers. But the vast majority are chairs."

    jump chairmaker_shack_interactions

label leave_chairmaker_shack:

    "You leave the shack."
    
    return

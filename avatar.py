
def main():
    print("----- AVATAR ----- ")

    answer = str(input("Select an Avatar or create your own:\n"))

    # Uses while loop to control the answer that is inputted.
    while answer != 'Jeff' and answer != 'Adam' and answer != 'Chris' and answer != 'custom' and answer != 'exit':
        answer = str(input("Select an Avatar or create your own:\n"))
    # ----------------------------------
    # Block of function calls that do not need further input from user
    if answer == 'Jeff':
        print()
        jeff()
    if answer == 'Adam':
        print()
        adam()
    if answer == 'Chris':
        print()
        chris()
    # ----------------------------------
    # Requires more input from user introduces variables ( hat_style, eye_style, hair_style,
    # arm_style, torso_length, leg_length, shoe_style)
    # Then calls functions passing needed variables as parameters.
    if answer == 'custom':
        print("Answer the following questions to create a custom avatar")
        hat_style = str(input('Hat style ?\n'))
        eye_style = str(input('Character for eye_style ?\n'))
        hair_style = str(input('Shaggy hair_style (True/False) ?\n'))
        arm_style = str(input('Arm style ?\n'))
        torso_length = int(input("Torso length ?\n"))
        leg_length = int(input("Leg length (1-4) ?\n"))
        shoe_style = str(input("Shoe look ?\n"))
        print()
        hat(hat_style)
        head(eye_style, hair_style)
        arm(arm_style)
        torso(torso_length)
        legs(leg_length, shoe_style)

# Static function that prints Jeff avatar


def jeff():

    print("       ~-~")
    print("     /-~-~-\ ")
    print(" ___/_______\___")
    print('    |"""""""| ')
    print("    | 0   0 | ")
    print("    |   V   | ")
    print("    |  ~~~  | ")
    print("     \_____/   ")
    print(" 0====|---|====0")
    print("      |-X-| ")
    print("      |-X-|   ")
    print("      HHHHH   ")
    print("     /// \\\\\\")
    print("    ///   \\\\\\")
    print("#HHH#       #HHH#")

# Static function that prints Adam avatar


def adam():

    print("       ~-~")
    print("     /-~-~-\ ")
    print("    /_______\\___")
    print("    |'''''''|")
    print("    | *   * |")
    print("    |   V   |")
    print("    |  ~~~  |")
    print("     \_____/")
    print("      |-X-|")
    print(" 0TTTT|---|TTTT0")
    print("      |-X-|")
    print("      |-X-|")
    print("      |-X-|")
    print("      HHHHH")
    print("     /// \\\\\\")
    print("    ///   \\\\\\")
    print("   ///     \\\\\\")
    print("<|||>       <|||>")

# Static function that prints adam avatar


def chris():

    print("       ~-~")
    print("     /-~-~-\ ")
    print("    /_______\ ")
    print('    |"""""""|')
    print("    | U   U |")
    print("    |   V   |")
    print("    |  ~~~  |")
    print("     \_____/")
    print("      |-X-|")
    print(" 0WWWW|---|WWWW0")
    print("      |-X-|")
    print("      HHHHH")
    print("     /// \\\\\\")
    print("    ///   \\\\\\")
    print("   ///     \\\\\\")
    print("  ///       \\\\\\")
    print("<>-<>       <>-<>")

# The hat function takes the parameter style from main then the if statements manage which style is printed.


def hat(style):
    if style == 'front':
        print("       ~-~")
        print("     /-~-~-\ ")
        print("    /_______\ ")
    if style == 'right':
        print("       ~-~")
        print("     /-~-~-\ ")
        print("    /_______\___ ")
    if style == 'left':
        print("       ~-~")
        print("     /-~-~-\ ")
        print(" ___/_______\ ")
    if style == 'both':
        print("       ~-~")
        print("     /-~-~-\ ")
        print(" ___/_______\___ ")

# The head function takes in 2 parameters from main eye which is passed to the function and prints out and
# hair which is evaluated by the if statement to determine if the avatar should have shaggy hair.


def head(eye, hair):
    if hair == 'True':
        print('    |"""""""|')
    else:
        print("    |'''''''|")
    print("    | "+eye+"   "+eye+" |")
    print("    |   V   |")
    print("    |  ~~~  |")
    print("     \_____/")

# The arn function takes the parameter style from main then the if statements manage which style is printed.


def arm(style):
    print(" 0"+style+style+style+style+"|---|"+style+style+style+style+"0")

# The torso function takes the parameter height from main then the while statement prints the correct torso height.


def torso(height):
    i = 0
    while i < height:
        print("      |-X-|")
        i += 1

# The leg function takes the parameters length and shoe_style from main. Then the if statements determine which
# tier of leg height to print. After the legs print the shoe_style is just printed.


def legs(length, shoe_style):
    print("      HHHHH")

    if length > 0:
        print("     /// \\\\\\")
    if length > 1:
        print("    ///   \\\\\\")
    if length > 2:
        print("   ///     \\\\\\")
    if length > 3:
        print("  ///       \\\\\\")
    print(shoe_style+"       "+shoe_style)


main()


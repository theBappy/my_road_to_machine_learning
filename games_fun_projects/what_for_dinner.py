import requests


def main():
    menu_detail = dict(
        requests.get("http://themealdb.com/api/json/v1/1/random.php").json()
    )["meals"][0] 

    menu_name = menu_detail["strMeal"]
    menu_category = menu_detail["strCategory"]
    menu_tags = menu_detail["strTags"]
    menu_country = menu_detail["strArea"]
    menu_instruction = menu_detail["strInstructions"]
    menu_video = menu_detail["strYoutube"]

    class b_colors:
        HEADER = "\033[95m"
        OKBLUE = "\033[94m"
        OKCYAN = "\033[96m"
        OKGREEN = "\033[92m"
        WARNING = "\033[93m"
        FAIL = "\033[91m"
        ENDC = "\033[0m"
        BOLD = "\033[1m"
        UNDERLINE = "\033[4m"

    print(f"-------------------------------------------------------------")
    print(f"Let's have a {b_colors.BOLD}{menu_name}{b_colors.ENDC} for dinner!")
    print(f"This menu is {menu_country} and it is {menu_category}!")
    print(
        f"You can follow this link: {b_colors.OKBLUE}{menu_video}{b_colors.ENDC} or the instructions to cook it:\n{menu_instruction}"
    )
    print(f"-------------------------------------------------------------")


if __name__ == "__main__":
    main()

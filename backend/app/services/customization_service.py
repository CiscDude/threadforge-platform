class CustomizationService:

    @staticmethod
    def get_available_colors():
        return [
            "Black",
            "White",
            "Red",
            "Blue",
            "Green",
            "Yellow"
        ]

    @staticmethod
    def get_available_sizes():
        return [
            "XS",
            "S",
            "M",
            "L",
            "XL",
            "XXL"
        ]

    @staticmethod
    def get_available_print_locations():
        return [
            "Front",
            "Back",
            "Left Sleeve",
            "Right Sleeve"
        ]

    @staticmethod
    def calculate_customization_price(color, size, print_location):
        base_price = 20.0

        if print_location in ["Back", "Left Sleeve", "Right Sleeve"]:
            base_price += 5.0

        return {
            "color": color,
            "size": size,
            "print_location": print_location,
            "price": base_price
        }

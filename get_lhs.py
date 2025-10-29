class Equation:
    def __init__(self, equation):
        """Initialize with the equation string"""
        self.equation = equation

    def get_lhs(self):
        """Return the Left-Hand Side (LHS) of the equation"""
        if "=" in self.equation:
            lhs = self.equation.split("=")[0].strip()
            return lhs
        else:
            return "No '=' found in the equation."

    def show_lhs(self):
        """Display the LHS clearly"""
        lhs = self.get_lhs()
        print(f"🔹 Left-Hand Side (LHS): {lhs}")

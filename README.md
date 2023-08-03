# CodeAlpha_Project_Name1
# CURRENCY CONVERTER
Here are the step-by-step instructions to build a currency converter with a graphical user interface using Python and the `forex-python` library:

1. Install the required libraries:
   - Install the `tkinter` library, which comes with Python's standard library and is used for GUI development.
   - Install the `forex-python` library to fetch real-time exchange rates and perform currency conversion.

2. Import the necessary libraries:
   - Import `tkinter` as `tk` for creating the GUI.
   - Import `CurrencyRates` from `forex_python.converter` for currency conversion.

3. Create a class `CurrencyConverterApp` to handle the GUI and currency conversion functionality.

4. Initialize the main GUI window:
   - Set the window title and dimensions.

5. Create labels and drop-down menus for currency selection:
   - Create labels for "From Currency" and "To Currency."
   - Fetch available currencies using the `get_rates` method from the `CurrencyRates` object.
   - Create `StringVar` objects to store the selected currencies.
   - Use `OptionMenu` to create drop-down menus with the available currencies.

6. Create a label and entry field for entering the amount to convert:
   - Create a label for "Amount."
   - Create an entry field using `Entry` to input the amount.

7. Create a button for currency conversion:
   - Create a button labeled "Convert."
   - Attach the `convert_currency` method as the command for the button.

8. Define the `convert_currency` method:
   - Get the selected currencies and the amount entered in the entry field.
   - Convert the amount using the `convert` method from the `CurrencyRates` object.
   - Display the result of the conversion in a label.

9. Handle exceptions during currency conversion:
   - Wrap the conversion process in a `try-except` block to handle any errors that may occur during conversion.

10. Start the GUI event loop:
    - Create a `tk.Tk()` instance to represent the main window.
    - Create an instance of the `CurrencyConverterApp` class, passing the main window as an argument.
    - Start the GUI event loop using `root.mainloop()`.

After following these steps, you will have a working currency converter with a graphical user interface, allowing you to input currencies and perform real-time currency conversion.

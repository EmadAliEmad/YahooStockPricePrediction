# Stock Price Prediction (SARIMAX)

This repository contains the code for a stock price prediction application using the SARIMAX time series forecasting model.

## Overview

This project aims to predict future stock prices based on historical data using the SARIMAX model. It allows a user to select a date within the dataset's range and make predictions for a specified forecasting horizon.

## Technologies Used

*   **Python:** The core programming language.
*   **Pandas:** For data manipulation and analysis.
*   **Statsmodels:** For time series modeling (SARIMAX).
*   **Scikit-learn (sklearn):** For evaluation metrics.
*   **Streamlit:** For building the interactive web application.
*   **Matplotlib:** For plotting results.

## Dataset

The data used for this project comes from the file `yahoo_stock.csv`. It's expected to have a 'Date' column as the index and a 'Close' column containing the closing stock prices.

## Project Structure

The project directory `project_for_github/` contains the following files:project_for_github/


## Project Structure

The project directory `project_for_github/` contains the following files:project_for_github/

project_for_github/
├── .gitignore # Specifies intentionally untracked files that Git should ignore.
├── app.py # Main Streamlit application code.
├── requirements.txt # Lists Python package dependencies.
├── sarimax_model.pkl # Trained SARIMAX model (if needed).
├── yahoo_stock.csv # Stock price data.
└── README.md # Project overview.




## How to Run the Application

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your_username/your_repository_name.git
    ```
    Replace `your_username` and `your_repository_name` with your actual GitHub username and repository name.

2.  **Navigate to the project directory:**
    ```bash
    cd project_for_github
    ```

3.  **Create a virtual environment and install dependencies:**

    * Create the virtual environment
        ```bash
         python -m venv env
         ```
    * Activate the virtual environment
      *  Windows:
          ```bash
           .\env\Scripts\activate
           ```
      *  Linux/macOS:
          ```bash
          source env/bin/activate
          ```
    * Install required packages:
        ```bash
        pip install -r requirements.txt
        ```

4.  **Run the Streamlit application:**

    ```bash
    streamlit run app.py
    ```

5.  Open the URL provided by Streamlit in your browser.

## Usage

1.  On the web interface, select a date from the dropdown menu. This date must be present in the provided dataset
2.  The application will display a stock price chart, showing the train, test data, and the predicted stock prices. It will also show the RMSE for that prediction.

## Notes
*   The SARIMAX model's parameters are set in the code and might need to be adjusted for different datasets or to improve accuracy.
* The window training size is set to 120, you can change this value in the code to better fit your application.

## Contact

If you have any questions or suggestions, please reach out to me at your_email@example.com

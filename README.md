# MultiLanguage Invoice Extractor

MultiLanguage Invoice Extractor is a Streamlit-based web application that allows users to upload an image of an invoice and get detailed information about it using Google's Generative AI model.

## Features

- Upload invoice images in JPG, JPEG, or PNG formats.
- Use Google's Gemini Pro Vision model to analyze the uploaded invoice.
- Extract and understand information from the invoice image based on user prompts.

## Requirements

- Python 3.7+
- Streamlit
- Python-dotenv
- Google Generative AI (Gemini Pro Vision)
- Pillow (PIL)

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/multilanguage-invoice-extractor.git
    cd multilanguage-invoice-extractor
    ```

2. Create and activate a virtual environment:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Set up your environment variables:

    Create a `.env` file in the root directory of the project and add your Google API key:

    ```dotenv
    GOOGLE_API_KEY=your_google_api_key
    ```

## Usage

1. Run the Streamlit application:

    ```sh
    streamlit run invoice_extrct_app.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Upload an image of an invoice and provide a prompt to extract information from the invoice.

## Code Explanation

- `invoice_extrct_app.py`: The main application file that sets up the Streamlit interface and handles image upload and AI interaction.
- `get_gemini_response`: Function to get a response from the Gemini Pro Vision model.
- `input_image_details`: Function to process the uploaded image file.

## Example

Here's an example of how to use the application:
![image](https://github.com/Subhradyuti/MultiLanguage-Invoice-Extractor/assets/133640355/ee2a70fa-db24-4ab6-95d5-6d897f41815e)

1. Open the application in your web browser.
2. Enter a prompt in the "Input Prompt" field.
3. Upload an invoice image using the "Choose an image of the invoice..." button.
4. Click on "Tell Me About The Invoice" to get the response from the AI.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any features, bugs, or enhancements.

## License

This project is licensed under the MIT License.


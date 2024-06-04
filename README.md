# WAP Twitch Test Suite

This repository contains a Selenium test suite for automating tests on a website(Mobile emulator from Google Chrome). 
The tests are written using Python and pytest.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Running Tests](#running-tests)
- [Visual Demonstration](#visual-demonstration)

## Prerequisites
- Python 3.x
- Google Chrome
- ChromeDriver

## Setup

1. **Clone the repository**:
    ```sh
    git clone https://github.com/shamannexus/wap_twitch_testing.git
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

## Running Tests

1. **Run the tests using pytest**:
    ```sh
    pytest
    ```

2. **Run a specific test**:
    ```sh
    pytest -k test_open_random_stream
    ```

## Visual Demonstration

Below is a GIF showing the test running locally:

![Test Running Locally](open_streamer_page.gif)


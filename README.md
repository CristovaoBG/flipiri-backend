# Festival Management System

This project is a comprehensive system for managing festivals, developed to replace Excel spreadsheet-based management. The system offers advanced functionalities for controlling authors, activities, travel, and accommodations, as well as providing alerts and cost calculations.

## DEMO

A demonstration can be accessed at the following link:
https://cristovaobg.github.io/flipiri-frontend/

## Main Features

- Management of authors and their participation in multiple activities
- Control of travel and accommodations for participants
- Detection and alerting of schedule conflicts (date and location collisions)
- Verification of author availability based on arrival and departure dates
- Control of accommodation vacancies
- Calculation and presentation of total costs
- Intuitive and responsive user interface

## Technologies Used

- Frontend: Vue 3
- Backend: Flask (Python)
- Database: MongoDB

## Project Structure

The project is divided into two repositories:
- Frontend: [https://github.com/CristovaoBG/flipiri-frontend](https://github.com/CristovaoBG/flipiri-frontend)
- Backend: [https://github.com/CristovaoBG/flipiri-backend](https://github.com/CristovaoBG/flipiri-backend)

## Installation and Configuration

### Frontend

1. Clone the repository:
   ```
   git clone https://github.com/CristovaoBG/flipiri-frontend.git
   ```
2. Navigate to the project directory:
   ```
   cd flipiri-frontend
   ```
3. Install the dependencies:
   ```
   npm install
   ```
4. Start the development server:
   ```
   npm run dev
   ```

### Backend

1. Clone the repository:
   ```
   git clone https://github.com/CristovaoBG/flipiri-backend.git
   ```
2. Navigate to the project directory:
   ```
   cd flipiri-backend
   ```
3. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
4. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Set the environment variable "FLIPIRI_K" with the MongoDB URL value;
6. Start the Flask server:
   ```
   python server.py
   ```

## Contact

- cristovao@live.com
- https://www.linkedin.com/in/crist%C3%B3v%C3%A3o-bartholo-ba5505202/
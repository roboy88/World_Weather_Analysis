# World_Weather_Analysis
For learning APIs from Module 6

Project Overview
create a PlanMyTrip app with weather description to the weather data and filter the data for user weather preferences, which will be used to identify potential travel destinations and nearby hotels. From the list of potential travel destinations, the user can choose four cities to create a travel itinerary. Also using the Google Maps Directions API, create a travel route between the four cities as well as a marker layer map.

Resources
Anaconda 4.11.0, Python 3.9, jupyter notebook
Library Pandas, gmaps api, openweather api, Numpy, requests,citypy
Challenge Overview
Prerequisite:

Deliverable 2: Download the Vacation_Search_starter_code.ipynb file and rename it to Vacation_Search.ipynb file.
Deliverable 3: Download the Vacation_Itinerary_starter_code.ipynb file and rename it to Vacation_Itinerary.ipynb file.
Deliverable 1: Retrieve Weather Data
Generate a set of 2,000 random latitudes and longitudes, retrieve the nearest city, and perform an API call with the OpenWeatherMap. In addition to the city weather data you gathered in this module, use your API skills to retrieve the current weather description for each city. Then, create a new DataFrame containing the updated weather data.

Use the step-by-step instructions below.

Step 1: Create a folder called Weather_Database.

Step 2: Create a new Jupyter Notebook file to retrieve the weather data, and name it Weather_Database.ipynb.

Step 3: Create a new set of 2,000 random latitudes and longitudes.

Step 4: Get the nearest city using the citipy module.

Step 5: Perform an API call with the OpenWeatherMap.

Step 6: Retrieve the following information from the API call:

-   Latitude and longitude
-   Maximum temperature
-   Percent humidity
-   Percent cloudiness
-   Wind speed
-   Weather description (for example, clouds, fog, light rain, clear sky)
Step 7: Add the data to a new DataFrame.

Step 8: Export the DataFrame as a CSV file, and save it as WeatherPy_Database.csv in the Weather_Database folder. The new cities_data DataFrame summarizes the current weather description.

Deliverable 2: Create a Customer Travel Destinations Map
Prerequisite 1: Create a folder called Vacation_Search.

Prerequisite 2: Download the Vacation_Search_starter_code.ipynb file into your Vacation_Search folder, and rename it Vacation_Search.ipynb.

Prerequisite 3:In the Vacation_Search.ipynb file, make sure the dependencies and API keys are imported correctly.

Use the instructions below to add code where indicated by the numbered-step comments in the starter code file.

Step 1: Import the WeatherPy_Database.csv file from your Weather_Database folder from Deliverable 1 as a DataFrame.

Step 2: Write two input statements that prompt the user to enter their minimum and maximum temperature criteria for their vacation.

Step 3: Use the loc method to filter the city_data_df DataFrame for temperature criteria collected in Step 2, then create a new DataFrame.

Steps 4a-b: Determine if there are any empty rows, then drop them if necessary and create a new DataFrame.

Steps 5a-b: Use the provided code to create a new DataFrame, hotel_df, that will hold the hotel names from the hotel search in Steps 6a-6f.

Step 6a: We have supplied the search parameters, which are the same as in this module, that you’ll need to use to search for a hotel for each city in Steps 6b-f.

Steps 6b-f: Iterate through the hotel_df DataFrame, retrieve the latitude and longitude of each city to find the nearest hotel based on the search parameters from Step 6a, then add the hotel name to the hotel_df
DataFrame. If a hotel isn't found, skip to the next city.

Step 7: Drop any rows in the hotel_df DataFrame where a hotel name is not found.

Steps 8a-b: Create an output file to store the hotel_df DataFrame as WeatherPy_vacation.csv in the Vacation_Search folder.

Step 9: Add the city name, the country code, the weather description, and the maximum temperature for the city to the info_box_template format template we have provided.

Step 10a: Use the provided list comprehension code to retrieve the city data from each row, which will then be added to the formatting template and saved in the hotel_info list.

Step 10b: Use the provided code snippet to retrieve the latitude and longitude from each row and store them in a new DataFrame.

Steps 11a-b: Refactor your previous marker layer map code to create a marker layer map that will have pop-up markers for each city on the map.

Step 12: Take a screenshot of your map and save it to the Vacation_Search folder as WeatherPy_vacation_map.png.

Deliverable 3: Create a Travel Itinerary Map
Prerequisite 1: Enable the "Directions API" in your Google account for your API key.

Prerequisite 2: Create a folder called Vacation_Itinerary.

Prerequisite 3: Download the Vacation_Itinerary_starter_code.ipynb file into your Vacation_Itinerary folder and rename it Vacation_Itinerary.ipynb.

Prerequisite 4: In the Vacation_Itinerary.ipynb file, make sure the dependencies and API keys are imported.

Use the instructions below to add code where indicated by the numbered-step comments in the starter code file.

Step 1: Import the WeatherPy_vacation.csv file from your Vacation_Search folder from Deliverable 2 as a DataFrame.

Steps 2-4: Copy or Refactor the code from Steps 11a-b of Deliverable 2 to create a marker layer map of the vacation search results. From the vacation search map, choose four cities that a customer might want to visit. They should be close together and in the same country.

Step 5: Use the variables we have provided and the loc method to create separate DataFrames for each city on the travel route.

Step 6: Use the to_numpy() function and list indexing to write code to retrieve the latitude-longitude pairs as tuples from each city DataFrame.

Step 7: Use the gmaps documentation to create a directions layer map using the variables from Step 6, where the starting and ending city are the same city, the waypoints are the three other cities, and the travel_mode is either "DRIVING", "BICYCLING", or "WALKING".

Step 8: Use the provided concat() function code snippet to combine the four separate city DataFrames into one DataFrame.

Steps 9-11: Refactor the code from Steps 2-4 to create a new marker layer map of the cities on the travel route. Take a screenshot of your map and save it to the Vacation_Itinerary folder as WeatherPy_travel_map_markers.png.


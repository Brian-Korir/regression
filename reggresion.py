import matplotlib.pyplot as plt
# Define hypothetical set of independent variables
hypothetical_data = {
    'Road conditions': 'wet',
    'Weather conditions': 'rainy',
    'Time of day': 'morning',
    'Type of road': 'city street',
    'Speed limit': 50,
    'Presence of traffic signals': True,
    'Presence of pedestrians': True,
    'Presence of cyclists': False,
    'Presence of heavy vehicles': True
}
# Separate independent variables and their values
variables = list(hypothetical_data.keys())
values = list(hypothetical_data.values())
plt.figure(figsize=(10, 6))
plt.barh(variables, values, color='lightblue')
plt.xlabel('Value')
plt.ylabel('Independent Variables')
plt.title('Hypothetical Set of Independent Variables')
plt.show()
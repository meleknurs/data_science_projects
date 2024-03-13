import matplotlib.pyplot as plt
import pandas as pd

seattle_weather= pd.read_csv("seattle_weather.csv")
austin_weather= pd.read_csv("austin_weather.csv")

# Use the "ggplot" style and create new Figure/Axes
fig, ax = plt.subplots()

plt.style.use("ggplot")

ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"])
plt.show()

# Use the "Solarize_Light2" style and create new Figure/Axes
fig,ax=plt.subplots()
plt.style.use('Solarize_Light2')
ax.plot(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"])
plt.show()
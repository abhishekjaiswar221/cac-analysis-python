import pandas as pd
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go

# Parameters are the variables passed to the function or method during function declaration or method declaration.
# It is also known as formal arguments.
# Arguments are the values passed to the function or method during
# function calling statement or method calling statement.
# It is also known as actual arguments.

data = pd.read_csv("./customer_acquisition_cost_dataset.csv")
# print(data.head())
# print(data.info())

data['CAC'] = data['Marketing_Spend'] / data['New_Customers']
# print(data['CAC'])

fig1 = px.bar(data, x='Marketing_Channel', y='CAC', title='CAC by Marketing Channel')
# fig1.show()

# Error:
fig2 = px.scatter(data, x='New_Customers', y='CAC', color='Marketing_Channel', title='New Customers vs. CAC', trendline='lowess')
# fig2.show()

summary_stats = data.groupby('Marketing_Channel')['CAC'].describe()
# print(summary_stats)

data['Conversion_Rate'] = data['New_Customers'] / data['Marketing_Spend'] * 100

# Conversion Rates by Marketing Channel
fig3 = px.bar(data, x='Marketing_Channel',
              y='Conversion_Rate',
              title='Conversion Rates by Marketing Channel')
# fig3.show()

# Error's:
fig4 = go.Figure()
# Actual Customers Acquired
fig4.add_trace(go.Bar(x=data['Marketing_Channel'], y=data['New_Customers'],
                      name='Actual Customers Acquired', marker_color='royalblue'))

# Break-Even Customers
fig4.add_trace(go.Bar(x=data['Marketing_Channel'], y=data['Break_Even_Customers'],
                      name='Break-Even Customers', marker_color='lightcoral'))

# Update the layout
fig4.update_layout(barmode='group', title='Actual vs. Break-Even Customers by Marketing Channel',
                   xaxis_title='Marketing Channel', yaxis_title='Number of Customers')

# Show the chart
fig4.show()

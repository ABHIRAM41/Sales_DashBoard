import pandas as pd
import plotly.express as px
import streamlit as st 

# PANDAS DATABASE CREATION
st.set_page_config(
  page_title="Sales Dashboard",
  page_icon=":bar_chart:",
  layout="wide"                 
)

@st.cache
def get_data_from_excel():
    df= pd.read_excel(
      io='sales_data_sample.xlsx',
      engine='openpyxl',
      sheet_name='Worksheet',
      skiprows=0,
      usecols='A:Y',
      
    )
    # Add 'hour' column to dataframe for second barchart
    df["Orders"]=df["ORDERNUMBER"]%4 +1 
    return df

df=get_data_from_excel()
 
# SIDEBAR
st.sidebar.header("Please Filter Here:")

Order= st.sidebar.multiselect(
  "Select the Orders:",
  options=df["Orders"].unique(),
  default=df["Orders"].unique()
)

Status_type= st.sidebar.multiselect(
  "Select the STATUS Type:",
  options=df["STATUS"].unique(),
  default=df["STATUS"].unique()
)

dealSize= st.sidebar.multiselect(
  "Select the DEALSIZE:",
  options=df["DEALSIZE"].unique(),
  default=df["DEALSIZE"].unique()
)

month= st.sidebar.multiselect(
  "Select the Month:",
  options=df["MONTH_ID"].unique(),
  default=df["MONTH_ID"].unique()
)

quarter= st.sidebar.multiselect(
  "Select the Quarter:",
  options=df["QTR_ID"].unique(),
  default=df["QTR_ID"].unique()
)

st.sidebar.subheader("Please Filter Here for months section:")

jan= st.sidebar.multiselect(
  "Select the Jauuary:",
  options=df["MONTH_ID"].unique(),
  default=1
)

feb= st.sidebar.multiselect(
  "Select the February:",
  options=df["MONTH_ID"].unique(),
  default=2
)

mar= st.sidebar.multiselect(
  "Select the March:",
  options=df["MONTH_ID"].unique(),
  default=3
)

apr= st.sidebar.multiselect(
  "Select the April:",
  options=df["MONTH_ID"].unique(),
  default=4
)

may= st.sidebar.multiselect(
  "Select the May:",
  options=df["MONTH_ID"].unique(),
  default=5
)

june= st.sidebar.multiselect(
  "Select the June:",
  options=df["MONTH_ID"].unique(),
  default=6
)

july= st.sidebar.multiselect(
  "Select the July:",
  options=df["MONTH_ID"].unique(),
  default=7
)

aug= st.sidebar.multiselect(
  "Select the August:",
  options=df["MONTH_ID"].unique(),
  default=8
)

sep= st.sidebar.multiselect(
  "Select the September:",
  options=df["MONTH_ID"].unique(),
  default=9
)

oct= st.sidebar.multiselect(
  "Select the October:",
  options=df["MONTH_ID"].unique(),
  default=10
)

nov= st.sidebar.multiselect(
  "Select the November:",
  options=df["MONTH_ID"].unique(),
  default=11
)

dec= st.sidebar.multiselect(
  "Select the Decenber:",
  options=df["MONTH_ID"].unique(),
  default=12
)

st.sidebar.subheader("Please Filter Here for Quarterly section:")

q1= st.sidebar.multiselect(
  "Select the Quarter: 1",
  options=df["QTR_ID"].unique(),
  default=1
)
q2= st.sidebar.multiselect(
  "Select the Quarter: 2",
  options=df["QTR_ID"].unique(),
  default=2
)
q3= st.sidebar.multiselect(
  "Select the Quarter: 3",
  options=df["QTR_ID"].unique(),
  default=3
)
q4= st.sidebar.multiselect(
  "Select the Quarter: 4",
  options=df["QTR_ID"].unique(),
  default=4
)

df_selection=df.query(
  "Orders== @Order  & MONTH_ID== @month & STATUS == @Status_type & QTR_ID== @quarter & DEALSIZE==@dealSize"
)

#months

df_selection_jan=df.query(
  "Orders== @Order  & MONTH_ID== @jan & STATUS == @Status_type & DEALSIZE==@dealSize"
)

df_selection_feb=df.query(
  "Orders== @Order  & MONTH_ID== @feb & STATUS == @Status_type & DEALSIZE==@dealSize"
)

df_selection_mar=df.query(
  "Orders== @Order  & MONTH_ID== @mar & STATUS == @Status_type & DEALSIZE==@dealSize"
)

df_selection_apr=df.query(
  "Orders== @Order  & MONTH_ID== @apr & STATUS == @Status_type & DEALSIZE==@dealSize"
)

df_selection_may=df.query(
  "Orders== @Order  & MONTH_ID== @may & STATUS == @Status_type & DEALSIZE==@dealSize"
)

df_selection_june=df.query(
  "Orders== @Order  & MONTH_ID== @june & STATUS == @Status_type & DEALSIZE==@dealSize"
)

df_selection_july=df.query(
  "Orders== @Order  & MONTH_ID== @july & STATUS == @Status_type & DEALSIZE==@dealSize"
)

df_selection_aug=df.query(
  "Orders== @Order  & MONTH_ID== @aug & STATUS == @Status_type & DEALSIZE==@dealSize"
)

df_selection_sep=df.query(
  "Orders== @Order  & MONTH_ID== @sep & STATUS == @Status_type & DEALSIZE==@dealSize"
)

df_selection_oct=df.query(
  "Orders== @Order  & MONTH_ID== @oct & STATUS == @Status_type & DEALSIZE==@dealSize"
)

df_selection_nov=df.query(
  "Orders== @Order  & MONTH_ID== @nov & STATUS == @Status_type & DEALSIZE==@dealSize"
)

df_selection_dec=df.query(
  "Orders== @Order  & MONTH_ID== @dec & STATUS == @Status_type & DEALSIZE==@dealSize"
)

#Quater

df_selection_q1=df.query(
  "Orders== @Order  & STATUS == @Status_type & QTR_ID== @q1 & DEALSIZE==@dealSize"
)
df_selection_q2=df.query(
  "Orders== @Order  & STATUS == @Status_type & QTR_ID== @q2 & DEALSIZE==@dealSize"
)
df_selection_q3=df.query(
  "Orders== @Order  & STATUS == @Status_type & QTR_ID== @q3 & DEALSIZE==@dealSize"
)
df_selection_q4=df.query(
  "Orders== @Order  & STATUS == @Status_type & QTR_ID== @q4 & DEALSIZE==@dealSize"
)

# MAINPAGE
st.title(":bar_chart: Sales Dashboard")
st.markdown("##")



# TOP KPI's
total_sales= int(df_selection["SALES"].sum())
# average_rating =round(df_selection["Rating"].mean(),1)
# star_rating=":star:" * int(round(average_rating,0))
average_sale_by_transaction=round(df_selection["SALES"].mean(),2)


# KPI's COLUMNS
left_column,right_column=st.columns(2)

# middle_column

with left_column:
  st.subheader("Total Sales:")
  st.subheader(f"US $ {total_sales:,}")
# with middle_column:
#   st.subheader("Average Rating:")
#   st.subheader(f"{average_rating} {star_rating}")
with right_column:
  st.subheader("Average Sales Per Transaction:")
  st.subheader(f"US $ {average_sale_by_transaction}")

st.markdown("---")







# BARCHARTS

# SALES BY PRODUCT LINE [BAR CHART]

sales_by_product_line=(
  df_selection.groupby(by=["PRODUCTLINE"]).sum()[["SALES"]].sort_values(by="SALES")
)

fig_product_sales = px.bar(
    sales_by_product_line,
    x="SALES",
    y=sales_by_product_line.index,
    orientation="h",
    title="<b>Sales by Product Line</b>",
    color_discrete_sequence=["#205295"] * len(sales_by_product_line),
    template="plotly_white",
)

fig_product_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)


# SALES BY Order [BAR CHART]

sales_by_order=df_selection.groupby(by=["Orders"]).sum()[["SALES"]]

fig_hourly_sales=px.bar(
    sales_by_order,
    x=sales_by_order.index,
    y="SALES",
    title="<b>Sales by Orders</b>",
    color_discrete_sequence=["#205295"] * len(sales_by_order),
    template="plotly_white",
)

fig_hourly_sales.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)


# Displaying charts
left_column,right_column=st.columns(2)
left_column.plotly_chart(fig_product_sales,use_container_width=True)
right_column.plotly_chart(fig_hourly_sales,use_container_width=True)


# SALES BY months [BAR CHART]

st.subheader("Monthly Total Sales:")

#jan
sales_by_order=df_selection_jan.groupby(by=["Orders"]).sum()[["SALES"]]

fig_order_sales_jan=px.bar(
    sales_by_order,
    x=sales_by_order.index,
    y="SALES",
    title="<b>January: Sales by Orders</b>",
    color_discrete_sequence=["#205295"] * len(sales_by_order),
    template="plotly_white",
)

fig_order_sales_jan.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)

#feb
sales_by_order=df_selection_feb.groupby(by=["Orders"]).sum()[["SALES"]]

fig_order_sales_feb=px.bar(
    sales_by_order,
    x=sales_by_order.index,
    y="SALES",
    title="<b>February: Sales by Orders</b>",
    color_discrete_sequence=["#205295"] * len(sales_by_order),
    template="plotly_white",
)

fig_order_sales_feb.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)

#mar
sales_by_order=df_selection_mar.groupby(by=["Orders"]).sum()[["SALES"]]

fig_order_sales_mar=px.bar(
    sales_by_order,
    x=sales_by_order.index,
    y="SALES",
    title="<b>March: Sales by Orders</b>",
    color_discrete_sequence=["#205295"] * len(sales_by_order),
    template="plotly_white",
)

fig_order_sales_mar.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)



# Displaying charts
left_column,middle_column,right_column=st.columns(3)
left_column.plotly_chart(fig_order_sales_jan,use_container_width=True)
middle_column.plotly_chart(fig_order_sales_feb,use_container_width=True)
right_column.plotly_chart(fig_order_sales_mar,use_container_width=True)

#apr
sales_by_order=df_selection_apr.groupby(by=["Orders"]).sum()[["SALES"]]

fig_order_sales_apr=px.bar(
    sales_by_order,
    x=sales_by_order.index,
    y="SALES",
    title="<b>April: Sales by Orders</b>",
    color_discrete_sequence=["#205295"] * len(sales_by_order),
    template="plotly_white",
)

fig_order_sales_apr.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)

#may
sales_by_order=df_selection_may.groupby(by=["Orders"]).sum()[["SALES"]]

fig_order_sales_may=px.bar(
    sales_by_order,
    x=sales_by_order.index,
    y="SALES",
    title="<b>May: Sales by Orders</b>",
    color_discrete_sequence=["#205295"] * len(sales_by_order),
    template="plotly_white",
)

fig_order_sales_may.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)

#june
sales_by_order=df_selection_june.groupby(by=["Orders"]).sum()[["SALES"]]

fig_order_sales_june=px.bar(
    sales_by_order,
    x=sales_by_order.index,
    y="SALES",
    title="<b>June: Sales by Orders</b>",
    color_discrete_sequence=["#205295"] * len(sales_by_order),
    template="plotly_white",
)

fig_order_sales_june.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)



# Displaying charts
left_column,middle_column,right_column=st.columns(3)
left_column.plotly_chart(fig_order_sales_apr,use_container_width=True)
middle_column.plotly_chart(fig_order_sales_may,use_container_width=True)
right_column.plotly_chart(fig_order_sales_june,use_container_width=True)

#july
sales_by_order=df_selection_july.groupby(by=["Orders"]).sum()[["SALES"]]

fig_order_sales_july=px.bar(
    sales_by_order,
    x=sales_by_order.index,
    y="SALES",
    title="<b>July: Sales by Orders</b>",
    color_discrete_sequence=["#205295"] * len(sales_by_order),
    template="plotly_white",
)

fig_order_sales_july.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)

#aug
sales_by_order=df_selection_aug.groupby(by=["Orders"]).sum()[["SALES"]]

fig_order_sales_aug=px.bar(
    sales_by_order,
    x=sales_by_order.index,
    y="SALES",
    title="<b>August: Sales by Orders</b>",
    color_discrete_sequence=["#205295"] * len(sales_by_order),
    template="plotly_white",
)

fig_order_sales_aug.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)

#sep
sales_by_order=df_selection_sep.groupby(by=["Orders"]).sum()[["SALES"]]

fig_order_sales_sep=px.bar(
    sales_by_order,
    x=sales_by_order.index,
    y="SALES",
    title="<b>September: Sales by Orders</b>",
    color_discrete_sequence=["#205295"] * len(sales_by_order),
    template="plotly_white",
)

fig_order_sales_sep.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)



# Displaying charts
left_column,middle_column,right_column=st.columns(3)
left_column.plotly_chart(fig_order_sales_july,use_container_width=True)
middle_column.plotly_chart(fig_order_sales_aug,use_container_width=True)
right_column.plotly_chart(fig_order_sales_sep,use_container_width=True)

#oct
sales_by_order=df_selection_oct.groupby(by=["Orders"]).sum()[["SALES"]]

fig_order_sales_oct=px.bar(
    sales_by_order,
    x=sales_by_order.index,
    y="SALES",
    title="<b>October: Sales by Orders</b>",
    color_discrete_sequence=["#205295"] * len(sales_by_order),
    template="plotly_white",
)

fig_order_sales_oct.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)

#nov
sales_by_order=df_selection_nov.groupby(by=["Orders"]).sum()[["SALES"]]

fig_order_sales_nov=px.bar(
    sales_by_order,
    x=sales_by_order.index,
    y="SALES",
    title="<b>November: Sales by Orders</b>",
    color_discrete_sequence=["#205295"] * len(sales_by_order),
    template="plotly_white",
)

fig_order_sales_nov.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)

#dec
sales_by_order=df_selection_dec.groupby(by=["Orders"]).sum()[["SALES"]]

fig_order_sales_dec=px.bar(
    sales_by_order,
    x=sales_by_order.index,
    y="SALES",
    title="<b>December: Sales by Orders</b>",
    color_discrete_sequence=["#205295"] * len(sales_by_order),
    template="plotly_white",
)

fig_order_sales_dec.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)



# Displaying charts
left_column,middle_column,right_column=st.columns(3)
left_column.plotly_chart(fig_order_sales_oct,use_container_width=True)
middle_column.plotly_chart(fig_order_sales_nov,use_container_width=True)
right_column.plotly_chart(fig_order_sales_dec,use_container_width=True)

#Quater

st.subheader("Quarterly Total Sales:")
#q1
sales_by_order=df_selection_q1.groupby(by=["Orders"]).sum()[["SALES"]]

fig_order_sales_q1=px.bar(
    sales_by_order,
    x=sales_by_order.index,
    y="SALES",
    title="<b>Quater 1: Sales by Orders</b>",
    color_discrete_sequence=["#205295"] * len(sales_by_order),
    template="plotly_white",
)

fig_order_sales_q1.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)

#q2
sales_by_order=df_selection_q2.groupby(by=["Orders"]).sum()[["SALES"]]

fig_order_sales_q2=px.bar(
    sales_by_order,
    x=sales_by_order.index,
    y="SALES",
    title="<b>Quater 2: Sales by Orders</b>",
    color_discrete_sequence=["#205295"] * len(sales_by_order),
    template="plotly_white",
)

fig_order_sales_q2.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)



# Displaying charts
left_column,right_column=st.columns(2)
left_column.plotly_chart(fig_order_sales_q1,use_container_width=True)
right_column.plotly_chart(fig_order_sales_q2,use_container_width=True)

#q3
sales_by_order=df_selection_q3.groupby(by=["Orders"]).sum()[["SALES"]]

fig_order_sales_q3=px.bar(
    sales_by_order,
    x=sales_by_order.index,
    y="SALES",
    title="<b>Quater 3: Sales by Orders</b>",
    color_discrete_sequence=["#205295"] * len(sales_by_order),
    template="plotly_white",
)

fig_order_sales_q3.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)

#q4
sales_by_order=df_selection_q4.groupby(by=["Orders"]).sum()[["SALES"]]

fig_order_sales_q4=px.bar(
    sales_by_order,
    x=sales_by_order.index,
    y="SALES",
    title="<b>Quater 4: Sales by Orders</b>",
    color_discrete_sequence=["#205295"] * len(sales_by_order),
    template="plotly_white",
)

fig_order_sales_q4.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)



# Displaying charts
left_column,right_column=st.columns(2)
left_column.plotly_chart(fig_order_sales_q3,use_container_width=True)
right_column.plotly_chart(fig_order_sales_q4,use_container_width=True)




# HIDE STREAMLIT STYLE
hide_st_style="""
            <style>
            #MainMenu {visibility:hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """

st.markdown(hide_st_style, unsafe_allow_html=True)


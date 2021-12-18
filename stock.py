from datetime import date
from typing import  DefaultDict, List
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import openpyxl
from streamlit.type_util import OptionSequence
from annotated_text import annotated_text

st.set_page_config(page_title='S&P 500(2014-2017)', page_icon='S&P.jpg')


sidebar=st.sidebar
st.markdown("<h1 style='text-align: center'><u>'S&P 500 Index Stock Prices and Charts'</u></h1>", unsafe_allow_html=True)


annotated_text( 
                ('YEAR', '', '#faa'),
                (' : '),
                ('2014','','#8ef'),
                (' - '),
                ('2017','', '#8ef'),
)

sidebar.image("https://media.giphy.com/media/WodUmk8kNCAu2kdWwu/giphy.gif", width=200)
#----------------------------------------------------------------------------------------------------

st.markdown('   ')
st.markdown('   ')
st.markdown('   ')

col1, col2, col3, col4, col5=st.columns(5)
col3.markdown("<p>'This project is about the Analysis of shares of S&P 500 and it\'s Companies from the year 2014-2017.'</p> <b>-Aryan Verma</b>", unsafe_allow_html=True)
col2.image('th.jpg',use_column_width=True)
col4.image('SP-500-Companies-List.png',use_column_width=True)
#--------------------------------------------------------------------------------
sidebar.markdown('---')  



st.markdown('---')
option = st.radio("Select:", ('Overview','Insight'))


with st.spinner('| Just a sec |'):


    if option == 'Overview':
        st.markdown("<h2 style='text-align: center'><u>'Overview'</u></h2>", unsafe_allow_html=True)
        df= pd.read_excel('S&P.xlsx')
        st.dataframe(df)

        st.markdown('---')
        
        fig= go.Figure(data=[go.Candlestick(x=df['Date'],open=df['Open'],high=df['High'],low=df['Low'],close=df['Close*'],increasing_line_color = 'cyan', decreasing_line_color='yellow')])
        fig.update_layout(xaxis_rangeslider_visible=False, template= 'plotly_dark',width =1100,  height=650)
        fig.update_layout(title='Candlestick Chart', yaxis_title='Stock Price',xaxis_title='Date')
        st.plotly_chart(fig)

        st.plotly_chart(px.bar(df, x='Date', y='Volume',template='plotly_dark',width =1100,  height=650 , title='Volume Of Shares traded every month'))
        
#-----------------------------------------------------------------------------------------------------------------------
        df.index= pd.to_datetime(df.index)
        df.reset_index(inplace=True)
        df['day'] = df['Date'].dt.day
        df['month'] = df['Date'].dt.month
        df['year'] = df['Date'].dt.year
        st.plotly_chart(px.pie(  df, names='year', values='Volume' , template='plotly_dark',width =1100,  height=650 , color_discrete_sequence=px.colors.sequential.dense_r , title='Volume Of Shares traded each Year'))
        st.markdown('---')
        
    #------------------------------------------------------------
        option1= sidebar.selectbox('About', ('"You should know!"','what is S&P 500 Companies?','History of S&P 500', 'How does the company enter the S&P 500?'))  
    
        if option1 =='what is S&P 500 Companies?':
            sidebar.write('The Standard and Poor\'s 500, or simply the S&P 500, is a stock market index tracking the performance of 500 large companies listed on stock exchanges in the United States.')

        elif option1 == 'History of S&P 500':
            sidebar.write('* In 1860, Henry Varnum Poor formed Poor\'s Publishing, which published an investor\'s guide to the railroad industry.') 
            sidebar.write('* In 1923, Standard Statistics Company (founded in 1906 as the Standard Statistics Bureau) began rating mortgage bonds and developed its first stock market index consisting of the stocks of 233 U.S. companies, computed weekly.')
            sidebar.write('* In 1926, it developed a 90-stock index, computed daily.')
            sidebar.write('* In 1941, Poor\'s Publishing merged with Standard Statistics Company to form Standard & Poor\'s.On Monday, March 4, 1957, the index was expanded to its current 500 companies and was renamed the S&P 500 Stock Composite Index.')


        elif option1 =='How does the company enter the S&P 500?':
            sidebar.write('* Market capitalization must be greater than or equal to US$13.1 billion according to 2021 guidelines.')
            sidebar.write('* Annual dollar value traded to float-adjusted market capitalization is greater than 1.0')
            sidebar.write('* Minimum monthly trading volume of 250,000 shares in each of the six months leading up to the evaluation date')
            sidebar.write('* Must be publicly listed on either the New York Stock Exchange (including NYSE Arca or NYSE American) or NASDAQ (NASDAQ Global Select Market, NASDAQ Select Market or the NASDAQ Capital Market).')
            sidebar.write('*  The company should be from the U.S')

        sidebar.markdown('---')   


        option3=sidebar.selectbox('S&P 500 Report',('"Select the Year"','2014','2015','2016','2017'))

        if option3=='2014':
            sidebar.write('* In 2014, the percentage of S&P 500 sales from foreign countries increased after five years of stagnation. The overall rate for 2014 was 47.82%, up from 46.29% in 2013 and the 46% rate from each of the prior four years (2009-2012).')
            sidebar.write('* European sales rebounded in 2014, accounting for 7.46% of all S&P 500 sales, up from the prior year’s 6.80%, which had declined from 2012’s 9.69% rate. Sales in the U.K. declined for the fourth year in a row to 0.89% from 1.12% in 2013, 1.73% in 2012, and 2.39% in 2011 European ex-U.K. sales represented 6.58% of all S&P 500 sales in 2014, increasing from 5.69% in 2013, but still down from the 7.97% level posted in 2012. ')
            sidebar.write('* Asian sales continued to increase, but at a slow pace; 7.80% of S&P 500 sales came from Asia, up from 7.71% in 2013 and 7.46% in 2012. Canadian sales increased to 3.51%, from the prior year’s 2.23% rate, but they were still short of the 4.10% rate in 2012. ')
            sidebar.write('* African declared sales increased to 4.09% from the 3.55% calculated for 2013 and 2012. ')
            sidebar.write('* Information technology continued to be the most successful (and exposed) sector in terms of foreign sales. In 2014, 59.4% of its declared sales were foreign, up from 56.6% in 2013. The sector’s representation rebounded to be 18.3% of all foreign sales, up from 2013’s 14.8% but still shy of the 2011 19.0% rate.') 
            sidebar.write('* In 2014, S&P 500 companies continued to send more payments to Washington for income taxes than they did to foreign governments, as the percentage going to the U.S. jumped to 61.8% of declared amounts, up from 54.9% in 2013 and 51.2% in 2012, with 38.2% of taxes being sent to foreign governments in 2014, down from 45.1% in 2013 and 48.8% in 2012. Actual payments to Washington increased 17.4% in 2014 to USD 185.2 billion from 2013’s USD 157.7 billion, as payments abroad declined 11.8% to USD 114.2 billion from USD 129.5 billion. ')
            sidebar.write('* The quantifiable data released with respect to foreign sales by issues for 2014 slightly improved, after a noticeable deterioration in 2013. Still, over half of S&P 500 issues did not report sufficient information to facilitate producing a complete report on global sales. Of the issues that did declare foreign sales, 46.4% of them used a term similar to “foreign country,” giving little breakdown of the area or country of the sales.')
            sidebar.write('* Given the ongoing debate and discussion of corporate domestic and foreign tax rates and policy, as well as inversions, the reduced level of specific data continues to be disappointing.  ')
        elif option3=='2015':
            sidebar.write('* In 2015, the percentage of S&P 500 sales from foreign countriesdecreased, compared with 2014 when they ticked up after five yearsof stagnation. The overall rate for 2015 was 44.3%, down from 47.8%in 2014 and up from the rate of 46% seen in each of the prior fiveyears (2009-2013). S&P 500 foreign sales represent products andservices produced and sold outside of the U.S.')
            sidebar.write('* European sales continued to increase in 2015, with Europe becomingthe dominant region and accounting for 7.79% of all S&P 500 sales,up from the prior year’s 7.46%, which was up from 2013’s 6.80% rate.After declining four years in a row, sales in the U.K. increased to 1.86% from 0.89% in 2014, 1.12% in 2013, 1.73% in 2012, and 2.39% in 2011.')
            sidebar.write('* Asian sales reversed their course and decreased, representing 6.77%of S&P 500 sales, down from 7.80% in 2014 and 7.71% in 2013.Canadian sales decreased to 1.17% from the prior year’s rate of3.51%, as declines were seen in oil and commodity prices, and demand for related services and equipment fell.')
            sidebar.write('* African declared sales decreased to 3.16% from the 4.09% calculated for 2014 and 3.55% for 2013.')
            sidebar.write('* Energy took the title of leader in exposure to foreign sales, as its domestic sales fell. The sector reported 57.88% of its sales as foreign, up from 2014’s 56.23%. Information technology’s exposure declined to 57.78% (a tick below energy’s) from its rate of 59.39% in2014. In terms of its sector-level representation of total sales,however, information technology represented 21.93% of all foreign sales, up from 18.34% in 2014, as energy represented 15.46%, down from 21.54% in 2014.')
            sidebar.write('* In 2015, S&P 500 companies continued to send more payments to Washington for income taxes than they did to foreign governments, as the percentage going to the U.S. again jumped, this time to 66.8% of declared amounts from 61.8% in 2014, 54.9% in 2013, and 51.2% in 2012. Meanwhile, 33.2% of taxes were sent to foreign governments in 2015, down from 38.2% in 2014, 45.1% in 2013, and 48.8% in 2012. Actual payments to Washington decreased 0.4% in 2015 to USD 184.4 billion, down from 2014’s USD 185.2 billion. Payments abroad again declined at a double-digit rate, down 19.9% to USD 91.4 billion from 2014’s 114.2 billion (and down 11.8% to USD 114.2 billion for 2013). ')
            sidebar.write('* In 2015, the quantifiable data released with respect to foreign sales by issues slightly improved again after a noticeable deterioration in 2013. Just over one-half of S&P 500 issues (255) reported sufficient information to facilitate producing a complete report on global sales for 2015. Of the issues that did declare foreign sales, 49.2% of them used a term similar to “foreign country,” giving little breakdown of the area or country of the sales country,” giving little breakdown of the area or country of the sales ')
            sidebar.write('* Given the ongoing debate and discussion of corporate domestic and foreign tax rates and policies, as well as inversions, the level of specific data disclosed by companies continues to be disappointing. ')
        elif option3=='2016':
            sidebar.write('')
        elif option3=='2017':
            sidebar.write('* In 2017, the percentage of S&P 500 sales from foreign countries increased slightly, after two years of measured decreases. The overall rate for 2017 was 43.6%, up from 43.2% in 2016, but down from 44.3% in 2015 and 47.8% in 2014, which was at least an 11-year record high. S&P 500 foreign sales represent products and services produced and sold outside of the U.S.')
            sidebar.write('* Sales in Asia declined, but they remained the highest of any region. Asia accounted for 8.26% of all S&P 500 sales, down from 8.46% in 2016, but up from 2015’s 6.77% and 2014’s 7.80%.')
            sidebar.write('* European sales ticked up for 2017, but they remained lower than Asia. For 2017, European sales increased to 8.14% of all sales, up from 8.13% in 2016, 7.79% in 2015 and 7.46% in 2014. The UK (which is part of European sales) increased to 1.12% from 2016’s 1.10%, after 2015’s increase to 1.86%.')
            sidebar.write('* Japanese sales decreased to 1.51% of all S&P 500 sales from 1.52% in 2016, and African sales inched down to 3.90% from 3.97% in 2017. Sales in Canada declined to 2.16% from 2.67% in 2016, after declining significantly to 1.17% in 2015 from 3.51% in 2014 (oilrelated sales were seen as a contributing factor).')
            sidebar.write('* Information technology had the most foreign exposure of any sector, even though it declined to 56.95% from 2016’s 57.15%. Energy, which was last year’s lead sector, declined to 54.06% from 58.88% in 2016.')
            sidebar.write('* Given the ongoing debate and legislative actions on sales, tariffs, and jobs, the level of specific data disclosed by companies continues to be disappointing.')

        sidebar.markdown('---')  
        

#------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    elif option == 'Insight':
        st.markdown("<h2 style='text-align: center'><u>'Insight'</u></h2>", unsafe_allow_html=True)
        df= pd.read_csv('stock prices.csv')
        df.rename(columns={'symbol':'Company', 'date': 'Date', 'open':'Open', 'high': 'High', 'low':'Low', 'close':'Close', 'volume':'Volume'},inplace=True) 
        
        company= sidebar.multiselect("Select the Company:",options=df["Company"].unique(), default=['AMZN','GOOGL'])
        
        df_selection = df.query(
        "Company== @company")
        
        st.dataframe(df_selection) 
        st.text('*Each record represents a single day of trading') 

        sidebar.write("<small>Recommendation: Try comparing different Companies for better understanding</small>",unsafe_allow_html=True)
        st.markdown('---')
        st.subheader(company)
        
        col1, col2=st.columns(2)
        col1.plotly_chart(px.line(df_selection, x='Date', y='Open',color = 'Company',template='plotly_dark',width =650,  height=650 , title='Opening Stock Price'))
        col2.plotly_chart(px.line(df_selection, x='Date', y='Close',color='Company',template='plotly_dark',width =650,  height=650,title='Closing Stock Price'))
        col1.plotly_chart(px.line(df_selection,x='Date', y='High',color = 'Company',template='plotly_dark',width =650,  height=650,title='Highest Stock Price'))
        col2.plotly_chart(px.line(df_selection,x='Date', y='Low',color = 'Company',template='plotly_dark',width =650,  height=650,title='Lowest Stock Price'))
        st.plotly_chart(px.line(df_selection,x='Date', y='Volume',color = 'Company',template='plotly_dark',width =1100,  height=650,title='Volume of Stock traded'))      
        

        st.markdown('---')
        sidebar.markdown('---')
        
        company2= sidebar.multiselect("Select the Company:(for candlestick chart)", options=df['Company'].unique(), default= 'AAPL' )
        df_selection1= df.query(
        "Company==@company2" )
        st.subheader(company2)

        sidebar.write("<small>Recommendation: Try one company a time.</small>",unsafe_allow_html=True)

        fig= go.Figure(data=[go.Candlestick(x=df_selection1['Date'],open=df_selection1['Open'],high=df_selection1['High'],low=df_selection1['Low'],close=df_selection1['Close'],increasing_line_color = 'cyan', decreasing_line_color='yellow')])
        fig.update_layout(xaxis_rangeslider_visible=False, template= 'plotly_dark',width =1100,  height=650)
        fig.update_layout(title='Candlestick Chart', yaxis_title='Stock Price',xaxis_title='Date')
        st.plotly_chart(fig)

        st.markdown('---')
        sidebar.markdown('---')  
#--------------------------------------------------------------------------------------------------------------------------------------------        
 #----------------------------------------------------------------------------------------------------


               

                

                
    
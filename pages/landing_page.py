import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import streamlit as st
import streamlit.components.v1 as components
from streamlit_timeline import timeline
from widgets import navbar,sankey_work_experience
class Landingpage:
  def run(self):

    #st.markdown("<h1 style='text-align: left; color: black;'>Gouri Benni</h1>", unsafe_allow_html=True)
    with st.sidebar:
       submit_button = st.button(label="*Download Resume*")
    '''
    left_co, cent_co,last_co = st.columns(3)
    with left_co:
        st.markdown("![Alt Text](https://media.giphy.com/media/CVtNe84hhYF9u/giphy.gif)")
        st.write("")
    
    '''
    # Profile Picture
    left_co, right_co = st.columns([1.2, 1.2])
    with right_co:
          st.image("https://github.com/gouribenni/portfolio_gouribenni/blob/main/assets/images/Gouri.png?raw=true",width=300)

    
    with left_co:
      #st.write("# Hi, I'm Gouri! 👋 ")
      st.markdown("""
      <style>
          h1, p{
          text-align: left;
          margin-top: 0;
          margin-bottom: 0;
          padding-top: 50px;
          padding-bottom: 0;}
      </style>
      <h1> Hi, I'm Gouri! 👋 </h1>
      <p><i> I am dedicated to harnessing the transformative power of Data Science, striving to become a catalyst for data-driven innovation that empowers businesses to navigate the complexities of the digital age and carve out new frontiers in their industries.</i></p>
       """, unsafe_allow_html=True)
      
      

    
    # Brief Introduction
    st.markdown("""
        <style>
            .about-container {
                color: #4f4f4f; /* Adjust the color as needed */
                text-align:left;
            }
            .about-header {
                color: #2874A6; /* Header color */
            }
            .highlight {
                color: #2E86C1; /* Highlights or key points */
            }
            .career-highlight {
                color: #21618C; /* Career highlights color */
                font-weight: bold;
            }
            .about-container h2, .about-container h3 {
            margin-top: 0;
            margin-bottom: 0;
            text-align: left;
            }
            /* Ensure that there is no extra space inherited from global styles */
            .about-container * {
            margin-top: 0;
            margin-bottom: 0;
            padding-top: 0;
            padding-bottom: 0;
            }
        </style>
        <div class="about-container">
        <hr>
        <p>I weave the art of innovation with the precision of data science, transforming the complex tapestry of data into actionable insights. I am a fervent explorer in the realm of data science, currently enriching my knowledge at San Jose State University's master's program. At the heart of my journey lies a pivotal role at Norfolk Southern, where I have pioneered data and strategic solutions. My adventure at ADP and FluxGen have sharpened my acumen, showcasing my adaptability across diverse industries.</p>
        <p>My unwavering mission is to distill vast oceans of data into potent elixirs of business intelligence, fuelling the growth of enterprises in this data-driven era. I navigate the realms of AI, Product Analytics, and Strategic Planning with an alchemist's touch, melding them into transformative business strategies.</p>
        <hr>
        <hr>
        <h3 class="highlight">Education</h3>
        <h4>San Jose State University</h4>
        <p><strong>     Master of Science (M.S) in Data Analytics</strong> | GPA: 3.4 | Aug 2022 - May 2024</p>
        <h4>Gogte Institute of Technology</h4>
        <p><strong>     Bachelor of Engineering (B.E) in Computer Science Engineering</strong> | GPA: 3.5 | Jul 2016 - Aug 2020</p>
        <hr>
        <h3 class="highlight">Contact Information</h3>
        <ul>
            <li>🌐: <a href="https://msoneai.com" target="_blank">msoneai.com</a></li>
            <li>🔗: <a href="https://www.linkedin.com/in/gouri-benni/" target="_blank">linkedin.com/in/gouri-benni</a></li>
            <li>🐙: <a href="https://github.com/gouribenni" target="_blank">github.com/gouribenni</a></li>
            <li>✉️: <a href="mailto:gouri.benni@gmail.com">gouri.benni@gmail.com</a></li>
            <li>📞: <a href="tel:+14086904151">(408)-690-4151</a></li></li>
        </ul>
        </div>
        <hr>
    """, unsafe_allow_html=True)

         # Create columns where the first one is empty and acts like a left margin
    left_margin, chart_column = st.columns([1, 20])  # Adjust the ratio to control the offset
                                # Add a button to download the resume
    

     # Render the chart in the right column
    #with chart_column:
        #st.plotly_chart(sankey_work_experience.render_image())  

        #st.markdown("""<h2 style='text-align: left; color: black; padding-top: 0; padding-bottom: 0;'>Career Timeline</h2>""",unsafe_allow_html=True)

        
    # load data
    with open('data/example_time_line_nitin.json', "r") as f:
        data = f.read()

    #st.markdown("<h2 style='text-align: left; color: black;'>Career Timeline</h1>", unsafe_allow_html=True)
    '''
    st.markdown("""
        <style>
            h1 {text-align: left;
            margin-top: 0;
            margin-bottom: 0;
            padding-top: 0;
            padding-bottom: 0;}
        </style>
        <h1> Career Timeline </h1>
    """, unsafe_allow_html=True)
    '''
    timeline(data, height=800)






    

if __name__=='__main__':
  Landingpage().run()
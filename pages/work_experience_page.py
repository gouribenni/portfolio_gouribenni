import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import streamlit as st
import streamlit.components.v1 as components
from streamlit_timeline import timeline
import matplotlib.pyplot as plt
import json
from widgets import sankey_work_experience


class WorkExperiencePage:
  def run(self):
    work_experience = [
        {
            "role": "Data Analyst",
            "company": "Norfolk Southern Corp",
            "period": "May 2023 - August 2023",
            "location": "Georgia, USA",
            "details": """
                <ul>
                    <li>Conducted advanced statistical analysis and A/B testing using Excel and SQL to optimize NS train schedules. Identified key patterns and anomalies,leading to a 25%' reduction in train delays, enhancing operational efficiency and customer satisfaction.</li>
                    <li>Built the creation of feature stores and data assets for machine learning models by integrating an analytics platform with Delta Lake on AWS. This initiative streamlined algorithmic workflows and accelerated data preparation, substantially reducing time spent by data scientists on model readiness.</li>
                    <li>Created Tableau dashboards for real-time monitoring of NS train delays, focusing on departure, arrival times, and delay causes. Improved operational efficiency and reliability, leading to a 15%' increase in on-time train arrivals.</li>
                    <li>Applied NLP techniques for textual analysis of unstructured NS operational data. Used sentiment analysis, topic modeling, and NER to extract insights, contributing to a 10%' improvement in operational decision-making accuracy.</li>
                    <li>Utilized deep learning models, including LLM and transformers, for inspecting NS trains and improved anomaly detection accuracy by 30%, enhancing safety and maintenance efficiency.</li>
                    <li>Implemented XGBoost and ARIMA models for predictive maintenance of NS rail tracks. Reduced maintenance-related delays by 18%' and enhanced lifespan of rail infrastructure.</li>
                </ul>
            """,
            "icon": "https://github.com/gouribenni/portfolio_gouribenni/blob/main/assets/images/NS.png?raw=true",
            "url":"https://www.norfolksouthern.com/",
        },
        {
            "role": "Data Analyst",
            "company": "ADP Pvt Ltd",
            "period": "September 2020 - June 2021",
            "location": "Hyderabad, India",
            "details": """
                <ul>
                    <li>Developed SQL and Python-based data models in ADP Data-Cloud to address payroll issues like overtime miscalculations and tax discrepancies, enhancing processing accuracy by 25%' and cut payroll errors by 15%.</li>
                    <li>Built a Data Lake enhancing ADP Assist’s AI, boosting predictive analytics for employee turnover and compliance. Achieved 30%' faster data retrieval and 20%' better processing efficiency.</li>
                    <li>Created Python-based ETL pipelines enhancing real-time data integration for ADP Workforce Now. This improvement enabled more dynamic tracking of employee time and attendance, reducing data latency by 35% and ensuring timelier and more accurate payroll and HR reporting.</li>
                    <li>Implemented data models and Tableau reports in ADP Vantage HCM, improving HR decision-making by 40%. Provided insights for employee development and talent management strategies.</li>
                    <li>Upgraded ADP’s data warehouse, enhancing data scalability and query performance. Essential for complex reporting for multinational clients.</li>
                    <li>Applied clustering algorithms to segment ADP's client base in ADP Analytics, leading to more tailored payroll and HR services. This approach helped in identifying unique client patterns, increasing satisfaction by 20% and boosting retention by 15% through more personalized service offerings.</li>
                    <li>Streamlined project management using Jira for ADP implementation projects, aligning them with business goals by 30%. Continuously learned and applied emerging technologies in AI and ML, improving team productivity and innovation by 20%.</li>
                </ul>
            """,
            "icon": "https://github.com/gouribenni/portfolio_gouribenni/blob/main/assets/images/ADP.png?raw=true",  # Replace with the actual URL or path to your icon
            "url":"https://in.adp.com/",
        }
    ]



    import streamlit as st

    st.title('My Work Experience')

    # Custom CSS to adjust the layout
    st.markdown("""
        <style>
        .job-container {
            display: flex;
            flex-direction: column;
        }
        .job-title {
            font-size: 30px;
            font-weight: bold;
        }
        .job-company {
            font-size: 18px;
            display: flex;
            align-items: center;
        }
        .job-icon {
            width: 100px;  /* Adjust the size of the icon */
            margin-left: 10px; /* Space between the company name and the icon */
        }
        .job-period-location {
            font-size: 16px;
            margin-top: 4px;
            margin-bottom: 10px;
        }
        </style>
    """, unsafe_allow_html=True)


    # Display each job entry
    for job in work_experience:
        # Use the image as a clickable link in the HTML string
        st.markdown(f"""
            <div class="job-container">
                <div class="job-title">{job['role']}</div>
                <div class="job-company">
                    <a href="{job['url']}" target="_blank">{job['company']}</a> 
                    <a href="{job['url']}" target="_blank">
                        <img class="job-icon" src="{job['icon']}" alt="{job['company']} Icon">
                    </a>
                </div>
                <div class="job-period-location">{job['period']} - {job['location']}</div>
            </div>
        """, unsafe_allow_html=True)

        with st.expander("See details"):
            st.markdown(f"<div>{job['details']}</div>", unsafe_allow_html=True)
             # Create columns where the first one is empty and acts like a left margin
    left_margin, chart_column = st.columns([1, 20])  # Adjust the ratio to control the offset

     # Render the chart in the right column
    #with chart_column:
        #st.plotly_chart(sankey_work_experience.render_image())  


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
        <h3 class="highlight"> Skills Overview Definition</h3>
        <h4>Programming/Tools:</h4>
        <ul>
                <li><strong>Languages & Frameworks:</strong> Proficient in Python, C, C++, R.</li>
                <li><strong>Web Technologies & Systems:</strong> Experienced in HTML and CSS.</li>
                <li><strong>Advanced Data Handling:</strong> Skilled in Advanced Excel for complex data analysis and manipulation.</li>
        </ul>

        <h4>Data Acquisition, Mining & Transformation:</h4>
        <ul>
                <li><strong>Data Acquisition:</strong> Expertise in acquiring data from diverse sources using APIs and AWS S3.</li>
                <li><strong>Mining with NLP:</strong> Utilizing NLP for extracting valuable insights from textual data.</li>
                <li><strong>Data Infrastructure & Management:</strong> Building Data Lake infrastructure, creating ETL/ELT pipelines, data modeling, and managing data architecture.</li>
                <li><strong>SQL Expertise:</strong> Proficient in SQL optimization and performance tuning.</li>
                <li><strong>Data Warehousing & Reporting:</strong> Experienced in Snowflake, AWS RDS, Postgres, Neo4j, Oracle SQL, MySQL, MongoDB for comprehensive data warehousing and reporting.</li>
        </ul>

        <h4>Visualization:</h4>
        <ul>
            <li>Proficient in Tableau, Matplotlib, Seaborn for crafting compelling data stories.</li>
        </ul>

        <h4>Machine Learning:</h4>
        <ul>
                <li><strong>ML Theory & Application:</strong> Deep understanding of machine learning theory and its practical application.</li>
                <li><strong>Model Evaluation & Optimization:</strong> Evaluating and optimizing machine learning models for performance, accuracy, and consistency.</li>
                <li><strong>Techniques & Algorithms:</strong> Proficient in regression, time series analysis (ARIMA), clustering, decision trees, random forest, XGBoost, PCA, and using SKLearn.</li>
        </ul>

        <h4>Analytics:</h4>
                <li><strong>Product Analytics:</strong> Skilled in analyzing both structured and unstructured data for product analytics.</li>
                <li><strong>Statistical Analysis:</strong> statistical methods to identify patterns, anomalies, relationships, and trends.</li>

        <h4>Statistics:</h4>
                <li><strong>Statistical Knowledge:</strong> Strong foundation in various statistical methods and mathematical disciplines.</li>
                <li><strong>Specialized Techniques:</strong> Proficient in Bayesian Analysis, Linear Programming, and conducting A/B testing.</li>

        <h4>Communication:</h4>
                <li><strong>Effective Articulation:</strong> Excel at conveying complex technical concepts and aligning them with business objectives to ensure comprehensive understanding across all organizational levels.</li>
                <li><strong>Senior Management Interaction:</strong> Proven ability to confidently influence and communicate with senior management, adept at presenting data-driven insights and findings succinctly.</li>
                <li><strong>Clear and Concise Reporting:</strong> Skilled in leading interactions with both business and technical stakeholders, presenting findings and recommendations through well-crafted reports and presentations.</li>
                <li><strong>Authentic Engagement:</strong> Committed to direct communication, offering candid feedback, and promoting authenticity, thereby fostering a transparent and efficient work environment.</li>
                <li><strong>Data Storytelling:</strong> Expert in navigating through complex data sets to extract meaningful stories, translating analytics into relevant business insights.</li>

        <h4>Team Management:</h4>
                <li><strong>Efficient Project Handling:</strong> Proficient in managing multiple projects with competing priorities, ensuring high organizational efficiency.</li>
                <li><strong>Culture of Accountability:</strong> Foster a team environment focused on accountability, open communication, and self-management.</li>
                <li><strong>Goal Achievement:</strong> Consistently surpass individual and team objectives through effective leadership and strategic planning.</li>
                <li><strong>Global Team Management:</strong> Experienced in coordinating and working with globally distributed teams, nurturing a diverse and inclusive work culture.</li>
                <li><strong>Talent Development:</strong> Passionate about developing talent within my team and beyond, focusing on continuous learning and career growth.</li>
                <li><strong>Adaptive Time Management:</strong> Demonstrated ability to prioritize tasks, manage time effectively, and adapt to shifting priorities in dynamic environments.</li>

        <h4>Collaboration and Cross Functional:</h4>
                <li><strong>Cross-Functional Collaboration:</strong> Expertise in working with cross-functional teams, including product managers, engineers, and operations, to integrate solutions into products.</li>
                <li><strong>Teamwork for Innovation:</strong> Collaborate effectively to promote speed, agility, and innovation in team endeavors.</li>
                <li><strong>AI-Driven Product Development:</strong> Partner with data scientists, software engineers, and product managers to deliver AI-powered products, integrating technical expertise with business goals.</li>

        <h4>Business Strategy:</h4>
                <li><strong>Translating Business Needs:</strong> Skilled in understanding and converting business requirements into data-driven and technical solutions.</li>
                <li><strong>Adaptive Strategy:</strong> Proficient in adjusting strategies to meet evolving business needs in a dynamic environment.</li>
                <li><strong>Analytics Strategy Contribution:</strong> Actively participate in shaping and governing the analytics strategy, aligning it with business objectives.</li>
                <li><strong>Data-Driven Business Insights:</strong> Possess a strong acumen for business, adept at linking data modeling activities with business challenges and opportunities.</li>

        <h4>General:</h4>
                <li><strong>Adaptability and Flexibility:</strong> Exhibits a positive and adaptable attitude, readily adjusting to new technologies and industry challenges.</li>
                <li><strong>Continuous Learning:</strong> Actively researches and stays abreast of emerging technologies, state-of-the-art methods, and applications in data science.</li>
                <li><strong>Inquisitive Nature:</strong> Known for a curiosity-driven approach, constantly seeking answers and pushing boundaries in knowledge and application.</li>
                <li><strong>Documentation and Knowledge Sharing:</strong> Maintains comprehensive documentation of machine learning modeling processes and procedures.</li>
                <li><strong>Open Source and Community Involvement:</strong> Actively contributes to GitHub, open-source initiatives, research projects, and engages in Kaggle competitions.</li>
                <li><strong>Democratization of Data:</strong> Committed to making data knowledge and insights accessible across various teams and disciplines.</li>

        <hr>
        <h3 class="highlight">Contact Information</h3>
        <ul>
            <li>🌐: <a href="https://msoneai.com" target="_blank">msoneai.com</a></li>
            <li>🔗: <a href="https://linkedin.com/in/gouri-benni" target="_blank">linkedin.com/in/gouri-benni</a></li>
            <li>🐙: <a href="https://github.com/gouribenni" target="_blank">github.com/gouribenni</a></li>
            <li>✉️: <a href="mailto:gouri.benni@gmail.com">gouri.benni@gmail.com</a></li>
            <li>📞: (408)-690-4151</li>
        </ul>
        </div>
        <hr>

    """, unsafe_allow_html=True)

        # Further details can be added here based on the selected company
    #st.download_button(label="Download Resume", data="Your resume content", file_name="assets/documents/Mali_Nitin_Resume_DS.pdf", mime="application/pdf")
    # Provide the path to your local PDF file
    file_path = 'assets/documents/resume_gouri_benni.pdf'
        # Read the PDF file into bytes
    with open(file_path, "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button(
        label="Download Resume",
        data=PDFbyte,
        file_name="resume_gouri_benni.pdf",
        mime="application/pdf"
    )

        # Add more interactive or visual elements as needed




if __name__=='__main__':
  WorkExperiencePage().run()
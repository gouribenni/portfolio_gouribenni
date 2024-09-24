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
            "role": "",
            "company": "Norfolk Southern Corp",
            "period": "May 2023 - August 2023",
            "location": "Georgia, USA",
            "details": """
                <ul>
                    <li>Performed quantitative and qualitative analysis on large datasets, identifying trends and deriving actionable insights, contributing to a 15% increase in on-time arrivals and enhanced overall operational efficiency.</li>
                    <li>Developed and tracked key KPIs such as average delay time and on-time arrival rates using SQL and Python, which reduced train delays by 25% and significantly improved schedule reliability and customer satisfaction.</li>
                    <li>Applied NLP techniques (e.g., sentiment analysis, topic modeling) using SpaCy and TF-IDF to analyze unstructured maintenance logs and operational data, improving decision-making accuracy by 10%.</li>
                    <li>Conducted A/B testing and statistical analysis using Python, R, and SQL to optimize train schedules.</li>
                    <li>Additionally, implemented time series forecasting models like ARIMA and Exponential Smoothing, predicting bottlenecks and improving scheduling accuracy by 10%, leading to a 15% reduction in delays.</li>
                    <li>Designed and implemented ETL pipelines using PySpark and Snowflake, efficiently processing over 10 million records across petabytes of data, optimizing data flow for train scheduling and analytics. Led data integration projects using AWS APIs to ingest real-time and historical data, improving forecast accuracy by 25%.</li>
                    <li>Managed large datasets with Amazon S3, Glue, and Athena, utilizing dbt for data transformation, accelerating report delivery by 20%.</li>
                    <li>Orchestrated batch and real-time pipelines using Docker, Kubernetes, and Jenkins for containerization and CI/CD deployment, reducing manual intervention and improving data validation by 20%.</li>
                    <li>Spearheaded the implementation of an AWS Data Lake to store train scheduling data, creating a scalable infrastructure that supported both data warehousing and big data analytics.</li>
                    <li>Designed and developed real-time Tableau dashboards visualizing key metrics like average delay times and on-time arrivals, enhancing decision-making tools for stakeholders and contributing to a 15% boost in operational efficiency.</li>
                    <li>Regularly communicated insights and strategic recommendations to internal and external teams via reports, dashboards, and presentations, aligning technical solutions with business goals.</li>
                    <li>Worked closely with cross-functional teams to integrate data from multiple sources, optimize data models, and implement business intelligence solutions, supporting data-driven decision-making across departments and improving overall operational effectiveness.</li>
                </ul>
            """,
            "icon": "https://github.com/gouribenni/portfolio_gouribenni/blob/main/assets/images/NS.png?raw=true",
            "url":"https://www.norfolksouthern.com/",
        },
        {
            "role": "",
            "company": "ADP Pvt Ltd",
            "period": "June 2019 - June 2022",
            "location": "Hyderabad, India",
            "details": """
                <ul>
                    <li>Led the design, development, and optimization of data-driven solutions at ADP, focusing on payroll accuracy, HR analytics, and scalable ETL pipelines to support predictive analytics for key clients like Dell, Amazon, Pfizer, Cisco, and Geico.</li>
                    <li>Developed and optimized SQL queries and Python-based models to address payroll discrepancies, improving data accuracy by 25% and enhancing HR decision-making by 40% through Tableau dashboards.</li>
                    <li>Provided actionable insights related to payroll, employee turnover, and compliance using advanced statistical methods and machine learning models like logistic regression and decision trees.</li>
                    <li>Applied AI-driven predictive analytics and machine learning techniques such as Random Forest, Gradient Boosting, and SVM to predict employee turnover and compliance, increasing prediction accuracy by 30%.</li>
                    <li>Utilized clustering algorithms (K-means and hierarchical) to segment clients based on payroll activity and HR service usage, enhancing client satisfaction by 20% and retention by 15%.</li>
                    <li>Designed and implemented Python-based ETL pipelines using Airflow for dynamic scheduling and Kafka for real-time data integration.</li>
                    <li>This reduced data latency by 35% for critical services like ADP Workforce Now. Built an AWS-based Data Lake for ADP Assist, boosting AI-driven analytics with 30% faster data retrieval and 20% better processing efficiency.</li>
                    <li>Architected scalable AWS-based data lakes and data marts, integrating data from multiple sources to support predictive analytics, improving overall processing efficiency.</li>
                    <li>Led the optimization of data warehouses using Snowflake, enhancing scalability and query performance for complex reporting.</li>
                    <li>Conducted feature engineering and applied clustering algorithms to segment clients and optimize HR and payroll services.</li>
                    <li>Implemented logistic regression and decision tree models to predict payroll discrepancies like overtime miscalculations, improving accuracy by 25% and reducing errors by 15%. Deployed advanced machine learning techniques such as XGBoost and recursive feature elimination, enhancing model accuracy by 20%.</li>
                    <li>Collaborated closely with data engineers to design foundational datasets using AWS Glue and Spark, enabling scalable data solutions.</li>
                    <li>Mentored junior team members in delivering BI reports and dashboards, fostering a culture of innovation and continuous learning across the team.</li>
                </ul>
            """,
            "icon": "https://github.com/gouribenni/portfolio_gouribenni/blob/main/assets/images/ADP.png?raw=true",  # Replace with the actual URL or path to your icon
            "url":"https://in.adp.com/",
        },
        {
            "role": "",
            "company": "FluxGen Engineering Technologies",
            "period": "January 2019 - May 2019",
            "location": "Bangalore, India",
            "details": """
                <ul>
                    <li>Collaborated with the engineering team to analyze real-time water flow and level data using AquaGen’s smart monitoring system. Applied data analytics to detect inefficiencies in water infrastructure, resulting in a 10% reduction in non-revenue water loss.</li>
                    <li>Employed advanced Excel techniques, including VLOOKUP, and conditional formatting to analyze and organize water flow data. Used SQLAlchemy to connect to the database for efficient data extraction and applied SQL queries to clean, transform, and normalize large datasets.</li>
                    <li>•	Developed and optimized data-driven insights on water consumption patterns and identified potential leakages. These analyses enabled proactive notifications for ground maintenance personnel, improving overall operational efficiency by 15%.</li>
                </ul>
            """,
            "icon": "https://github.com/gouribenni/portfolio_gouribenni/blob/assets/images/fulxgen.png?raw=true",  # Replace with the actual URL or path to your icon
            "url":"https://fluxgen.com/"
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
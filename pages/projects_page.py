import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import streamlit as st
import streamlit.components.v1 as components
from streamlit_timeline import timeline
from widgets import navbar
class ProjectPage:
    def run(self):

        st.markdown("""
            <style>
            .card {
                margin-bottom: 20px;
                border-radius: 10px;
                border: none;
                box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
            }
            .card-body {
                padding: 15px;
            }
            .card-title {
                margin-bottom: 15px;
                font-weight: bold;
            }
            .card-text {
                font-size: 14px;
                margin-bottom: 15px;
            }
            .image {
                height: auto;
                max-height: 400px;
                width: 100%;
                border-top-left-radius: 10px;
                border-top-right-radius: 10px;
                object-fit: contain;
                border: 0.5px solid #000000; /* Add a border to the image */
            }
            .streamlit-button {
                margin-top: 10px;
                border-radius: 5px;
            .streamlit-expander-header { /* Adjust the styling for the expander header */
                font-size: 16px;
                font-weight: bold;
            }
            .streamlit-expander { /* Adjust the styling for the expander */
                margin-top: 0px;
                border-top: none;
                position: absolute;
                bottom: 0;
                left: 0;
            }
            
            </style>
        """, unsafe_allow_html=True)

        import base64
        # Function to convert PDF file to base64
        def get_base64_of_pdf(pdf_file_path):
            with open(pdf_file_path, "rb") as pdf_file:
                return base64.b64encode(pdf_file.read()).decode('utf-8')
        def return_pdf_embed(pdf_file_path):
            base64_pdf = get_base64_of_pdf(pdf_file_path)
            # Embed the PDF in the app
            pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
            return pdf_display

        # Assuming you have a PDF file named 'example.pdf' in the same directory as your Streamlit script
        pdf_file_path_smart_dustbin_project = 'assets/documents/Smart_Dustbin_manthan.pdf'
        pdf_file_path_isro_project = 'assets/documents/ISRO.pdf'
        # Sample project data
        projects = [
            {
                "title": "Improving Supply Chain Efficiency in the Market via Predictive Analysis Techniques",
                "image": "https://github.com/gouribenni/portfolio_gouribenni/blob/main/assets/images/supplychain.jpeg?raw=true",
                "description": "Utilizing advanced predictive analysis techniques to enhance supply chain operations, fostering market adaptability and streamlined logistical performance",
                "details": "We ventured into the intricate world of supply chain optimization, deploying predictive analytics to streamline end-to-end operations from raw material acquisition to final product delivery. By analyzing vast datasets spanning global trade statistics and daily e-commerce demands, we aimed to mitigate operational risks and enhance customer satisfaction. Our approach fused sophisticated machine learning models, including ARIMA and adaptive boosting, with IoT and machine learning technologies to refine supply chain visibility and forecast demand with unprecedented precision. This data-driven strategy promises to revolutionize inventory management, reduce lead times, and curtail logistics costs, setting a new benchmark for supply chain efficiency in the digital era.",
                "insights": "Insights from Project 1",
                "visualizations": "URL_to_visualization_1", 
                "code": "https://github.com/gouribenni/Supply_chain",
                "conclusion": "Conclusion of Project 1",
                "pdf":False

            },
            {
                "title": "Sports analysis: Beyond the numbers",
                "image": "https://github.com/gouribenni/portfolio_gouribenni/blob/main/assets/images/sports_analysis.png?raw=true",
                "description": "Developed an advanced sports analysis website, specializing in cricket data analytics, with a focus on comprehensive player performance and game insights.",
                "details": "The sports analysis website developed is a specialized platform dedicated to cricket data analytics, offering in-depth insights into player performances and various aspects of the game. This project involved sourcing comprehensive datasets from cricbuzz.com, which were initially in JSON format. A significant portion of the work entailed meticulous data cleaning and processing to transform and standardize this information for analytical purposes. To accurately represent and analyze the unique characteristics and statistics of cricket, a bespoke data model was created. For efficient data management and retrieval, SQL was employed as the backbone for query execution. The analytical prowess of the website is further enhanced by the use of Tableau, which was instrumental in developing a series of dynamic and interactive dashboards. These dashboards provide detailed and visually engaging insights into individual cricketer performances and various dimensions of cricket. The end result is a user-friendly platform that converts raw cricket data into easily understandable, yet comprehensive analytical insights, catering to enthusiasts and professionals alike who seek a deeper understanding of the sport.",
                "insights": "Insights from Project 1",
                "visualizations": "URL_to_visualization_1", 
                "code": "https://github.com/gouribenni/Sports_analysis",
                "conclusion": "Conclusion of Project 1",
                "pdf":False

            },

            {
                "title": "Automated Time-Table Scheduler using Genetic Algorithm",
                "image": "https://github.com/gouribenni/portfolio_gouribenni/blob/main/assets/images/generator.png?raw=true",
                "description": "An Automated Time-Table Scheduler harnessing the power of genetic algorithms to optimize academic scheduling, ensuring maximum efficiency and minimal conflicts",
                "details":'',
                "insights": "Insights from Project 1",
                "visualizations": "URL_to_visualization_1",  # or path to local file
                "code": "",
                "conclusion": "Conclusion of Project 1",
                "pdf":True,
                "pdf_file_path":'assets/documents/FinalPR.pdf'
            },
            {
                "title": "Credit Risk Analysis: Mitigate your Risk",
                "image": "https://github.com/gouribenni/portfolio_gouribenni/blob/main/assets/images/risk.jpeg?raw=true",
                "description": "Focuses on employing advanced analytical techniques to assess and reduce financial risks in lending and credit operations",
                "details":'',
                "insights": "Insights from Project 1",
                "visualizations": "URL_to_visualization_1",  # or path to local file
                "code": "",
                "conclusion": "Conclusion of Project 1",
                "pdf":True,
                "pdf_file_path":'assets/documents/credit_risk_compressed.pdf'
            },
            {
                "title": "Analysis of Energy Consumption by various departments in San Jose",
                "image": "https://github.com/gouribenni/portfolio_gouribenni/blob/main/assets/images/energy.png?raw=true",
                "description": "An in-depth analysis focused on evaluating and optimizing energy consumption across different departments in San Jose, aiming for sustainable and efficient energy use.",
                "details":'',
                "insights": "Insights from Project 1",
                "visualizations": "URL_to_visualization_1",  # or path to local file
                "code": "",
                "conclusion": "Conclusion of Project 1",
                "pdf":True,
                "pdf_file_path":'assets/documents/energy_consumption.pdf'
            },
            {
                "title": "NeuroNest: Deep Learning Chatbot for Applied Data Science department",
                "image": "https://github.com/gouribenni/portfolio_gouribenni/blob/main/assets/images/bot.png?raw=true",
                "description": "The NeuroNest project revolutionizes communication within the Applied Data Science department through a deep learning-powered chatbot, integrating advanced language models like llama2, GPT-3.5, and RAG for accurate, context-aware responses.",
                "details":'The NEURONEST project involved the development of a deep learning chatbot, integrating advanced language models like Llama2 and GPT-3.5, trained on a vast dataset of over 370,000 academic interactions. Python-based web scraping tools such as BeautifulSoup and Selenium were used to create this dataset, significantly enhancing the chatbot response accuracy by 35%. The project leveraged advanced Transformer architectures in language models, achieving a notable 40% increase in text processing efficiency and contextual understanding. Key performance metrics included a 0.79 SAS (Semantic Accuracy Score) and a 0.76 BLEU (Bilingual Evaluation Understudy) score, reflecting high levels of semantic accuracy and linguistic precision. Additionally, innovations like LoRA layers and dropout regularization were integrated to reduce overfitting, along with the paged_adamw_8bit AdamW optimizer to improve memory usage efficiency, culminating in a 20%' 'increase in user satisfaction over traditional academic communication methods.',
                "insights": "Insights from Project 1",
                "visualizations": "URL_to_visualization_1",  # or path to local file
                "code": "https://github.com/gouribenni/AI_ChatBot",
                "conclusion": "Conclusion of Project 1",
                "pdf":False,
                "pdf_file_path":''
            },
            {
                "title": "Ranked Stack Overflow: Mathematics and Statistical Analysis",
                "image": "https://github.com/gouribenni/portfolio_gouribenni/blob/main/assets/images/stack.png?raw=true",
                "description": "A specialized tool that efficiently categorizes and prioritizes Stack Overflow content, using advanced algorithms to enhance the accessibility and relevance of mathematical and statistical information for users.",
                "details":"",
                "insights": "Insights from Project 1",
                "visualizations": "URL_to_visualization_1",  # or path to local file
                "code": "https://github.com/gouribenni/Ranked_Stack_Overflow-Mathematics-Statistical-Analytics",
                "conclusion": "Conclusion of Project 1",
                "pdf":False,
                "pdf_file_path":'assets/documents/Stack1.pdf'
            },
            {
                "title": "AI Powered Job Transition Pathway using Generative LSTM Models",
                "image": "https://github.com/gouribenni/portfolio_gouribenni/blob/main/assets/images/job_transition.png?raw=true",
                "description": "This comprehensive project in Data Science delves into the dynamic nature of the modern workforce.",
                "details":'''<div>
                            <h2>FutureScape Navigator: Transforming Career Journeys with Generative AI and LSTM Insights</h2>
                            <h3>Motivation</h3>
                            <p>
                                The modern workforce's dynamic nature calls for continuous adaptation in skills and knowledge. This project arose from a deep understanding of the challenges faced by professionals in plotting their career paths amidst rapidly changing job categories and skill requirements. By leveraging machine learning models, specifically seq2seq models with bidirectional LSTM and attention mechanisms, the project aims to offer tailored career guidance solutions, adapting to the fast-paced professional environment.
                            </p>
                            <h3>Background Information</h3>
                            <p>
                                The research underscores the trend of career switching, reflecting the changing dynamics of work, skill demands, and personal aspirations. It highlights the increasing trend of labor mobility across various age groups, emphasizing the need for tools that facilitate smooth career transitions and enable professionals to tailor their career paths.
                            </p>
                            <h3>Literature Review</h3>
                            <p>
                                The study juxtaposes its unique approach against existing literature, focusing on the enhancement of job-skill representation and the importance of understanding job transition patterns. It stands out for its emphasis on predicting educational courses and career progression using a novel AI approach.
                            </p>
                            <h3>Methodology</h3>
                            <p>
                                Comprehensive data collection from online job portals, skill repositories, and educational platforms form the foundation of this research. The methodology encompasses data cleaning, exploratory data analysis, and sophisticated data processing techniques, including the use of Phrase Matcher Models and fuzzy matching to refine and correlate data across different domains.
                            </p>
                            <h3>ML Modeling</h3>
                            <p>
                                The heart of the project lies in its advanced ML modeling, utilizing Seq2Seq architecture with LSTM layers. These models, coupled with BERT embeddings, are adept at capturing the nuances of language and context, crucial for accurately mapping career paths and skill development trajectories.
                            </p>
                            <h3>Experiments and Model Evaluation</h3>
                            <p>
                                The project delves into various experiments to fine-tune the model, exploring different embeddings and LSTM configurations. The evaluation metrics focus on the model's accuracy in forecasting job roles and the relevance of course recommendations, providing an objective assessment of its effectiveness.
                            </p>
                            <h3>Project Results</h3>
                            <p>
                                The project successfully demonstrates a model-generated output showcasing potential career pathways, requisite skills, and tailored course recommendations, thus offering a comprehensive tool for career planning and skill development.
                            </p>
                            <h3>Discussion and Future Improvement</h3>
                            <p>
                                The research concludes with a critical discussion on its holistic approach, potential improvements, and future directions. It emphasizes the need for continuous refinement of the model to keep pace with the evolving job market and skill landscape.
                            </p>
                        </div>''',
                "insights": "Insights from Project 1",
                "visualizations": "URL_to_visualization_1",  # or path to local file
                "code": "https://github.com/gouribenni/job_transition",
                "conclusion": "Conclusion of Project 1",
                "pdf":False,
                "pdf_file_path":''
            },
            # Add more projects as needed...
        ]

        def create_tabs(project,pdf=True):
            with st.expander("View More",expanded=False):
                tab1, tab2, tab3 = st.tabs(["Details", "Code", "Conclusion"])

                with tab1:
                    if not pdf:
                        st.markdown(project["details"], unsafe_allow_html=True)
                    else:
                        st.markdown(return_pdf_embed(project["pdf_file_path"]), unsafe_allow_html=True)

                with tab2:
                    st.markdown(f"[Code Repository]({project['code']})")
                    # Create the nbviewer URL for your notebook
                    
                with tab3:
                    st.write(project["conclusion"])


        # Number of columns for the grid
        cols_per_row = 2
        def is_iframe(image_string):
            return "<iframe" in image_string

        # Create the card layout
        for i in range(0, len(projects), cols_per_row):
            cols = st.columns(cols_per_row)
            for j in range(cols_per_row):
                if i + j < len(projects):
                    project = projects[i + j]
                    if is_iframe(project["image"]):
                        # If it's an iframe, render it directly
                        media_html = project["image"]
                    else:
                        # If it's an image URL, use the img tag
                        media_html = f'<img class="image" src="{project["image"]}" alt="{project["title"]}">'

                    with cols[j]:
                        st.markdown(f"""
                            <div class="card">
                                {media_html}
                                <div class="card-body">
                                    <h5 class="card-title">{project['title']}</h5>
                                    <p class="card-text">{project['description']}</p>
                                </div>
                            </div>
                        """, unsafe_allow_html=True)
                        create_tabs(project,project["pdf"])

                st.markdown("""
                    <hr style="
                        border: none; 
                        height: 1px; 
                        background: linear-gradient(to right, #B2DFDB 0%, #B2DFDB 100%); 
                        margin-top: 0px; 
                        margin-bottom: 0px;">
                """, unsafe_allow_html=True)



                #st.markdown('<hr style="border:2px solid #008080; width:50%; margin:auto;"/>', unsafe_allow_html=True)

   







            





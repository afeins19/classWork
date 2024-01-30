# Text Summarizer That Can Detect Political Party
<div align="center">
  <img src="https://github.com/BabyKangaroo117/Frugl-APP/assets/13011373/b5efcc9f-946b-44ee-88cb-0036170282ff">
  <br>
 </div>
 
 ## Abstract
 Create a text summarizer that can take a body of text, and summarize if the text contains a republican or democratic view. It can also conclude if the view is neurtral. This application uses NLP to achieve this. For the initial planning phase of this application, research will be conducted by the development
 team, to gain knowledge on NLP and applications similar to this this one. The theory that each programmer understands, will be tested when it comes time to implement this application. Various libraries will need to be researched, and each
 one considered for the application should be useful in their own way. Each programmer will have various tasks assigned to them, to simulate a real world data science work flow.
 ## Goal
 The ulimate goal of this application is to fully understand NLP in terms of Artificial Intelligence and create a succesful application that can demonstrate this. As the team of programmers conducts research to understand this data science application, there should be hard focus on thinking in terms of a data scienctist to fully understand that program and data being worked with. A programmers job is to make sure the application is built on time and ensure the application is what it is said be. The other important goal in this project is to fully understand how a team in the real world would create this project.

#### Important Goals:
- Understand NLP and how it will be used within the application.
- Work as a team to set deadlines and simulate a real world environment. This can be done through scrum meetings.
- Work with multiple NLP libraries to get a grasp on them and pick which ones would be most beneficial to the project.
- Test and document the application as much as possible.
- Demonstrate that the application is practical and could have real world use.
- Compare project to succesful NLP related applications, to ensure the programmers on the correct path. These checks will be performed every so often.
- Find data that will allow the application to be efficient.

 ## Objectives
- Learn about NLP techniques and libraries such as NLTK, spaCy, TextBlob, PyTorch and what advantages and disadvantages they each have.
- Create a bot that can summarize a paper and determine determine the political party.
#### Key Objectives
##### Gather Data
- Collect data from corpuses, and other text collections and datasets that contain articles that have political biases to them
#### Text Preprocessing
- Preprocess the data, clean up the input, and remove all stopwords, unneeded punctuation, and unrelated things from the text.
- Label the sentences and words that show political bias
##### Sumarization
- Train or create a model that can summarize preprocessed data to our specific needs.
##### UX/UI Design
- Design a user interface that will allow the application to be not only usable, but user friendly.
 ## Class and Block Diagram
<div align="center">
  <img src="https://github.com/justyden/Text_Summary_Using_NLP/blob/main/UML%20class.jpeg">
  <br>
 </div>

## Unique Feature (Django)
our project will be hosted on an interactive website created within the django framework.
Users will be able to paste text into a search bar and the text data will be sent for
processing to the backend of our app. After processing, users will be presented with the following
- Sentiment analysis of the overall "theme" of the text (positive, negative, or neutral)
- emotional classification based on NRCLex 
- some general information about the text 

### Django Site Schematic
- TextAnalyzer  
  - Interface with the user and get text input via a form 
  - pass data to our custom sentiment analyzer/emotional classifier modules
  - port a visual representation of our analysis back to the user 
 
 ## Contribution Plan
 #### Tyler Thompson
 - Help research useful NLP related techniques. Help problem solve NLP related issues we may run into.
 - Document the code properly and effectively.
 - Try and be more have a back end engineer for the project.
#### Love-Divine Onwulata
- Research which NLP libraries will be most useful to the project
- Implement the NLP into the application
- Help implement the summarization model
- Help label the datasets
#### Joseph H Porrino
- Research and collect datasets and articles that have political bias
- Label and filter articles for the feature extraction
- Create the User Interface for the application
- Help with bias detection
#### Aaron Feinberg
- Develop the Bias Detection functionality for the application
- Help with the summarization model
- Help with the UX/UI design

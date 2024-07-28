<!DOCTYPE html>
<html>

<head></head>

<body>

  <h1>Twitter Post Automation 🚀</h1>

  <h2>Overview</h2>

  <p>The Twitter Post Automation project is designed to increase user engagement on a personal Twitter account, targeting individuals interested in technology and coding. The project utilizes Python, Tweepy, Github Actions, and REST APIs to achieve its objectives. 🌐</p>

  <h2>Features</h2>

  <ol>
    <li>
      <h3>Encouraging 100DaysOfCode Tweets 💬:</h3>
      <ul>
        <li>The script queries tweets related to the "100DaysOfCode" hashtag.</li>
        <li>Retrieves user details from the tweets and replies to them with a random encouraging quote to motivate them in their coding streak.</li>
      </ul>
    </li>
    <li>
      <h3>Tech-Meme Posting 😄:</h3>
      <ul>
        <li>Implements the functionality to extract random tech-meme images using JokeAPI.</li>
        <li>Posts the extracted meme images as tweets to add a humorous touch to the Twitter account.</li>
      </ul>
      
    </li>
    <li>
      <h3>Scheduled Execution with GitHub Actions 🕒:</h3>
      <ul>
        <li>Utilizes GitHub Actions workflow to schedule project execution based on specific time intervals each day.</li>
        <li>Ensures that the automation runs seamlessly at predetermined times.</li>
      </ul>
    </li>
  </ol>

  <h2>Code Structure</h2>

  <p>The main logic of the project is implemented in the Python script <code>twitterBot_scratch.py</code>, which contains the following key sections:</p>

  <ul>
    <li>
      <h3>Tweet Encouragement Logic:</h3>
      <ul>
        <li>Queries tweets related to "100DaysOfCode" and replies with an encouraging quote.</li>
      </ul>
    </li>
    <li>
      <h3>Tech-Meme Posting Logic:</h3>
      <ul>
        <li>Fetches a random tech meme using the JokeAPI and posts it on Twitter.</li>
        <li>Handles exceptions gracefully to ensure robust execution. 🛡️</li>
      </ul>
    </li>
    <li>
      <h3>Authentication and Setup:</h3>
      <ul>
        <li>Utilizes Tweepy for Twitter API interactions.</li>
        <li>Includes necessary imports, credentials, and API setup. 🔐</li>
      </ul>
    </li>
  </ul>

<h2> Output Examples </h2>
![Meme1](https://github.com/user-attachments/assets/7435858e-96ce-450c-8d32-7c9f8c27ccb0)
![Meme2](https://github.com/user-attachments/assets/f95a90ee-feca-44e5-b028-040dcb90130f)
![Info2](https://github.com/user-attachments/assets/4e03b755-b55c-4385-a478-582792136f0d)
![Info1](https://github.com/user-attachments/assets/b6ab3abd-a366-4f8b-b087-683826c97b37)



  <h2>How to Use</h2>

  <ol>
    <li>Clone the repository to your local machine:
    </li>
    <li>Install the required dependencies:
      <br>
      <code>pip install -r requirements.txt</code>
    </li>
    <li>Set up your Twitter API credentials by creating a file named <code>credentials.py</code> and providing the required keys and tokens.</li>
    <li>Adjust the scheduled execution time in the script if needed.</li>
    <li>Run the script:
      <br>
      <code>python twitterBot_scratch.py</code>
    </li>
  </ol>

  <h2>Dependencies</h2>

  <ul>
    <li>Tweepy</li>
    <li>Requests</li>
    <li>PIL (Pillow)</li>
  </ul>



  <p>Feel free to contribute, open issues, or provide feedback. 🎉</p>

</body>

</html>

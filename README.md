This is a Dockerized Python Flask web app that allows you to play a "Rock Paper Scissors" game in Lithuanian.
1. Logic of the game: 
  - Each game consists of 10 rounds that you play with a computer by choosing one of the free game options. You either win or lose each round.
  - After 10 rounds, if you have more points than the computer, you get to choose a prize for your winning. Your options are a joke, an interesting fact or a surprise.
  - If you enjoyed the game you are welcome to play again and try different prizes if you win.
2. The app is supported by several html files for better user experience.
3. Dockerization process:
  - Additionally to .py and .html files, a requirements.txt and a docker file were created with the instruction to build the Docker image.
  - The dockerfile:
    - defines which Python image to use,
    - sets the working directory in the container,
    - copies the code,
    - installs the dependancies
    - from the requirements file,
    - exposes the port to use and runs the code
  - writing commands in the terminal the docker image was created (docker build -t julija024/rps_game), tagged (docker tag), pushed to Docker hub (docker push)
  - After some modifications were made to the Python code, the imaged was rebuilt and pushed again
  - Also tested my work be pulling the image and playing the game (docker pull julija024/rps_game; docker run -p 5000:5000 julija024/rps_game)
I hope you enjoy the game!
